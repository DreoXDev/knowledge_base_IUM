# Piano Codex — Inizializzazione Knowledge Base IUM

> Progetto: Knowledge Base Obsidian per **Interazione Uomo-Macchina**  
> Focus: preparazione alla parte **scritta teorica** dell’esame  
> Metodo: repository Markdown leggibile in Obsidian, aggiornata tramite AI/Codex, con analisi progressiva degli asset uno per uno.

---

## 1. Obiettivo della repo

Questa repo deve diventare un vault Obsidian strutturato per studiare la parte teorica dell’esame di **Interazione Uomo-Macchina**.

L’esame, per questa fase del progetto, viene trattato come un esame:

- prevalentemente teorico;
- senza esercizi numerici o procedurali;
- basato su concetti, definizioni, esempi, confronti e domande note;
- da preparare attraverso memorizzazione, comprensione e capacità di risposta sintetica.

La repo non deve essere scritta manualmente in modo libero, ma deve essere progettata per essere mantenuta tramite AI/Codex, usando un flusso controllato:

1. caricare asset raw nella repo;
2. analizzare ogni asset singolarmente con ChatGPT web chat;
3. produrre un report di analisi per ogni asset;
4. passare il report a Codex;
5. far aggiornare la knowledge base in modo ordinato, tracciabile e coerente.

La repo deve rimanere leggibile direttamente da Obsidian.

---

## 2. Asset iniziali del progetto

Gli asset di partenza sono:

```text
assets/raw/
├── domande/
│   └── Domande IUM.pdf
├── appunti-studenti/
│   ├── Appunti Collettivi 2025-2026.md
│   ├── Appunti IUM 2021.pdf
│   ├── AppuntiIUM2022.pdf
│   └── IUM - Appunti collettivi collaborativi 2024-25.pdf
```

### Ruolo degli asset

| Asset | Ruolo nella repo | Attendibilità iniziale |
|---|---|---|
| Domande note | Base per costruire FAQ, flashcard e simulazioni d’esame | Media-bassa: risposte da verificare |
| Appunti cumulativi studenti anni passati | Fonte principale per ricostruire il programma e i concetti ricorrenti | Media |
| Appunti collettivi recenti | Fonte utile per capire il taglio più aggiornato del corso | Media-alta, ma comunque da verificare |

Nessun asset deve essere considerato automaticamente affidabile. Tutti i contenuti devono essere integrati nella knowledge base solo dopo essere passati da un report di analisi.

---

## 3. Principi generali

### 3.1 La repo è una knowledge base, non una cartella di appunti casuali

Ogni nota deve avere una funzione precisa:

- spiegare un concetto;
- collegare concetti correlati;
- preparare una possibile domanda d’esame;
- raccogliere dubbi o conflitti tra fonti;
- sintetizzare cosa va memorizzato.

Evitare note lunghe senza struttura.

---

### 3.2 Separare sempre raw, analisi e knowledge base finale

Non modificare mai direttamente gli asset raw.

Ogni informazione deve passare da questi livelli:

```text
assets/raw/                  # file originali non modificati
analysis/reports/             # report prodotti dopo analisi AI dei singoli asset
knowledge_base/               # note finali consolidate per lo studio
exam_prep/                    # domande, flashcard, simulazioni, checklist
```

---

### 3.3 Le risposte alle domande note non sono affidabili finché non vengono validate

Le domande note servono soprattutto per capire:

- quali concetti sono stati chiesti;
- con che formulazione vengono chiesti;
- quali distrattori o ambiguità compaiono spesso;
- quali definizioni vanno sapute in modo preciso.

Le risposte già presenti devono essere classificate come:

```text
VALIDATA
PROBABILE
DA VERIFICARE
POTENZIALMENTE ERRATA
```

---

### 3.4 La knowledge base deve essere Obsidian-first

Tutti i file Markdown devono essere leggibili bene in Obsidian.

Usare:

- link interni `[[Nome Nota]]`;
- tag coerenti;
- callout Obsidian;
- sezioni brevi;
- tabelle quando aiutano;
- blocchi “Da ricordare” e “Possibile domanda d’esame”.

Evitare markdown troppo complesso o dipendente da plugin non standard.

---

## 4. Struttura iniziale della repo

Codex deve creare questa struttura:

```text
knowledge_base_IUM/
├── README.md
├── PROJECT_CONTEXT.md
├── CODEX_INSTRUCTIONS.md
├── .gitignore
├── assets/
│   ├── raw/
│   │   ├── domande/
│   │   └── appunti-studenti/
│   └── processed/
│       ├── extracted-text/
│       └── normalized/
├── analysis/
│   ├── reports/
│   │   ├── README.md
│   │   ├── 00_template_asset_report.md
│   │   └── index.md
│   ├── source_registry.md
│   ├── conflict_log.md
│   └── pending_questions.md
├── knowledge_base/
│   ├── 00_Index.md
│   ├── 01_Fondamenti_HCI/
│   ├── 02_Sistemi_Socio_Tecnici/
│   ├── 03_Usabilita/
│   ├── 04_Affordance_Mapping_Constraints/
│   ├── 05_Valutazione_Usabilita/
│   ├── 06_Valutazione_Euristica/
│   ├── 07_Questionari_e_Valutazione_Quantitativa/
│   ├── 08_Dark_Patterns_e_Persuasione/
│   ├── 09_Semiotica_e_Ingegneria_Semiotica/
│   ├── 10_Automazione_Bias_e_Conseguenze_Inattese/
│   └── 99_Glossario/
├── exam_prep/
│   ├── 00_Index.md
│   ├── domande_note/
│   │   ├── README.md
│   │   ├── domande_chiuse.md
│   │   ├── domande_aperte.md
│   │   └── domande_da_verificare.md
│   ├── flashcards/
│   │   ├── README.md
│   │   └── ium_flashcards.md
│   ├── simulazioni/
│   │   ├── README.md
│   │   └── simulazione_01.md
│   └── checklist_ripasso.md
├── templates/
│   ├── concept_note_template.md
│   ├── question_note_template.md
│   ├── asset_report_template.md
│   ├── conflict_entry_template.md
│   └── flashcard_template.md
└── workflows/
    ├── 00_workflow_generale.md
    ├── 01_import_asset.md
    ├── 02_analisi_asset_con_chatgpt.md
    ├── 03_update_kb_from_report.md
    ├── 04_validazione_domande.md
    └── 05_generazione_materiale_esame.md
```

---

## 5. File principali da creare

### 5.1 `README.md`

Deve spiegare in modo sintetico:

- cos’è la repo;
- che esame riguarda;
- dove si trovano gli asset raw;
- dove si trovano le note finali;
- come usare la repo in Obsidian;
- qual è il workflow AI-based.

Contenuto minimo:

```md
# Knowledge Base IUM

Vault Obsidian per la preparazione della parte teorica dell’esame di Interazione Uomo-Macchina.

La repo separa:

- asset originali;
- report di analisi;
- knowledge base consolidata;
- materiale di ripasso per l’esame.

Il flusso consigliato è:

1. importare un asset in `assets/raw/`;
2. analizzarlo con ChatGPT;
3. salvare il report in `analysis/reports/`;
4. usare Codex per aggiornare le note in `knowledge_base/`;
5. aggiornare domande, flashcard e checklist in `exam_prep/`.
```

---

### 5.2 `PROJECT_CONTEXT.md`

Deve contenere il contesto permanente per tutte le AI che lavorano sulla repo.

Contenuto richiesto:

```md
# Project Context — Knowledge Base IUM

Questa repo serve per costruire una knowledge base in Markdown/Obsidian per l’esame scritto teorico di Interazione Uomo-Macchina.

Il corso riguarda concetti come:

- Human-Computer Interaction;
- ergonomia cognitiva;
- sistemi socio-tecnici;
- usabilità;
- affordance, mapping e constraints;
- valutazione di usabilità;
- valutazione euristica;
- questionari psicometrici e scale Likert;
- dark patterns;
- tecnologie persuasive;
- semiotica e ingegneria semiotica;
- overreliance, automation bias, complacency, overconfidence e overdependence.

Gli asset iniziali includono appunti collettivi di diversi anni e un file di domande note.

Le domande note possono contenere risposte imprecise o sbagliate: non devono essere copiate nella knowledge base senza validazione.

La repo deve essere mantenuta da AI/Codex, ma deve restare leggibile e studiabile in Obsidian.
```

---

### 5.3 `CODEX_INSTRUCTIONS.md`

Codex deve seguire queste regole.

```md
# Codex Instructions

## Regole fondamentali

1. Non modificare mai i file in `assets/raw/`.
2. Non integrare contenuti nella knowledge base senza un report in `analysis/reports/`.
3. Quando aggiorni una nota, mantieni lo stile Obsidian.
4. Usa link interni `[[...]]` tra concetti correlati.
5. Non duplicare lo stesso contenuto in più note: crea una nota principale e collegala.
6. Se due fonti sono in conflitto, aggiorna `analysis/conflict_log.md` invece di scegliere arbitrariamente.
7. Se una risposta a una domanda nota non è verificata, marcarla come `DA VERIFICARE`.
8. Ogni nota concettuale deve contenere almeno:
   - definizione;
   - spiegazione breve;
   - esempio;
   - collegamenti;
   - possibili domande d’esame.
9. Non usare emoji nei file Markdown.
10. Scrivi in italiano chiaro, con tono da appunti universitari.

## Stile Markdown

Usa callout Obsidian quando utili:

```md
> [!info] Definizione
> Testo della definizione.

> [!example] Esempio
> Esempio pratico.

> [!warning] Attenzione d’esame
> Errore comune o distinzione importante.

> [!question] Possibile domanda d’esame
> Domanda formulata come potrebbe comparire nello scritto.
```

## Output atteso dopo ogni update

Ogni volta che aggiorni la repo, restituisci un riepilogo con:

- file creati;
- file modificati;
- concetti aggiunti;
- domande aggiornate;
- conflitti o dubbi aperti;
- prossimo asset consigliato da analizzare.
```

---

## 6. Template delle note concettuali

Codex deve creare `templates/concept_note_template.md`:

```md
# {{Titolo Concetto}}

Tags: #ium #concetto/{{categoria}}

---

## Definizione breve

> [!info] Definizione
> {{definizione sintetica e memorizzabile}}

---

## Spiegazione

{{spiegazione chiara del concetto}}

---

## Perché è importante in IUM

{{ruolo del concetto nel corso}}

---

## Esempio

> [!example] Esempio
> {{esempio pratico}}

---

## Distinzioni importanti

| Concetto | Differenza |
|---|---|
| {{concetto correlato}} | {{differenza}} |

---

## Possibili domande d’esame

> [!question] Domanda
> {{domanda possibile}}

Risposta attesa:

{{risposta sintetica}}

---

## Collegamenti

- [[Concetto collegato 1]]
- [[Concetto collegato 2]]

---

## Fonti interne

- {{asset/report da cui deriva la nota}}

---

## Stato

Stato: `BOZZA | DA VERIFICARE | CONSOLIDATO`
```

---

## 7. Template report di analisi asset

Codex deve creare `templates/asset_report_template.md` e copiarlo anche in `analysis/reports/00_template_asset_report.md`.

