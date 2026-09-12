---
File: BF_11_Series_Continuity_Bible.md
Versione: 1.0
Ultimo aggiornamento: 2026-04-28
Modifiche: Versione iniziale
---

# SERIES CONTINUITY BIBLE — Bibbia di Continuità per Collane e Sequel

Questo file definisce il sistema di **Bibbia di Continuità**: un documento strutturato che il GPT compila e mantiene aggiornato per garantire coerenza assoluta tra capitoli, volumi e sequel.

---

## COS'È LA BIBBIA DI CONTINUITÀ

La Bibbia di Continuità è la **fonte di verità unica** per tutto l'universo narrativo (fiction) o per l'intero ecosistema di contenuti (non-fiction) di una serie/collana.

### Scopo
- Evitare contraddizioni nei fatti, nella timeline, nei personaggi
- Mantenere coerenza tra volumi diversi scritti in sessioni separate
- Fornire al GPT un riferimento strutturato da consultare **prima di ogni capitolo**
- Tracciare l'evoluzione di personaggi, relazioni, trame e concetti volume per volume

### Quando compilarla
| Situazione | Quando |
|------------|--------|
| Percorso D — Nuova collana da zero | Alla fine della Fase 3 (indice), prima di scrivere |
| Percorso D — Sequel da libro esistente | Dopo l'analisi del libro precedente (compilazione automatica) |
| Percorso D — Nuovo volume di collana in corso | L'utente la fornisce o il GPT la ricostruisce |
| Percorso A — Libro singolo (opzionale) | Su richiesta dell'utente, alla fine della Fase 3 |
| Percorso C — Continuare libro (opzionale) | Su richiesta, dopo l'analisi stilistica |

### Chi la compila
**Il GPT la compila automaticamente.** L'utente conferma, corregge e integra.

---

## TEMPLATE — SCHEMA LOGICO (LOGIC_MAP)

Lo Schema Logico documenta **i fatti, le regole e la sequenza degli eventi** dell'universo narrativo.

```
📐 SCHEMA LOGICO — [Titolo della serie]

═══ TIMELINE ═══

Volume [N]:
├── [Data/Momento] — [Evento]
├── [Data/Momento] — [Evento]
└── ...

Note sulla cronologia: [tempo lineare / flashback / parallelo / salti temporali]
Durata complessiva della storia: [...]

═══ FATTI STABILITI ═══
(Verità del mondo narrativo che NON possono essere contraddette)

1. [Fatto] — Stabilito in: Vol. [N], Cap. [N]
2. [Fatto] — Stabilito in: Vol. [N], Cap. [N]

═══ REGOLE DEL MONDO ═══

Sistema magico / tecnologico:
├── Regola 1: [...]
├── Limitazioni: [...]
└── Costi / conseguenze: [...]

Leggi / costumi / struttura sociale: [...]
Geografia / ambientazione: [...]

═══ CATENE CAUSA-EFFETTO ═══

1. [Evento A] → [Conseguenza B] → [Situazione C]

═══ MISTERI E RIVELAZIONI ═══

| Mistero | Stato | Noto a chi | Rivelato in | Note |
|---------|-------|------------|-------------|------|
| [...] | 🔒 Nascosto / 🔓 Rivelato | [...] | Vol.X Cap.Y | [...] |

═══ PROMESSE NARRATIVE APERTE ═══

1. [Promessa] — Creata in: Vol. [N], Cap. [N] — Stato: ⏳ Aperta / ✅ Risolta

═══ STATO ATTUALE DEL MONDO ═══

[Descrizione sintetica della situazione corrente]
```

---

## TEMPLATE — SCHEMA RELAZIONALE (RELATION_MAP)

Lo Schema Relazionale documenta **le connessioni tra personaggi, luoghi, oggetti e fazioni**.

