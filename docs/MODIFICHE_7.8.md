# BookForge 7.8.0: modifiche effettive

**Obiettivo.** Correggere il limite principale della 7.7. La 7.7 era solida su processo, stato e cautele, ma debole nella guida generativa: diceva poco su *come* si costruiscono un attacco, un dialogo, una descrizione, la distanza psichica, un raccordo o un finale. La 7.8 aggiunge questo strato di mestiere. La dottrina resta invariata:
- la voce dell'autore è sovrana;
- la chiarezza viene prima di tutto;
- le regole sono contestuali, non quote;
- in stesura si danno imperativi positivi, i divieti stanno nella revisione.

**Compatibilità.** Schema dello stato, script, test ed esempio sono invariati. Lo stato continua a dichiarare `bookforge_version` 7.7.0 (schema 2.0) e `stylometry.py` resta 7.7.0. I file di stato esistenti restano validi senza migrazione. I nuovi dati narrativi (`motifs`, `turns`, `places`) vivono nel campo libero `narrative_state`.

## Moduli nuovi

| File | Contenuto | Fonti principali |
|---|---|---|
| `references/scena.md` | Preparazione invisibile (contenitore, che cosa è in moto, asimmetria, fraintendimento del POV, uscita); varianti divergenti nei punti decisivi; scena, sommario, indiretto ed ellissi; durata; ingresso; descrizione filtrata e dettaglio da addetto ai lavori; oggetto che porta il non detto; trama verticale; digressione; raccordi; chiusure; fantascienza e novum | Franzoso (Aggregatore, raccordi, contenitore, insider); Carver (cosa è in moto, ordinario reso strano); Gotham (scena/sommario, densità che segue l'arco, trapianto); Cotroneo/Loi (chiave e zoom, orologio ambientale, stanza doppia, durata); Novak (trama verticale, impossibile detto piano); ricerca su mode collapse e Verbalized Sampling |
| `references/dialogo.md` | Argomento ufficiale e reale, aggancio e scarto, «dietro la porta», innesco visibile, stessa battuta con cornice diversa, voci che resistono all'emozione, corpo e luogo, attribuzioni, forme, dialetto, procedura in sei passi | Franzoso B; Gotham cap. 6; Carver (corpo e innesco); Cotroneo (dietro la porta, un indizio); Loi n. 33 (doppio binario); Novak (G1, registro come retaggio) |
| `references/narratore.md` | Narratore scelto prima della trama, distanza psichica, coscienza fallibile, regola della fonte, quattro modi del discorso riportato, tempi verbali italiani come distanza (onda remoto–imperfetto, cambi voluti con motivo e ponte, imperfetto di cortesia), persona, prove mirate | Franzoso C (tempi, persona, narratore, James); Gotham cap. 4; Carver (aggettivo valutativo del POV); Cotroneo (narratore che sa o che scopre) |
| `references/architettura.md` | Posta dell'autore, timone in 25 parole, domanda drammatica, premessa a strati, contenitore; causalità, prove su misura, niente escalation per mancanza di idee, sorpresa onesta, fasi del discorso; montaggio; motivi e scene gemelle; incipit e finale del libro; tema raccolto dopo; stesura di linea e modalità germe | Franzoso A; Gotham capp. 3, 9, 10; Carver (niente trucchi, finale come piccolo sollevamento); Novak (premessa a strati, latenza, centro provvisorio); Loi (tipi di colpo di scena) |
| `references/promozione.md` | Principi (specificità, incongruenza, carico cognitivo, nuovo ancorato al noto, livelli che non si ripetono, promessa mantenuta) e procedure per logline, quarta, descrizione Amazon, pitch, titolo, bio, lettori anticipati, newsletter, revisione per l'ascolto; pratiche escluse | Losito (adattato e filtrato); Halls (memoria di lavoro, scrittura per l'orecchio) |

## Moduli rivisti

