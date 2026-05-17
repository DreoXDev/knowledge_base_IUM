# Piano Codex - Iterazione 04 Knowledge Base IUM
## Fonte: `Appunti Collettivi 2025-2026.md`

> [!info] Obiettivo
> Aggiornare la knowledge base IUM usando il file `Appunti Collettivi 2025-2026.md` come fonte recente, senza sovrascrivere in modo cieco le note già consolidate da 2021, 2022 e 2024-25.
>
> Questa iterazione deve anche correggere alcuni problemi strutturali emersi nello stato attuale della repo.

---

## 0. Stato attuale rilevato nella repo

Repo di riferimento:

```text
https://github.com/DreoXDev/knowledge_base_IUM
```

La repo è già organizzata come vault Obsidian con struttura corretta:

```text
analysis/
assets/
exam_prep/
knowledge_base/
templates/
workflows/
README.md
CODEX_INSTRUCTIONS.md
PROJECT_CONTEXT.md
```

Nella `knowledge_base/` sono presenti macro-sezioni ordinate:

```text
01_Fondamenti_HCI/
02_Sistemi_Socio_Tecnici/
03_Usabilita/
04_Affordance_Mapping_Constraints/
05_Valutazione_Usabilita/
06_Valutazione_Euristica/
07_Questionari_e_Valutazione_Quantitativa/
08_Dark_Patterns_e_Persuasione/
09_Semiotica_e_Ingegneria_Semiotica/
10_Automazione_Bias_e_Conseguenze_Inattese/
99_Glossario/
00_Index.md
```

La base concettuale è quindi impostata bene, ma prima di aggiungere il nuovo asset servono alcuni fix.

---

## 1. Fix strutturali da fare prima dell'integrazione

### 1.1 Correggere file Markdown "appiattiti" su una sola riga

Alcuni file risultano poco leggibili perché il contenuto è stato scritto quasi tutto su una singola riga.

Controllare e correggere almeno:

```text
analysis/source_registry.md
knowledge_base/00_Index.md
analysis/reports/04_appunti_ium_2021.md
analysis/reports/05_appunti_ium_2022.md
```

Obiettivo:

- ogni heading deve stare su una riga propria;
- ogni tabella Markdown deve avere righe separate;
- ogni lista deve essere una lista Markdown leggibile;
- i callout Obsidian devono rispettare la forma:

```md
> [!info] Titolo
> Testo del callout.
```

Non cambiare il contenuto concettuale durante questo passaggio: fare solo reformatting leggibile.

---

### 1.2 Allineare `README.md` e `source_registry.md`

Attualmente il README dichiara come "fonti integrate" anche:

```text
Appunti collettivi 2025-26
Domande note
```

ma nel registro fonti risultano ancora `Da analizzare`.

Correggere il README in modo che distingua chiaramente:

```md
### Fonti integrate
- Appunti IUM 2021
- Appunti IUM 2022
- Appunti collettivi 2024-25

### Fonti in corso / da analizzare
- Appunti Collettivi 2025-2026.md
- Domande IUM.pdf
```

Dopo questa iterazione, `Appunti Collettivi 2025-2026.md` potrà essere spostato tra le fonti integrate.

---

### 1.3 Verificare report mancante 2024-25

Nel `source_registry.md` la fonte 2024-25 punta a:

```text
[[reports/02_appunti_collettivi_2024_2025]]
```

ma nella cartella `analysis/reports/`, da controllo remoto, risultano visibili solo:

```text
00_template_asset_report.md
04_appunti_ium_2021.md
05_appunti_ium_2022.md
README.md
index.md
```

Azioni richieste:

1. Controllare se `analysis/reports/02_appunti_collettivi_2024_2025.md` esiste localmente ma non è stato committato.
2. Se esiste, aggiungerlo al commit.
3. Se non esiste, creare un report sintetico di recupero per la fonte 2024-25.
4. Aggiornare `analysis/reports/index.md`.

> [!warning] Nota
> Non procedere fingendo che il report esista. Il registro fonti deve puntare solo a report realmente presenti nella repo.

---

### 1.4 Sistemare stato del registro fonti