```
🔗 SCHEMA RELAZIONALE — [Titolo della serie]

═══ RELAZIONI TRA PERSONAGGI ═══

[Personaggio A] ←→ [Personaggio B]
├── Tipo: [parentela / amicizia / amore / rivalità / alleanza / conflitto / mentore-allievo]
├── Stato attuale: [attiva / spezzata / segreta / in evoluzione]
├── Evoluzione:
│   ├── Vol. 1: [stato]
│   └── Vol. N: [stato attuale]
└── Note: [...]

═══ MAPPA DELLE FAZIONI / GRUPPI ═══

Fazione 1: [Nome]
├── Membri: [elenco]
├── Obiettivo: [...]
├── Alleata con: [...] / In conflitto con: [...]
└── Stato: [attiva / sciolta / in crisi]

═══ RELAZIONI PERSONAGGIO-LUOGO ═══

| Personaggio | Luogo | Tipo di legame | Volume |
|-------------|-------|----------------|--------|
| [...] | [...] | Residenza / Origine / Esilio | Vol. N |

═══ RELAZIONI PERSONAGGIO-OGGETTO ═══

| Personaggio | Oggetto | Tipo di legame | Volume |
|-------------|---------|----------------|--------|
| [...] | [...] | Possesso / Ricerca / Perdita | Vol. N |

═══ MAPPA VISIVA (consultazione rapida) ═══

[Protagonista] ——amore——→ [Personaggio B]
       |                         |
    mentore                   sorella
       ↓                         ↓
[Mentore]               [Personaggio C] ——rivale——→ [Antagonista]
```

---

## TEMPLATE — SCHEDA PERSONAGGI (CHARACTER_BIBLE)

### Personaggio principale — Template completo

```
👤 SCHEDA PERSONAGGIO — [Nome]

═══ IDENTITÀ ═══
Nome completo: [...]
Soprannomi / Alias: [...]
Età: [...] (inizio) → [...] (attuale)

═══ ASPETTO FISICO ═══
Altezza / Corporatura: [...]
Capelli / Occhi: [...]
Segni particolari: [...]
Impressione che fa: [...]

═══ PERSONALITÀ ═══
Tratti dominanti: [3-5 tratti]
Difetto fatale (flaw): [...]
Forza principale: [...]
Paure: [...]
Desideri profondi: [...]
Tic / Abitudini: [...]
Sotto pressione: [come reagisce]

═══ BACKGROUND ═══
Famiglia: [...]
Traumi significativi: [...]
Segreti: [cosa nasconde e a chi]

═══ MOTIVAZIONE ═══
Obiettivo dichiarato: [...] / Obiettivo reale: [...]
Ostacolo interno: [...] / Ostacolo esterno: [...]
Posta in gioco: [...]

═══ ARCO EVOLUTIVO ═══
Chi è all'inizio: [...] → Chi diventa alla fine: [...]
Evoluzione per volume:
├── Vol. 1: [stato, trasformazione]
└── Vol. N: [stato attuale]

═══ VOCE ═══
Come parla: [registro, ritmo]
Intercalari: [...]
Differenze con altri personaggi: [...]

═══ CONOSCENZE ═══

| Informazione | La sa? | Da quando | Volume/Capitolo |
|-------------|--------|-----------|----------------|
| [...] | ✅ Sì / ❌ No / 🔶 Sospetta | [...] | Vol.X Cap.Y |

═══ STATO PER VOLUME ═══

| Volume | Stato | Posizione | Situazione |
|--------|-------|-----------|------------|
| Vol. 1 | Vivo | [dove] | [situazione] |
```

### Personaggio secondario — Template sintetico

```
👤 [Nome] — Personaggio secondario
Ruolo: [mentore / alleato / antagonista / ...]
Tratti chiave: [2-3 tratti]
Funzione narrativa: [perché esiste]
Relazione con il protagonista: [...]
Voce: [come parla]
Arco: [statico / evolve / muore / ...]
Presente in: Vol. [elenco]
Stato attuale: [...]
```

---

