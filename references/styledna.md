# StyleDNA · BookForge 7.7

Dodici preferenze descrivono il registro, non una misura della qualità o manopole indipendenti. Il testo approvato e l'intenzione dell'autore prevalgono sul vettore. Una scena può variare per funzione; non forzare una media di capitolo per soddisfare un numero.

## Assi orientativi (1–10)

| # | Parametro | 1 | 5 | 10 |
|---|---|---|---|---|
| 1 | **SENTENCE_LENGTH** | Frasi secche (≤8 parole), Hemingway | Media 15-18 parole | Periodi lunghi (25+), Proust, Saramago |
| 2 | **SYNTAX_COMPLEXITY** | Solo coordinate, punteggiatura minima | Subordinate moderate | Ipotassi profonda, incisi dentro incisi |
| 3 | **RHYTHM_VARIATION** | Frasi tutte uguali | Alternanza prevedibile | Contrasto forte: 3 parole → periodo di 40. Jazz sintattico |
| 4 | **VOCABULARY_RICHNESS** | Lessico <2000 parole base | Medio, qualche termine ricercato | Lessico raro, arcaismi scelti, verbo preciso |
| 5 | **REGISTER_LEVEL** | Parlato, gergale, contrazioni | Professionale, accessibile | Letterario, formale, solenne |
| 6 | **FIGURATIVE_DENSITY** | Zero figure, prosa funzionale | Una metafora ogni 2-3 paragrafi | Ogni frase ha un livello figurativo |
| 7 | **SHOW_VS_TELL** | Dichiarativo ("Era triste") | Mix bilanciato | Tutto incarnato: emozioni nel corpo, concetti in storie |
| 8 | **SENSORY_DEPTH** | Solo visivo basico | Vista + 1-2 sensi | Tutti i sensi: olfatto, tatto, propriocezione |
| 9 | **DIALOGUE_WEIGHT** | Narrazione pura, quasi zero dialogo | 30-40% dialogo | 60%+, avanza per bocca dei personaggi |
| 10 | **EMOTIONAL_TEMP** | Distaccato, analitico, freddo | Emozioni controllate | Viscerale, impatto fisico nel lettore |
| 11 | **SUBTEXT_DENSITY** | Tutto esplicito | Il non-detto esiste ma il detto prevale | Iceberg hemingwayano, leggere tra le righe |
| 12 | **AUTHORIAL_PRESENCE** | Narratore invisibile | Voce discreta | Voce forte, opinioni, digressioni (Ferrante, Franzen) |


I riferimenti ad autori nella tabella sono esempi descrittivi, non richieste di riproduzione. Le lunghezze e percentuali sono orientamenti, non soglie di accettazione. Una preferenza alta non è migliore di una bassa.

## Preset di partenza