Aggiornare `analysis/source_registry.md` usando una tabella leggibile.

Stato finale atteso dopo questa iterazione:

```md
| ID Fonte | Nome file | Tipo | Anno | Stato analisi | Attendibilità | Report collegato | Note |
|---|---|---|---|---|---|---|---|
| SRC-DOM-001 | Domande IUM.pdf | domande note | 2020-2021 | Da analizzare | Media-bassa |  | Risposte non affidabili da verificare |
| SRC-APP-001 | Appunti Collettivi 2025-2026.md | appunti collettivi / sintesi recente | 2025-2026 | Analizzato | Media, da verificare | [[reports/06_appunti_collettivi_2025_2026]] | Fonte recente ma parziale e probabilmente rielaborata da AI |
| SRC-APP-002 | Appunti IUM 2021.pdf | appunti studenti | 2020-2021 | Analizzato | Media-bassa | [[reports/04_appunti_ium_2021]] | Prima fonte integrata |
| SRC-APP-003 | AppuntiIUM2022.pdf | appunti studenti | 2022 | Analizzato | Media | [[reports/05_appunti_ium_2022]] | Fonte ampia già integrata |
| SRC-APP-004 | IUM __ Appunti collettivi collaborativi 2024-25.pdf | appunti collettivi | 2024-2025 | Analizzato | Media-alta | [[reports/02_appunti_collettivi_2024_2025]] | Fonte recente già integrata, verificare presenza report |
```

---

## 2. Analisi del nuovo file

Fonte:

```text
assets/raw/appunti-collettivi/Appunti Collettivi 2025-2026.md
```

Creare il report:

```text
analysis/reports/06_appunti_collettivi_2025_2026.md
```

### 2.1 Natura della fonte

Questa fonte è diversa dalle precedenti:

- è un file Markdown già rielaborato;
- è più recente;
- contiene sezioni molto discorsive e ben scritte;
- contiene un marcatore `Gemini 2.5 Pro`;
- sembra essere una sintesi parziale, non un set completo di appunti del corso;
- si concentra soprattutto su:
  - questionari psicometrici;
  - HCI e storia dell'interazione;
  - centralità dell'utente;
  - valutazione empirica;
  - sistemi socio-tecnici;
  - conseguenze inattese;
  - overreliance, overdependence e overconfidence.

Per questo motivo non trattarla come fonte definitiva o completa. Usarla come:

```text
fonte recente di conferma/rafforzamento + fonte di formulazioni più pulite
```

ma non come unica fonte da cui rimpiazzare gli appunti precedenti.

---

### 2.2 Problemi qualitativi da registrare nel report

Nel report segnalare esplicitamente:

```md
## Problemi qualitativi della fonte
- Il file contiene un marker `Gemini 2.5 Pro`, quindi alcune parti potrebbero essere state generate o rielaborate da AI.
- La numerazione degli heading non è coerente: dopo le prime sezioni numerate riparte una nuova struttura con `### 1`, `### 2`, ecc.
- Alcuni argomenti sono duplicati, specialmente questionari psicometrici e definizione di HCI.
- La fonte è parziale: termina nella parte su overconfidence e non copre l'intero programma.
- Alcune affermazioni storiche o metodologiche vanno confermate con fonti precedenti o domande note.
```

---

## 3. Concetti da integrare o rafforzare

### 3.1 Questionari psicometrici

Aggiornare o consolidare le note in:

```text
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/
```

Note da aggiornare:

```text
Questionari psicometrici.md
Scala Likert.md
Bias di risposta.md
Acquiescence bias.md
Central tendency bias.md
Valutazione quantitativa.md
```

Eventuali nuove note da creare:

```text
Validazione questionari.md
Forward-backward translation.md
Item invertiti.md
Non so nei questionari.md
Outlier nei questionari.md
Questionario attitudini IA.md
```

Contenuti da integrare:

- un questionario psicometrico validato non è un semplice modulo;
- la validazione è un processo statistico, non una certificazione formale;
- la validazione serve a dimostrare che gli item misurano coerentemente un costrutto;
- i questionari tradotti richiedono una procedura di forward-backward translation;
- le scale Likert sono ordinali e possono essere pari o dispari;
- le scale dispari offrono un punto neutro, ma possono favorire central tendency bias;
- le scale pari forzano una presa di posizione;
- gli item invertiti aiutano a controllare incoerenze e acquiescence bias;
- l'opzione "non so / non posso rispondere" può essere utile, ma va gestita con attenzione;
- la media può essere fuorviante in presenza di outlier;
- per interpretare i dati bisogna affiancare media, mediana, deviazione standard e distribuzione.

> [!warning] Importante
> Non duplicare le note già presenti su SUMI, SUS, UEQ, AttrakDiff e NPS se non sono direttamente trattate nel file 2025-26. Questa fonte parla soprattutto di struttura generale dei questionari, validazione, Likert e bias.

---

### 3.2 Esperimento didattico con chatbot

Creare una nota breve, oppure aggiungere una sezione in una nota esistente:

```text
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/Questionario attitudini IA.md
```

oppure:

```text
knowledge_base/10_Automazione_Bias_e_Conseguenze_Inattese/Chatbot didattico e attitudini IA.md
```

Contenuti:

- durante il corso viene citata una sperimentazione con chatbot basato su GPT-4;
- il chatbot è integrato nel sito didattico;
- viene somministrato un questionario sulle attitudini verso l'IA all'inizio e alla fine del corso;
- obiettivo: osservare se l'uso del chatbot influenza le attitudini degli studenti verso l'IA;
- partecipazione anonima e facoltativa;
- dati analizzati in forma aggregata.

Marcare come:

```yaml
stato: da-verificare
fonte: SRC-APP-001
```

perché è informazione molto legata all'anno corrente del corso.

---

### 3.3 Definizione formale di HCI

Aggiornare:

```text
knowledge_base/01_Fondamenti_HCI/Human-Computer Interaction.md
```

Rafforzare la definizione:

```text
HCI = disciplina che si occupa di progettazione, realizzazione e valutazione di sistemi interattivi dotati di capacità computazionale, destinati all'uso umano, e dello studio dei fenomeni che ne circondano l'utilizzo.
```

Aggiungere:

- HCI non è solo sviluppo tecnico;
- include valutazione sistematica della qualità d'uso;
- studia fenomeni cognitivi, sociali e organizzativi;
- si distingue dall'ingegneria del software perché l'utente e il contesto reale sono parte dell'oggetto di studio.

Aggiornare anche:

```text
knowledge_base/01_Fondamenti_HCI/IUUMM.md
knowledge_base/01_Fondamenti_HCI/Ergonomia cognitiva.md
knowledge_base/01_Fondamenti_HCI/Progettista e utente.md
```

---

### 3.4 Storia dell'HCI e GUI

Creare o aggiornare:

```text
knowledge_base/01_Fondamenti_HCI/Storia dell_HCI.md
```

Contenuti da aggiungere:

- anni 50-60: mainframe, schede perforate, assenza del concetto moderno di utente finale;
- anni 70: terminali interattivi e time-sharing;
- anni 80: interfaccia grafica, Xerox PARC, WIMP, mouse, metafora del desktop;
- 1984: Apple Macintosh e diffusione della GUI per il pubblico non tecnico;
- 1982: nascita SIGCHI;
- 1983: conferenza CHI;
- anni 2000 e oltre: web, mobile, interfacce tattili, vocali, immersive, AI, ubiquità.

> [!warning] Verifica
> La fonte afferma dettagli storici specifici. Non farli diventare "confermati" finché non sono confrontati con appunti precedenti o fonti attendibili. Per ora usare stato `da-verificare`.

Aggiornare `knowledge_base/00_Index.md` aggiungendo il link:

```md
- [[Storia dell_HCI]]
```

---

### 3.5 Valutazione empirica con utenti

Aggiornare:

```text
knowledge_base/05_Valutazione_Usabilita/Valutazione di usabilità.md
knowledge_base/05_Valutazione_Usabilita/User test.md
```

Contenuti da integrare:

- la valutazione è parte costitutiva dell'HCI, non un'attività opzionale;
- progettare bene non basta: bisogna testare con utenti reali;
- il test valuta il sistema attraverso gli utenti, non gli utenti;
- si assegnano task, si osservano comportamenti, si registrano dati qualitativi e quantitativi;
- pochi utenti ben scelti possono rivelare molti problemi sistematici.

Collegare con:

```text
[[Protocollo think-aloud]]
[[Valutazione euristica]]
[[Questionari psicometrici]]
```

---

### 3.6 "Tu non sei l'utente"

Creare o aggiornare:

```text
knowledge_base/01_Fondamenti_HCI/Progettista e utente.md
```

Aggiungere una sezione:

```md
## Tu non sei l'utente
```

Punti:

- il progettista conosce troppo bene il sistema;
- questa conoscenza distorce il suo giudizio;
- non può vedere il prodotto con gli occhi di un neofita;
- l'introspezione non basta;
- la soluzione è coinvolgere utenti reali in modo iterativo.

Collegare a:

```text
[[Valutazione di usabilità]]
[[User test]]
[[Sistema socio-tecnico]]
```

---

### 3.7 Varietà dei sistemi, utenti e contesti

Aggiornare:

```text
knowledge_base/01_Fondamenti_HCI/Progettista e utente.md
knowledge_base/01_Fondamenti_HCI/Human-Computer Interaction.md
```

oppure creare:

```text
knowledge_base/01_Fondamenti_HCI/Varietà nell_interazione.md
```

Contenuti:

- varietà dei sistemi interattivi;
- varietà degli utenti;
- varietà degli scopi e dei contesti d'uso;
- un'interfaccia usabile in un contesto tranquillo può essere inadatta in un contesto frenetico o critico.

---

### 3.8 Sistemi socio-tecnici e fallacia del progettista

Aggiornare:

```text
knowledge_base/02_Sistemi_Socio_Tecnici/Sistema socio-tecnico.md
knowledge_base/02_Sistemi_Socio_Tecnici/Proprietà emergenti.md
knowledge_base/02_Sistemi_Socio_Tecnici/Conseguenze inattese.md
```

Nuova nota consigliata:

```text
knowledge_base/02_Sistemi_Socio_Tecnici/Fallacia del progettista.md
```

Contenuti:

- un sistema socio-tecnico non è solo tecnologia;
- componente sociale e componente tecnica sono inestricabilmente legate;
- nessuna delle due componenti raggiunge l'obiettivo da sola;
- il comportamento complessivo emerge dall'interazione;
- la fallacia del progettista consiste nel credere che il lavoro finisca al rilascio della tecnologia;
- invece il sistema comincia davvero a vivere quando viene appropriato nel contesto reale.

Collegare:

```text
[[STS thinking]]
[[Conseguenze inattese]]
[[Overreliance]]
```

---

### 3.9 Conseguenze inattese, Effetto Peltzman ed Effetto Cobra

Aggiornare:

```text
knowledge_base/02_Sistemi_Socio_Tecnici/Conseguenze inattese.md
knowledge_base/02_Sistemi_Socio_Tecnici/Effetto Peltzman.md
```

Creare:

```text
knowledge_base/02_Sistemi_Socio_Tecnici/Effetto Cobra.md
```

Contenuti:

- conseguenze inattese: effetti imprevisti a lungo termine dell'introduzione di tecnologie o incentivi;
- possono essere positive o negative;
- effetto Peltzman: protezioni o strumenti di sicurezza possono abbassare la percezione del rischio e incentivare comportamenti più rischiosi;
- effetto Cobra: un incentivo progettato per risolvere un problema finisce per peggiorarlo.

> [!warning] Esame
> L'effetto Peltzman è già ricorrente nelle fonti precedenti ed è importante. L'effetto Cobra è utile come esempio/collegamento, ma verificare se compare anche nelle domande note prima di dargli priorità alta.

---

### 3.10 Overreliance, overdependence e overconfidence

Aggiornare:

```text
knowledge_base/10_Automazione_Bias_e_Conseguenze_Inattese/Overreliance.md
knowledge_base/10_Automazione_Bias_e_Conseguenze_Inattese/Overdependence.md
knowledge_base/10_Automazione_Bias_e_Conseguenze_Inattese/Overconfidence.md
```

Integrare esempi:

- perdita di abilità;
- mancanza di piano B;
- tecnologia considerata infallibile;
- sottovalutazione di bug e fallimenti catastrofici;
- esempio del primario/ospedale senza moduli cartacei;
- esempio del chip Intel solo se già presente o se viene marcato come `da-verificare`.

---

## 4. Note da NON aggiornare in modo pesante in questa iterazione

Questa fonte non copre in modo completo:

```text
Affordance, mapping, constraints
Valutazione euristica dettagliata
Dark patterns
Captologia
CASA
Semiotica
Ingegneria semiotica
SUS/SUMI/UEQ/AttrakDiff/NPS in dettaglio
```

Quindi:

- non riscrivere queste note partendo dal file 2025-26;
- al massimo aggiungere un link o una conferma se il concetto è citato;
- lasciare come fonti principali 2021, 2022 e 2024-25 per questi argomenti.

---

## 5. Aggiornamenti richiesti in `exam_prep/`

Creare o aggiornare:

```text
exam_prep/domande_note/domande_appunti_collettivi_2025_2026.md
```

Aggiungere domande aperte sintetiche:

```md
## Domande aperte derivate da Appunti Collettivi 2025-2026