```md
# Asset Report — {{Nome asset}}

Data analisi: {{data}}
Asset analizzato: `{{path asset}}`
Tipo asset: `appunti | domande | slide | altro`
Stato report: `BOZZA | COMPLETO | DA RIVEDERE`

---

## 1. Riassunto dell’asset

{{breve descrizione del contenuto}}

---

## 2. Struttura rilevata

{{capitoli, sezioni, argomenti principali}}

---

## 3. Concetti principali estratti

| Concetto | Categoria | Priorità esame | Note |
|---|---|---|---|
| {{concetto}} | {{categoria}} | Alta/Media/Bassa | {{nota}} |

---

## 4. Definizioni utili

| Termine | Definizione proposta | Attendibilità | Azione richiesta |
|---|---|---|---|
| {{termine}} | {{definizione}} | Alta/Media/Bassa | Integrare/Verificare/Ignorare |

---

## 5. Esempi rilevanti

| Esempio | Concetto collegato | Utilità |
|---|---|---|
| {{esempio}} | [[{{concetto}}]] | {{perché serve}} |

---

## 6. Domande d’esame collegate

| Domanda | Tipo | Risposta presente? | Stato risposta |
|---|---|---|---|
| {{domanda}} | chiusa/aperta | sì/no | validata/probabile/da verificare |

---

## 7. Conflitti o dubbi

| Punto dubbio | Fonte/Sezione | Descrizione | Azione consigliata |
|---|---|---|---|
| {{dubbio}} | {{fonte}} | {{descrizione}} | {{azione}} |

---

## 8. Azioni richieste a Codex

- [ ] Creare nuove note per i concetti mancanti.
- [ ] Aggiornare note esistenti con definizioni migliori.
- [ ] Aggiungere esempi rilevanti.
- [ ] Aggiornare il glossario.
- [ ] Aggiornare le domande note.
- [ ] Aggiungere eventuali conflitti a `analysis/conflict_log.md`.
- [ ] Aggiornare `knowledge_base/00_Index.md`.

---

## 9. Note finali per lo studio

{{cosa deve ricordare lo studente da questo asset}}
```

---

## 8. Registry delle fonti

Codex deve creare `analysis/source_registry.md`:

```md
# Source Registry

Registro degli asset usati per costruire la knowledge base.

| ID Fonte | Nome file | Tipo | Anno | Stato analisi | Attendibilità | Report collegato | Note |
|---|---|---|---|---|---|---|---|
| SRC-DOM-001 | Domande IUM.pdf | domande note | 2020-2021 | Da analizzare | Media-bassa | | Risposte non affidabili da verificare |
| SRC-APP-001 | Appunti Collettivi 2025-2026.md | appunti collettivi | 2025-2026 | Da analizzare | Media-alta | | Fonte recente |
| SRC-APP-002 | Appunti IUM 2021.pdf | appunti studenti | 2020-2021 | Da analizzare | Media | | Fonte storica |
| SRC-APP-003 | AppuntiIUM2022.pdf | appunti studenti | 2022 | Da analizzare | Media | | Fonte ampia |
| SRC-APP-004 | IUM - Appunti collettivi collaborativi 2024-25.pdf | appunti collettivi | 2024-2025 | Da analizzare | Media-alta | | Fonte recente |
```

---

## 9. Log conflitti

Codex deve creare `analysis/conflict_log.md`:

```md
# Conflict Log

Usare questo file quando due fonti danno informazioni diverse, ambigue o potenzialmente incompatibili.

| ID | Concetto | Fonti coinvolte | Descrizione conflitto | Gravità | Stato | Decisione finale |
|---|---|---|---|---|---|---|
| CFL-001 | | | | Alta/Media/Bassa | Aperto | |
```

Esempi di conflitti da registrare:

- definizioni diverse dello stesso concetto;
- esempi invertiti o attribuiti al concetto sbagliato;
- risposte a domande note non coerenti con gli appunti;
- concetti presenti in anni vecchi ma assenti negli appunti recenti.

---

## 10. File dei dubbi aperti

Codex deve creare `analysis/pending_questions.md`:

```md
# Pending Questions

Dubbi da chiarire durante l’analisi degli asset o con fonti più affidabili.

| ID | Domanda/Dubbio | Collegato a | Priorità | Stato | Note |
|---|---|---|---|---|---|
| Q-001 | | | Alta/Media/Bassa | Aperto | |
```

---

## 11. Indice della knowledge base

Codex deve creare `knowledge_base/00_Index.md`:

```md
# Knowledge Base IUM — Index

> [!info] Obiettivo
> Questa knowledge base raccoglie i concetti teorici principali per preparare la parte scritta dell’esame di Interazione Uomo-Macchina.

---

## Fondamenti HCI

- [[Human-Computer Interaction]]
- [[Ergonomia cognitiva]]
- [[Sistema interattivo]]
- [[Interfaccia]]
- [[Utente]]
- [[Task]]

---

## Sistemi socio-tecnici

- [[Sistema socio-tecnico]]
- [[STS thinking]]
- [[Proprietà emergenti]]
- [[Conseguenze inattese]]

---

## Usabilità

- [[Usabilità]]
- [[Bassa usabilità]]
- [[Norman doors]]
- [[Floyd toilet]]
- [[Wake up and use]]

---

## Interazione e progettazione

- [[Affordance]]
- [[Mapping]]
- [[Constraints]]
- [[Workaround]]
- [[Multifunzionalità]]

---

## Valutazione

- [[Valutazione di usabilità]]
- [[Valutazione euristica]]
- [[Euristiche di Nielsen]]
- [[Test con utenti]]
- [[Questionari psicometrici]]
- [[Scala Likert]]

---

## Automazione e bias

- [[Overreliance]]
- [[Overdependence]]
- [[Overconfidence]]
- [[Complacency]]
- [[Automation bias]]
- [[Effetto Peltzman]]

---

## Persuasione, dark patterns e semiotica

- [[Dark patterns]]
- [[Captologia]]
- [[Tecnologie persuasive]]
- [[CASA]]
- [[Ethopoeia]]
- [[Semiotica]]
- [[Ingegneria semiotica]]

---

## Preparazione esame

- [[../exam_prep/domande_note/domande_chiuse|Domande chiuse]]
- [[../exam_prep/domande_note/domande_aperte|Domande aperte]]
- [[../exam_prep/flashcards/ium_flashcards|Flashcards]]
- [[../exam_prep/checklist_ripasso|Checklist ripasso]]
```

---

## 12. Categorie iniziali della knowledge base

Codex deve creare le cartelle anche se inizialmente vuote.

### `01_Fondamenti_HCI/`

Contiene concetti come:

- HCI / IUM;
- IUUMM;
- ergonomia;
- ergonomia cognitiva;
- sistema interattivo;
- interfaccia;
- task;
- utente;
- progettazione per l’utente;
- differenza tra verifica e valutazione.

### `02_Sistemi_Socio_Tecnici/`

Contiene:

- sistema socio-tecnico;
- componente sociale e tecnica;
- proprietà emergenti;
- STS thinking;
- joint optimization;
- conseguenze inattese;
- effetto cobra / effetto Peltzman.

### `03_Usabilita/`

Contiene:

- usabilità;
- bassa usabilità;
- danni e problemi;
- Norman doors;
- Floyd toilet;
- wake up and use;
- user-centered design.

### `04_Affordance_Mapping_Constraints/`

Contiene:

- affordance;
- affordance cognitive, fisiche, sensoriali, funzionali, emozionali, sociali;
- mapping;
- constraints;
- constraint attivi/passivi;
- workaround;
- multifunzionalità;
- complessità funzionale/strutturale/d’uso.

### `05_Valutazione_Usabilita/`

Contiene:

- valutazione di usabilità;
- test con utenti;
- valutazione qualitativa;
- valutazione quantitativa;
- numero di utenti;
- errori, efficacia, efficienza, soddisfazione.

### `06_Valutazione_Euristica/`

Contiene:

- valutazione euristica;
- esperti;
- euristiche più usate;
- Nielsen;
- severità dei problemi;
- metodo di raccolta e aggregazione.

### `07_Questionari_e_Valutazione_Quantitativa/`

Contiene:

- questionari psicometrici;
- questionari validati;
- scala Likert;
- bias di risposta;
- media, mediana, outlier;
- Mann-Whitney;
- Kruskal-Wallis;
- uso dei questionari nel progetto d’esame.

