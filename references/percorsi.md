# Percorsi e comandi · BookForge 7.7

Dedurre il percorso dalla richiesta; chiedere soltanto quando ambiguo. Preservare le deleghe e le scelte precedenti.

| Percorso | Flusso |
|---|---|
| A `/nuovo` | Brief → ricerca se utile → indice → stesura → revisione → pacchetto facoltativo |
| B `/revisiona` | Testo + mandato → diagnosi → livello → revisione nel mandato → log |
| C `/continua` | Testo e intenzione → voce + canone con incertezze → parte mancante → continuità |
| D `/collana`, `/sequel` | Serie nuova / sequel / volume successivo → Bibbia → arco → stesura → snapshot |
| Q `/analisi` | Una risposta con punti di forza, problemi prioritari, esempi e prossimo intervento |

Per `/analisi` non imporre salvataggio, questionario o voto commerciale. Se richiesto un giudizio sulla vendibilità distingui evidenze, impressione editoriale e dati di mercato assenti. Per continuare un autore, correggere lo stile non è implicitamente autorizzato: preservare voce e scelte.

## Modalità

**Guidata:** proporre le decisioni sostanziali con poche alternative; domande proporzionate all'esperienza. **Operativa:** proseguire entro un mandato registrato in `workflow.delegations`; non ripetere conferme già ricevute. Le deleghe indicano ambito e limiti. Il comando «continua» può autorizzare la prossima unità senza accettare automaticamente tutto il testo precedente.

L'accettazione del testo e l'approvazione di nuovi fatti sono eventi distinti. Per cambiare il canone o pubblicare serve l'autorizzazione pertinente; una precedente autorizzazione esplicita e ancora applicabile non va chiesta nuovamente.

## Comandi disponibili come scorciatoie

`/scheda`, `/ricerca`, `/indice`, `/scrivi`, `/revisione`, `/kdp` (alias `/pacchetto`), `/lancio`, `/seo`: fasi e KDP. `/personaggio`, `/worldbuilding`: costruzione del progetto. `/clone`: calibrazione da testo. `/granularita capitolo|scena|beat`, `/scena`, `/beat`: unità di lavoro. `/lettore`: lettura critica. `/canon`: coerenza. `/salva`, `/carica`, `/stato`, `/diagrammi`: gestione del progetto. Questi comandi non richiedono parser dedicato: sono richieste in linguaggio naturale.

I percorsi di manuali, saggi e low-content mantengono i loro obiettivi; non imporre personaggi, trauma o conflitto drammatico alla non-fiction. Consulta [generi](generi.md) per adattamenti e [fasi](fasi.md) per gli output.
