---
File: BF_06_KDP_Package_Template.md
Versione: 1.0
Ultimo aggiornamento: 2026-04-27
Modifiche: Versione iniziale
---

# KDP PACKAGE TEMPLATE — Template pacchetto editoriale KDP

## Istruzioni d'uso
Questo template viene usato nella Fase 6. Ogni campo deve essere compilato con contenuti specifici per il progetto, NON generici. I testi commerciali devono essere coerenti con il posizionamento definito nella Fase 2 e con la Scheda Strategica della Fase 1.

---

## 1. DATI IDENTIFICATIVI

| Campo | Valore |
|-------|--------|
| Titolo definitivo | [max 200 caratteri, keyword inclusa] |
| Sottotitolo | [5-15 parole, beneficio + target] |
| Autore | [nome autore] |
| Lingua | [lingua del libro] |
| Genere/Categoria | [genere principale] |

### Criteri per il titolo
- 3-8 parole (ideale: 4-6)
- Contiene almeno 1 keyword principale
- Chiaro: il lettore capisce immediatamente il tema
- Memorabile: facile da ricordare e cercare
- Differenziato: non si confonde con competitor
- NON usa: numeri criptici, giochi di parole incomprensibili, titoli troppo lunghi

### Criteri per il sottotitolo
- 5-15 parole
- Specifica la promessa o il beneficio
- Può contenere keyword secondarie
- Formule efficaci:
  - "[Beneficio] per [target]"
  - "[Metodo] per [risultato]"
  - "Come [azione] per [beneficio]"
  - "La guida [aggettivo] per [target]"

---

## 2. TESTI AMAZON

### Descrizione breve (max 150 caratteri)
```
[Hook + promessa principale in una riga]
```
Questo testo appare nei risultati di ricerca e nelle anteprime. Deve catturare l'attenzione in pochi secondi.

### Descrizione lunga (max 4000 caratteri)
```html
<b>[HOOK — 1-2 frasi che catturano l'attenzione]</b>

<br><br>

[PAIN POINT — Descrivi il problema o il desiderio del lettore. 2-3 frasi che fanno sentire il lettore compreso.]

<br><br>

[PROMESSA — Cosa offre questo libro come soluzione. 2-3 frasi chiare e specifiche.]

<br><br>

<b>In questo libro scoprirai:</b>

<br><br>

✅ [Beneficio 1 — specifico e verificabile]<br>
✅ [Beneficio 2 — specifico e verificabile]<br>
✅ [Beneficio 3 — specifico e verificabile]<br>
✅ [Beneficio 4 — specifico e verificabile]<br>
✅ [Beneficio 5 — specifico e verificabile]<br>
✅ [Beneficio 6 — specifico e verificabile]<br>
✅ [Beneficio 7 — specifico e verificabile]<br>

<br>

[DIFFERENZIAZIONE — Cosa rende questo libro diverso dagli altri. 1-2 frasi.]

<br><br>

[SOCIAL PROOF / CREDIBILITÀ — Credenziali dell'autore, esperienze, risultati. Se applicabile.]

<br><br>

<b>[CTA — Invito all'azione chiaro e diretto]</b>
```

### HTML permesso su Amazon
| Tag | Uso |
|-----|-----|
| `<b>` | Grassetto |
| `<i>` | Corsivo |
| `<br>` | A capo |
| `<h1>` — `<h6>` | Titoli (supporto variabile) |
| `<ul><li>` | Elenco puntato |
| `<ol><li>` | Elenco numerato |
| `<p>` | Paragrafo |

---

## 3. KEYWORD KDP

### Le 7 keyword (max 50 caratteri ciascuna)

| # | Keyword | Tipo | Note |
|---|---------|------|------|
| 1 | [keyword] | Principale | Alta pertinenza |
| 2 | [keyword] | Principale | Volume buono |
| 3 | [keyword] | Secondaria | Specifica |
| 4 | [keyword] | Long-tail | Bassa competizione |
| 5 | [keyword] | Long-tail | Nicchia specifica |
| 6 | [keyword] | Secondaria | Sinonimo/variante |
| 7 | [keyword] | Cross-genre | Pubblico adiacente |

