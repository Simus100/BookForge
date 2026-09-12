#!/usr/bin/env python3
"""
stylometry.py — Analisi stilometrica per BookForge.

Usato da /clone (estrazione StyleDNA quantitativa) e /revisione livello 3.
Nessuna dipendenza esterna: usa solo la libreria standard.

Uso:
    python scripts/stylometry.py <file.txt> --lang it --json

Calcola metriche misurabili e suggerisce i 5 assi StyleDNA quantitativi:
ASL→SENTENCE_LENGTH, dev.std lunghezze→RHYTHM_VARIATION, MATTR→VOCABULARY_RICHNESS,
punteggiatura interna→SYNTAX_COMPLEXITY, % dialogo→DIALOGUE_WEIGHT.
I 7 assi qualitativi (RL, FD, ST, SD, ET, SUB, AP) vanno valutati dall'LLM dopo la lettura.

Inoltre: scanner anglicismi/calchi, distribuzione descrittiva del ritmo e per paragrafo,
MATTR (vocabolario robusto alla lunghezza) e un blocco `baseline` con le chiavi
pronte per voice_fingerprint.stylometry_baseline del BSR.
"""

import argparse
import json
import re
import sys
import statistics
import unicodedata
from collections import Counter

ANALYZER_VERSION = "7.7.0"

# Filler/intercalari tipici dell'italiano (densità = segnale di registro colloquiale)
IT_FILLERS = {
    "insomma", "cioè", "praticamente", "diciamo", "comunque", "ecco",
    "appunto", "tipo", "magari", "boh", "beh", "allora", "dunque",
}
# Avverbi in -mente: conteggio descrittivo via regex, da leggere nel contesto.

# Stopword italiane: usate per scartare gli n-gram fatti solo di parole vuote
IT_STOPWORDS = {
    "il", "lo", "la", "i", "gli", "le", "un", "uno", "una", "di", "a", "da",
    "in", "con", "su", "per", "tra", "fra", "e", "o", "ma", "che", "non",
    "si", "se", "del", "della", "dei", "delle", "al", "alla", "nel", "nella",
    "come", "più", "anche", "poi", "ci", "lo", "ne", "è", "era", "sono", "ha",
    "il", "suo", "sua", "lui", "lei", "gli", "mi", "ti", "se",
}


def find_repeated_ngrams(words, n, min_count, top_k=12):
    """Trova gli n-gram ripetuti almeno min_count volte (esclude quelli solo-stopword)."""
    from collections import Counter
    grams = Counter()
    for i in range(len(words) - n + 1):
        gram = words[i:i + n]
        if all(w in IT_STOPWORDS for w in gram):
            continue  # salta n-gram fatti solo di parole vuote
        grams[" ".join(gram)] += 1
    repeated = [(g, c) for g, c in grams.items() if c >= min_count]
    repeated.sort(key=lambda x: (-x[1], x[0]))
    return repeated[:top_k]



def clamp(value, lo=1, hi=10):
    return max(lo, min(hi, value))


def normalize_text(text):
    return unicodedata.normalize("NFC", text).translate(str.maketrans({"’": "'", "‘": "'", "ʼ": "'"}))


def split_sentences(text):
    """Segmentazione euristica; abbreviazioni, decimali e chiusure di dialogo."""
    text = re.sub(r"\s+", " ", normalize_text(text).strip())
    for abbr in ["p.es.", "ecc.", "es.", "sig.", "dott.", "prof.", "n.", "pag."]:
        text = re.sub(re.escape(abbr), lambda m: m[0].replace(".", "\ue000"), text, flags=re.I)
    text = re.sub(r"(?<=\d)\.(?=\d)", "\ue000", text)
    parts = re.findall(r'.+?(?:[.!?…]+[»”"\)\]]*(?=\s|$)|$)', text)
    return [x.replace("\ue000", ".").strip() for x in parts if x.strip()]


def word_spans(text):
    return list(re.finditer(r"[^\W_]+(?:'[^\W_]+)*", normalize_text(text), re.UNICODE))


def tokenize_words(text):
    return [m[0].lower() for m in word_spans(text)]