| File | Modifica |
|---|---|
| `SKILL.md` | Descrizione più precisa sul perimetro (capitoli, scene, dialoghi, testi promozionali); tabella con i cinque moduli nuovi; ciclo con scheda invisibile, varianti nei punti decisivi, revisione che aggiunge quanto toglie; avvertenza sulle distorsioni del giudizio del modello |
| `carta.md` | Da 10 a 12 principi: limite dello sguardo, superficie e motore, cose che lavorano, scelta oltre la prima idea, chiusura sull'azione; sempre in forma positiva |
| `scrittura.md` | Riscaldamento sulla voce e sul timone; scheda scena con contenitore, motore, asimmetria, fraintendimento, uscita; scheda invisibile; PIP con raccordi e motivi; NST con `motifs` e `turns`; `/lettore` con due domande nuove (dove smette di credere; quale pagina rileggerebbe per piacere) |
| `anti-ai.md` | Cancellature distinte dalle proposte; due nemici speculari; sette famiglie di intervento ricavate dagli studi sulle correzioni di scrittori professionisti; catalogo ampliato (figure prese alla lettera, frasi gemelle, io percettivo, attribuzioni enfatiche, «come sai», anticipazione che rivela, sorpresa da informazione taciuta, simbolismo spiegato, bella frase); calchi italiani concreti con eccezioni; ordine della micro-revisione |
| `fasi.md` | Brief di fiction con posta, timone, domanda drammatica, narratore; indice con sotto-domanda, fase e ordine alternativo; livello 3 ampliato; passate separate e distanza dal testo |
| `valutazione.md` | 14 controlli sì/no di mestiere (adattati dal Torrance Test of Creative Writing); avvertenza sulle distorsioni dei giudizi automatici |
| `psicologia.md` | Personaggi in scena: orbite, marcatori con un budget, nomi, prima entrata, luce riflessa, canali in discrepanza, norma e scarto, tratto ricorrente, conflitto fra ragioni, registro, coerenza d'epoca |
| `styledna.md` | Preset Minimalista; modulazioni per posizione nel libro; densità legata a una ragione narrativa |
| `generi.md` | Fantascienza con novum; noir; strumenti trasversali; percorso dal presente nella Worldbuilding Bible |
| `continuita.md` | `motifs`, `turns`, `places` in `narrative_state`; «chi entra va pagato» |
| `kdp.md`, `percorsi.md` | Rimando a promozione; nuovi comandi: `/timone`, `/tema`, `/motivi`, `/varianti`, `/dialogo`, `/incipit`, `/finale`, `/quarta`, `/logline`, `/pitch` |

## Che cosa è stato scartato dalle fonti, e perché

- **Divieti assoluti** (avverbi, passivi, negazioni, «come se», frasi lunghe): tradotti in domande contestuali, perché contraddicono la dottrina e penalizzerebbero voci legittime.
- **«Un conflitto in ogni frase» e «mostra, non dire» come dogmi**: BookForge è già più fine (asse show/tell regolabile, pause legittime).
- **Verbi dichiarativi sostitutivi e cataloghi del linguaggio del corpo** (Novak, in parte Loi): sono proprio i cliché che la revisione deve togliere.
- **Diffidenza di Franzoso e Carver verso la fantascienza**: respinta la generalizzazione, conservato il principio della specificità verificabile.
- **Tattiche manipolative di copywriting** (scarsità falsa, testimonianze riscritte, credibilità fabbricata): escluse esplicitamente.
- **Regole di scrittura per l'orecchio come quota nella prosa**: valgono per promozione e audio, non come stile del romanzo.
- **Esempi d'autore**: descritti per meccanismo, nessun passaggio riprodotto.

## Ricerca consultata

- Chakrabarty et al., *Can AI writing be salvaged?* (CHI 2025): tassonomia di sette categorie di correzione, le più frequenti; la revisione di uno scrittore è preferita a quella del modello. https://arxiv.org/abs/2409.14509
- Chakrabarty et al., *Art or Artifice?* (CHI 2024): 14 test TTCW; i divari maggiori dei modelli sono su originalità della forma, complessità retorica, figure, originalità di pensiero. https://arxiv.org/abs/2309.14556
- Zhang et al., *Verbalized Sampling* (2025): mode collapse legato alla preferenza per il familiare; chiedere più candidati con stima di probabilità aumenta la diversità senza perdere qualità. https://arxiv.org/abs/2510.01171
- Huot et al., *Agents' Room* (ICLR 2025): decomporre pianificazione (conflitto, personaggi, ambientazione, trama) e stesura per sezioni migliora i racconti rispetto alla generazione in un passaggio. https://arxiv.org/abs/2410.02603
- Xu et al., *Echoes in AI* (2025): le trame generate si ripetono molto più di quelle umane. https://arxiv.org/abs/2501.00273