### `08_Dark_Patterns_e_Persuasione/`

Contiene:

- dark patterns;
- tecnologie persuasive;
- captologia;
- nudging;
- etica della progettazione.

### `09_Semiotica_e_Ingegneria_Semiotica/`

Contiene:

- semiotica;
- segno;
- significante/significato;
- icona, indice, simbolo;
- sintassi, semantica, pragmatica;
- ingegneria semiotica;
- comunicabilità.

### `10_Automazione_Bias_e_Conseguenze_Inattese/`

Contiene:

- automation bias;
- complacency;
- overreliance;
- overdependence;
- overconfidence;
- automation-related complacency;
- rischio e compensazione del rischio.

### `99_Glossario/`

Contiene:

- `Glossario_IUM.md`;
- definizioni brevi da memorizzare;
- eventuali sinonimi o traduzioni inglese/italiano.

---

## 13. Materiale per l’esame

### 13.1 `exam_prep/domande_note/`

Codex deve creare:

```text
exam_prep/domande_note/
├── README.md
├── domande_chiuse.md
├── domande_aperte.md
└── domande_da_verificare.md
```

Formato consigliato per ogni domanda:

```md
## Q-0001 — {{Titolo breve}}

Tipo: `chiusa | aperta`
Fonte: `SRC-DOM-001`
Stato risposta: `VALIDATA | PROBABILE | DA VERIFICARE | POTENZIALMENTE ERRATA`
Concetti collegati:
- [[Affordance]]
- [[Mapping]]

### Domanda

{{testo domanda}}

### Risposta breve

{{risposta sintetica}}

### Spiegazione

{{spiegazione utile per ricordare}}

### Note di validazione

{{perché è validata / cosa resta da controllare}}
```

---

### 13.2 `exam_prep/flashcards/ium_flashcards.md`

Formato base:

```md
# Flashcards IUM

## Fondamenti

### Che cos’è l’HCI?

L’HCI è la disciplina che si occupa della progettazione, realizzazione e valutazione di sistemi interattivi con capacità computazionale destinati all’uso umano, e dello studio dei fenomeni che circondano tale uso.

---

### Perché l’usabilità non è una caratteristica intrinseca del sistema?

Perché è un effetto dell’interazione tra utenti, sistema, compiti e contesto d’uso; quindi deve essere valutata coinvolgendo utenti reali o rappresentativi.
```

---

### 13.3 `exam_prep/checklist_ripasso.md`

Checklist iniziale:

```md
# Checklist Ripasso IUM

## Fondamenti

- [ ] So definire HCI/IUM.
- [ ] So spiegare perché IUM è interdisciplinare.
- [ ] So distinguere sistema interattivo e interfaccia.
- [ ] So spiegare perché l’utente non coincide con il progettista.

## Sistemi socio-tecnici

- [ ] So definire sistema socio-tecnico.
- [ ] So spiegare cosa sono le proprietà emergenti.
- [ ] So spiegare STS thinking e joint optimization.
- [ ] So fare un esempio di conseguenza inattesa.

## Usabilità

- [ ] So definire l’usabilità.
- [ ] So spiegare perché l’usabilità non è intrinseca.
- [ ] So spiegare Norman doors e Floyd toilet.
- [ ] So collegare bassa usabilità a danni e problemi.

## Affordance, mapping e constraints

- [ ] So definire affordance.
- [ ] So distinguere affordance cognitive, fisiche, sensoriali, funzionali, emozionali e sociali.
- [ ] So definire mapping.
- [ ] So definire constraint attivi e passivi.
- [ ] So spiegare il concetto di workaround.

## Valutazione

- [ ] So spiegare la valutazione di usabilità.
- [ ] So spiegare la valutazione euristica.
- [ ] So spiegare il ruolo degli esperti.
- [ ] So spiegare il ruolo dei questionari.

## Bias, automazione e conseguenze inattese

- [ ] So definire overreliance.
- [ ] So distinguere overdependence e overconfidence.
- [ ] So spiegare automation bias.
- [ ] So spiegare complacency.
- [ ] So spiegare effetto Peltzman / risk compensation.

## Semiotica e persuasione

- [ ] So definire captologia.
- [ ] So spiegare CASA.
- [ ] So distinguere icona, indice e simbolo.
- [ ] So spiegare sintassi, semantica e pragmatica.
```

