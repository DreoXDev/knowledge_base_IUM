# Piano Codex — Fix finale integrazione Domande IUM

## Obiettivo

Completare davvero la fase finale della knowledge base IUM integrando `Domande IUM.pdf` come fonte critica per la preparazione dell’esame scritto.

La repo non deve essere considerata finita finché:

- tutte le domande del PDF non sono state estratte;
- ogni domanda non ha una risposta validata o marcata come dubbia;
- ogni domanda non ha una flashcard corrispondente;
- gli indici non puntano a file inesistenti;
- `source_registry.md` e README sono coerenti con lo stato reale.

---

## 1. Correggere lo stato della fonte domande

Aprire:

```text
analysis/source_registry.md
```

Aggiornare la riga:

```text
SRC-DOM-001 | Domande IUM.pdf
```

Solo dopo aver completato i passaggi sotto, impostare:

```text
Stato analisi: Analizzato
Report collegato: [[reports/07_domande_ium]]
Note: Domande note d’esame validate contro la KB consolidata; alcune risposte originali erano incomplete o potenzialmente errate.
```

Fino a quel momento lasciarla come `In lavorazione`.

---

## 2. Creare il report di analisi delle domande

Creare:

```text
analysis/reports/07_domande_ium.md
```

Il report deve contenere:

```md
# Report Analisi — Domande IUM

## Fonte

- ID fonte: SRC-DOM-001
- File: Domande IUM.pdf
- Tipo: domande note d’esame
- Stato: analizzato
- Attendibilità originale: media-bassa
- Metodo: ogni risposta è stata verificata contro la knowledge base consolidata.

## Struttura della fonte

- Domande chiuse: 82
- Domande aperte: 3
- Macroaree:
  - Concetti di base
  - Concetti avanzati
  - Valutazione qualitativa
  - Valutazione quantitativa
  - Dark patterns
  - Tecnologie persuasive
  - Domande aperte

## Problemi trovati nella fonte

- Risposte originali non sempre affidabili.
- Alcune risposte sono incomplete.
- Alcune domande hanno testo parziale o opzioni mancanti.
- Alcune risposte statistiche richiedono correzione concettuale.

## Domande critiche da trattare con attenzione

- p-value vs alpha
- NPS
- ABX test
- stima dei problemi non trovati
- test binomiale
- significatività statistica vs pratica
- usabilità ISO 9241
- intervallo di confidenza
```

Aggiungere poi una sezione con elenco sintetico delle domande processate e relativo stato:

```md
| ID | Tipo | Macroarea | Stato | Note |
|---|---|---|---|---|
| Q-001 | chiusa | Concetti base | VALIDATA | Ergonomia |
| ... | ... | ... | ... | ... |
```

---

## 3. Popolare le domande chiuse

Sostituire completamente il placeholder in:

```text
exam_prep/domande_note/domande_chiuse.md
```

Creare una voce per ogni domanda chiusa del PDF, da `Q-001` a `Q-082`.

Formato obbligatorio:

```md
## Q-001 — Ergonomia

**Tipo:** chiusa  
**Fonte:** SRC-DOM-001  
**Macroarea:** Concetti di base  
**Stato risposta:** VALIDATA  
**Concetti collegati:** [[Ergonomia]], [[Ergonomia cognitiva]], [[HCI]]

### Domanda

Una definizione accettabile di ergonomia può essere?

### Risposta corretta

L’ergonomia può essere intesa come studio delle attività e, più nello specifico nel contesto HCI, come ergonomia cognitiva: studio dell’interazione tra l’uomo e gli strumenti per l’elaborazione dell’informazione, considerando processi come percezione, attenzione, memoria, pensiero, linguaggio ed emozioni.

### Spiegazione

Nel corso di IUM il concetto viene collegato alla progettazione per l’utente. L’ergonomia generale riguarda lo studio delle attività, mentre l’ergonomia cognitiva si concentra sui processi cognitivi coinvolti nell’uso di strumenti e sistemi interattivi.

### Note di validazione

Risposta validata contro la KB consolidata. La risposta originale era accettabile ma va resa più chiara distinguendo ergonomia generale ed ergonomia cognitiva.
```

Regole:

- non copiare passivamente le risposte originali;
- usare la KB come fonte principale;
- mantenere risposte di media lunghezza;
- se la domanda è incompleta, usare stato `DA VERIFICARE`;
- se la risposta originale è sbagliata, usare `POTENZIALMENTE ERRATA` nelle note, ma fornire comunque la risposta corretta.

---

## 4. Popolare le domande aperte

Sostituire il placeholder in:

```text
exam_prep/domande_note/domande_aperte.md
```

Creare le tre domande aperte finali:

```text
Q-A01 — Definizione di usabilità secondo ISO 9241
Q-A02 — Definizione e ruolo del p-value nelle valutazioni di usabilità
Q-A03 — Intervallo di confidenza e rilevanza nella valutazione di usabilità
```

Formato:

```md
## Q-A01 — Definizione di usabilità secondo ISO 9241

**Tipo:** aperta  
**Fonte:** SRC-DOM-001  
**Stato risposta:** VALIDATA  
**Concetti collegati:** [[Usabilita]], [[ISO 9241]], [[Efficacia]], [[Efficienza]], [[Soddisfazione]]

### Domanda

Dare la definizione di usabilità secondo lo standard ISO 9241.

### Risposta da esame

Secondo ISO 9241, l’usabilità è il grado con cui un prodotto può essere usato da determinati utenti per raggiungere determinati obiettivi con efficacia, efficienza e soddisfazione in un determinato contesto d’uso.

L’efficacia riguarda il raggiungimento corretto e completo degli obiettivi; l’efficienza riguarda il rapporto tra obiettivi raggiunti e risorse impiegate, come tempo o sforzo; la soddisfazione riguarda il grado di comfort e accettabilità percepito dall’utente.

Un punto fondamentale è che l’usabilità non è una proprietà assoluta del sistema: dipende sempre da utenti, obiettivi, attività e contesto d’uso.
```

---

## 5. Creare una flashcard per ogni domanda

Creare un nuovo file:

```text
exam_prep/flashcards/IUM_domande_flashcards.md
```

Non usare solo `ium_flashcards.md`, che resta come flashcard teoriche generali.

Ogni domanda deve avere una flashcard.

Formato consigliato, leggibile in Obsidian:

```md
## FC-Q001 — Ergonomia

**Domanda:** Qual è una definizione accettabile di ergonomia in IUM?

**Risposta:** L’ergonomia è lo studio delle attività; nel contesto HCI, l’ergonomia cognitiva studia l’interazione tra persone e strumenti per elaborare informazioni, considerando processi come percezione, attenzione, memoria, pensiero, linguaggio ed emozioni.

**Collegata a:** [[domande_note/domande_chiuse#Q-001 — Ergonomia]]
```

Per le domande aperte:

```md
## FC-QA01 — Usabilità ISO 9241

**Domanda:** Qual è la definizione ISO 9241 di usabilità?

**Risposta:** È il grado con cui un prodotto può essere usato da determinati utenti per raggiungere determinati obiettivi con efficacia, efficienza e soddisfazione in uno specifico contesto d’uso.

**Collegata a:** [[domande_note/domande_aperte#Q-A01 — Definizione di usabilità secondo ISO 9241]]
```

Obiettivo minimo:

- 82 flashcard per domande chiuse;
- 3 flashcard per domande aperte;
- totale atteso: 85 flashcard.

---

## 6. Aggiornare domande da verificare

Popolare:

```text
exam_prep/domande_note/domande_da_verificare.md
```

Solo con domande realmente problematiche.

Includere almeno:

```md
| ID | Domanda | Problema | Azione richiesta |
|---|---|---|---|
| Q-045 | livello di significatività osservato | Possibile confusione tra p-value e alpha | Verificare e correggere nella risposta |
| Q-066 | ABX 10/12, 11/12, 7/12 | Richiede calcolo statistico preciso | Controllare con test binomiale |
| Q-068 | stima problemi non trovati | Risposta originale ambigua | Verificare formula e risultato |
| Q-069 | NPS = 10 | Risposta originale probabilmente errata: NPS 10 non implica tutti promotori | Correggere |
| Q-070 | test binomiale nei test trasversali | Risposta originale vaga | Collegare alla priorizzazione/differenze di proporzioni |
```

---

## 7. Correggere gli indici rotti

Aggiornare:

```text
exam_prep/00_Index.md
```

Sostituire link inesistenti:

```md
## Domande note

- [[domande_note/README|README Domande Note]]
- [[domande_note/domande_chiuse|Domande chiuse validate]]
- [[domande_note/domande_aperte|Domande aperte validate]]
- [[domande_note/domande_da_verificare|Domande da verificare]]

## Flashcards

- [[flashcards/README|README Flashcards]]
- [[flashcards/IUM_domande_flashcards|Flashcards da domande d’esame]]
- [[flashcards/ium_flashcards|Flashcards teoriche generali]]
```

Rimuovere o correggere link a:

- `domande/00_Index`
- `domande/domande_note_validate`
- `flashcards/00_Index`
- `checklists/checklist_domande_note`

se quei file non esistono.

---

## 8. Aggiornare README e source registry solo alla fine

Dopo aver completato tutto:

- README può mantenere `Domande note` tra le fonti integrate.
- `analysis/source_registry.md` deve segnare `SRC-DOM-001` come `Analizzato`.
- `analysis/reports/index.md` deve includere `07_domande_ium.md`.
- `exam_prep/flashcards/README.md` deve indicare che esiste un file specifico per le flashcard da domande d’esame.

---

## 9. Criteri di completamento

La task è completa solo se:

- [ ] `analysis/reports/07_domande_ium.md` esiste.
- [ ] `SRC-DOM-001` è segnato come `Analizzato`.
- [ ] `domande_chiuse.md` contiene Q-001 ... Q-082 e non placeholder.
- [ ] `domande_aperte.md` contiene Q-A01 ... Q-A03 e non placeholder.
- [ ] `IUM_domande_flashcards.md` contiene 85 flashcard.
- [ ] `domande_da_verificare.md` contiene solo domande realmente dubbie.
- [ ] `exam_prep/00_Index.md` non contiene link a file o cartelle inesistenti.
- [ ] README e registry sono coerenti.
- [ ] Non restano placeholder tipo “Da inserire dopo analisi asset”.

---

## Verdetto operativo

La repo non è ancora finita, ma è vicina. Serve un ultimo giro Codex molto vincolato e verificabile, centrato solo su:

- domande note;
- risposte validate;
- flashcard;
- report finale;
- registry;
- link rotti.
