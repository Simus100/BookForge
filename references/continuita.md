# Canone, conoscenze e serie · BookForge 7.7

La Bibbia serve anche un volume singolo quando il progetto lo richiede. Conserva l'archivio completo; prepara una vista di lavoro con le sole entità, regole, eventi e promesse pertinenti. Una vista condensata non sostituisce l'archivio.

## Tipi di informazioni

| Tipo | Significato |
|---|---|
| `canon` | Fatto approvato del mondo; corredato da origine e approvazione |
| `hypothesis` | Possibilità ancora da decidere; non è verità |
| `belief` | Ciò che un personaggio crede, anche se falso |
| `knowledge` | Informazione attribuita a un personaggio; include origine e momento |
| `rule` | Limite o funzionamento approvato del mondo |

Il campo `known_by` collega le informazioni ai personaggi; `reader_knows` indica se sono state comunicate al lettore. Un progetto con flashback deve esplicitare il momento narrativo in `source` o nei dati aggiuntivi; il validatore non deduce cronologia o onniscienza dal testo.

Usa ID stabili e distinti di progetto, volume, capitolo, scena e personaggio. Una promessa ha origine, stato e eventuale risoluzione; un rinvio consapevole non è una dimenticanza. Relazioni e timeline possono essere strutturate in `narrative_state` e nei file di archivio del manifest.

## `/canon`

Estrai affermazioni e implicazioni rilevanti con posizione nel testo; confrontale con fatti, regole, cronologia e conoscenze pertinenti. Esiti: coerente, non coperto, conflitto. Cita le due evidenze nei conflitti, proponi correzione del testo o emendamento; non risolvere silenziosamente.

Nuovi fatti dalle bozze restano proposte. Un emendamento approvato crea una nuova voce con `supersedes` verso la vecchia; la vecchia passa a `superseded`. Mantieni origine, motivo e approvazione. Decisioni ripetute devono essere idempotenti: non creare lo stesso evento a ogni `/salva`.

## Serie e sequel

Scegli episodico (archi chiusi), seriale (arco distribuito), ibrido. Per un sequel estrai una Bibbia retroattiva con incertezze dichiarate e riferimenti alla prosa. Per nuova serie progetta l'arco condiviso e ciò che ogni volume chiude. Prima di scrivere recupera le promesse e le conoscenze pertinenti; dopo aggiorna solo le decisioni accettate.

A fine volume salva stato del mondo, archi chiusi/aperti, relazioni, ganci e promesse. Il volume successivo usa lo snapshot e l'archivio. Prima della consegna verifica fatti, costi delle regole, voci, cronologia e payoff fra volumi. Il controllo semantico riduce il rischio, non certifica assenza di contraddizioni.

Per non-fiction usa la stessa distinzione fra affermazione, ipotesi e evidenza; conserva fonti e progressione didattica, senza classificare una fonte come vera perché è nel JSON.