def dialogue_spans(text):
    """Unione delle battute; quelle a trattino terminano a fine riga o al trattino di chiusura.
    Non distingue citazioni da dialoghi né ogni inciso narrativo: quota approssimata.
    """
    spans = []
    for rx in (r'«[^»]*»', r'“[^”]*”', r'"[^"\n]*"'):
        spans.extend((m.start(), m.end()) for m in re.finditer(rx, text))
    for m in re.finditer(r"(?m)^[ \t]*[—–-][ \t]+[^\n]+", text):
        close = re.search(r"[ \t]+[—–][ \t]+", m[0])
        spans.append((m.start(), m.start()+close.start() if close else m.end()))
    merged = []
    for lo, hi in sorted(spans):
        if merged and lo <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(hi, merged[-1][1]))
        else:
            merged.append((lo, hi))
    return merged


def dialogue_mask(text):
    spans = dialogue_spans(text)
    result, j = [], 0
    for token in word_spans(text):
        while j < len(spans) and token.start() >= spans[j][1]:
            j += 1
        result.append(j < len(spans) and token.start() >= spans[j][0] and token.end() <= spans[j][1])
    return result


# --- Anglicismi: liste curate per la prosa italiana (il cyberpunk tira verso l'inglese) ---
# Forestierismi evitabili (sostantivi/invariabili): match esatto su parola.
FORESTIERISMI = {
    "device": "dispositivo", "tool": "strumento", "feature": "funzione",
    "deadline": "scadenza", "meeting": "riunione", "team": "squadra",
    "mood": "umore/atmosfera", "step": "passo/fase", "background": "sfondo/passato",
    "feedback": "riscontro", "default": "predefinito", "boost": "spinta",
    "random": "casuale", "fake": "falso", "smart": "intelligente",
    "skill": "abilità", "task": "compito", "link": "collegamento",
    "location": "luogo", "timing": "tempismo", "trend": "tendenza",
    "update": "aggiornamento", "core": "nucleo", "layer": "strato",
    "target": "obiettivo/bersaglio", "look": "aspetto", "screenshot": "schermata",
    "report": "resoconto",
}
# Pseudo-anglicismi non coniugabili (aggettivi/sostantivi pseudo-italiani): match esatto.
PSEUDO_EXACT = {"performante": "efficiente", "settaggio": "impostazione"}
# Pseudo-anglicismi verbali in -are (radice inglese): match su radice + desinenze -are.
# Si tiene -ò (passato remoto, frequente in narrativa) ma si evitano le vocali nude
# (a/o/i) che collidono con sostantivi ("setta" = setta religiosa).
PSEUDO_STEMS = {
    "sett": "impostare", "download": "scaricare", "upload": "caricare",
    "switch": "commutare", "check": "controllare", "skipp": "saltare",
    "kill": "eliminare", "spamm": "tempestare", "link": "collegare",
    "tagg": "etichettare", "googl": "cercare in rete", "forward": "inoltrare",
}
_ARE = r"(?:are|at[oaie]|ando|iamo|ate|av[ao]|avano|ò|arono|er[àò]|eranno)"
# Calchi semantici (parola italiana vera usata col senso inglese): da verificare in contesto.
CALCHI_PATTERNS = [
    (r"realizz" + _ARE, "realizzare", "se vale «capire» → «rendersi conto»"),
    (r"support" + _ARE, "supportare", "se vale «sostenere/aiutare» → «sostenere»"),
    (r"implement" + _ARE, "implementare", "se vale «attuare» → «attuare/realizzare»"),
    (r"eventualmente", "eventualmente", "se vale «infine» (eventually) → «alla fine»"),
    (r"attualmente", "attualmente", "se vale «in realtà» (actually) → «in realtà»"),
    (r"performance", "performance", "→ «prestazione/resa»"),
    (r"focus", "focus", "→ «attenzione/fulcro»"),
]