### Questionari psicometrici
1. Che cosa significa che un questionario è validato?
2. Perché non basta tradurre informalmente un questionario validato?
3. Che cos'è la forward-backward translation?
4. Perché in un questionario si usano item invertiti?
5. Qual è la differenza tra scala Likert pari e dispari?
6. Che cos'è il central tendency bias?
7. Perché la media può essere fuorviante nei questionari?

### Fondamenti HCI
8. Dai una definizione formale di HCI.
9. Perché l'HCI è una disciplina multidisciplinare?
10. Perché l'utente e il contesto reale sono centrali nell'HCI?
11. Che cosa significa "tu non sei l'utente"?

### Storia HCI
12. Qual è il ruolo degli anni 80 nella storia dell'HCI?
13. Che cosa sono Xerox PARC, WIMP e desktop metaphor?
14. Perché il Macintosh del 1984 è considerato importante nella storia dell'interazione?

### Valutazione
15. Perché progettare bene non basta?
16. Che cosa significa valutare un sistema attraverso gli utenti?
17. Quali dati si raccolgono in un test di usabilità?

### Sistemi socio-tecnici
18. Che cos'è un sistema socio-tecnico?
19. Che cosa sono le proprietà emergenti?
20. Che cosa sono le conseguenze inattese?
21. Spiega effetto Peltzman ed effetto Cobra.
22. Qual è la differenza tra overdependence e overconfidence?
```

Aggiornare:

```text
exam_prep/flashcards/ium_flashcards.md
exam_prep/checklist_ripasso.md
```

Aggiungere flashcard solo per concetti nuovi o rafforzati:

- validazione questionari;
- forward-backward translation;
- item invertiti;
- "tu non sei l'utente";
- storia HCI;
- fallacia del progettista;
- effetto Cobra.

---

## 6. Aggiornamenti al glossario

Aggiornare:

```text
knowledge_base/99_Glossario/
```

Aggiungere o verificare voci:

```text
Back-translation
Central tendency bias
Effetto Cobra
Forward-backward translation
Item invertiti
Questionario validato
SIGCHI
CHI
WIMP
Desktop metaphor
Fallacia del progettista
```

Per ogni voce usare formato breve:

```md
# Termine