---

## 14. Workflow operativo

Codex deve creare i file in `workflows/`.

---

### 14.1 `workflows/00_workflow_generale.md`

```md
# Workflow Generale

## Obiettivo

Aggiornare la knowledge base IUM in modo progressivo, tracciabile e controllato.

## Flusso

1. Inserire asset raw in `assets/raw/`.
2. Registrare asset in `analysis/source_registry.md`.
3. Analizzare asset con ChatGPT web chat.
4. Salvare report in `analysis/reports/`.
5. Chiedere a Codex di aggiornare la knowledge base sulla base del report.
6. Aggiornare domande, flashcard, glossario e checklist.
7. Registrare conflitti e dubbi.
8. Fare commit.

## Regola importante

La knowledge base non viene aggiornata direttamente dagli asset raw, ma solo dai report di analisi.
```

---

### 14.2 `workflows/02_analisi_asset_con_chatgpt.md`

Questo file deve contenere il prompt da usare nella web chat di ChatGPT.

```md
# Workflow — Analisi Asset con ChatGPT

Usare questo prompt quando si analizza un asset singolo.

---

## Prompt

Sto costruendo una knowledge base Obsidian per preparare la parte teorica dell’esame di Interazione Uomo-Macchina.

Analizza il file allegato come singolo asset del progetto.

Non devi aggiornare direttamente la knowledge base. Devi produrre un report strutturato che poi passerò a Codex.

Obiettivi dell’analisi:

1. identificare i concetti teorici principali;
2. estrarre definizioni utili;
3. individuare esempi importanti;
4. evidenziare possibili domande d’esame;
5. segnalare parti ambigue, obsolete, ridondanti o potenzialmente sbagliate;
6. indicare quali note della knowledge base andrebbero create o aggiornate.

Usa questo formato:

[incollare qui il contenuto di `templates/asset_report_template.md`]

Regole:

- non fidarti automaticamente delle risposte già presenti;
- se l’asset contiene domande note, classifica le risposte come VALIDATA, PROBABILE, DA VERIFICARE o POTENZIALMENTE ERRATA;
- scrivi in italiano;
- mantieni un taglio utile per studiare l’esame scritto;
- non fare ancora una riorganizzazione completa della knowledge base;
- produci un report operativo per Codex.
```

---

### 14.3 `workflows/03_update_kb_from_report.md`

Questo file deve contenere il prompt da usare con Codex.

```md
# Workflow — Update Knowledge Base da Report

Usare questo prompt con Codex dopo aver salvato un report in `analysis/reports/`.

---

## Prompt Codex

Leggi il report:

`analysis/reports/{{nome_report}}.md`

Aggiorna la knowledge base IUM seguendo queste regole:

1. Non modificare gli asset raw.
2. Integra solo informazioni presenti nel report.
3. Crea nuove note concettuali quando mancano.
4. Aggiorna note esistenti senza duplicare contenuti.
5. Usa il template `templates/concept_note_template.md`.
6. Aggiorna `knowledge_base/00_Index.md`.
7. Aggiorna `analysis/source_registry.md` marcando l’asset come analizzato.
8. Aggiungi conflitti a `analysis/conflict_log.md`.
9. Aggiungi dubbi a `analysis/pending_questions.md`.
10. Aggiorna `exam_prep/domande_note/` solo se il report contiene domande.
11. Aggiorna `exam_prep/flashcards/ium_flashcards.md` solo con concetti già consolidati o ad alta priorità.
12. Aggiorna `exam_prep/checklist_ripasso.md` se emergono nuovi macro-concetti.

Alla fine restituisci:

- file creati;
- file modificati;
- concetti aggiunti;
- concetti aggiornati;
- domande aggiunte/modificate;
- conflitti aperti;
- dubbi aperti;
- suggerimento per il prossimo asset da analizzare.
```