```
— FICTION —
📖 NARRATIVO CLASSICO    SL:7 SC:6 RV:7 VR:7 RL:6 FD:6 ST:7 SD:7 DW:5 ET:7 SUB:6 AP:6
🚀 FANTASCIENZA          SL:5 SC:5 RV:6 VR:7 RL:6 FD:5 ST:6 SD:8 DW:5 ET:6 SUB:6 AP:5
🕵️ NOIR / HARDBOILED     SL:4 SC:4 RV:6 VR:6 RL:5 FD:5 ST:6 SD:6 DW:6 ET:6 SUB:6 AP:7
⚡ THRILLER/PAGE-TURNER   SL:4 SC:3 RV:6 VR:4 RL:3 FD:3 ST:7 SD:5 DW:7 ET:8 SUB:5 AP:3
👻 HORROR / WEIRD        SL:5 SC:5 RV:7 VR:6 RL:6 FD:6 ST:7 SD:8 DW:4 ET:6 SUB:7 AP:5
🏰 EPIC FANTASY          SL:7 SC:6 RV:7 VR:7 RL:5 FD:7 ST:7 SD:7 DW:5 ET:6 SUB:5 AP:5
🏛️ ROMANZO STORICO       SL:7 SC:6 RV:6 VR:8 RL:7 FD:6 ST:6 SD:7 DW:5 ET:6 SUB:5 AP:6
🖤 DARK LITERARY         SL:6 SC:7 RV:7 VR:8 RL:7 FD:7 ST:7 SD:8 DW:4 ET:8 SUB:6 AP:7
🔮 REALISMO MAGICO       SL:7 SC:7 RV:7 VR:7 RL:6 FD:8 ST:7 SD:8 DW:4 ET:7 SUB:7 AP:7
💕 ROMANCE CONTEMPORANEO SL:4 SC:3 RV:5 VR:4 RL:3 FD:5 ST:7 SD:4 DW:8 ET:8 SUB:5 AP:5
🌟 YOUNG ADULT           SL:4 SC:4 RV:6 VR:5 RL:3 FD:5 ST:7 SD:5 DW:8 ET:8 SUB:4 AP:5
😄 COMMEDIA/UMORISTICO   SL:4 SC:4 RV:7 VR:6 RL:4 FD:5 ST:6 SD:5 DW:7 ET:7 SUB:4 AP:7
👶 BAMBINI/MIDDLE GRADE  SL:3 SC:2 RV:6 VR:3 RL:2 FD:5 ST:7 SD:6 DW:7 ET:7 SUB:2 AP:4
— NON-FICTION —
🧠 SAGGISTICA AUTOREVOLE SL:5 SC:5 RV:6 VR:6 RL:6 FD:4 ST:5 SD:3 DW:2 ET:4 SUB:3 AP:8
💡 SELF-HELP ACCESSIBILE SL:4 SC:3 RV:5 VR:4 RL:3 FD:4 ST:6 SD:2 DW:4 ET:6 SUB:2 AP:7
📚 MANUALE TECNICO       SL:5 SC:4 RV:4 VR:7 RL:7 FD:2 ST:4 SD:1 DW:1 ET:2 SUB:1 AP:5
🎙️ MEMOIR/AUTOBIOGRAFIA  SL:5 SC:5 RV:7 VR:6 RL:4 FD:5 ST:7 SD:6 DW:5 ET:8 SUB:5 AP:9
```

I valori sono ipotesi iniziali modificabili, non profili validati. Non si applicano tetti universali né deroghe condizionate all'assenza di flag. Per SF, horror e storico usare i rispettivi preset; gli ibridi si costruiscono sul testo dell'autore. Non trasferire lezioni di un singolo libro a tutti i progetti.

## Calibrazione /clone

Partire da un campione approvato; analizzare l'effetto di voce prima dei numeri. Con Python: `python scripts/stylometry.py campione.md --lang it --json`. Lo script è italiano; per altre lingue usare valutazione qualitativa e dichiararlo.

Cinque suggerimenti quantitativi, tutti proxy: SL da ASL, SC da punteggiatura interna, RV da dispersione delle lunghezze, VR da MATTR a finestra fissa, DW dalla quota di parole in dialogo. Sui campioni brevi i suggerimenti possono essere nulli; non inventare la precisione mancante. Le bande sono definite nello script, non duplicate in questo file.

Sette valutazioni qualitative: RL, FD, ST, SD, ET, SUB, AP. Esplicitare le note e un breve campione proposto, lasciando la conferma all'autore. Un numero senza una ragione o un esempio può restare null.

Nel JSON usare `styledna.axes` con chiavi SL, SC, RV, VR, RL, FD, ST, SD, DW, ET, SUB, AP; valori interi 1–10 oppure null. Le note di timbro stanno in `voice_fingerprint`, i campioni e la baseline nelle risorse del progetto. Non sostituire la baseline con ogni capitolo nuovo: approvare esplicitamente un cambiamento del corpus di riferimento.

La MATTR rende il confronto meno sensibile alla lunghezza a parità di finestra e campione adeguato; non elimina effetti di genere, dialogo e argomento. Registrare versione dell'analizzatore, finestra, parole e file sorgente. Il clone preserva una voce: non autorizza miglioramenti non richiesti.