### Regole keyword
1. ❌ No singole parole generiche
2. ❌ No ripetizione del titolo esatto
3. ❌ No nomi di autori famosi
4. ❌ No "bestseller", "free", "discount", "gratis"
5. ✅ Mescolare keyword di nicchia e di volume
6. ✅ Includere almeno 2 long-tail
7. ✅ Pensare come cercherebbe il lettore target
8. ✅ Ogni keyword deve essere pertinente al contenuto reale

---

## 4. CATEGORIE KDP

| # | Categoria | Motivazione |
|---|-----------|-------------|
| 1 | [Categoria principale] | [perché è pertinente] |
| 2 | [Categoria secondaria] | [perché è pertinente] |
| 3 | [Categoria alternativa] | [perché è pertinente, meno competitiva] |

---

## 5. TESTI PROMOZIONALI

### Sinossi (200-300 parole)
```
[Riassunto del libro che comunica tema, approccio e valore.
Per non-fiction: problema → metodo → risultato atteso.
Per fiction: ambientazione → personaggio → conflitto → posta in gioco.]
```

### Logline (1 frase, max 30 parole)
```
[Una frase che cattura l'essenza del libro]
```
Formula non-fiction: "[Libro] è [cosa] che aiuta [chi] a [cosa] attraverso [come]."
Formula fiction: "Quando [evento], [protagonista] deve [azione] prima che [posta in gioco]."

### Pitch commerciale (3-5 frasi)
```
[Versione elevator pitch del libro. Usabile per email, social media, presentazioni.]
```

### Abstract (150-200 parole)
```
[Versione più formale/accademica della sinossi. Usabile per communication, press kit, biblioteche.]
```

### Testo quarta di copertina
```
[Il testo che appare sul retro del Paperback/Hardcover.
Struttura:
1. Hook (1-2 frasi)
2. Corpo (3-5 frasi che vendono il contenuto)
3. CTA o frase finale d'impatto
Opzionale: blurb/citazione]
```

---

## 6. BIO AUTORE

### Bio breve (max 100 parole)
```
[Nome Autore] [breve descrizione professionale e personale].
[Esperienza/credenziali rilevanti per il libro].
[Tocco personale: interessi, luogo, famiglia].
[Eventuale rimando a sito/social].
```

### Bio lunga (max 250 parole)
```
[Versione estesa con:
- Background professionale
- Motivazione per aver scritto il libro
- Credenziali e esperienza
- Altri libri pubblicati (se presenti)
- Visione o missione
- Dettagli personali
- Contatti/social]
```

---

## 7. BENEFICI PER IL LETTORE
```
Dopo aver letto questo libro, il lettore sarà in grado di:

1. [Beneficio concreto e misurabile]
2. [Beneficio concreto e misurabile]
3. [Beneficio concreto e misurabile]
4. [Beneficio concreto e misurabile]
5. [Beneficio concreto e misurabile]
6. [Beneficio concreto e misurabile] (opzionale)
7. [Beneficio concreto e misurabile] (opzionale)
```

### Regole
- Ogni beneficio deve essere SPECIFICO, non generico
- ❌ "Migliorerai la tua vita" → ✅ "Saprai creare una routine mattutina in 15 minuti"
- Ogni beneficio deve essere VERIFICABILE dal lettore
- I benefici devono essere COERENTI con il contenuto reale del libro

---

## 8. CALL TO ACTION

### CTA principale (per la descrizione Amazon)
```
[Invito all'azione chiaro. Es: "Scorri verso l'alto e clicca su Acquista ora per iniziare il tuo percorso."]
```

### CTA per la fine del libro
```
[Invito a lasciare una recensione, seguire l'autore, comprare il prossimo libro.
Es: "Se questo libro ti è stato utile, ti sarei grato per una recensione su Amazon. Il tuo feedback aiuta altri lettori a trovare questo libro."]
```

### CTA per la pagina autore
```
[Invito a scoprire gli altri libri o a connettersi.
Es: "Scopri tutti i miei libri su Amazon cercando [Nome Autore] oppure visita [sito web]."]
```

---

## 9. COPERTINA

### Prompt per generazione AI
```
[Prompt dettagliato per DALL·E, Midjourney o altro tool.
Includere: stile, colori, composizione, elementi, mood, testo da inserire, formato.]
```

