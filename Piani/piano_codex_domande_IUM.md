# Piano Codex — Integrazione `Domande IUM.pdf` nella Knowledge Base IUM

## Obiettivo dell'iterazione

Integrare nella repo `knowledge_base_IUM` il file `Domande IUM.pdf`, che contiene domande note dagli esami passati di Interazione Uomo-Macchina.

Questa iterazione è critica perché le domande note devono diventare il materiale principale di ripasso attivo. Il file contiene risposte già presenti, ma non devono essere considerate automaticamente affidabili: vanno validate usando la knowledge base consolidata costruita dagli appunti 2021, 2022, 2024-25 e 2025-26.

Output principale richiesto:

1. una flashcard per ogni domanda del file;
2. una risposta validata, completa e corretta per ogni domanda;
3. risposte di media lunghezza, adatte allo studio e all'esame scritto;
4. collegamenti interni Obsidian alle note teoriche già presenti nella KB;
5. marcatura esplicita delle domande incomplete, ambigue o con risposta originale sospetta.

---

## Stato attuale da controllare prima di iniziare

Prima di lavorare sulle domande, Codex deve fare un controllo veloce della repo.

### 1. Controllare registro fonti

Aprire:

```text
analysis/source_registry.md
```

Verificare che le fonti di appunti siano segnate come analizzate:

- `Appunti IUM 2021.pdf`
- `AppuntiIUM2022.pdf`
- `IUM __ Appunti collettivi collaborativi 2024-25.pdf`
- `Appunti Collettivi 2025-2026.md`

Se `Appunti Collettivi 2025-2026.md` risulta ancora `Da analizzare`, correggere lo stato in `Analizzato` e collegare il relativo report già creato.

Per `Domande IUM.pdf`, impostare temporaneamente:

```text
Stato analisi: In analisi
Attendibilità: Media-bassa
Note: Fonte critica per exam prep; risposte originali da validare contro KB consolidata.
```

Dopo il completamento dell'iterazione, aggiornare a:

```text
Stato analisi: Analizzato
Report collegato: [[reports/07_domande_ium]]
```

### 2. Controllare README

Aprire:

```text
README.md
```

Correggere eventuali discrepanze tra:

- fonti integrate;
- fonti in corso;
- fonti da analizzare.

Dopo questa iterazione, `Domande IUM.pdf` deve risultare tra le fonti integrate.

### 3. Controllare leggibilità Markdown

Prima di aggiungere nuovo materiale, verificare che i file modificati non vengano appiattiti in pochissime righe.

Regola obbligatoria:

- ogni heading deve stare su una riga propria;
- ogni lista deve avere un elemento per riga;
- ogni tabella deve avere una riga per record;
- evitare paragrafi lunghissimi;
- mantenere il vault leggibile in Obsidian senza plugin speciali.

---

## Fonte da integrare

File:

```text
assets/raw/Domande IUM.pdf
```

Contenuto atteso:

- domande chiuse su concetti di base;
- domande chiuse su concetti avanzati;
- domande su valutazione qualitativa;
- domande su valutazione quantitativa e statistica;
- domande su dark patterns;
- domande su tecnologie persuasive;
- domande aperte finali.

Il file sembra contenere:

- 82 domande chiuse numerate;
- 3 domande aperte;
- alcune risposte incomplete, mancanti o probabilmente errate;
- alcune domande con opzioni non presenti;
- alcune risposte che sono più appunti grezzi che risposte definitive.

---

## Principio fondamentale: non fidarsi delle risposte originali

Codex deve trattare il file come fonte di domande, non come fonte definitiva di risposte.

Per ogni domanda:

1. estrarre il testo della domanda;
2. leggere la risposta proposta nel PDF;
3. cercare nella KB consolidata le note collegate;
4. generare una risposta finale corretta;
5. segnalare se la risposta originale era:
   - corretta;
   - incompleta;
   - ambigua;
   - probabilmente errata;
   - impossibile da verificare;
6. creare una flashcard autonoma.

Le risposte finali devono essere formulate per studiare, non solo per scegliere una crocetta.

---

## Struttura dei nuovi file da creare

Creare o aggiornare questa struttura:

```text
analysis/reports/07_domande_ium.md
exam_prep/domande/00_Index.md
exam_prep/domande/domande_note_validate.md
exam_prep/flashcards/00_Index.md
exam_prep/flashcards/IUM_domande_flashcards.md
exam_prep/flashcards/IUM_domande_flashcards_anki.tsv
exam_prep/checklists/checklist_domande_note.md
```

Se alcune cartelle non esistono, crearle.

---

## File 1 — Report di analisi

Creare:

```text
analysis/reports/07_domande_ium.md
```

### Contenuto richiesto

```markdown
# Report 07 — Domande IUM

> [!Info]
> Fonte: `Domande IUM.pdf`  
> Tipo: domande note da esami passati  
> Attendibilità risposte originali: media-bassa  
> Uso principale: generazione flashcard e controllo copertura KB

## Sintesi

Breve descrizione del file e del suo ruolo.

## Sezioni individuate

| Sezione | Range domande | Tema |
|---|---:|---|
| Concetti di base | 1-24 | HCI, ergonomia, usabilità, affordance, mapping, constraint, STS |
| Concetti avanzati | 25-33 | CASA, captologia, ethopoeia, semiotica |
| Valutazioni qualitative | 34-39 | valutazione euristica, undo, sistemi modali |
| Valutazioni quantitative | 40-73 | UX, usabilità ISO, inferenza statistica, p-value, NPS, Likert, low use |
| Dark patterns | 74-76 | trappola per insetti, forced continuity, bait and switch |
| Tecnologie persuasive | 77-82 | credibilità, Hook model, Fogg behavior model |
| Domande aperte | A1-A3 | usabilità ISO, p-value, intervallo di confidenza |

## Copertura rispetto alla KB

Tabella con:

| Tema | Note KB usate | Copertura | Azione |
|---|---|---|---|

## Domande problematiche

Elencare tutte le domande con risposta originale mancante, dubbia o errata.

## Decisioni di integrazione

Spiegare come sono state generate le flashcard e dove sono state salvate.
```

---

## File 2 — Domande validate

Creare:

```text
exam_prep/domande/domande_note_validate.md
```

Questo file deve contenere tutte le domande con risposta validata, organizzate per sezione.

### Formato per ogni domanda chiusa

Usare questo formato:

```markdown
## Q001 — Ergonomia

> [!Question]
> Una definizione accettabile di ergonomia può essere?

**Risposta validata:**  
L'ergonomia è lo studio delle attività umane e, nel contesto HCI, dell'interazione tra persone e strumenti per l'elaborazione dell'informazione. L'ergonomia cognitiva considera processi come percezione, attenzione, memoria, pensiero, linguaggio ed emozioni, con l'obiettivo di progettare strumenti più adatti alle capacità e ai limiti degli utenti.

**Risposta originale:** corretta ma da precisare.

**Note KB collegate:**
- [[Ergonomia]]
- [[Ergonomia cognitiva]]
- [[HCI]]

**Stato:** validata
```

### Formato per domande aperte

```markdown
## QA01 — Definizione di usabilità secondo ISO 9241

> [!Question]
> Dare la definizione di usabilità secondo lo standard ISO 9241.

**Risposta da esame:**  
Secondo ISO 9241, l'usabilità è il grado con cui un prodotto può essere usato da determinati utenti per raggiungere determinati obiettivi con efficacia, efficienza e soddisfazione in uno specifico contesto d'uso. La definizione implica che l'usabilità non sia una proprietà assoluta del sistema, ma dipenda da utenti, obiettivi e contesto. L'efficacia riguarda il raggiungimento corretto e completo degli obiettivi, l'efficienza riguarda le risorse impiegate, mentre la soddisfazione riguarda la qualità percepita dell'esperienza d'uso.

**Note KB collegate:**
- [[Usabilità secondo ISO 9241]]
- [[Efficacia]]
- [[Efficienza]]
- [[Soddisfazione]]
- [[Contesto d'uso]]

**Stato:** validata
```

---

## File 3 — Flashcard Obsidian

Creare:

```text
exam_prep/flashcards/IUM_domande_flashcards.md
```

Questo file deve contenere una flashcard per ogni domanda.

### Formato obbligatorio

Usare il formato semplice domanda/risposta, leggibile anche senza plugin:

```markdown
## FC-Q001 — Ergonomia

**Domanda**  
Una definizione accettabile di ergonomia può essere?

**Risposta**  
L'ergonomia è lo studio delle attività umane. Nel contesto HCI, l'ergonomia cognitiva studia l'interazione tra persone e strumenti di elaborazione dell'informazione, considerando processi cognitivi come percezione, attenzione, memoria, pensiero, linguaggio ed emozioni, per progettare strumenti più adatti agli utenti.

**Tag:** #ium #flashcard #concetti-base #ergonomia

---
```

### Lunghezza risposta

Le risposte devono essere di media lunghezza:

- non una sola parola;
- non un paragrafo enciclopedico;
- idealmente 4-8 righe per le domande teoriche;
- 6-10 righe per domande statistiche o domande aperte;
- più brevi solo per definizioni molto semplici.

---

## File 4 — Export Anki TSV

Creare:

```text
exam_prep/flashcards/IUM_domande_flashcards_anki.tsv
```

Formato tab-separated:

```text
ID<TAB>Domanda<TAB>Risposta<TAB>Tags
```

Esempio:

```text
Q001	Una definizione accettabile di ergonomia può essere?	L'ergonomia è lo studio delle attività umane...	ium concetti-base ergonomia
```

Regole:

- una riga per flashcard;
- non inserire tab dentro domanda o risposta;
- sostituire eventuali newline interni con `<br>`;
- usare tag senza `#` nell'export Anki.

---

## File 5 — Checklist di copertura

Creare:

```text
exam_prep/checklists/checklist_domande_note.md
```

Contenuto:

```markdown
# Checklist — Domande note IUM

## Stato generale

- [ ] Tutte le domande del PDF sono state estratte.
- [ ] Ogni domanda ha una risposta validata.
- [ ] Ogni domanda ha almeno una flashcard.
- [ ] Le risposte originali dubbie sono state segnalate.
- [ ] Le domande con opzioni mancanti sono state marcate.
- [ ] Le flashcard sono esportate anche in TSV per Anki.
- [ ] README e source registry aggiornati.

## Copertura per sezione

- [ ] Concetti di base: Q001-Q024
- [ ] Concetti avanzati: Q025-Q033
- [ ] Valutazioni qualitative: Q034-Q039
- [ ] Valutazioni quantitative: Q040-Q073
- [ ] Dark patterns: Q074-Q076
- [ ] Tecnologie persuasive: Q077-Q082
- [ ] Domande aperte: QA01-QA03
```

---

## Mappatura degli ID

Usare ID stabili.

### Domande chiuse

```text
Q001 ... Q082
```

Mantenere lo stesso ordine del PDF.

### Domande aperte

```text
QA01 ... QA03
```

### Flashcard

```text
FC-Q001 ... FC-Q082
FC-QA01 ... FC-QA03
```

---

## Sezioni e tag consigliati

Usare questi tag nelle flashcard:

```text
#ium
#flashcard
#concetti-base
#concetti-avanzati
#valutazione-qualitativa
#valutazione-quantitativa
#dark-patterns
#tecnologie-persuasive
#statistica
#semiotica
#usabilita
#questionari
```

Esempi:

- Q001-Q024: `#concetti-base`
- Q025-Q033: `#concetti-avanzati`
- Q034-Q039: `#valutazione-qualitativa`
- Q040-Q073: `#valutazione-quantitativa`
- Q074-Q076: `#dark-patterns`
- Q077-Q082: `#tecnologie-persuasive`
- QA01-QA03: `#domande-aperte`

---

## Domande da trattare con attenzione speciale

Durante la validazione, controllare in modo particolare queste domande.

### Q033 — Motivazioni intrinseche e umane supportate da tecnologia mobile

Nel PDF la risposta sembra mancante. Cercare nella KB se il tema è stato trattato. Se non c'è copertura sufficiente, creare flashcard con stato:

```text
Stato: da verificare / risposta non coperta dalla KB attuale
```

Non inventare una risposta lunga se la KB non contiene abbastanza materiale.

### Q045 — Livello di significatività osservato

Nel PDF la risposta sembra confondere `p-value` e `alpha`.

Correzione attesa:

- il livello di significatività osservato è il `p-value`;
- `alpha` è il livello di significatività fissato a priori;
- si rigetta H0 quando `p-value < alpha`.

### Q046 — Alpha

Questa risposta è probabilmente corretta, ma va distinta chiaramente da Q045.

### Q056-Q057-Q069 — NPS

Controllare bene.

- NPS = `% promotori - % detrattori`;
- promotori: 9-10;
- passivi: 7-8;
- detrattori: 0-6;
- range: da -100 a +100.

Attenzione: un NPS di 10 non significa che tutti siano promotori o che i detrattori siano zero. Significa che la percentuale dei promotori supera quella dei detrattori di 10 punti percentuali.

### Q059 — Asterischi del p-value

Verificare la convenzione usata nella KB. Se non esiste una convenzione esplicita, usare quella tipica:

- `*` per `p < 0.05`;
- `**` per `p < 0.01`;
- `***` per `p < 0.001`.

Segnalare che le convenzioni possono variare, quindi va sempre riportata una legenda.

### Q064 — Tipi di variabili e media

La domanda nel PDF sembra incompleta o con opzioni ambigue.

Risposta concettuale da validare:

- media: appropriata per variabili quantitative, soprattutto scale a intervalli o rapporti;
- mediana: più adatta a variabili ordinali;
- moda: adatta a variabili categoriche/nominali.

### Q066 — ABX test

Il file contiene opzioni numeriche. Validare con attenzione.

Per 12 tentativi e ipotesi nulla di scelta casuale con probabilità 0.5, il numero minimo di risposte corrette per significatività al 5% è probabilmente 10/12, perché la probabilità di ottenere almeno 10 successi su 12 per caso è inferiore a 0.05.

Codex deve verificare il calcolo e spiegare la logica nella risposta.

### Q068 — Stima problemi non trovati

Controllare la formula e il risultato.

Formula utile:

```text
problemi_trovati = totale_problemi * (1 - (1 - p)^n)
```

Con:

- problemi trovati = 12;
- p = 0.70;
- n = 3.

Allora:

```text
probabilità di trovare un problema dal gruppo = 1 - 0.3^3 = 0.973
problemi totali stimati = 12 / 0.973 ≈ 12.33
problemi non ancora identificati ≈ 0.33
```

In una risposta a crocette, la scelta più ragionevole potrebbe essere `0`, ma va spiegato che il valore stimato è circa un terzo di problema, quindi praticamente nessuno.

### Q070 — Test binomiale nei comparativi trasversali

La risposta originale è troppo vaga o sospetta. Validare contro la KB.

Il test binomiale può essere usato quando si contano successi/insuccessi o preferenze binarie, per verificare se una proporzione osservata differisce da quella attesa sotto H0.

### Domanda aperta 2 — p-value

Nel PDF c'è un errore nella frase:

```text
si può rigettare l'ipotesi nulla e ipotizzare che l'ipotesi nulla sia vera
```

Correggere in:

```text
si può rigettare l'ipotesi nulla e considerare supportata l'ipotesi alternativa, nei limiti del test e del livello alpha scelto.
```

---

## Uso della KB consolidata

Per ogni risposta, Codex deve cercare le note collegate nella KB.

Esempi di mapping:

| Domande | Note KB probabili |
|---|---|
| Q001 | `Ergonomia`, `Ergonomia cognitiva`, `HCI` |
| Q002, QA01 | `Usabilità secondo ISO 9241`, `Efficacia`, `Efficienza`, `Soddisfazione` |
| Q004-Q006 | `Affordance`, `Mapping` |
| Q007 | `Constraint`, `Workaround` |
| Q010-Q015 | `Overreliance`, `Automation bias`, `Overconfidence`, `Overdependence`, `Complacency` |
| Q021 | `Sistema socio-tecnico`, `Proprietà emergenti`, `Conseguenze inattese` |
| Q025-Q032 | `CASA`, `Captologia`, `Ethopoeia`, `Semiotica`, `Peirce`, `Abduzione` |
| Q034-Q039 | `Valutazione euristica`, `Undo`, `Sistema modale`, `Problemi prioritizzati` |
| Q040-Q073 | `Valutazione quantitativa`, `p-value`, `alpha`, `NPS`, `Likert`, `Mann-Whitney`, `Low Use` |
| Q074-Q076 | `Dark patterns` |
| Q077-Q082 | `Credibilità`, `Hook model`, `Fogg Behavior Model` |

