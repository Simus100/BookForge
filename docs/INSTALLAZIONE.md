# Usare BookForge 7.7

## Pacchetto e ambienti

Conservare l'intera struttura del pacchetto. `archive/` contiene materiale superato: non caricarlo insieme ai riferimenti attuali nell'assistente. La release è predisposta per ambienti che leggono skill Markdown e per adattamento a GPT/progetti; l'importazione nell'interfaccia specifica dell'utente non è stata provata.

In un ambiente compatibile con skill, importare la cartella con `SKILL.md` seguendo il meccanismo dell'ambiente. `agents/openai.yaml` fornisce i metadati di presentazione dove supportati. Nessuna installazione personale viene effettuata dalla consegna di questo pacchetto.

Per un GPT/progetto, usare [INSTRUCTIONS_GPT.md](INSTRUCTIONS_GPT.md), derivato dal punto d'ingresso, e rendere disponibili i riferimenti pertinenti in `references/`. Se la piattaforma appiattisce i file caricati, i nomi base permettono di riconoscere i moduli; gli script richiedono invece le cartelle `scripts/`, `schemas/` ed `examples/` nella loro struttura originale. Disponibilità di file, esecuzione Python e salvataggio durevole dipendono dall'ambiente: la skill deve dichiarare le capacità effettive.

Il master delle precedenti Instructions non era fra gli allegati: `SKILL.md` è un nuovo punto d'ingresso ricostruito dalle fonti fornite, non una copia verificata del vecchio master.

## Primo progetto

1. Creare una cartella esterna al pacchetto per il libro.
2. Copiare `examples/minimal/bookforge_state.json`; sostituire ID e titolo con quelli del progetto.
3. Definire il brief e la prima unità di lavoro. Aggiungere soltanto campioni realmente approvati dall'autore.
4. Salvare la prosa in file di revisione distinti. Compilare manifest, SHA-256 e riferimenti prima di dichiarare una ripresa verificata.
5. Usare il [protocollo di stato](../references/stato-bsr.md) per salva/carica e il [modello di continuità](../references/continuita.md) per fatti, ipotesi e conoscenze.

L'esempio è intenzionalmente vuoto: non contiene personaggi o decisioni da importare accidentalmente in un libro reale. Copiare soltanto il JSON non trasferisce i manoscritti indicizzati.

## Strumenti

Python 3.10+; nessun pacchetto Python esterno. Eseguire dalla radice del pacchetto:

```bash
python -m unittest discover -s tests -v
python scripts/validate_state.py examples/minimal/bookforge_state.json --root examples/minimal
python scripts/stylometry.py /percorso/capitolo.txt --lang it --json
```

`validate_state.py` implementa i vincoli usati dallo schema fornito: non è un motore JSON Schema generale. Il controllo di struttura e hash non certifica la coerenza narrativa. I salvataggi cooperativi sono protetti da lock, controllo revisione e sostituzione atomica del JSON, non da una transazione distribuita.

Per migrare uno stato 7.6/7.6.1:

```bash
python scripts/migrate_state.py vecchio.json --output candidato-migrato.json --project-id mio-libro
```

Completare la revisione descritta in [stato-bsr](../references/stato-bsr.md) prima di attivarlo. Il migratore conserva il payload originale e non deduce approvazioni o file mancanti.

## Preparazione editoriale

Il pacchetto fornisce procedure e strumenti di supporto. Non contiene esportatori nativi EPUB, DOCX o PDF, né un collegamento operativo all'account KDP. Per i materiali finali occorrono gli strumenti del proprio ambiente e una verifica del risultato effettivamente esportato.