### Indicazioni stile copertina
| Aspetto | Indicazione |
|---------|-------------|
| Colori principali | [palette specifica] |
| Font titolo | [serif/sans-serif, stile] |
| Font sottotitolo | [stile, peso] |
| Elementi visivi | [cosa deve apparire] |
| Mood/atmosfera | [es. professionale, misterioso, energetico] |
| Stile grafico | [illustrazione, foto, tipografico, minimalista, bold] |
| Riferimenti visivi | [copertine di riferimento, stili simili] |
| Formato | [eBook: 2560x1600px / Paperback: specificare trim size] |

---

## 10. PREZZO E FORMATO

### Indicazioni
| Aspetto | Raccomandazione |
|---------|-----------------|
| Formato consigliato | [eBook / Paperback / Hardcover / Tutti] |
| Prezzo eBook | $[X.XX] |
| Prezzo Paperback | $[X.XX] |
| Prezzo Hardcover | $[X.XX] (se applicabile) |
| KDP Select | [Sì / No / Da valutare] |
| Motivo KDP Select | [perché sì o perché no] |
| Distribuzione estesa | [Sì / No] |

### Logica di pricing
- eBook $2.99-$9.99: 70% royalty (range ottimale)
- Confrontare con i prezzi dei competitor
- Libri brevi (<100pp): fascia bassa ($2.99-$4.99)
- Libri medi (100-250pp): fascia media ($4.99-$9.99)
- Libri lunghi (>250pp): fascia media-alta ($7.99-$9.99)
- Paperback: mai sotto il costo di stampa + margine minimo

---

## 11. DISCLAIMER (se necessario)
```
[Disclaimer legale appropriato per il contenuto del libro.

Esempi:
- Salute: "Le informazioni contenute in questo libro non sostituiscono il parere di un medico..."
- Finanza: "Le informazioni contenute in questo libro sono a scopo educativo..."
- Fiction con fatti reali: "Questo è un'opera di narrativa. Qualsiasi somiglianza..."
- Contenuti AI: "Questo libro è stato scritto con l'assistenza di strumenti AI..."]
```

---

## 12. CHECKLIST PRE-PUBBLICAZIONE

```
═══ MANOSCRITTO ═══
☐ Testo completo e revisionato (Livello 2 o 3)
☐ Indice dei contenuti presente e funzionante
☐ Pagina copyright presente
☐ Pagina del titolo presente
☐ Dedica presente (se desiderata)
☐ Ringraziamenti presenti (se desiderati)
☐ Bio autore alla fine del libro
☐ CTA alla fine del libro
☐ Disclaimer presente (se necessario)
☐ Note/bibliografia presenti (se necessarie)

═══ FORMATTAZIONE ═══
☐ eBook: formattazione verificata su KDP Previewer
☐ eBook: indice navigabile con link
☐ eBook: nessuna numerazione di pagina
☐ Paperback: margini conformi alle specifiche KDP
☐ Paperback: numerazione pagine presente
☐ Paperback: font leggibile (11-12pt corpo testo)
☐ Immagini: min 300 DPI

═══ COPERTINA ═══
☐ Copertina fronte pronta
☐ Copertina retro pronta (Paperback/Hardcover)
☐ Dorso calcolato (Paperback/Hardcover)
☐ Risoluzione 300 DPI
☐ Formato corretto per il trim size scelto
☐ Anteprima copertina verificata

═══ AMAZON LISTING ═══
☐ Titolo e sottotitolo definitivi
☐ Descrizione Amazon scritta e formattata in HTML
☐ 7 keyword selezionate
☐ Categorie selezionate (max 3)
☐ Prezzo definito per ogni formato
☐ Bio autore scritta
☐ KDP Select: decisione presa

═══ LEGALE/AMMINISTRATIVO ═══
☐ Diritti di pubblicazione confermati
☐ Nessuna violazione copyright
☐ Disclaimer inseriti dove necessari
☐ Informazioni fiscali aggiornate su KDP
☐ Metodo di pagamento configurato
☐ ISBN (se necessario per distribuzione estesa)
☐ Contenuti AI dichiarati (se applicabile)

═══ REVISIONE FINALE ═══
☐ Ultima rilettura completata
☐ Anteprima verificata su tutti i formati
☐ Tutto il pacchetto editoriale è coerente e completo
```
