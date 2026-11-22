# Architettura: posta, struttura, motivi, finale · BookForge 7.8

Da consultare per brief, indice, revisione di livello 3, apertura e chiusura del libro. Ogni strumento è un'opzione da adattare all'opera, non un obbligo. Le strutture canoniche sono in [generi](generi.md).

## 1. Posta in gioco e timone

- **Posta dell'autore.** È ciò che l'autore ritiene importante raccontare, distinto dalla promessa di genere. Chiedila all'autore, non inventarla. Ogni elemento del libro deve renderne conto. Nel testo non va mai enunciata come tesi.
- **Timone in 25 parole.** La storia in due righe: protagonista, desiderio, ostacolo, svolta. Proponila e falla approvare, poi rileggila prima di ogni capitolo. Se non converge, l'idea è ancora sfocata: dillo invece di andare avanti. Il timone frena la deriva centrifuga del modello, che tende a seguire l'ultima associazione. Non è una frase di vendita.
- **Domanda drammatica principale.** Una domanda sì/no che nasce da protagonista, obiettivo e ostacolo. Va posta presto e trova risposta alla fine (sì, no, oppure un «forse» motivato) grazie a un'azione o a una scelta del protagonista. Per ogni capitolo, indica quale sotto-domanda apre o chiude. Non forzarla su opere corali o d'atmosfera.
- **Desiderio astratto, obiettivo concreto.** Un desiderio astratto, come essere capiti o tornare a casa, si lega a un obiettivo tangibile che il personaggio persegue in scena.
- **Premessa a strati, catena delle conseguenze.** Ricava ogni elemento di mondo e personaggi da quelli precedenti: il luogo suggerisce il mestiere, il mestiere le relazioni. A ogni strato proponi tre opzioni, scarta la più ovvia e lascia scegliere l'autore. Un elemento che si può togliere senza perdite era di repertorio. Fermati quando la premessa contiene desiderio, ostacolo e una domanda aperta.
- **Contenitore semplice.** Una storia forte e semplice (una fuga, un ritorno, un'attesa, un'indagine) dà senso a tutto ciò che vi entra. Test: un incontro casuale arricchisce il libro o resta un corpo estraneo?

## 2. Trama e tensione lunga