---

## 15. Ordine consigliato di analisi degli asset

Non analizzare tutto insieme. Procedere in questo ordine:

### Step 1 — Appunti collettivi 2025-2026

Motivo:

- sono probabilmente i più vicini al corso attuale;
- aiutano a definire la struttura moderna della knowledge base;
- permettono di capire quali argomenti sono ancora centrali.

Output atteso:

```text
analysis/reports/01_appunti_collettivi_2025_2026.md
```

---

### Step 2 — Appunti collettivi 2024-2025

Motivo:

- altra fonte recente;
- utile per confrontare programma e concetti con il 2025-2026.

Output atteso:

```text
analysis/reports/02_appunti_collettivi_2024_2025.md
```

---

### Step 3 — Appunti IUM 2022

Motivo:

- fonte ampia;
- utile per arricchire esempi, definizioni e dettagli;
- può contenere materiale non più centrale, quindi da classificare.

Output atteso:

```text
analysis/reports/03_appunti_ium_2022.md
```

---

### Step 4 — Appunti IUM 2021

Motivo:

- fonte storica;
- utile per trovare concetti ricorrenti negli anni;
- utile per validare domande vecchie.

Output atteso:

```text
analysis/reports/04_appunti_ium_2021.md
```

---

### Step 5 — Domande IUM

Motivo:

- va analizzato dopo aver costruito una base teorica;
- le risposte non sono affidabili;
- a questo punto è possibile validarle o correggerle usando la knowledge base.

Output atteso:

```text
analysis/reports/05_domande_ium.md
```

---

## 16. Prima richiesta operativa per Codex

Usare questo prompt per inizializzare la repo.

```md
Inizializza la repo `knowledge_base_IUM` come vault Obsidian per la preparazione della parte teorica dell’esame di Interazione Uomo-Macchina.

Segui il piano nel file `piano_codex_knowledge_base_IUM.md`.

Devi creare:

1. struttura cartelle completa;
2. README.md;
3. PROJECT_CONTEXT.md;
4. CODEX_INSTRUCTIONS.md;
5. registry fonti;
6. conflict log;
7. pending questions;
8. index principale della knowledge base;
9. template markdown;
10. workflow markdown;
11. file iniziali in `exam_prep/`.

Non analizzare ancora gli asset.
Non creare ancora note concettuali complete, tranne eventuali placeholder minimi se servono per far funzionare l’indice.
Non copiare contenuto dagli asset raw nella knowledge base.

La repo deve essere pronta per il workflow successivo:

1. analisi asset singolo con ChatGPT;
2. salvataggio report;
3. update knowledge base da report tramite Codex.

Alla fine restituisci:

- elenco file creati;
- eventuali assunzioni fatte;
- prossimo comando/prompt consigliato per analizzare il primo asset.
```

---

## 17. Criteri di qualità

La repo inizializzata è corretta se:

- gli asset raw sono separati dalla knowledge base;
- esiste un workflow chiaro per analisi e aggiornamento;
- Codex ha istruzioni precise e non ambigue;
- Obsidian può aprire la repo come vault leggibile;
- ci sono template per note, domande, report e conflitti;
- le domande note non vengono trattate come verità;
- la knowledge base è pronta a crescere progressivamente;
- i file sono in italiano;
- non sono presenti emoji nei Markdown;
- ogni cartella ha uno scopo chiaro.

---

## 18. Prossimo step dopo inizializzazione

Dopo che Codex ha creato la struttura, il primo asset da analizzare sarà:

```text
assets/raw/appunti-studenti/Appunti Collettivi 2025-2026.md
```

La web chat di ChatGPT dovrà produrre il report:

```text
analysis/reports/01_appunti_collettivi_2025_2026.md
```

Solo dopo quel report Codex potrà iniziare a popolare realmente la knowledge base.
