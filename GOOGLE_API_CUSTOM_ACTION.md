# GOOGLE SEARCH API SETUP PER CUSTOM GPT

Questo documento spiega come abilitare la ricerca tramite **Google Search API** in modo nativo su ChatGPT per bypassare i blocchi dello scraping web nativo (molto utile per la ricerca dei competitor su Amazon KDP).

## 1. OTTENERE LE CREDENZIALI (Gratuito)

Hai bisogno di due cose:
1. **API Key (Google Cloud)**:
   - Vai su Google Cloud Console.
   - Crea un nuovo progetto.
   - Vai in "Libreria API" e abilita la **Custom Search API**.
   - Genera le Credenziali -> Chiave API. Copia questa chiave.
2. **Search Engine ID (CX)**:
   - Vai su [Programmable Search Engine](https://programmablesearchengine.google.com/).
   - Crea un motore di ricerca che cerca su tutto il web (o solo su amazon.com, amazon.it, se preferisci).
   - Dalle impostazioni, copia il tuo `Search engine ID` (CX).

## 2. CONFIGURAZIONE NEL CUSTOM GPT

Vai su **Edit GPT** -> **Configure** -> **Create new Action**.

Incolla nel blocco **Schema** il seguente codice YAML:

```yaml
openapi: 3.1.0
info:
  title: Google Custom Search API
  description: Esegue ricerche su Google per analizzare trend, competitor e dati di mercato KDP scavalcando i blocchi del Web Browsing nativo.
  version: 1.0.0
servers:
  - url: https://www.googleapis.com
paths:
  /customsearch/v1:
    get:
      summary: Cerca su Google Custom Search
      operationId: searchGoogle
      parameters:
        - name: q
          in: query
          description: La query di ricerca (es. "thriller books amazon.com").
          required: true
          schema:
            type: string
        - name: cx
          in: query
          description: Il tuo Search Engine ID.
          required: true
          schema:
            type: string
        - name: key
          in: query
          description: La tua API Key di Google Cloud.
          required: true
          schema:
            type: string
        - name: num
          in: query
          description: Numero di risultati (max 10).
          required: false
          schema:
            type: integer
            default: 10
      responses:
        '200':
          description: Risultato della ricerca.
          content:
            application/json:
              schema:
                type: object
```

### 3. ISTRUZIONI FINALI
Nel Prompt principale, ChatGPT è già istruito a usare la funzione `searchGoogle` passando sempre nella query i parametri fissi `cx` (inserisci qui il tuo id nel prompt master) e `key` (inserisci qui la chiave nel prompt master).
*(Nota: per maggiore sicurezza, la chiave può essere inserita in "Authentication" impostata su "API Key" usando "Custom", nominandola `key` nel Custom GPT, ma passare il parametro fisso è più immediato).*