## ADATTAMENTO PER NON-FICTION (COLLANE DIDATTICHE)

```
📚 BIBBIA DI CONTINUITÀ — Collana Non-Fiction: [Titolo]

═══ MAPPA CONCETTUALE ═══

Volume 1: [Titolo]
├── Concetti introdotti: [elenco]
├── Terminologia definita: [elenco]
├── Livello: [base / intermedio / avanzato]
└── Prerequisiti: [nessuno]

Volume 2: [Titolo]
├── Concetti introdotti: [elenco]
├── Concetti ripresi dal Vol. 1: [elenco]
└── Prerequisiti: [Vol. 1]

═══ GLOSSARIO UNIFICATO ═══

| Termine | Definizione | Introdotto in | Usato in |
|---------|-------------|--------------|----------|
| [...] | [...] | Vol. 1, Cap. 3 | Vol. 1, 2, 3 |

═══ PROGRESSIONE DIDATTICA ═══
Vol. 1: [Cosa impara il lettore]
Vol. 2: [Cosa impara — costruisce su Vol. 1]

═══ RIFERIMENTI INCROCIATI ═══

| Da Volume | Riferisce a | Contesto |
|-----------|-------------|----------|
| Vol. 2, Cap. 4 | Vol. 1, Cap. 2 | Riprende il concetto di [...] |

═══ PROMESSA DELLA COLLANA ═══
Complessiva: [cosa ottiene completando tutta la collana]
Per volume: [cosa ottiene da ogni volume]

═══ COERENZA STILISTICA ═══
Tono: [uniforme tra volumi]
Formato capitoli: [struttura ricorrente]
Elementi ricorrenti: [box, checklist, esercizi]
```

---

## PROTOCOLLO DI AGGIORNAMENTO DELLA BIBBIA

### Regole operative

1. **PRIMA di ogni capitolo**: consultare la Bibbia per verificare coerenza
2. **DOPO ogni capitolo**: aggiornare la Bibbia con nuovi elementi introdotti
3. **ALLA FINE di ogni volume**: produrre lo Snapshot di Fine Volume
4. **ALL'INIZIO di ogni nuovo volume**: rileggere l'intera Bibbia e lo Snapshot precedente
5. **MAI cancellare**: le informazioni superate vanno storicizzate, non cancellate

### Checklist post-capitolo

```
☐ Nuovi personaggi introdotti? → Aggiungere alla Character Bible
☐ Nuove relazioni create o cambiate? → Aggiornare Relation Map
☐ Nuovi fatti stabiliti? → Aggiungere ai Fatti Stabiliti
☐ Timeline aggiornata? → Aggiungere eventi
☐ Misteri rivelati o nuovi misteri? → Aggiornare Misteri e Rivelazioni
☐ Conoscenze dei personaggi cambiate? → Aggiornare tabella Conoscenze
☐ Promesse narrative create? → Aggiungere alle Promesse Aperte
```

### Checklist pre-capitolo

```
☐ Tratti, voce e stato dei personaggi coerenti con la Bibbia?
☐ Timeline coerente con gli eventi già stabiliti?
☐ Fatti menzionati non contraddicono i Fatti Stabiliti?
☐ Relazioni riflettono lo stato attuale nella Relation Map?
☐ Conoscenze dei personaggi rispettate (nessuno sa cose che non dovrebbe)?
☐ Regole del mondo rispettate?
```

---

## TEMPLATE — SNAPSHOT DI FINE VOLUME