Se una nota non esiste ma il concetto è presente in altra nota più ampia, usare il link alla nota più ampia. Se il concetto è importante e ricorrente, creare una nuova nota atomica nella sezione corretta della KB.

---

## Regole per nuove note atomiche

Creare nuove note solo se servono davvero.

Possibili nuove note da creare o controllare:

```text
knowledge_base/08_Tecnologie_Persuasive/Hook Model.md
knowledge_base/08_Tecnologie_Persuasive/Fogg Behavior Model.md
knowledge_base/08_Tecnologie_Persuasive/Credibilita.md
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/NPS.md
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/ABX test.md
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/Test binomiale.md
knowledge_base/06_Valutazione_Qualitativa/Flip undo.md
knowledge_base/06_Valutazione_Qualitativa/Sistema modale.md
```

Non duplicare contenuti già presenti. Se una nota esiste già, aggiornarla e aggiungere backlink dalle flashcard.

---

## Qualità delle risposte

Ogni risposta deve essere:

- corretta rispetto alla KB;
- abbastanza completa da essere studiabile;
- non troppo lunga;
- scritta in italiano pulito;
- priva di tono incerto quando la KB supporta bene il concetto;
- marcata come `da verificare` quando la KB non basta;
- utile sia per domande chiuse sia per possibili domande aperte.

### Evitare

- copiare passivamente le risposte del PDF;
- lasciare risposte con errori già noti;
- creare flashcard troppo vaghe;
- creare risposte da una riga quando il concetto è importante;
- creare spiegazioni lunghissime che rendono le flashcard inutilizzabili;
- duplicare la stessa risposta in più note senza linkare concetti comuni.

---

## Aggiornamento degli indici

Aggiornare:

```text
exam_prep/00_Index.md
exam_prep/domande/00_Index.md
exam_prep/flashcards/00_Index.md
knowledge_base/00_Index.md
README.md
analysis/source_registry.md
```

Gli indici devono permettere di trovare rapidamente:

- domande validate;
- flashcard;
- export Anki;
- checklist;
- report di analisi.

---

## Workflow consigliato per Codex

1. Leggere `Domande IUM.pdf` o la sua trascrizione disponibile in `assets/raw/`.
2. Estrarre tutte le domande in ordine.
3. Creare una tabella temporanea con:
   - ID;
   - testo domanda;
   - risposta originale;
   - sezione;
   - stato risposta originale;
   - note KB da usare.
4. Validare ogni risposta contro la KB.
5. Scrivere `analysis/reports/07_domande_ium.md`.
6. Scrivere `exam_prep/domande/domande_note_validate.md`.
7. Scrivere `exam_prep/flashcards/IUM_domande_flashcards.md`.
8. Scrivere `exam_prep/flashcards/IUM_domande_flashcards_anki.tsv`.
9. Scrivere `exam_prep/checklists/checklist_domande_note.md`.
10. Aggiornare README, source registry e indici.
11. Fare un controllo finale di coerenza.

---

## Controllo finale richiesto

Alla fine, Codex deve riportare nel suo output:

```markdown
## Controllo finale

- Numero domande chiuse estratte: ...
- Numero domande aperte estratte: ...
- Numero flashcard create: ...
- Numero risposte validate: ...
- Numero risposte marcate da verificare: ...
- File creati/modificati: ...
- Domande problematiche principali: ...
```

Criteri di accettazione:

- Devono esserci almeno 85 flashcard totali se il file contiene 82 domande chiuse + 3 aperte.
- Nessuna domanda deve essere saltata silenziosamente.
- Le domande incomplete devono essere presenti e marcate come incomplete, non rimosse.
- Le risposte statistiche devono correggere eventuali errori del PDF.
- `NPS`, `p-value`, `alpha`, `intervallo di confidenza`, `ABX`, `test binomiale` devono essere trattati con particolare attenzione.
- Il vault deve restare leggibile in Obsidian.

---

## Commit consigliato

Messaggio commit consigliato:

```text
feat(exam-prep): add validated IUM questions and flashcards
```

