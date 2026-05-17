# Piano Codex — Audit finale Knowledge Base IUM prima delle domande note

## Contesto

Repo: `https://github.com/DreoXDev/knowledge_base_IUM`

La knowledge base ha completato l’integrazione delle fonti teoriche/appunti:

- `Appunti IUM 2021.pdf`
- `AppuntiIUM2022.pdf`
- `IUM __ Appunti collettivi collaborativi 2024-25.pdf`
- `Appunti Collettivi 2025-2026.md`

Il prossimo asset sarà `Domande IUM.pdf`, cioè il file di domande note degli esami passati. Prima di usarlo per generare flashcard e risposte validate, è necessario fare un audit finale della repo per evitare che errori strutturali, duplicazioni o note incoerenti si propaghino nelle risposte d’esame.

---

## Obiettivo di questa iterazione

Questa iterazione NON deve ancora analizzare `Domande IUM.pdf`.

Deve invece:

1. controllare lo stato reale della knowledge base;
2. sistemare discrepanze tra README, registry, report e file effettivamente presenti;
3. sistemare problemi di leggibilità Markdown causati da file appiattiti su poche righe;
4. ridurre duplicazioni dannose;
5. preparare la struttura per la successiva generazione di una flashcard per ogni domanda nota;
6. creare un report di audit finale.

---

## Problemi rilevati da correggere

### 1. `source_registry.md` non è allineato

File: `analysis/source_registry.md`

Problema: `Appunti Collettivi 2025-2026.md` risulta ancora `Da analizzare`, ma esiste già il report `06_appunti_collettivi_2025_2026.md` e sono state create note/domande derivate da quella fonte.

Azione:

- Impostare `SRC-APP-001` come `Analizzato`.
- Collegare il report `[[reports/06_appunti_collettivi_2025_2026]]`.
- Aggiornare la nota descrittiva indicando che la fonte è recente ma parziale e rielaborata, con presenza del marker `Gemini 2.5 Pro`.
- Lasciare `SRC-DOM-001 | Domande IUM.pdf` come `Da analizzare`.

Esempio riga corretta:

```md
| SRC-APP-001 | Appunti Collettivi 2025-2026.md | appunti collettivi / sintesi recente | 2025-2026 | Analizzato | Media, con cautela | [[reports/06_appunti_collettivi_2025_2026]] | Fonte recente ma parziale; contiene marker AI e richiede conferma tramite domande note |
```

---

### 2. README non rispecchia completamente lo stato attuale

File: `README.md`

Problema: il README attuale dichiara tra le fonti integrate solo 2021, 2022 e 2024-25, mentre `2025-26` è indicata ancora come fonte in corso/da analizzare.

Azione:

Aggiornare la sezione `Stato knowledge base` così:

```md
### Fonti teoriche integrate

- Appunti IUM 2021
- Appunti IUM 2022
- Appunti collettivi 2024-25
- Appunti Collettivi 2025-2026

### Fonti ancora da analizzare

- Domande IUM.pdf

### Stato attuale

La knowledge base teorica è consolidata in prima versione. Prima di analizzare le domande note è stato svolto un audit finale per verificare coerenza, leggibilità, duplicazioni e collegamenti interni.
```

---

### 3. File Markdown appiattiti su poche righe

Diversi file risultano tecnicamente leggibili ma non comodi in Obsidian perché molti paragrafi, heading, frontmatter e callout sono appiattiti su una sola riga.

Esempi rilevati:

- `README.md`
- `knowledge_base/00_Index.md`
- `analysis/source_registry.md`
- `analysis/conflict_log.md`
- `analysis/pending_questions.md`
- diversi report in `analysis/reports/`
- alcune domande in `exam_prep/domande_note/`
- alcune note teoriche come `Human-Computer Interaction.md`, `Forward-backward translation.md`, `Storia dell_HCI.md`

Azione:

Eseguire un passaggio di formatting conservativo:

- non cambiare il contenuto semantico;
- non riscrivere le spiegazioni;
- non cambiare titoli o path;
- inserire solo newline, righe vuote, separatori e indentazione Markdown;
- preservare frontmatter YAML valido;
- preservare callout Obsidian (`> [!info]`, `> [!question]`, `> [!answer]`, ecc.);
- preservare link interni `[[...]]`;
- preservare tabelle Markdown.

Priorità alta:

1. `README.md`
2. `analysis/source_registry.md`
3. `analysis/reports/index.md`
4. `knowledge_base/00_Index.md`
5. `analysis/conflict_log.md`
6. `analysis/pending_questions.md`
7. `exam_prep/domande_note/*.md`
8. `exam_prep/flashcards/*.md`

---

### 4. Report presenti ma non sempre visibili/ordinati in modo coerente

Controllare `analysis/reports/`.

Devono esistere e risultare linkati:

```md
00_template_asset_report.md
02_appunti_collettivi_2024_2025.md
04_appunti_ium_2021.md
05_appunti_ium_2022.md
06_appunti_collettivi_2025_2026.md
index.md
README.md
```

Azione:

- Verificare che tutti i link nell’indice puntino a file realmente presenti.
- Rimuovere o chiarire riferimenti obsoleti come `03_appunti_ium_2022`, se non esiste più.
- Lasciare `05_domande_ium` / `07_domande_ium` come `Da creare` solo se si stabilisce un nome coerente per il prossimo report.

Nome consigliato per il prossimo report:

```md
analysis/reports/07_domande_ium.md
```

---

### 5. Duplicazioni tra glossario e note teoriche

Sono presenti note duplicate o pseudo-duplicate tra cartelle concettuali e `99_Glossario`.

Esempi:

- `knowledge_base/07_Questionari_e_Valutazione_Quantitativa/Forward-backward translation.md`
- `knowledge_base/99_Glossario/Forward-backward translation.md`
- `knowledge_base/07_Questionari_e_Valutazione_Quantitativa/Item invertiti.md`
- `knowledge_base/99_Glossario/Item invertiti.md`

Azione consigliata:

- Mantenere la nota concettuale completa nella cartella tematica.
- Rendere la voce in `99_Glossario` una mini-voce di glossario o redirect esplicito.
- Non duplicare spiegazioni complete nel glossario.
- Ogni voce glossario deve avere al massimo:
  - definizione brevissima;
  - link alla nota principale;
  - eventuali alias.

Formato consigliato per voci glossario:

```md
# Forward-backward translation

Definizione breve: procedura di traduzione e retro-traduzione usata per mantenere equivalente un questionario validato in un'altra lingua.

Nota principale: [[Forward-backward translation]]

Alias: [[Back-translation]]
```

---

### 6. Link interni potenzialmente ambigui

La KB usa molti link `[[Nome nota]]` senza path. In Obsidian va bene se non esistono note con lo stesso nome in cartelle diverse, ma la presenza di duplicati nel glossario può generare ambiguità.

Azione:

- Cercare note con lo stesso nome in cartelle diverse.
- Se il duplicato è solo un redirect glossario, tenerlo solo se Obsidian non crea ambiguità fastidiosa.
- Se crea ambiguità, rinominare le voci di glossario con suffisso chiaro, ad esempio:
  - `Glossario - Forward-backward translation.md`
  - `Glossario - Item invertiti.md`
- Aggiornare i link interni dove necessario.

Non rinominare note centrali senza aggiornare tutti i backlink.

---

### 7. Stato `da-verificare` da ricontrollare

Alcune note recenti sono correttamente marcate `da-verificare`, soprattutto quando derivano solo dalla fonte 2025-26.

Azione:

Fare una revisione conservativa:

- Se un concetto è confermato da almeno due fonti teoriche indipendenti, impostare `status: confermato`.
- Se deriva solo dal file 2025-26 o contiene dettagli storici molto specifici, mantenere `status: da-verificare`.
- Se è una informazione legata al progetto pratico o a modalità d’esame di un anno specifico, tenerla separata da `knowledge_base/` e lasciarla in `analysis/info_progetto_potenzialmente_obsolete.md`.

Esempi:

- `Human-Computer Interaction.md`: confermato.
- `Sistema socio-tecnico.md`: confermato.
- `Usabilità.md`: confermato.
- `Storia dell_HCI.md`: da-verificare o “parzialmente confermato”, perché alcuni dettagli storici specifici arrivano soprattutto dal 2025-26.
- `Questionario attitudini IA.md`: da-verificare / informazione contestuale al corso.
- `Esperimento Chatbot IA`, se presente: non trattarlo come teoria d’esame centrale.

---

### 8. `pending_questions.md` va aggiornato

Molti dubbi presenti in `pending_questions.md` erano da verificare con gli appunti recenti. Ora gli appunti recenti sono stati analizzati.

Azione:

Aggiornare lo stato:

- Chiudere dubbi risolti dalle fonti 2024-25 e 2025-26.
- Lasciare aperti solo quelli che devono essere verificati tramite `Domande IUM.pdf`.

Esempi:

- Q-003 sulla stabilità della classificazione delle affordance: probabilmente risolta/confermata.
- Dubbi su questionari psicometrici: parzialmente risolti dagli appunti 2024-25 e 2025-26, ma da confrontare con domande note.
- Dubbi su dettagli del progetto: restano aperti ma non rilevanti per lo scritto teorico.

Aggiungere una nuova sezione:

```md
## Da verificare con Domande IUM.pdf

- Quali concetti sono effettivamente ricorrenti negli esami passati?
- Quali definizioni vengono chieste in forma chiusa?
- Quali argomenti avanzati sono davvero richiesti nello scritto?
- Le risposte presenti nel file domande sono coerenti con la KB consolidata?
```

---

### 9. `conflict_log.md` va consolidato

Azione:

- Chiudere i conflitti risolti dalle fonti successive.
- Lasciare aperti solo:
  - dettagli amministrativi/progetto;
  - concetti presenti in una sola fonte;
  - discrepanze da confrontare con domande note.

In particolare:

- `CFL-001`: può essere chiuso se le nozioni 2021 sono state confermate da 2022/2024/2025.
- `CFL-003`: semiotica probabilmente ancora da verificare con domande note se non abbastanza coperta dalle fonti recenti.
- `CFL-005`: SUS e score psicometrici va probabilmente aggiornato con quanto emerso dalle fonti 2024-25 e 2025-26.

---

## Preparazione alla prossima iterazione: Domande IUM.pdf

Dopo i fix, Codex deve preparare la repo per analizzare `Domande IUM.pdf`.

### Requisito fondamentale

Per ogni domanda nota deve essere generata almeno una flashcard.

La risposta non deve copiare ciecamente le risposte presenti nel PDF delle domande, perché il file contiene risposte non affidabili. La risposta deve essere ricostruita usando:

1. la domanda originale;
2. la knowledge base consolidata;
3. eventuali note correlate;
4. lo stato di attendibilità del concetto.

---

## Struttura consigliata per la prossima iterazione

### Nuovo report

Creare:

```md
analysis/reports/07_domande_ium.md
```

Contenuto previsto:

```md
# Report analisi - Domande IUM

## Asset
- File: `assets/raw/domande/Domande IUM.pdf`
- Fonte: `SRC-DOM-001`
- Tipo: domande note esami passati
- Attendibilità risposte originali: media-bassa

## Metodo
- Estrarre ogni domanda.
- Separare domande chiuse e aperte.
- Non fidarsi automaticamente delle risposte originali.
- Per ogni domanda, cercare la nota KB più vicina.
- Generare risposta media, completa, memorizzabile.
- Marcare stato risposta: VALIDATA / PROBABILE / DA VERIFICARE.

## Output richiesti
- `exam_prep/domande_note/domande_ium_validate.md`
- `exam_prep/flashcards/domande_ium_flashcards.md`
- eventuale update di `exam_prep/checklist_ripasso.md`
- eventuale update di note KB se una domanda evidenzia lacune
```

---

## Formato flashcard richiesto

File consigliato:

```md
exam_prep/flashcards/domande_ium_flashcards.md
```

Formato:

```md
## FC-DOM-001

**Domanda:** Una definizione accettabile di ergonomia può essere?

**Risposta:**  
L’ergonomia è lo studio delle attività umane e dell’interazione tra persone, strumenti e ambienti. In IUM è particolarmente importante l’ergonomia cognitiva, che studia come gli strumenti per elaborare informazioni coinvolgono processi come percezione, attenzione, memoria, pensiero, linguaggio ed emozioni, con l’obiettivo di migliorare l’interazione.

**Concetti collegati:** [[Ergonomia cognitiva]], [[Human-Computer Interaction]]

**Fonte domanda:** `Domande IUM.pdf`

**Stato:** `VALIDATA`

**Note:** risposta ricostruita dalla KB, non copiata dalla fonte originale.
```

---

## Formato per domande validate

File consigliato:

```md
exam_prep/domande_note/domande_ium_validate.md
```

Formato:

```md
## DOM-001 - Ergonomia

**Tipo:** chiusa  
**Tema:** Fondamenti HCI  
**Domanda originale:** Una definizione accettabile di ergonomia può essere?

> [!answer] Risposta validata
> ...

**Motivazione:**  
...

**Note KB usate:**  
- [[Ergonomia cognitiva]]
- [[Human-Computer Interaction]]

**Stato:** `VALIDATA`
```

---

## Lunghezza delle risposte

Per ogni domanda:

- Risposta breve ma completa.
- Obiettivo: media lunghezza, adatta a ripasso d’esame.
- Evitare risposte di una sola riga se il concetto è teorico.
- Evitare spiegazioni troppo lunghe stile appunto completo.
- Per domande chiuse: indicare anche perché le alternative corrette sono corrette, se utile.
- Per domande con risposte multiple: gestire tutte le formulazioni corrette senza trattarle come alternative incompatibili.

Target indicativo:

- domanda semplice: 3-5 righe;
- domanda teorica centrale: 6-10 righe;
- domanda avanzata: massimo 12 righe, con link alle note.

---

## Audit finale richiesto prima di passare alle domande

Creare:

```md
analysis/reports/99_audit_pre_domande.md
```

Deve contenere:

```md
# Audit pre-domande

## Stato generale
- [ ] README allineato
- [ ] source_registry allineato
- [ ] report index allineato
- [ ] pending questions aggiornate
- [ ] conflict log aggiornato
- [ ] note duplicate controllate
- [ ] file principali formattati in modo leggibile per Obsidian
- [ ] link interni principali controllati

## Fonti teoriche integrate
- [ ] 2021
- [ ] 2022
- [ ] 2024-25
- [ ] 2025-26

## Fonte successiva
- [ ] Domande IUM.pdf pronta da analizzare

## Problemi rimasti
Elencare solo problemi reali e non bloccanti.
```

---

## Checklist operativa per Codex

1. Eseguire audit dei file principali.
2. Formattare i Markdown appiattiti.
3. Allineare `README.md`.
4. Allineare `analysis/source_registry.md`.
5. Allineare `analysis/reports/index.md`.
6. Aggiornare `analysis/pending_questions.md`.
7. Aggiornare `analysis/conflict_log.md`.
8. Controllare duplicati tra cartelle tematiche e glossario.
9. Non cambiare contenuti teorici se non necessario.
10. Non analizzare ancora `Domande IUM.pdf`.
11. Creare `analysis/reports/99_audit_pre_domande.md`.
12. Terminare con un breve riepilogo dei fix applicati.

---

## Regole di sicurezza contenutistica

- Non eliminare note solo perché sembrano duplicate: prima verificare se sono redirect, alias o voci di glossario.
- Non promuovere informazioni da `da-verificare` a `confermato` se derivano da una sola fonte.
- Non integrare risposte delle domande note senza validarle con la KB.
- Non modificare gli asset raw.
- Non introdurre informazioni nuove da web o memoria esterna.
- Non fare refactor aggressivi dei path senza aggiornare link e indici.

---

## Risultato atteso

Alla fine di questa iterazione la repo deve essere pronta per il passaggio più importante:

> analizzare `Domande IUM.pdf` e generare una flashcard validata per ogni domanda nota, usando la KB appena costruita come fonte primaria per risposte corrette, complete e di media lunghezza.