- **Causalità.** Ogni evento accade «perché», non «e poi». Prima di scegliere, elenca molti ostacoli, interni ed esterni. L'escalation riguarda l'arco nel suo insieme: non serve un conflitto in ogni scena.
- **Prove su misura del protagonista.** Ogni ostacolo colpisce la sua convinzione sbagliata o la sua debolezza specifica. Gli errori insegnano qualcosa che servirà più avanti.
- **Non alzare la posta per mancanza di idee.** Sostituisci escalation immotivate (iperboli, colpi di scena a catena) con complicazioni più piccole e precise. I generi che promettono escalation la mantengono, ma ogni salto deve essere specifico.
- **Suspense e sorpresa.** La suspense nasce dall'asimmetria informativa e dall'avvicinamento; la sorpresa dura un istante. I colpi di scena:
  - pochi;
  - legati al nodo centrale;
  - di tipi diversi (cliffhanger, rovescio di fortuna, riconoscimento; quest'ultimo perde forza se ripetuto).

  Registrali in `narrative_state.turns` (tipo, capitolo, che cosa ribaltano) per controllarne varietà e distanza.
- **Sorpresa onesta.** Nasce dalle conseguenze di ciò che il lettore sa. Da evitare:
  - colpi di scena basati su informazioni che il POV possedeva e ha taciuto senza motivo;
  - «era un sogno».

  Le svolte di carattere vanno preparate da indizi; se mancano, seminali a ritroso.
- **Centro e climax.** Al centro, una soluzione provvisoria che sembra funzionare e che la seconda svolta distrugge. Il climax è un fatto: investi nelle scene che lo preparano e in quelle che ne traggono le conseguenze, invece di gonfiarlo.
- **Le fasi del libro.** In genere l'esordio e la prima parte sono più distesi; il centro procede per scene concatenate e ritmo serrato; dopo il climax prevale il sommario e cresce la distanza; il congedo è riflessivo. È un orientamento, non uno schema: un tono uniforme o un montaggio che fonde le fasi sono scelte legittime.

## 3. Montaggio

- **La posizione cambia il senso.** La stessa scena all'inizio o alla fine, o preceduta dall'esito, si legge diversamente. Nell'indice prova almeno un ordine alternativo per le scene chiave e descrivi che cosa cambia. Alcune possibilità:
  - l'esito in apertura;
  - la partenza dal dopo-climax, con due linee che convergono;
  - capitoli come petali attorno a un centro.

  È utile soprattutto quando contano il come e il perché.
- **Sottotrame.** Annota la funzione di ciascuna (specchio, anticipazione, ritmo) e come si chiude. Spesso il cambiamento vero passa da lì.

## 4. Motivi e corrispondenze

- **Motivi.** Scegli pochi motivi per libro: elementi presenti alla lettera nella storia, che ritornano cambiando valore (variati, rovesciati, rafforzati). Prima apparizione discreta nel primo atto, ritorno nel finale. Registrali in `narrative_state.motifs` (posizione → forma → valore). Il registro serve anche a distinguere un motivo voluto da un tic, che il PIP deve segnalare.
- **Scene gemelle.** Una coppia prima/dopo che misura il cambiamento: il primo e il secondo interrogatorio, il primo e l'ultimo pasto.
- **Anticipazioni e doppi.** Un personaggio minore vive prima ciò che toccherà al protagonista; un doppio dice ciò che il protagonista non sa dirsi.
- **Rarità.** Un simbolo per paragrafo è manierismo.

## 5. Incipit del libro

- **Onesto.** Mostra il mondo e il tono reali del libro, senza promesse che il libro non manterrà.
- **Comincia nel momento del cambiamento.** Dai solo l'informazione necessaria in quel momento e fai aprire a ogni frase una domanda concreta. Inquadratura stretta, non panoramica: un dettaglio, un elemento laterale, un desiderio. Non riassumere e non annunciare l'esito.
- **Curiosità o immersione.** Scegli fra un attacco anomalo che incuriosisce e un'immersione graduale. Se parti con lo shock, entro la prima pagina trasformalo in un personaggio che vuole qualcosa.
- **Tempo verbale e respiro.** Scegli il tempo verbale per la relazione che crea ([narratore](narratore.md) §6). Dopo due colpi forti, cambia sintassi e lascia respirare.
- **Scrivilo, o rivedilo, per ultimo.** Test: togli il primo capoverso e rileggi.

## 6. Finale del libro

- **Lente retroattiva.** Il lettore rilegge tutto alla luce delle ultime pagine. Il cambiamento deve essere proporzionato alle forze messe in campo.
- **Crisi → climax → conseguenze.** Il climax risponde alla domanda drammatica grazie al protagonista; le conseguenze sono brevi, sentite più che spiegate. Sorprendente e inevitabile: trova i punti precedenti che lo preparano. Se mancano, seminali invece di cambiare il finale.
- **Nessuna morale enunciata.** Il senso passa per un motivo già costruito o per un gesto sommesso che conferma il carattere. I fatti possono restare aperti; la presa di coscienza no. Fatto chiaro, senso aperto.
- **Congedo.** Se serve, uno specchio dell'incipit, il ritorno del motivo portante, una distanza che cresce.

## 7. Il tema, dopo

Partire da un tema dichiarato produce testi didascalici. Procedi così:

1. Dopo una prima stesura, o dopo un atto, rileggi raccogliendo le ricorrenze: immagini, parole, scelte ripetute, titolo, climax.
2. Proponi alcuni temi possibili; l'autore ne sceglie uno, in una o due parole.
3. Da quel momento il tema diventa un criterio di revisione: taglia ciò che non lo serve e verifica che POV, ambientazione, dialoghi e finale lavorino per lui.

Non dichiararlo mai nel testo.

## 8. Stesure

- **Per unità (predefinita).** Scrivi, rileggi, consegna l'unità.
- **Stesura di linea**, su richiesta o per libri lunghi. Capitoli consecutivi, rapidi e lineari, con marcatori [DA RISOLVERE] al posto delle soluzioni. Poi passate separate: struttura → scene → lingua. Evita il libro «a scatti» che nasce dal lucidare una scena alla volta.
- **Modalità germe.** Si parte da un'immagine o da un gesto anomalo e si scrive per scoprire. La scheda si compila dopo la bozza, quando qualcosa diventa inevitabile. Gli elementi emersi si registrano nell'NST come semi da riprendere.
- **A fine sessione** annota il movimento successivo: conviene fermarsi sapendo che cosa viene dopo.
