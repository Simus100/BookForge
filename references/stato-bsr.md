# Stato e ripresa · BookForge 7.7 / schema 2.0

`bookforge_state.json` è il registro canonico delle decisioni e un indice dei file. Non contiene necessariamente la prosa; una nuova chat deve ricevere anche i file richiesti dal manifest. Il Markdown è una vista generata, non un secondo stato da aggiornare.

## Struttura e separazione

Schema eseguibile: [bookforge_state.schema.json](../schemas/bookforge_state.schema.json). Esempio vuoto valido: [bookforge_state.json](../examples/minimal/bookforge_state.json). Copiarlo nella cartella del proprio progetto e assegnare un ID specifico. I campioni dimostrativi non sono canone o voce approvata.

- `project`, `workflow`, `resume_cursor`: identità, modalità/deleghe, cursore fino al beat e prossima azione.
- `volumes`, `chapters`, `scenes`, `characters`: ID stabili e legami; numero del capitolo univoco nel volume. Profili dei personaggi in `profile`, senza compressioni obbligatorie.
- `files`: ID, percorso relativo alla cartella del progetto, SHA-256, ruolo e necessità per la ripresa. Una revisione accettata usa un nuovo file immutabile, per esempio `manuscript/v1-c001-r002.md`.
- `facts`, `promises`, `decisions`: origine, stato, approvazione ed emendamenti; vedi [continuita](continuita.md).
- `styledna`, `voice_fingerprint`: preferenze, campioni e baseline approvata. Una nuova misura non sostituisce la baseline.
- `narrative_state`: brief (`strategic_board`), timeline, relazioni, conoscenze al lettore, archi, PIP e note specifiche. JSON libero per non perdere il dettaglio; i link contenuti qui richiedono verifica editoriale.
- `legacy_payload`, `migration`: dati originali e stato della revisione dopo migrazione.

Ruoli file: `chapter`, `voice`, `canon`, `notes`. La prosa accettata deve essere presente, avere un riassunto e un riferimento all'accettazione (`accepted_ref`). Gli altri file richiesti per la continuità vanno marcati `required_for_resume: true`. Il validatore controlla i campi strutturati dello schema, non ogni riferimento in testo libero.

## `/salva`: protocollo concreto

1. Partire dallo stato caricato; distinguere bozze e decisioni approvate. Scrivere prima la nuova prosa in un file di revisione nuovo, mai sull'unico file già accettato. Calcolare l'hash sui byte effettivamente salvati.
2. Preparare `candidate.json`: aggiornare manifest, riassunti, cursore, approvazioni e `revision = precedente + 1`. I record di file e decisioni già salvati restano; nuovi file hanno nuovi ID e percorsi. Un capitolo accettato modificato richiede un nuovo riferimento di accettazione; un suo ramo alternativo vive come bozza separata.
3. Controllare semanticamente nuovi fatti e promesse. Un conflitto va risolto con l'autore; il JSON valido non certifica il canone.
4. Eseguire dalla cartella del pacchetto (sostituire i percorsi con quelli reali):

```bash
python scripts/validate_state.py /percorso/progetto/candidate.json --root /percorso/progetto
python scripts/state_io.py /percorso/progetto/candidate.json /percorso/progetto/bookforge_state.json --root /percorso/progetto --expected-revision 0
python scripts/render_state.py /percorso/progetto/bookforge_state.json --output /percorso/progetto/bookforge_state.md
```

`0` è l'esempio della prima revisione: usare sempre la revisione realmente letta. `state_io.py` blocca revisioni obsolete, identità diverse, file mancanti/hash diversi, riscritture dei record storici e migrazioni ancora da rivedere. Salva il JSON con sostituzione atomica e conserva il precedente in `.bak`; il lock impedisce due scritture cooperative simultanee. Se interrotto prima del commit, la prosa nuova può restare non referenziata e il vecchio stato rimane valido. Non è una transazione distribuita né una protezione da processi che modificano i file senza seguire il protocollo.

I capitoli si conservano anche se scartati; le promesse conservano identità e origine. Per cambiare una promessa, chiudere la precedente con decisione esplicita e crearne una nuova. Un lock rimasto dopo la terminazione del processo non va eliminato alla cieca: accertare che non vi siano scrittori attivi e controllare stato e backup prima di rimuoverlo.

5. Confermare il salvataggio soltanto dopo esito positivo; il Markdown può essere rigenerato se la sua scrittura fallisce. La copia locale non equivale automaticamente a un backup remoto: usare il salvataggio durevole disponibile nell'ambiente.

Senza Python controllare manualmente struttura e riferimenti e dichiarare mancata verifica deterministica; senza file consegnare JSON/prosa copiabili e dichiarare che non sono stati salvati. Non dichiarare un autosave automatico tra messaggi: la skill opera solo durante l'esecuzione.

## `/carica`, `/stato`, `/diagrammi`

Validare JSON e file con `--root` prima di promettere una ripresa completa. Senza root è stata verificata solo la struttura. Una risorsa richiesta mancante o alterata blocca la continuità verificata; riportare quale file occorre senza inventarne il contenuto. Il fallback dal solo Markdown è una ricostruzione da confermare, non un ripristino equivalente.

Mostrare: progetto, revisione, file verificati o mancanti, cursore e prossima azione. Riprendere entro il mandato già autorizzato. `/stato` non scrive file; `/diagrammi` crea viste opzionali dai dati reali, mai parte del payload minimo.

Conservare l'archivio completo; caricare per la scena fatti e personaggi pertinenti, promesse coinvolte, ultimo testo e campioni. Non reimportare Markdown e JSON duplicando i dati. La selezione del contesto è responsabilità del modello/autore: questa release non contiene un motore di ricerca semantica.

## Migrazione 7.6 / 7.6.1

```bash
python scripts/migrate_state.py vecchio.json --output candidato-migrato.json --project-id mio-libro
```

Il comando non sovrascrive input o output esistenti. Conserva ogni valore originale in `legacy_payload`, mappa campi recuperabili e produce `review_required`. Non indovina file, accettazioni o conoscenze: i fatti legacy diventano proposte da verificare; i capitoli «completato» diventano revisionati in attesa di conferma. Le promesse, i profili e il cursore originali restano nel payload finché l'autore li riconcilia.

Prima di attivare: completare manifest/hash, ID, conoscenze, promesse, profili e cursore; verificare le approvazioni; conservare un backup; annotare una decisione di migrazione e impostare `migration.status = clear`. Validare e provare una ripresa su copia. Il nuovo registro parte da revisione 0 e non sostituisce direttamente lo stato legacy: mantenere i due file distinti fino alla verifica.