# --- Tic da LLM (anti-ai.md §tic): rilevazione post-scrittura. SEGNALAZIONI, non bersagli. ---
# Antitesi-riflesso: "non è (solo) X, ma/è Y", "non si tratta di", "più che X, è Y".
ANTITESI_PATTERNS = [
    re.compile(r"\bnon\s+(?:è|era|sono|erano)\s+(?:solo|soltanto|semplicemente)\b", re.I),
    re.compile(r"\bnon\s+si\s+tratt\w+\s+(?:solo\s+|soltanto\s+)?di\b", re.I),
    re.compile(r"\bnon\s+(?:è|era)\s+(?:un[ao']?\s+|il\s+|la\s+|l')?\w+[,;:]?\s+(?:ma|bensì)\b", re.I),
    re.compile(r"\bpiù\s+che\s+(?:un[ao']?\s+|il\s+|la\s+|l')?\w+,", re.I),
    # Forma asindetica con verbo ripetuto: "Non era paura, era qualcosa di peggio."
    re.compile(r"\bnon\s+(è|era|sono|erano)\s+[^,.;:!?]{1,40},\s+\1\b", re.I),
]
# Aggettivi-portata "atmosferici": dichiarano l'atmosfera invece di farla vedere.
# Lista volutamente CORTA e ad alto segnale: spia morbida, il grosso resta giudizio (anti-ai.md).
ATMO_RX = re.compile(
    r"\b(atmosferic[oaie]|atmosferiche|palpabil[ei]|etere[oa]|eterei|eteree|surreal[ei]|"
    r"indefinibil[ei]|indescrivibil[ei]|ineffabil[ei]|evanescent[ei]|vibrant[ei]|"
    r"ultraterren[oaie])\b", re.I)
# Parole-portata dell'enfasi: gonfiano la significatività (anti-ai.md §"Gonfiare il piccolo")
# invece di alzare la precisione del dettaglio. Spia gemella di ATMO_RX, stessa filosofia:
# segnale MORBIDO a grappolo. Lista volutamente ad alto segnale — parole quasi sempre vuote
# come intensificatori; gli usi enfatici di termini comuni (profondo, fondamentale) restano
# giudizio della dottrina, per non generare falsi positivi.
GONFIAGGIO_RX = re.compile(
    r"\b(crucial[ei]|epocal[ei]|epic[oaie]|epiche|inesorabil[ei]|viscerale|viscerali|"
    r"indelebil[ei]|travolgent[ei]|devastant[ei]|trasformativ[oaie]|vertiginos[oaie]|"
    r"abissal[ei]|sconfinat[oaie]|struggent[ei]|lancinant[ei]|incommensurabil[ei]|"
    r"dirompent[ei]|sconvolgent[ei])\b", re.I)
# Lessico somatico: per scovare lo schema corporeo ripetuto (il "personaggio-termostato").
SOMA_LEX = {
    "pelle", "petto", "gola", "stomaco", "mani", "mano", "dita", "nuca", "tempie",
    "orecchie", "respiro", "fiato", "cuore", "spalle", "schiena", "ventre", "polso",
    "polsi", "mascella", "denti", "pugni", "sterno", "vertebre", "diaframma",
}


