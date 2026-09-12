# Verifiche della release 7.7.0

Data: 12 settembre 2026. Le prove tecniche e il controllo qualitativo descritti qui sono distinti da un benchmark editoriale con lettori reali.

## Test automatici

```bash
python -m unittest discover -s tests -v
```

**Esito: 40 test, tutti superati.** Ambiente di sviluppo Python; la suite usa soltanto la libreria standard.

| Area | Casi coperti |
|---|---|
| Stilometria — 17 test | Apostrofi e Unicode, abbreviazioni/decimali, chiusure di citazione, dialoghi lunghi/a trattino/annidati, ripetizioni nei terzi, MATTR confrontato con calcolo diretto, campioni brevi, campi diagnostici disabilitati, CLI testo/JSON e lingua non supportata |
| Stato — 23 test | Template, tipi, assi, ID, riferimenti, cursore, conoscenze, emendamenti/cicli, promesse, accettazione, file e hash, traversal/symlink, chiavi JSON duplicate, validazione parziale senza root, lock, revisioni obsolete, isolamento del progetto, cronologia canonica, backup e interruzione simulata |
| Migrazione e vista — inclusi nei 23 | Payload conservato, attivazione bloccata prima della revisione, output non sovrascritto, tutti i campi presenti nella vista Markdown |

Il test di interruzione forza un errore sulla sostituzione del JSON: verifica che stato precedente e backup restino leggibili. Non simula ogni guasto di sistema, arresto hardware o scrittore esterno non cooperativo.

## Prova comportamentale separata

Un'esecuzione separata ha letto il punto d'ingresso e i moduli pertinenti per continuare una scena noir in 180–250 parole. Vincoli: voce breve, un dispositivo stilistico deliberato da conservare, Marco crede che Lia abbia venduto una chiave ma l'ha persa lui; Lia sa soltanto che manca; nessuna rivelazione anticipata; testo non ancora accettato.

Il risultato ha conservato il dispositivo, mantenuto il sospetto distinto dalla conoscenza di Lia e indicato la bozza come non accettata. È una verifica qualitativa di un solo caso, eseguita da un modello e controllata in revisione. Non dimostra preferenza dei lettori, qualità su un romanzo intero o robustezza su tutti i modelli e contesti.

## Controlli di confezionamento

- Frontmatter della skill validato con il validatore del pacchetto skill-creator.
- Stato minimo validato con la root del progetto; salva/carica e vista Markdown provati anche da riga di comando su una copia temporanea.
- Link Markdown dei documenti correnti controllati come percorsi locali; l'archivio storico resta materiale non operativo.
- Pacchetto ZIP confrontato con i file tracciati della release e verificato tramite CRC; manifest SHA-256 dei file incluso.

## Verifiche ancora necessarie

Non sono stati eseguiti test con lettori umani, confronti statistici o misure di risparmio token; non è stato pubblicato alcun libro. Mancano prova di importazione nel GPT dell'utente, migrazione di uno stato reale completo, collaudo su sistemi operativi diversi e misure di domanda commerciale. Il protocollo successivo è in [valutazione](../references/valutazione.md).

Un JSON valido non certifica la verità del canone. Le metriche stilometriche sono proxy euristici dell'italiano: non misurano originalità, qualità letteraria, validità psicologica o provenienza AI. I requisiti KDP vanno ricontrollati sulle fonti ufficiali al momento della pubblicazione.