```
📸 SNAPSHOT DI FINE VOLUME — [Titolo] — Volume [N]

═══ STATO DEI PERSONAGGI ═══

| Personaggio | Stato | Posizione | Situazione emotiva |
|-------------|-------|-----------|--------------------|
| [Protagonista] | Vivo | [dove] | [come sta] |
| [Personaggio B] | Morto | — | Morto in Cap. [N] |

═══ TRAME RISOLTE ═══
✅ [Trama 1] — Risolta in Cap. [N]: [come]

═══ TRAME IRRISOLTE ═══
⏳ [Trama 1] — Stato: [dove si è fermata]

═══ GANCI PER IL VOLUME SUCCESSIVO ═══
🪝 [Hook 1]: [descrizione]

═══ FORESHADOWING ATTIVO ═══
🌱 [Elemento 1] — Seminato in Cap. [N]

═══ PROMESSE AL LETTORE NON ANCORA MANTENUTE ═══
📌 [Promessa 1] — Fatta in Vol. [N], Cap. [N]

═══ EVOLUZIONE DEL TEMA ═══
Tema principale: [...] — Dove si è sviluppato: [...] — Dove potrebbe andare: [...]

═══ NOTE PER IL PROSSIMO VOLUME ═══
- [Nota 1]
- [Nota 2]
```

---

## REVISIONE DI CONTINUITÀ INTER-VOLUME

```
📝 REVISIONE DI CONTINUITÀ INTER-VOLUME — Volume [N]

═══ COERENZA CON I VOLUMI PRECEDENTI ═══
☐ Nessuna contraddizione con i Fatti Stabiliti
☐ Timeline coerente con gli eventi dei volumi precedenti
☐ Regole del mondo rispettate
☐ Aspetto fisico e tratti dei personaggi coerenti
☐ Relazioni coerenti con lo stato documentato
☐ Conoscenze dei personaggi rispettate
☐ Tono e stile coerenti con i volumi precedenti
☐ Voce dei personaggi riconoscibile e coerente
☐ Luoghi e ambientazioni descritti coerentemente

═══ GESTIONE TRAME ═══
☐ Trame irrisolte dal volume precedente gestite
☐ Foreshadowing precedente utilizzato o mantenuto attivo
☐ Promesse narrative in corso di risoluzione
☐ Nessuna trama dimenticata senza motivo

═══ ARCO DI SERIE ═══
☐ La macro-trama è avanzata
☐ L'escalation è credibile
☐ I personaggi sono cresciuti rispetto al volume precedente
☐ Il volume aggiunge qualcosa di nuovo (non è riempitivo)
☐ Il lettore ha motivo per leggere il volume successivo

═══ AUTONOMIA DEL VOLUME ═══
☐ Un nuovo lettore può comprendere la storia? (se previsto)
☐ Il recap è sufficiente ma non invasivo?
☐ Il volume ha una propria trama con inizio, sviluppo e conclusione?

═══ GIUDIZIO ═══
[SEAMLESS / BUONO / ACCETTABILE / DISCONTINUITÀ RILEVATE]
Note: [...]
Azioni correttive: [...]
```

---

## REGOLE DI SERIALIZZAZIONE

### Per Fiction

1. **Ogni volume deve avere un proprio arco narrativo** — il lettore deve sentire una risoluzione parziale
2. **Il primo capitolo di ogni sequel** deve ri-orientare il lettore senza essere un riassunto noioso
3. **L'escalation tra volumi** deve essere naturale, non inflazionistica
4. **I personaggi devono crescere** volume per volume
5. **I cliff-hanger di fine volume** devono essere significativi, non artificiali
6. **Variazione dei pattern narrativi**: evitare di ripetere le stesse strutture di scena (es. lo stesso tipo di scontro, la stessa dinamica di risoluzione dei problemi) nei vari volumi per garantire molteplicità e freschezza.
7. **La Bibbia di Continuità è sacra** — se qualcosa la contraddice, il GPT si ferma e segnala

### Per Non-Fiction

1. **Ogni volume deve essere autosufficiente** — valore anche senza gli altri
2. **La progressione deve essere chiara** — il lettore sa cosa serve prima
3. **La terminologia deve essere coerente** — stessi termini in tutta la collana
4. **I riferimenti incrociati** devono essere espliciti e precisi
5. **Il formato deve essere coerente** — stessa struttura tra volumi
