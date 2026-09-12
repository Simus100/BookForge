# BookForge 7.7.0 — modifiche effettive

La release rende il metodo più flessibile nella scrittura e più verificabile nella gestione del progetto. Questo documento descrive interventi realizzati; le attività future sono indicate separatamente.

**Base di lavoro:** i 13 file di progetto forniti dall'autore, in prevalenza 7.6.1, e il documento di consigli `llm-scrittura-creativa.md`. La repository è stata allineata a queste fonti a partire dal commit `963f6a2dbaa66f2777e419ec8324cbd3827c0b67` di `main`. Data delle verifiche: 12 settembre 2026.

## Risultato concreto

- Nuovo punto d'ingresso `SKILL.md`, riferimenti modulari e istruzioni adattabili a GPT/progetti.
- Dottrina editoriale rivista: intenzione, causalità, voce e contesto precedono gli indicatori numerici.
- Stato schema 2.0 con validazione eseguibile, salvataggio controllato, migrazione conservativa e vista Markdown derivata.
- Analizzatore italiano corretto nei casi coperti dai test e più esplicito sui propri limiti.
- README di presentazione, installazione, esempio vuoto e 40 test automatici.
- Vecchi documenti della repository conservati in `archive/legacy-main/`, separati dai moduli operativi.

## Interventi sui file forniti

| Fonte | Destinazione e modifica realizzata | Effetto atteso |
|---|---|---|
| `carta.md` | `references/carta.md`: principi positivi, tecniche contestuali, rimozione di quote universali | Preservare la voce evitando correzioni meccaniche |
| `anti-ai.md` | `references/anti-ai.md`: separati errori verificati, vincoli dell'autore e segnali da interpretare | Ridurre falsi allarmi e riscritture omologanti |
| `scrittura.md` | `references/scrittura.md`: funzione dell'unità, causalità, beat ricomposti nella scena, revisione ordinata | Migliorare leggibilità e conseguenze narrative |
| `psicologia.md` | `references/psicologia.md`: motivazioni e relazioni in azione; assi ed enneagramma facoltativi | Alleggerire schede e rigidità psicologiche |
| `antologia.md` | `references/antologia.md`: campioni separati per progetto, approvazione esplicita e baseline stabile | Evitare contaminazione e deriva della voce |
| `styledna.md` | `references/styledna.md`: conservati 12 assi e 17 preset; distinti 5 proxy quantitativi e 7 assi qualitativi; VR basato su MATTR | Usare il profilo come orientamento interpretabile |
| `continuita.md` | `references/continuita.md`: canone, ipotesi, credenze, conoscenze, promesse ed emendamenti con origine | Ridurre contraddizioni e rivelazioni indebite |
| `fasi.md` | `references/fasi.md`: percorso flessibile; revisione da struttura a forma; ricerca commerciale quando pertinente | Ridurre passaggi superflui |
| `percorsi.md` | `references/percorsi.md`: mantenute scorciatoie e modalità; recupero delle decisioni e deleghe entro il mandato | Riprendere il lavoro senza menu o conferme ripetitive |
| `generi.md` | `references/generi.md`: conservate strutture, generi e worldbuilding; lunghezze indicative, domanda da verificare, criteri per formati diversi | Evitare di applicare al saggio o al libro per bambini le stesse regole del romanzo |
| `kdp.md` | `references/kdp.md`: fonti/data/mercato nelle ricerche; distinzione preparazione editoriale e verifica del file; classificazione AI da verificare sulle policy correnti | Consegnare materiali con limiti e verifiche espliciti |
| `stato-bsr.md` | `references/stato-bsr.md`: JSON canonico schema 2.0, manifest, hash, cursore, lifecycle e protocollo salva/carica | Ripresa controllabile tramite file effettivamente accessibili |
| `stylometry.py` | `scripts/stylometry.py`: normalizzazione Unicode/apostrofi, segmentazione migliorata, dialoghi lunghi e annidati, PIP per posizione dei token, MATTR a finestra | Rendere i conteggi più coerenti e riproducibili |

Gli effetti attesi sono ipotesi di prodotto: non sono risultati commerciali o preferenze dei lettori già misurati.

## Refactoring dello stato e strumenti aggiunti