## Stato delle prove

- **Test automatici:** 40 superati, invariati.
- **Confronto 7.7/7.8 su quattro prompt in italiano:** apertura SF nel mondo de *La Chiave di Vetro*, continuazione con voce data, revisione di un passo artificiale, dialogo con due segreti. Le 16 asserzioni oggettive passano per entrambe le versioni: il modello di base rispetta già i vincoli espliciti, quindi la differenza sta nella qualità della prosa. Le uscite sono state consegnate all'autore in forma anonima per il giudizio alla cieca.
- **Costo:** la 7.8 consuma in media circa il 15% di token in più e il 39% di tempo in più per run.
- **Omologazione:** nel caso SF le due versioni, eseguite separatamente, condividevano molte immagini di contorno (la passante con il cappotto color tabacco, le gambe come «attrezzo prestato», la centrifuga, la vista che si stringe «in un tubo»). Dopo il run sono stati aggiunti il «territorio occupato della premessa» (scena §2) e l'indizio «immagine di repertorio» (anti-ai). Questa correzione non è ancora stata verificata in un secondo giro.

Finché manca il giudizio dell'autore, il beneficio sulla prosa resta un'ipotesi. Vale la dottrina della 7.6: l'orecchio dell'autore decide.

## 7.8.1: correzioni dopo l'audit

Solo sottrazioni e chiarimenti; nessuna tecnica nuova. Script, schema e stato invariati.

- **Oggetto che porta il non detto:** resta soltanto in scena §6, come tecnica rara e senza posizioni fisse. Tolto da carta, scheda scena, elenco dei punti decisivi e dialogo. Il PIP ne registra l'uso. Motivo: nei test compariva con lo stesso disegno (entra, torna, chiude) e rischiava di diventare una firma.
- **Quote numeriche:** undici soglie («5–8 candidati», «non più di due risposte piene», «mai tre frasi di fila» e simili) riscritte come criteri con il loro motivo, in linea con la dottrina delle regole contestuali.
- **anti-ai diviso in due:** nucleo con nove indizi principali; il resto (altri nove indizi, calchi italiani, ordine della micro-revisione) in `anti-ai-catalogo.md`, da aprire solo per revisioni di frase approfondite.
- **Scheda scena:** la regola della scheda invisibile sta solo in scrittura; scena §1 ne spiega i campi; SKILL.md rimanda.
- Corretto un refuso in dialogo §5.

### Verifica della 7.8.1

Dodici stesure (quattro prompt, 7.8 e 7.8.1), lette in forma anonima prima di rivelare la versione.

- Nessun peggioramento: vincoli rispettati e qualità equivalente in tutti i confronti; costo per stesura invariato.
- Oggetto ricorrente che chiude la scena: presente in una delle due aperture SF della 7.8, in nessuna delle due della 7.8.1. Campione troppo piccolo per una prova. Nel dialogo il test non distingue, perché la premessa (sgomberare una casa) porta comunque oggetti ricorrenti.
- Omologazione delle immagini: resta in entrambe le versioni (la tessera che cade, la sacca sollevata con due dita, i bollini rossi e verdi). Il passo «territorio occupato della premessa» non la riduce in modo visibile: è un limite del modello, non risolvibile con le sole istruzioni.

## 7.8.2: il mondo dell'autore contro l'omologazione

- Il passo «territorio occupato della premessa», che nei test non riduceva le immagini in comune fra stesure, è sostituito da «prima il mondo dell'autore, poi il repertorio»: i dettagli di contorno si cercano anzitutto nel canone e nei materiali del progetto.
- Nuovo campo facoltativo `narrative_state.palette` (tavolozza del mondo) e scorciatoia `/tavolozza`. Sta nel campo libero dello stato: schema e script invariati, gli stati esistenti restano validi.
- Carta e scrittura non sono state fuse: il risparmio sarebbe minimo (il costo di una stesura dipende dal lavoro del modello, non dal numero di file) e la fusione toccherebbe test e documenti.