def detect_llm_tics(text, sentences, words, n_words):
    """Tic da LLM misurabili (anti-ai.md). Esegui DOPO la scrittura: sono spie, non quote.
    Se scrivi per azzerare questi contatori invece che per servire la scena, il riflesso
    è già un tell (anti-ai.md, incipit)."""
    per1k = lambda c: round(c * 1000 / n_words, 2) if n_words else 0.0

    # 1) Antitesi-riflesso
    anti_count, anti_ex = 0, []
    for s in sentences:
        for rx in ANTITESI_PATTERNS:
            if rx.search(s):
                anti_count += 1
                if len(anti_ex) < 3:
                    anti_ex.append(s if len(s) <= 90 else s[:87] + "…")
                break

    # 2) Terzine (triadi coordinate "X, Y e Z" di elementi brevi)
    terzine = re.findall(r"\b\w+(?:\s\w+)?,\s+\w+(?:\s\w+)?\s+ed?\s+\w+\b", text)
    terzine_density = per1k(len(terzine))

    # 3) Trattino lungo: totale, e quota "drammatica" (singolo, a chiudere la frase con coda corta)
    dashes = len(re.findall(r"[—–]", text))
    dramatic = 0
    for s in sentences:
        d = re.findall(r"[—–]", s)
        if len(d) == 1:
            tail = s.split("—")[-1].split("–")[-1]
            if len(tokenize_words(tail)) <= 8:
                dramatic += 1
    dashes_per_page = round(dashes / max(1, n_words / 250), 2)  # pagina ≈ 250 parole

    # 4) Frase-sentenza in chiusura di paragrafo (epigramma in posa)
    paras = split_paragraphs(text)
    closers, eligible = 0, 0
    for p in paras:
        ps = split_sentences(p)
        if len(ps) < 2:
            continue
        eligible += 1
        last = ps[-1]
        if last.lstrip()[:1] not in "«\"“—–" and 0 < len(tokenize_words(last)) <= 9:
            closers += 1
    closer_ratio = round(closers / eligible, 2) if eligible else 0.0

    # 5) Schema somatico ripetuto: n-gram corporei che ricorrono. Trigramma ≥3 = schema
    #    già formato; bigramma ≥4 = vocabolario corporeo che si sta fissando.
    soma_hits = []
    for n in (3, 2):
        for g, c in find_repeated_ngrams(words, n, min_count=3, top_k=20):
            if any(w in SOMA_LEX for w in g.split()):
                if any(g in h["ngram"] for h in soma_hits):
                    continue  # bigramma già coperto da un trigramma
                soma_hits.append({"ngram": g, "n": n, "conteggio": c})
    soma_hits.sort(key=lambda h: -h["conteggio"])
    soma_warn = any((h["n"] == 3 and h["conteggio"] >= 3) or (h["n"] == 2 and h["conteggio"] >= 4)
                    for h in soma_hits)

    # 6) Raffica di "come se": una similitudine è ritmo, tre di fila in un paragrafo sono
    #    un'anafora da pilota automatico. Il bigramma è fatto di stopword, quindi sfugge
    #    allo scanner n-gram: serve un contatore dedicato. Warn solo sul grappolo.
    cs_rx = re.compile(r"\bcome\s+se\b", re.I)
    cs_total = len(cs_rx.findall(text))
    cs_burst = max((len(cs_rx.findall(p)) for p in paras), default=0)
    cs_warn = cs_burst >= 3 or (cs_total >= 4 and per1k(cs_total) > 2.0)

    # 7) Aggettivi-portata: spia MORBIDA (la più permissiva). Uno guadagnato non scatta mai;
    #    si segnala solo il grappolo. Il giudizio vero resta nella dottrina (anti-ai.md).
    atmo_total = len(ATMO_RX.findall(text))
    atmo_burst = max((len(ATMO_RX.findall(p)) for p in paras), default=0)
    atmo_examples = list(dict.fromkeys(w.lower() for w in ATMO_RX.findall(text)))[:6]
    atmo_warn = atmo_burst >= 2 or (atmo_total >= 3 and per1k(atmo_total) > 1.2)

    # 8) Gonfiaggio della significatività: parole-portata dell'enfasi (anti-ai.md §"Gonfiare il
    #    piccolo"). Spia MORBIDA gemella di aggettivi_portata — una guadagnata non scatta mai,
    #    solo il grappolo. Distinta dagli aggettivi atmosferici (ATMO_RX): qui non si dichiara
    #    un'atmosfera, si alza il volume su un gesto ordinario («un momento cruciale»).
    gonf_total = len(GONFIAGGIO_RX.findall(text))
    gonf_burst = max((len(GONFIAGGIO_RX.findall(p)) for p in paras), default=0)
    gonf_examples = list(dict.fromkeys(w.lower() for w in GONFIAGGIO_RX.findall(text)))[:6]
    gonf_warn = gonf_burst >= 2 or (gonf_total >= 3 and per1k(gonf_total) > 1.2)

    # Soglie euristiche di segnalazione, senza calibrazione empirica di qualità.
    return {
        "_lettura": ("Spie post-scrittura per il passo PULIZIA del controllo finale. "
                     "NON sono bersagli da ottimizzare in scrittura: vale anti-ai.md, incipit."),
        "antitesi_riflesso": {"conteggio": anti_count, "per_1000_parole": per1k(anti_count),
                              "esempi": anti_ex, "warn": anti_count >= 2 and per1k(anti_count) > 0.8},
        "terzine": {"conteggio": len(terzine), "per_1000_parole": terzine_density,
                    "warn": len(terzine) >= 4 and terzine_density > 2.5},
        "trattino": {"totale": dashes, "per_pagina": dashes_per_page, "drammatici": dramatic,
                     "warn": dashes_per_page > 2.5 or dramatic >= 4},
        "frase_sentenza_chiusura": {"paragrafi_chiusi_a_epigramma": closers,
                                    "su_paragrafi": eligible, "ratio": closer_ratio,
                                    "warn": closers >= 3 and closer_ratio > 0.35},
        "schema_somatico": {"ricorrenze": soma_hits[:8], "warn": soma_warn},
        "come_se_raffica": {"totale": cs_total, "max_per_paragrafo": cs_burst,
                            "per_1000_parole": per1k(cs_total), "warn": cs_warn},
        "aggettivi_portata": {"totale": atmo_total, "max_per_paragrafo": atmo_burst,
                              "esempi": atmo_examples, "warn": atmo_warn},
        "gonfiaggio_significativita": {"totale": gonf_total, "max_per_paragrafo": gonf_burst,
                                       "esempi": gonf_examples, "warn": gonf_warn},
    }