| Componente | Comportamento implementato |
|---|---|
| `schemas/bookforge_state.schema.json` | Tipi e vincoli dello stato 2.0; ID per progetti, volumi, capitoli, scene, personaggi, fatti e decisioni |
| `scripts/validate_state.py` | Controllo struttura, ID/riferimenti, accettazione, emendamenti, promesse, percorsi sicuri, file richiesti e SHA-256; JSON duplicato/non finito rifiutato |
| `scripts/state_io.py` | Revisione attesa, lock cooperativo, backup precedente e sostituzione atomica del JSON; blocco di riscritture della storia canonica, cambi di progetto e perdita di promesse |
| `scripts/migrate_state.py` | Migrazione 7.6/7.6.1 in candidato da rivedere; payload originale conservato; nessuna accettazione inventata né sovrascrittura dei file esistenti |
| `scripts/render_state.py` | Vista Markdown rigenerabile con tutti i campi, senza introdurre un secondo registro manuale |
| `examples/minimal/bookforge_state.json` | Stato vuoto valido, senza personaggi o prosa che possano diventare canone accidentale |

La prosa accettata usa revisioni separate e hash; non viene ricostruita dai riassunti. Lo stato distingue bozza, revisione e accettazione. I file e le decisioni storiche sono immutabili nel protocollo di salvataggio; i fatti approvati si emendano con nuovi record. Il manifest e il canone in testo libero richiedono comunque cura editoriale.

## Correzioni della stilometria

MATTR sostituisce il TTR come base del proxy di varietà lessicale; sotto 300 parole il proxy VR non viene fornito. Le finestre MATTR sono di 100 parole. Il conteggio dei dialoghi gestisce più delimitatori, evita sovrapposizioni annidate e rimuove il limite che escludeva battute lunghe. I dialoghi ripetuti sono collocati nei terzi del testo per posizione dei token.

La quota di frasi nominali e il flag di provenienza «anglo-tradotta» diventano `null`: le vecchie euristiche non sostenevano quelle conclusioni. La densità di frasi brevi resta una misura descrittiva. L'analisi automatica accetta soltanto italiano; altre lingue richiedono valutazione qualitativa dichiarata. Segmentazione, dialoghi e dizionari rimangono euristici; le citazioni possono essere contate come dialogo.

**Compatibilità:** consumatori esterni devono gestire i campi ora nulli, le etichette `short_dense` / `short_mixed` / `ok` e il nuovo significato di VR. Una baseline precedente va ricalcolata sullo stesso corpus approvato, senza confrontare direttamente vecchi e nuovi valori. I nuovi percorsi sono `references/` e `scripts/`; lo stato 7.6 richiede migrazione e revisione.

## Come sono stati usati i consigli allegati

Sono stati tradotti in un ciclo editoriale centrato su funzione e causalità, esempi di voce approvati, revisione a livelli e una rubrica di valutazione separata dagli indicatori linguistici. È stato aggiunto `references/valutazione.md` con un protocollo di confronto e misurazione del costo per testo accettato.

Fine-tuning, reward model e reinforcement learning non sono stati implementati: richiedono dati e infrastruttura propri. Il loro richiamo nell'allegato non è stato trasformato in una promessa della skill. Non sono state aggiunte chiamate esterne o spese automatiche.

## Verifiche eseguite e aspettative

**40 test automatici superati.** Coprono stilometria, integrità e transizioni dello stato, migrazione e salvataggio interrotto simulato. Un esercizio separato di continuazione noir ha rispettato una voce breve autorizzata e la distinzione fra ciò che sa il lettore, ciò che crede Marco e ciò che sa Lia; il testo è rimasto una bozza. Vedi [VALIDAZIONE.md](VALIDAZIONE.md) per il perimetro delle prove.

La release è una base tecnica ed editoriale verificata nei casi elencati, pronta per un pilot. Non è ancora dimostrato che produca libri migliori, riduca i token di una certa percentuale o abbia domanda pagante. Non è stata eseguita una migrazione di un progetto reale completo, né l'importazione in un GPT specifico, né la pubblicazione di un libro.

## Prossima roadmap, ancora da eseguire

| Ordine | Attività | Condizione per procedere |
|---|---|---|
| 1 | Prova su un progetto reale con riprese, cambio canone e revisione di capitolo accettato | Nessuna perdita di prosa o decisioni; autore in grado di riprendere senza ricostruzioni arbitrarie |
| 2 | Confronto su sei brief, due configurazioni e tre lettori target | Valutazioni grezze e disaccordi documentati; beneficio riconoscibile nei casi d'uso scelti |
| 3 | Confronto con un prompt essenziale e misurazione di tempo/costo per testo accettato | Il metodo aggiunge valore rispetto al solo modello; moduli che pesano senza aiutare vengono ridotti |
| 4 | Pilot con autori del segmento iniziale e definizione dell'offerta | Evidenze di uso ripetuto, lavoro risparmiato e disponibilità a pagare; supporto e condizioni definiti |

Il posizionamento da verificare è un assistente di lavoro per autori che devono mantenere voce e continuità durante un progetto lungo. Prezzo e promessa commerciale vanno fissati dopo il pilot. Non sono stati aggiunti stime di fatturato, benchmark inventati o garanzie di vendita.