> [!summary] Definizione
> Definizione sintetica in 2-4 righe.

## Collegamenti
- [[Nota collegata]]
```

---

## 7. Aggiornare report e indici

### 7.1 Report

Creare:

```text
analysis/reports/06_appunti_collettivi_2025_2026.md
```

Struttura consigliata:

```md
# Report analisi - Appunti Collettivi 2025-2026

Data analisi: 2026-05-17  
Asset analizzato: `assets/raw/appunti-collettivi/Appunti Collettivi 2025-2026.md`  
Tipo asset: `appunti collettivi / sintesi recente`  
Stato report: `COMPLETO`

## 1. Sintesi della fonte
## 2. Qualità e limiti della fonte
## 3. Concetti confermati
## 4. Concetti nuovi o rafforzati
## 5. Note create o aggiornate
## 6. Domande/flashcard aggiunte
## 7. Dubbi e conflitti
## 8. Azioni completate da Codex
```

### 7.2 Report index

Aggiornare:

```text
analysis/reports/index.md
```

Aggiungere:

```md
- [[06_appunti_collettivi_2025_2026]] - Fonte recente ma parziale su questionari, HCI, valutazione empirica e sistemi socio-tecnici.
```

### 7.3 Knowledge base index

Aggiornare:

```text
knowledge_base/00_Index.md
```

Aggiungere link nuovi, se creati:

```md
- [[Storia dell_HCI]]
- [[Validazione questionari]]
- [[Forward-backward translation]]
- [[Item invertiti]]
- [[Fallacia del progettista]]
- [[Effetto Cobra]]
- [[Questionario attitudini IA]]
```

---

## 8. Regole di qualità per questa iterazione

### 8.1 Non duplicare concetti

Prima di creare una nuova nota:

1. cercare se una nota equivalente esiste già;
2. se esiste, aggiornare quella;
3. se il nome nuovo è utile come alias, aggiungere link/alias invece di duplicare.

Esempi:

```text
Questionario validato -> potrebbe essere sezione in Questionari psicometrici
Back-translation -> alias di Forward-backward translation
Interazione Uomo-Macchina -> alias di Human-Computer Interaction
```

---

### 8.2 Stato delle informazioni

Usare questi stati nelle note:

```yaml
stato: confermato
```

solo se il concetto è già presente in almeno due fonti tra 2021, 2022, 2024-25 e 2025-26.

Usare:

```yaml
stato: da-verificare
```

per:

- dettagli storici specifici;
- informazioni sull'anno 2025-26;
- esperimento con chatbot;
- esempi non ancora confermati dalle domande note;
- parti che sembrano generate/rielaborate da AI.

---

### 8.3 Stile Obsidian

Mantenere stile Obsidian pulito:

- heading gerarchici;
- link interni `[[...]]`;
- callout `> [!info]`, `> [!warning]`, `> [!example]`;
- niente emoji nei titoli o nei nomi file;
- evitare muri di testo;
- preferire definizione breve + spiegazione + esempio + collegamenti;
- non copiare interi blocchi dalla fonte raw: riscrivere e consolidare.

---

## 9. Checklist finale per Codex

Alla fine dell'iterazione verificare:

- [ ] `analysis/source_registry.md` è leggibile e non appiattito su una sola riga.
- [ ] `knowledge_base/00_Index.md` è leggibile e non appiattito su una sola riga.
- [ ] `analysis/reports/04_appunti_ium_2021.md` e `05_appunti_ium_2022.md` sono formattati correttamente.
- [ ] Esiste oppure è stato recuperato `analysis/reports/02_appunti_collettivi_2024_2025.md`.
- [ ] Esiste `analysis/reports/06_appunti_collettivi_2025_2026.md`.
- [ ] `source_registry.md` segna `Appunti Collettivi 2025-2026.md` come `Analizzato`.
- [ ] Il README distingue fonti integrate e fonti ancora da analizzare.
- [ ] Le note sui questionari sono aggiornate senza duplicare contenuti.
- [ ] Le note su HCI, storia HCI, progettista/utente e sistemi socio-tecnici sono aggiornate.
- [ ] `exam_prep/domande_note/domande_appunti_collettivi_2025_2026.md` è stato creato.
- [ ] Le flashcard sono aggiornate solo con concetti utili.
- [ ] Le informazioni legate all'anno corrente sono marcate `da-verificare`.
- [ ] Nessuna nota importante contiene testo copiato integralmente dalla fonte raw.
- [ ] Tutti i nuovi file sono linkati da almeno un indice.

---

## 10. Commit suggerito

```bash
git status
git add README.md analysis/ knowledge_base/ exam_prep/
git commit -m "Integrate 2025-2026 collective notes into IUM knowledge base"
```

Dopo il commit, controllare:

```bash
git status
```

Deve risultare pulito.