def pip_hints(text, sentences, n_words):
    """Dati grezzi per il Ledger PIP (NST): apertura, chiusura, distribuzione del dialogo.
    La classificazione finale (azione/immagine/riflessione…) resta al modello: qui solo fatti."""
    first = sentences[0] if sentences else ""
    last = sentences[-1] if sentences else ""
    is_dialogue = lambda s: s.lstrip()[:1] in "«\"“—–"
    mask = dialogue_mask(text)
    thirds = []
    for i in range(3):
        part = mask[len(mask)*i//3:len(mask)*(i+1)//3]
        thirds.append(round(sum(part)/len(part), 3) if part else 0.0)
    return {
        "apertura": {"prima_frase": first if len(first) <= 120 else first[:117] + "…",
                     "dialogo": is_dialogue(first)},
        "chiusura": {"ultima_frase": last if len(last) <= 120 else last[:117] + "…",
                     "dialogo": is_dialogue(last)},
        "dialogo_per_terzo": thirds,
        "nota": "Compila il Ledger PIP partendo da questi dati; senso dominante e campo metaforico restano valutazione del modello.",
    }


def _build_patterns():
    fore = [(re.compile(r"\b" + re.escape(t) + r"\b", re.I), t, s) for t, s in FORESTIERISMI.items()]
    pex = [(re.compile(r"\b" + re.escape(t) + r"\b", re.I), t, s) for t, s in PSEUDO_EXACT.items()]
    pst = [(re.compile(r"\b" + st + _ARE + r"\b", re.I), st + "are", s) for st, s in PSEUDO_STEMS.items()]
    cal = [(re.compile(r"\b" + rx + r"\b", re.I), disp, nota) for rx, disp, nota in CALCHI_PATTERNS]
    return fore, pex + pst, cal


def _scan_patterns(sentences, patterns, label_key):
    """Cerca i pattern e restituisce hit con conteggio ed esempi (max 2 per termine)."""
    hits = []
    for rx, display, payload in patterns:
        count, examples = 0, []
        for s in sentences:
            found = rx.findall(s)
            if found:
                count += len(found)
                if len(examples) < 2:
                    examples.append(s if len(s) <= 90 else s[:87] + "…")
        if count:
            hits.append({"term": display, label_key: payload, "conteggio": count, "esempi": examples})
    hits.sort(key=lambda h: -h["conteggio"])
    return hits


def scan_anglicisms(text, sentences):
    fore_p, pseudo_p, calchi_p = _build_patterns()
    forestierismi = _scan_patterns(sentences, fore_p, "suggerito")
    pseudo = _scan_patterns(sentences, pseudo_p, "suggerito")
    calchi = _scan_patterns(sentences, calchi_p, "nota")
    totale = sum(h["conteggio"] for h in forestierismi) + sum(h["conteggio"] for h in pseudo)
    return {
        "forestierismi": forestierismi,
        "pseudo_anglicismi": pseudo,
        "calchi_da_verificare": calchi,
        "totale_forestierismi": totale,
        "hint": "Occorrenze da valutare nel registro e nel contesto; nessuna sostituzione automatica.",
    }


def mattr(words, window=100):
    """Moving-Average TTR: vocabolario robusto alla lunghezza (media su finestre scorrevoli)."""
    if len(words) < window:
        return None
    counts = Counter(words[:window])
    total, count = len(counts) / window, 1
    for i in range(window, len(words)):
        old = words[i-window]
        counts[old] -= 1
        if not counts[old]:
            del counts[old]
        counts[words[i]] += 1
        total += len(counts) / window
        count += 1
    return total / count


def split_paragraphs(text):
    """Paragrafi su righe vuote; se il testo è un blocco unico, finestre di ~5 frasi."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if len(paras) > 1:
        return paras
    sents = split_sentences(text)
    return [" ".join(sents[i:i + 5]) for i in range(0, len(sents), 5)] or [text]


def paragraph_register(text):
    """ASL e quota di frasi corte per paragrafo; nessuna inferenza sull'origine."""
    flagged = []
    for idx, p in enumerate(split_paragraphs(text), 1):
        s = split_sentences(p)
        if not s:
            continue
        lengths = [len(tokenize_words(x)) for x in s]
        asl_p = sum(lengths) / len(lengths)
        short_p = sum(1 for L in lengths if 0 < L < 7) / len(lengths)
        if asl_p < 11 and short_p > 0.35:
            flagged.append({
                "paragrafo": idx,
                "asl": round(asl_p, 1),
                "short_ratio": round(short_p, 2),
                "anteprima": p if len(p) <= 90 else p[:87] + "…",
            })
    return flagged


def analyze(text, lang="it"):
    if lang != "it":
        raise ValueError("Lingua non supportata: l'analizzatore è solo italiano")
    text = normalize_text(text)
    if not tokenize_words(text):
        raise ValueError("Il campione non contiene parole")
    sentences = split_sentences(text)
    words = tokenize_words(text)
    n_words = len(words)
    n_sentences = max(1, len(sentences))

    # Lunghezza frasi (in parole)
    sent_lengths = [len(tokenize_words(s)) for s in sentences] or [0]
    asl = sum(sent_lengths) / len(sent_lengths)
    rhythm_std = statistics.pstdev(sent_lengths) if len(sent_lengths) > 1 else 0.0
    # % di frasi cortissime (< 7 parole): descrive la distribuzione delle lunghezze.
    very_short = sum(1 for L in sent_lengths if 0 < L < 7)
    short_ratio = very_short / len(sent_lengths) if sent_lengths else 0.0
    # Disabilitata la vecchia euristica sui verbi: non consente una stima attendibile.
    nominal_ratio = None

    # TTR (Type-Token Ratio) + MATTR (robusto alla lunghezza del campione)
    ttr = len(set(words)) / n_words if n_words else 0.0
    mattr_val = mattr(words, window=100)

    # Punteggiatura interna per frase (virgole, ; : — incisi)
    internal_punct = len(re.findall(r"[,;:—–\(\)]", text))
    punct_per_sentence = internal_punct / n_sentences

    # % dialogo: righe/segmenti con virgolette o trattino di battuta
    dialogue_chars = len(re.findall(r"[«»\"“”]", text))
    dialogue_lines = len(re.findall(r"(^|\n)\s*[—–-]\s+\S", text))
    # stima grezza della quota di dialogo sul testo
    dialogue_word_count = sum(dialogue_mask(text))
    dialogue_ratio = dialogue_word_count / n_words

    # Densità avverbi in -mente e filler
    adverbs_mente = len(re.findall(r"\b\w+mente\b", text.lower()))
    adverb_density = adverbs_mente / n_words if n_words else 0.0
    fillers = sum(1 for w in words if w in IT_FILLERS)
    filler_density = fillers / n_words if n_words else 0.0

    # --- Mappatura sugli assi StyleDNA quantitativi (1-10) ---
    # SENTENCE_LENGTH: ~8 parole -> 1, ~26+ -> 10
    sl = clamp(round((asl - 8) / 2) + 1)
    # RHYTHM_VARIATION: dev.std bassa (~2) -> 2, alta (~12+) -> 10
    rv = clamp(round(rhythm_std / 1.5) + 1)
    # VOCABULARY_RICHNESS: proxy da MATTR; non misura ricchezza letteraria.
    vr = clamp(round((mattr_val - 0.35) * 14) + 1) if mattr_val is not None and n_words >= 300 else None
    # SYNTAX_COMPLEXITY: ~0.5 segni/frase -> 1, ~5+ -> 10
    sc = clamp(round(punct_per_sentence * 1.8))
    # DIALOGUE_WEIGHT: 0% -> 1, 60%+ -> 10
    dw = clamp(round(dialogue_ratio * 15) + 1)

    # Tic ripetuti (N-Grams): bigrammi e trigrammi che ricorrono troppo
    bigrams = find_repeated_ngrams(words, 2, min_count=max(4, n_words // 400))
    trigrams = find_repeated_ngrams(words, 3, min_count=max(3, n_words // 600))

    # Densità di frasi brevi, senza diagnosi di provenienza o giudizio stilistico.
    paragraphs_flagged = paragraph_register(text)
    if asl < 11 and short_ratio > 0.35:
        density_severity = "short_dense"
    elif asl < 13 and short_ratio > 0.28:
        density_severity = "short_mixed"
    else:
        density_severity = "ok"
    anglicism_scan = scan_anglicisms(text, sentences)
    llm_tics = detect_llm_tics(text, sentences, words, n_words)
    pip = pip_hints(text, sentences, n_words)

    return {
        "analyzer_version": ANALYZER_VERSION,
        "limitations": ["Regex: segmentazione e dialoghi approssimati", "Citazioni possono essere contate come dialogo", "Nessuna diagnosi di provenienza AI o qualità", "Frasi nominali non misurate"],
        "metrics": {
            "words": n_words,
            "sentences": len(sentences),
            "avg_sentence_length": round(asl, 2),
            "sentence_length_stdev": round(rhythm_std, 2),
            "very_short_sentence_ratio": round(short_ratio, 3),
            "nominal_sentence_ratio": nominal_ratio,
            "type_token_ratio": round(ttr, 4),
            "mattr": round(mattr_val, 4) if mattr_val is not None else None,
            "internal_punct_per_sentence": round(punct_per_sentence, 2),
            "dialogue_ratio": round(dialogue_ratio, 4),
            "dialogue_markers": dialogue_chars + dialogue_lines,
            "adverb_mente_density": round(adverb_density, 4),
            "filler_density": round(filler_density, 4),
        },
        "styledna_quantitative_suggestion": {
            "SENTENCE_LENGTH": sl,
            "RHYTHM_VARIATION": rv,
            "VOCABULARY_RICHNESS": vr,
            "SYNTAX_COMPLEXITY": sc,
            "DIALOGUE_WEIGHT": dw,
        },
        "styledna_qualitative_todo": [
            "REGISTER_LEVEL", "FIGURATIVE_DENSITY", "SHOW_VS_TELL", "SENSORY_DEPTH",
            "EMOTIONAL_TEMP", "SUBTEXT_DENSITY", "AUTHORIAL_PRESENCE",
        ],
        "tic_detection": {
            "repeated_bigrams": bigrams,
            "repeated_trigrams": trigrams,
            "hint": "Frasi ricorrenti = possibili tic da variare (vedi anti-ai.md §Meta-principio).",
        },
        "italian_register": {
            "anglo_translated_flag": None,
            "note": "Campo legacy disabilitato: non si inferisce una traduzione dal ritmo.",
            "severity": density_severity,
            "paragraphs_flagged": paragraphs_flagged,
            "diagnosis": "Distribuzione descrittiva del ritmo; valutare nel registro scelto, senza soglie di qualità.",
        },
        "anglicism_scan": anglicism_scan,
        "llm_tics": llm_tics,
        "pip_hints": pip,
        "baseline": {
            "ASL": round(asl, 2),
            "RHYTHM_VARIATION": round(rhythm_std, 2),
            "TTR": round(ttr, 4),
            "MATTR": round(mattr_val, 4) if mattr_val is not None else None,
            "dialogue_ratio": round(dialogue_ratio, 4),
            "analyzer_version": ANALYZER_VERSION,
            "window": 100,
            "words": n_words,
            "nota": "Confrontare con il corpus approvato; non sostituire automaticamente la baseline.",
        },
        "notes": {
            "high_adverb_density": adverb_density > 0.03,
            "colloquial_signal": filler_density > 0.01,
            "short_sample_warning": n_words < 300,
            "short_sample_note": (
                "Campione < 300 parole: TTR (e quindi VOCABULARY_RICHNESS) "
                "è poco affidabile. VR non viene suggerito: usa un estratto più lungo."
                if n_words < 300 else ""
            ),
        },
    }


def main():
    ap = argparse.ArgumentParser(description="Analisi stilometrica BookForge")
    ap.add_argument("file", help="Percorso del file di testo da analizzare")
    ap.add_argument("--lang", default="it", choices=["it"], help="Unica lingua supportata: it")
    ap.add_argument("--json", action="store_true", help="Output in formato JSON")
    args = ap.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"Errore lettura file: {e}", file=sys.stderr)
        sys.exit(1)

    if not text.strip():
        print("Errore: file vuoto.", file=sys.stderr)
        sys.exit(1)

    try:
        result = analyze(text, args.lang)
    except ValueError as e:
        print(f"Errore: {e}", file=sys.stderr)
        sys.exit(1)
    result["lang"] = args.lang

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        m = result["metrics"]
        s = result["styledna_quantitative_suggestion"]
        print(f"Parole: {m['words']} | Frasi: {m['sentences']} | ASL: {m['avg_sentence_length']}")
        print(f"Dev.std lunghezze: {m['sentence_length_stdev']} | TTR: {m['type_token_ratio']}")
        print(f"Frasi cortissime: {m['very_short_sentence_ratio']*100:.0f}% | Nominali: non misurate")
        print(f"Punteggiatura interna/frase: {m['internal_punct_per_sentence']} | Dialogo: {m['dialogue_ratio']*100:.1f}%")
        print(f"Densità avverbi -mente: {m['adverb_mente_density']} | Filler: {m['filler_density']}")
        ir = result["italian_register"]
        badge = ir["severity"]
        print(f"\n🇮🇹 Registro italiano: {badge}")
        print(f"   {ir['diagnosis']}")
        for pf in ir.get("paragraphs_flagged", [])[:5]:
            print(f"   §{pf['paragrafo']}: ASL {pf['asl']}, corte {int(pf['short_ratio']*100)}% — {pf['anteprima']}")
        ang = result["anglicism_scan"]
        if ang["forestierismi"] or ang["pseudo_anglicismi"] or ang["calchi_da_verificare"]:
            print("\n🔤 Anglicismi:")
            for h in ang["forestierismi"][:8]:
                print(f"   «{h['term']}» ×{h['conteggio']} → {h['suggerito']}")
            for h in ang["pseudo_anglicismi"][:8]:
                print(f"   «{h['term']}» ×{h['conteggio']} → {h['suggerito']}")
            for h in ang["calchi_da_verificare"][:6]:
                print(f"   ? «{h['term']}» ×{h['conteggio']} — {h['nota']}")
        tics = result["tic_detection"]
        if tics["repeated_bigrams"] or tics["repeated_trigrams"]:
            print("\n🔁 Tic ricorrenti (da variare):")
            for g, c in (tics["repeated_trigrams"] + tics["repeated_bigrams"])[:8]:
                print(f"   «{g}» × {c}")
        lt = result["llm_tics"]
        warns = [(k, v) for k, v in lt.items() if isinstance(v, dict) and v.get("warn")]
        if warns:
            print("\n🤖 Tic da LLM (spie post-scrittura — NON bersagli):")
            labels = {"antitesi_riflesso": "antitesi-riflesso", "terzine": "terzine",
                      "trattino": "trattino drammatico",
                      "frase_sentenza_chiusura": "epigrammi in chiusura di paragrafo",
                      "schema_somatico": "schema somatico ripetuto",
                      "come_se_raffica": "raffica di «come se»",
                      "aggettivi_portata": "aggettivi-portata (mood vago)",
                      "gonfiaggio_significativita": "gonfiaggio della significatività (enfasi vuota)"}
            for k, v in warns:
                if k == "schema_somatico":
                    detail = ", ".join(f"«{h['ngram']}»×{h['conteggio']}" for h in v["ricorrenze"][:3])
                elif k in ("aggettivi_portata", "gonfiaggio_significativita"):
                    detail = ", ".join(f"«{w}»" for w in v["esempi"][:4]) + f" (×{v['totale']})"
                elif k == "come_se_raffica":
                    detail = f"×{v['totale']}, max {v['max_per_paragrafo']}/paragrafo"
                else:
                    detail = v.get("conteggio", v.get("totale", v.get("ratio", "")))
                print(f"   ⚠️ {labels.get(k, k)}: {detail} — vedi anti-ai.md")
        else:
            print("\n🤖 Tic da LLM: nessuna spia sopra soglia.")
        print("\nSuggerimento StyleDNA (assi quantitativi):")
        print(f"  SL:{s['SENTENCE_LENGTH']} SC:{s['SYNTAX_COMPLEXITY']} RV:{s['RHYTHM_VARIATION']} "
              f"VR:{s['VOCABULARY_RICHNESS']} DW:{s['DIALOGUE_WEIGHT']}")
        print("  (RL, FD, ST, SD, ET, SUB, AP → valutazione qualitativa dell'LLM)")


if __name__ == "__main__":
    main()
