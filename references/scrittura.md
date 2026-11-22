# Stesura, scene e lettore · BookForge 7.8

## Preparare il contesto

Recupera dalla cartella del progetto l'unità richiesta, l'ultima prosa accettata, i fatti pertinenti, pochi campioni approvati e, se esiste, la tavolozza del mondo (`narrative_state.palette`). Rileggi il timone in 25 parole, se esiste ([architettura](architettura.md) §1), e le ultime pagine accettate, così da riallinearti alla voce prima di scrivere. Leggi la [Carta](carta.md). Consulta StyleDNA solo per le preferenze che servono. Per scrivere una scena non caricare il modulo KDP né l'intera Bibbia. Se mancano dei file, dichiaralo prima di presumere continuità.

Strumenti di mestiere, da caricare quando servono:
- [scena](scena.md): preparazione, varianti, scena e sommario, descrizione, raccordi, chiusure, fantascienza;
- [dialogo](dialogo.md): quando il dialogo pesa;
- [narratore](narratore.md): distanza, regola della fonte, tempi verbali;
- [psicologia](psicologia.md): personaggi in scena.

## Scheda scena

È uno strumento di lavoro breve: compila solo i campi che servono. Mostrala solo se occorre una scelta dell'autore.

| Fiction | Non-fiction |
|---|---|
| Funzione nella storia, POV, distanza e tempo verbale | Domanda del lettore e risultato atteso |
| Contenitore: che cosa sa già il lettore, che cosa posso togliere | Tesi o concetto della sezione |
| Chi vuole che cosa; ostacolo concreto; che cosa è già in moto | Evidenze e fonti; stato di verifica |
| Scelta, costo e conseguenza; stato iniziale → che cosa cambia | Progressione rispetto alle sezioni vicine |
| Che cosa sa ciascuno; che cosa sa il lettore che il POV ignora; che cosa fraintende il POV | Esempio, esercizio o applicazione utile |
| Uscita (ultima azione o immagine) | Registro, prerequisiti e limiti |

Non tutte le scene devono contenere un conflitto aperto: una pausa può cambiare una comprensione, una relazione o un'aspettativa. Se una scena non ha funzione, chiediti se comprimerla o eliminarla. Scene & Sequel, MRU e salti temporali sono strumenti facoltativi, non strutture da imporre a ogni paragrafo.

**La scheda resta invisibile.** La prosa non enuncia la funzione della scena e non spiega ciò che la scena mostra. È il rischio di chi pianifica bene: senza questa attenzione la scena diventa una didascalia.

## PIP: osservare la varietà

Quando noti una ripetizione, consulta gli ultimi capitoli. Controlla:
- apertura e chiusura;
- tipo di raccordo;
- oggetti ricorrenti usati per portare il non detto ([scena](scena.md) §6);
- senso dominante;
- campo metaforico;
- modalità (scena, sommario, riflessione).

Nel `narrative_state.pip_ledger` registra solo ciò che aiuta a decidere. Ripetere lo stesso asse è lecito: conserva una scelta coerente, cambia invece un automatismo. Un motivo registrato in `narrative_state.motifs` è una ricorrenza voluta, non un tic. Nessun senso è obbligatorio nelle prime frasi. Elenchi di dettagli possibili e attacchi alternativi servono sulle scene chiave o su richiesta, non a ogni capitolo.

## Granularità e ciclo

- `/granularita capitolo|scena|beat` cambia il default; `/scena` e `/beat` valgono solo per l'unità corrente. Registra il cursore anche a metà scena.
- **Capitolo:** consegna l'unità intera quando i limiti dell'ambiente lo consentono. Evita troncamenti: per lavori lunghi concorda come dividere.
- **Scena:** sviluppa una scena completa.
- **Beat:** lavora su un singolo movimento drammatico, senza quota di parole. A scena chiusa rileggi l'insieme e ricuci le giunture; non allungare le frasi per forza.
- Per la stesura di linea o la modalità germe vedi [architettura](architettura.md) §8.
- Le deleghe operative permettono di proseguire entro i limiti stabiliti, ma non promuovono il testo o il canone ad approvati. In modalità guidata chiedi sulle scelte sostanziali, non sui dettagli già risolti.

Prepara la scheda, poi scrivi la bozza in un solo movimento. Nei punti decisivi (attacco, svolta, dettaglio rivelatore, chiusura) genera prima alcune alternative ([scena](scena.md) §2).

Rileggi in quest'ordine:
1. comprensione e conseguenze;
2. voce, emozione e ritmo;
3. forma.

Consulta [anti-ai](anti-ai.md) se serve. Usa lo script solo su un file reale; per le lingue non supportate dichiara che l'analisi è qualitativa. Non mostrare una chiusura «completato» prima della revisione prevista.

Consegna la prosa e le note essenziali, senza esporre tutta la preparazione. La nuova versione resta bozza o revisione finché l'autore non la accetta. I fatti nuovi sono proposte da confrontare con il canone; aggiorna soltanto le decisioni approvate. Salva fisicamente quando possibile con il protocollo [BSR](stato-bsr.md), senza dichiarare un salvataggio che non è avvenuto.

## NST

Registra:
- posizione nell'arco;
- domande aperte e promesse;
- informazioni date al lettore;
- sottotrame;
- stato emotivo e relazioni cambiate;
- motivi e loro ritorni (`motifs`), colpi di scena (`turns`), semi emersi in stesura.

I riferimenti usano gli ID stabili del progetto, non solo il numero del capitolo. Le valutazioni di tensione sono note qualitative o preferenze, non misure certificate. Tieni distinte conoscenze, supposizioni e fatti del mondo.

## `/lettore`

Se possibile usa una lettura separata, con solo la prosa fino al punto indicato, senza scaletta e senza soluzioni future. Altrimenti dichiara che ciò che è già emerso nella conversazione può influenzare il giudizio.

Riporta, indicando sempre la posizione nel testo:
1. punti di confusione;
2. cali d'attenzione;
3. prevedibilità;
4. domande per il seguito;
5. emozioni plausibilmente trasmesse;
6. il punto in cui il lettore smette di credere a un personaggio o a un fatto;
7. quale pagina rileggerebbe per piacere.

Sono ipotesi sul lettore: non emozioni di un essere umano né risultati di un beta test. Poi confronta le domande con l'NST.
