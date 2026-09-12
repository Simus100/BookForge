<p align="center"><img src="icon.png" alt="BookForge: un libro sopra un'incudine" width="140"></p>

<h1 align="center">BookForge</h1>
<p align="center"><strong>La tua voce. Una storia che tiene. Un progetto che puoi riprendere.</strong></p>
<p align="center">Versione 7.7.0 · Skill editoriale modulare · Italiano · Python senza dipendenze esterne</p>

BookForge accompagna un libro dall'idea alla revisione e alla preparazione dei materiali editoriali. Collega intenzione dell'autore, voce, personaggi e continuità fra capitoli e volumi, con uno stato di progetto verificabile e strumenti di analisi linguistica.

[Inizia qui](docs/INSTALLAZIONE.md) · [Modifiche della versione](docs/MODIFICHE_7.7.md) · [Report HTML](docs/REPORT_MODIFICHE_7.7.html) · [Verifiche e limiti](docs/VALIDAZIONE.md)

## Cosa puoi costruire

| Il tuo obiettivo | Il contributo di BookForge |
|---|---|
| Dare forma a un'idea | Brief, lettore, struttura e percorso proporzionato al progetto |
| Scrivere con una voce riconoscibile | Carta stilistica, campioni approvati, 12 assi StyleDNA e 17 preset orientativi |
| Far funzionare una scena | Desiderio, ostacolo, scelta, conseguenza e revisione in contesto |
| Continuare un libro o una serie | Canone distinto dalle ipotesi, conoscenze dei personaggi e promesse narrative |
| Riprendere il lavoro | Manifest dei file, hash, cursore e salvataggi versionati |
| Preparare la pubblicazione | Materiali KDP, verifiche da effettuare e ricerca commerciale con fonti dichiarate |

Puoi partire da un romanzo, una raccolta, un saggio o un manoscritto da revisionare. Il percorso cambia con il formato; la tua intenzione resta il riferimento delle scelte editoriali.

## Una richiesta per cominciare

> Ho una bozza di romanzo noir. Aiutami a capire se la struttura funziona, conservando la voce asciutta del primo capitolo. Parti da una diagnosi breve e proponi la prossima unità di lavoro.

Non serve imparare una sintassi. Scorciatoie come `/salva`, `/carica`, `/stato` e quelle dei [percorsi](references/percorsi.md) aiutano a organizzare il dialogo; sono istruzioni della skill, non funzioni native dell'app.

## Avvio rapido

1. Scarica il pacchetto completo e mantieni la struttura delle cartelle.
2. Segui la [guida](docs/INSTALLAZIONE.md) per usare `SKILL.md` in un ambiente compatibile o adattare le istruzioni a un GPT/progetto.
3. Crea una cartella separata per ogni libro: prosa, campioni e stato appartengono al progetto.

Gli strumenti richiedono Python 3.10 o successivo e usano soltanto la libreria standard:

```bash
python -m unittest discover -s tests -v
python scripts/validate_state.py examples/minimal/bookforge_state.json --root examples/minimal
python scripts/stylometry.py references/carta.md --lang it --json
```

L'ultimo comando è una dimostrazione tecnica su un documento, non una valutazione narrativa. Senza Python rimane utilizzabile il percorso editoriale, con verifiche manuali esplicitate.

## Dentro il pacchetto

| Percorso | Contenuto |
|---|---|
| `SKILL.md`, `agents/` | Punto d'ingresso e metadati della skill |
| `references/` | 13 moduli editoriali caricabili quando servono |
| `scripts/` | Stilometria, validazione, salvataggio, migrazione e vista Markdown |
| `schemas/`, `examples/` | Schema dello stato e progetto minimo vuoto |
| `tests/` | 40 test automatici di regressione |
| `docs/` | Installazione, modifiche effettive e risultati delle verifiche |
| `archive/legacy-main/` | Documenti della precedente repository, conservati per consultazione storica |

## Cosa significa questa release

La 7.7 introduce regole stilistiche contestuali, stato strutturato e controlli eseguibili. I test tecnici sono passati; un esercizio narrativo separato ha verificato il comportamento su voce e conoscenze dei personaggi. La qualità editoriale su opere complete, l'utilità percepita e la disponibilità a pagare richiedono ancora una prova con autori e lettori reali.

BookForge richiede un assistente compatibile: non include un modello, memoria autonoma permanente, un esportatore EPUB/PDF o un servizio di pubblicazione. La stilometria fornisce indicatori dell'italiano, non un voto di qualità né un rilevatore di origine AI. La preparazione KDP non implica conformità tecnica già verificata o vendite garantite.

Le condizioni di distribuzione commerciale e la licenza del prodotto restano da definire dal titolare. Questa release non introduce una nuova licenza.
