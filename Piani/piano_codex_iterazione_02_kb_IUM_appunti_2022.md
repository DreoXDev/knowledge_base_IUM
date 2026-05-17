# Piano Codex — Iterazione 02 Knowledge Base IUM

## Obiettivo

Aggiornare la repository `knowledge_base_IUM` dopo la prima integrazione basata su `Appunti IUM 2021.pdf`, correggendo eventuali problemi strutturali emersi e integrando il secondo asset:

- `AppuntiIUM2022.pdf`
- Fonte: appunti studenti 2022
- Attendibilità: media
- Stato atteso dopo questa iterazione: analizzato, integrato, ma con parti storiche/progettuali marcate come potenzialmente obsolete

Questa iterazione non deve trasformare la repo in un archivio completo di appunti copiati. Deve consolidare una knowledge base teorica per l’esame scritto di Interazione Uomo-Macchina, leggibile come vault Obsidian e mantenibile con successive analisi fonte-per-fonte.

---

## Stato repo osservato prima dell’iterazione

La repo risulta già inizializzata con questa struttura principale:

```text
analysis/
assets/
exam_prep/
knowledge_base/
templates/
workflows/
CODEX_INSTRUCTIONS.md
PROJECT_CONTEXT.md
README.md
```

La cartella `knowledge_base/` contiene già una buona tassonomia di moduli:

```text
knowledge_base/
├── 00_Index.md
├── 01_Fondamenti_HCI/
├── 02_Sistemi_Socio_Tecnici/
├── 03_Usabilita/
├── 04_Affordance_Mapping_Constraints/
├── 05_Valutazione_Usabilita/
├── 06_Valutazione_Euristica/
├── 07_Questionari_e_Valutazione_Quantitativa/
├── 08_Dark_Patterns_e_Persuasione/
├── 09_Semiotica_e_Ingegneria_Semiotica/
├── 10_Automazione_Bias_e_Conseguenze_Inattese/
└── 99_Glossario/
```

La cartella `analysis/` contiene già:

```text
analysis/
├── reports/
├── appunti_ium_2021_source.md
├── conflict_log.md
├── info_progetto_potenzialmente_obsolete.md
├── pending_questions.md
└── source_registry.md
```

La prima iterazione sembra avere creato molte note atomiche e domande derivate, ma ci sono alcuni punti da correggere prima di aggiungere il nuovo contenuto.

---

## Problemi da correggere prima dell’integrazione 2022

### 1. README troppo ottimistico sullo stato delle fonti

Nel README la sezione `Stato knowledge base` indica già come fonti integrate:

```text
Appunti IUM 2022
Appunti collettivi 2024-25
Appunti collettivi 2025-26
Domande note
```

ma in `analysis/source_registry.md` `AppuntiIUM2022.pdf` risulta ancora `Da analizzare`, mentre le altre fonti non sono ancora state integrate in questa fase.

#### Azione Codex

Aggiornare `README.md` in modo che distingua chiaramente:

```md
### Fonti integrate
- Appunti IUM 2021

### Fonti in lavorazione
- Appunti IUM 2022

### Fonti da analizzare
- Appunti collettivi 2024-25
- Appunti collettivi 2025-26
- Domande note
```

Dopo questa iterazione, spostare `Appunti IUM 2022` in `Fonti integrate`.

---

### 2. Mancano accenti in varie note

Dalla struttura visibile ci sono file e titoli senza accenti:

- `Usabilita`
- `Proprieta`
- `Valutazione di usabilita`
- `Semiotica` / `Semeiotica` da uniformare
- `Euristica` / `euristiche`

#### Azione Codex

Non rinominare subito tutti i file se questo rompe i link Obsidian, ma:

1. Nei contenuti leggibili usare sempre gli accenti corretti:
   - `usabilità`
   - `proprietà`
   - `valutazione`
   - `affidabilità`
   - `perché`
   - `è`
   - `più`
2. Se si rinominano file, aggiornare tutti i wikilink.
3. Preferire una strategia conservativa:
   - mantenere filename ASCII se già usato;
   - correggere titoli H1 e testo interno;
   - aggiornare `00_Index.md` solo se il link rimane funzionante.

---

### 3. Marking di attendibilità troppo generico

La fonte 2021 era dichiarata nel file stesso come potenzialmente imprecisa, quindi le note derivate sono state marcate come da verificare. Con il file 2022, molti concetti confermano il 2021 e possono passare da `DA VERIFICARE` a `CONFERMATO DA 2 FONTI`.

#### Azione Codex

Per ogni nota già esistente aggiornata anche dal 2022:

```md
> [!success] Stato
> Concetto confermato da `Appunti IUM 2021` e `AppuntiIUM2022`.
```

Per contenuti presenti solo nel 2022:

```md
> [!warning] Stato
> Concetto estratto da `AppuntiIUM2022`; da verificare con fonti successive o domande note.
```

Per informazioni legate al progetto o alla modalità d’esame:

```md
> [!danger] Obsolescenza possibile
> Informazione legata all’anno 2022 o al progetto; non usarla automaticamente per lo scritto teorico attuale senza verifica.
```

---

### 4. Separazione insufficiente tra teoria d’esame e progetto

`AppuntiIUM2022.pdf` contiene molte informazioni progettuali: numeri di utenti, valutazione euristica, user test, questionari, rapporto finale. Queste informazioni sono utili come contesto IUM, ma il focus attuale è lo scritto teorico.

#### Azione Codex

Separare sempre:

```text
knowledge_base/          -> teoria consolidata per scritto
exam_prep/               -> domande, flashcard, checklist
analysis/                -> report fonte, dubbi, conflitti, informazioni obsolete
```

Le indicazioni pratiche del progetto vanno:
- sintetizzate nelle note teoriche solo se spiegano un concetto;
- archiviate in `analysis/info_progetto_potenzialmente_obsolete.md` se sono numeri, consegne, scadenze, regole progettuali;
- non trasformate in “verità d’esame scritto” senza conferma.

---

## Nuovo asset da integrare

### File

```text
assets/raw/appunti-studenti/AppuntiIUM2022.pdf
```

Se il file non è già presente in repo, copiarlo nella cartella raw corretta.

### Metadata da creare

Creare:

```text
analysis/appunti_ium_2022_source.md
```

Contenuto minimo:

```md
---
type: fonte
source_kind: appunti_studenti
course: Interazione Uomo-Macchina
year: 2022
reliability: media
status: analyzed
processed: true
---

# Appunti IUM 2022

## Descrizione

Appunti studenti del corso di Interazione Uomo-Macchina 2022. Fonte ampia, più estesa rispetto agli appunti 2021, utile soprattutto per confermare concetti già estratti e aggiungere dettagli su valutazione quantitativa, questionari psicometrici, dark patterns, tecnologie persuasive e semiotica.

> [!warning] Affidabilità
> Fonte studentesca: usare per consolidamento e confronto, non come autorità finale.

## Collegamenti

- File raw: `assets/raw/appunti-studenti/AppuntiIUM2022.pdf`
- Estrazione testo: `assets/processed/extracted-text/appunti_ium_2022_extracted.txt`
- Report analisi: [[reports/05_appunti_ium_2022]]
```

Aggiornare anche `analysis/source_registry.md`:

```md
SRC-APP-003 | AppuntiIUM2022.pdf | appunti studenti | 2022 | Analizzato | Media | [[reports/05_appunti_ium_2022]] | Fonte ampia, conferma molti concetti 2021 e aggiunge dettagli
```

---

## Report da creare

Creare:

```text
analysis/reports/05_appunti_ium_2022.md
```

Il report deve contenere:

```md
# Report analisi — Appunti IUM 2022

## 1. Sintesi fonte

## 2. Concetti confermati rispetto al 2021

## 3. Concetti nuovi o più dettagliati

## 4. Concetti da correggere nella KB

## 5. Informazioni progettuali potenzialmente obsolete

## 6. Note da aggiornare

## 7. Domande d’esame / flashcard da aggiungere

## 8. Dubbi e conflitti
```

---

## Concetti principali da integrare o rafforzare

### A. Fondamenti HCI

Aggiornare o creare note in:

```text
knowledge_base/01_Fondamenti_HCI/
```

#### Note da aggiornare

- `Human-Computer Interaction.md`
- `Ergonomia cognitiva.md`
- `Sistema interattivo.md`
- `Interfaccia.md`
- `Task.md`
- eventuale nuova nota: `IUUMM.md`

#### Contenuti da integrare

- HCI come disciplina che riguarda progettazione, realizzazione e valutazione di sistemi interattivi con capacità computazionale destinati all’uso umano.
- HCI come studio dei fenomeni che circondano l’uso dei sistemi interattivi.
- IUUMM: Interazione Uomo-Uomo Mediata dalla Macchina, perché l’essere umano è sociale e l’interfaccia spesso media relazioni tra persone.
- Differenza valutazione/verifica:
  - verifica: più formale, centrata sulle funzionalità;
  - valutazione: centrata su requisiti, aspettative, qualità non funzionali e contesto reale.
- Il progettista non è l’utente: evitare introspezione ingenua.

#### Checklist Codex

- Consolidare con note già create dal 2021.
- Aggiungere esempi brevi e puliti.
- Collegare a `[[Usabilita]]`, `[[Sistema socio-tecnico]]`, `[[Interfaccia]]`.

---

### B. Sistemi socio-tecnici e conseguenze inattese

Aggiornare:

```text
knowledge_base/02_Sistemi_Socio_Tecnici/
knowledge_base/10_Automazione_Bias_e_Conseguenze_Inattese/
```

#### Note da aggiornare

- `Sistema socio-tecnico.md`
- `STS thinking.md`
- `Proprieta emergenti.md`
- `Conseguenze inattese.md`
- `Effetto Peltzman.md`
- `Overreliance.md`
- `Overdependence.md`
- `Overconfidence.md`
- `Complacency.md`
- `Automation bias.md`

#### Contenuti da integrare

- Il perimetro del sistema socio-tecnico dipende dall’osservatore.
- Componente sociale e componente tecnica sono inestricabili.
- Proprietà emergenti:
  - funzionali;
  - non funzionali.
- STS thinking come approccio di joint optimization tra componente sociale e tecnica.
- Effetto Peltzman / risk compensation.
- Overreliance come trasposizione del problema in ambito tecnologico.
- Distinzione:
  - overdependence: abuso, mancanza di autonomia, assenza di piano B;
  - overconfidence: credere che il sistema non cada, non faccia danni, non sbagli;
  - complacency: abbassamento dell’attenzione perché si presume che il sistema funzioni sempre;
  - automation bias: eccessiva fiducia nel supporto decisionale, con errori di omissione o commissione.

#### Nuove note opzionali

- `Risk compensation.md`
- `Startle effect.md`
- `Peltzman effect.md` come alias o sezione di `Effetto Peltzman.md`.

---

### C. Usabilità

Aggiornare:

```text
knowledge_base/03_Usabilita/
```

#### Note da aggiornare

- `Usabilita.md`
- `Bassa usabilita.md`
- `Efficacia.md`
- `Efficienza.md`
- `Soddisfazione.md`
- `Low use.md`
- `Norman doors.md`
- `Floyd toilet.md`

#### Nuove note consigliate

- `Potenziale usabilita.md`
- `Robustezza.md`
- `Apprendibilita.md`
- `Ricordabilita.md`
- `Trade-off di usabilita.md`
- `Learnability.md` come alias o redirect a `Apprendibilita.md`
- `Memorability.md` come alias o redirect a `Ricordabilita.md`

#### Contenuti da integrare

- Definizione ISO-like di usabilità:
  - grado con cui un prodotto può essere usato da determinati utenti;
  - per raggiungere determinati obiettivi;
  - con efficacia, efficienza e soddisfazione;
  - in un determinato contesto d’uso.
- Non ha senso parlare di usabilità “del sistema in sé”: l’usabilità dipende da utenti, obiettivi e contesto.
- Potenziale usabilità: possibilità ragionevole che un sistema sia usabile in certi contesti, da confermare empiricamente.
- Estensioni:
  - robustezza;
  - apprendibilità;
  - ricordabilità.
- Trade-off:
  - learnability vs soddisfazione nel lungo periodo;
  - robustezza vs efficienza;
  - vincoli utili vs eccesso di vincoli.
- Bassa usabilità come causa di danni, errori, frustrazione e low use.

---

### D. Affordance, mapping, constraints

Aggiornare:

```text
knowledge_base/04_Affordance_Mapping_Constraints/
```

#### Note da aggiornare

- `Affordance.md`
- `Mapping.md`
- `Constraints.md`
- `Workaround.md`
- `Skeuomorfismo.md`
- `User-created affordances.md`
- `Legge di Fitts.md`
- `Errori di giustapposizione.md`
- `Multifunzionalita.md`
- `Complessita d'uso strutturale funzionale.md`

#### Contenuti da integrare

- Affordance secondo Gibson / Norman / formulazione usata nel corso.
- Tipologie:
  - cognitive;
  - fisiche;
  - sensoriali;
  - funzionali;
  - emozionali;
  - sociali;
  - user-created affordances.
- Mapping come caratteristica dell’affordance:
  - relazione tra controllo, azione e effetto nel mondo reale/applicativo.
- Mapping:
  - arbitrario/convenzionale;
  - diretto/naturale;
  - topologico;
  - funzionale.
- Regola importante:
  - non puoi avere mapping senza affordance;
  - puoi avere affordance senza mapping.
- Vincoli:
  - strutturali/passivi;
  - funzionali/attivi.
- Workaround come segnale di mismatch tra designed path e pratiche reali dell’utente.
- Fitts:
  - utile per ragionare su dimensione e distanza dei comandi;
  - non trasformare la formula in focus principale dello scritto, ma tenerla come concetto.

#### Fix terminologico

Uniformare:

- `Skeuomorfismo` oppure `Scheumorfismo`.

Nel corso/appunti compare spesso “scheumorfismo”, ma in italiano tecnico è comune anche “skeuomorfismo”. Usare una nota principale:

```md
# Skeuomorfismo

Alias: scheumorfismo
```

e aggiornare `00_Index.md` per evitare doppioni.

---

### E. Valutazione di usabilità ed euristica

Aggiornare:

```text
knowledge_base/05_Valutazione_Usabilita/
knowledge_base/06_Valutazione_Euristica/
```

#### Note da aggiornare

- `Valutazione di usabilita.md`
- `Valutazione quantitativa.md`
- `Valutazione euristica.md`
- `Valutazione olistica.md`
- `Valutazione task-oriented.md`
- `Protocollo think-aloud.md`
- `User test.md`
- `Euristiche di Nielsen.md`
- `ISO 9241-110.md`
- `IXD Checklist.md`
- `Severita problemi di usabilita.md`
- `Prioritizzazione problemi di usabilita.md`
- `Matrice problemi valutatori.md`
- `Rapporto finale valutazione euristica.md`

#### Contenuti da integrare

- Valutazione qualitativa:
  - interpretazione di esperti/utenti;
  - non trattata statisticamente;
  - non vaga: è sistematica e strutturata.
- Valutazione euristica:
  - tecnica sistematica di ispezione predittiva;
  - olistica o task-oriented;
  - con o senza osservatori;
  - produce elenco di problemi associati a euristiche e pesati per gravità.
- Differenza tra:
  - principi;
  - standard;
  - design pattern;
  - regole di progetto.
- Livelli di autorevolezza:
  - A: supporto empirico;
  - B: pratica documentata;
  - C: opinione professionale esperta;
  - D: opinione individuale.
- Nielsen:
  - usare sia i 10 principi originali sia la rielaborazione Mussio in macro-aree:
    - percezione;
    - cognizione;
    - errori.
- Metodo:
  - scegliere applicazione;
  - definire 2-3 task;
  - valutazione esperta;
  - coinvolgimento esperti di dominio;
  - think-aloud;
  - estrazione problemi;
  - fusione liste;
  - prioritizzazione;
  - associazione alle euristiche.
- Task:
  - realistici;
  - eseguibili;
  - non troppo guidati;
  - non devono contenere micro-step.

#### Importante

Le indicazioni numeriche 3+3, 12, 24, 5-15 minuti ecc. vanno trattate come:

- utili per capire il metodo;
- potenzialmente obsolete per il progetto attuale;
- non centrali per lo scritto teorico.

Spostare dettagli numerici in:

```text
analysis/info_progetto_potenzialmente_obsolete.md
```

---

### F. Questionari psicometrici e valutazione quantitativa

Aggiornare:

```text
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/
```

#### Note da aggiornare

- `Questionari psicometrici.md`
- `Scala Likert.md`
- `Bias di risposta.md`
- `Valutazione quantitativa.md`

#### Nuove note consigliate

- `SUMI.md`
- `SUS.md`
- `UEQ.md`
- `AttrakDiff.md`
- `NPS.md`
- `Mann-Whitney.md`
- `Kruskal-Wallis.md`
- `Wilcoxon.md`
- `Test binomiale.md`
- `Boxplot e violin plot.md`
- `Variabili ordinali continue discrete.md`
- `Fatigue bias.md`
- `Acquiescence bias.md`
- `Central tendency bias.md`
- `Option order bias.md`

#### Contenuti da integrare

- Questionari citati:
  - SUMI;
  - AttrakDiff;
  - UEQ;
  - SUS;
  - NPS.
- SUMI:
  - misura Quality of Use;
  - sottodimensioni: efficiency, affect, helpfulness, controllability, learnability;
  - lungo, rischio fatigue bias.
- SUS:
  - breve, noto, score 0-100;
  - trasformazione item pari/dispari;
  - attenzione: somma valori ordinali e mescola usabilità/apprendibilità.
- NPS:
  - misura raccomandabilità;
  - promotori/detrattori;
  - semplice, ma riduttivo.
- Variabili di stratificazione:
  - genere;
  - età;
  - familiarità col software.
- Statistica:
  - ordinali: mediana, moda, ranghi, Mann-Whitney/Wilcoxon/Kruskal-Wallis/Friedman;
  - continue: media, deviazione standard, t-test se appropriato;
  - discrete/dicotomiche: chi-quadro o test su proporzioni;
  - visualizzazioni: boxplot per scale ordinali, violin plot per tempi continui.
- Distinzione:
  - significatività pratica;
  - significatività statistica.

---

### G. Dark patterns e tecnologie persuasive

Aggiornare:

```text
knowledge_base/08_Dark_Patterns_e_Persuasione/
```

#### Note da aggiornare

- `Dark patterns.md`
- `Tecnologie persuasive.md`
- `Captologia.md`
- `CASA.md`
- `Ethopoeia.md`

#### Nuove note consigliate

- `Macrosuasione.md`
- `Microsuasione.md`
- `Credibilita.md`
- `Bait and switch.md`
- `Confirmshaming.md`
- `Disguised ad.md`
- `Forced continuity.md`
- `Friend spam.md`
- `Hidden costs.md`
- `Misdirection.md`
- `Price comparison prevention.md`
- `Privacy Zuckering.md`
- `Roach motel.md`
- `Sneak into basket.md`
- `Trick questions.md`
- `Von Restorff effect.md`
- `Halo effect.md`
- `Priming.md`
- `Effetto familiarita.md`

#### Contenuti da integrare

- Dark patterns come uso manipolativo del design per orientare l’utente contro il suo interesse o senza piena consapevolezza.
- Elenco dei 12 dark patterns citati nel 2022.
- Tecnologie persuasive:
  - sistemi interattivi progettati per modificare atteggiamenti o comportamenti;
  - persuasione distinta da coercizione e inganno.
- Captology:
  - Computer As Persuasive Technology.
- Macrosuasione:
  - prodotto nato principalmente per persuadere/motivare.
- Microsuasione:
  - elementi persuasivi inseriti in un sistema con obiettivo principale diverso.
- Credibilità come qualità percepita:
  - affidabilità;
  - competenza.
- CASA:
  - utenti tendono a trattare le macchine come attori sociali.
- Meccanismi psicologici:
  - riflesso pavloviano;
  - effetto placebo;
  - effetto camaleonte/specchio;
  - effetto alone;
  - effetto isolamento;
  - priming;
  - familiarità;
  - gratificazioni/incentivi.

---

### H. Semiotica e ingegneria semiotica

Aggiornare:

```text
knowledge_base/09_Semiotica_e_Ingegneria_Semiotica/
```

#### Note da aggiornare

- `Semiotica.md`
- `Segno simbolo icona indice.md`
- `Significante significato oggetto.md`
- `Ingegneria semiotica.md`

#### Nuove note consigliate

- `Sintassi semantica pragmatica.md`
- `Saussure.md`
- `Peirce.md`
- `Semiosi.md`
- `Abduzione.md`
- `Decodifica aberrante.md`
- `Designer deputy.md`
- `Comunicative breakdown.md`
- `Metodo di ispezione semiotica.md`
- `Segni linguistici e metalinguistici.md`

#### Contenuti da integrare

- Semiotica/semeiotica:
  - studio dei segni;
  - studio di come viene costruito il significato;
  - studio dell’efficacia della comunicazione.
- Tre ambiti:
  - sintassi: relazioni tra segni;
  - semantica: relazioni tra segni e ciò a cui si riferiscono;
  - pragmatica: relazioni tra segni e effetti/pratiche.
- Segno:
  - qualunque cosa percepibile che ha significato per qualcuno in un contesto sociale.
- Saussure:
  - significante/significato.
- Peirce:
  - representamen/rappresentante;
  - interpretant;
  - object/oggetto.
- Semiosi:
  - processo interpretativo, potenzialmente infinito;
  - ragionamento abduttivo: si formulano ipotesi interpretative, poi si confermano o riformulano.
- Simbolo:
  - relazione arbitraria/convenzionale.
- Icona:
  - somiglianza percepita.
- Indice:
  - connessione fisica/causale/contigua.
- Un segno può combinare simbolo, icona e indice.
- Ingegneria semiotica:
  - interazione uomo-macchina come comunicazione progettista-utente mediata dal sistema;
  - interfaccia come messaggio del progettista;
  - designer’s deputy come porzione del sistema che parla per il progettista;
  - breakdown comunicativi come fallimenti nella comunicazione mediata dall’interfaccia.

#### Fix importante

Nel conflict log era già presente un problema su “Semiotica - significato” dalla fonte 2021. Il file 2022 dà definizioni più complete. Aggiornare `analysis/conflict_log.md`:

```md
CFL-003 | Semiotica - significato | [[Appunti IUM 2021]], [[AppuntiIUM2022]] | Le definizioni 2021 erano colloquiali/incomplete; il 2022 chiarisce Saussure, Peirce, sintassi/semantica/pragmatica e tipologie di segni. | Media | Risolto parzialmente | Usare il 2022 come base provvisoria, da confermare con appunti collettivi recenti.
```

---

## Domande d’esame e flashcard da aggiungere

Aggiornare:

```text
exam_prep/domande_note/
exam_prep/flashcards/
exam_prep/checklist_ripasso.md
```

### Domande aperte consigliate

Aggiungere domande tipo:

```md
## Domande aperte da Appunti IUM 2022

### HCI e fondamenti
- Definisci l’HCI e spiega perché è una disciplina multidisciplinare.
- Spiega perché l’utente non coincide con il progettista.
- Spiega la differenza tra verifica e valutazione.

### Sistemi socio-tecnici
- Definisci sistema socio-tecnico e proprietà emergenti.
- Spiega lo STS thinking.
- Spiega overreliance, overdependence, overconfidence, complacency e automation bias.

### Usabilità
- Definisci usabilità secondo efficacia, efficienza e soddisfazione.
- Perché l’usabilità non è una proprietà intrinseca del sistema?
- Spiega robustezza, apprendibilità e ricordabilità.
- Spiega un trade-off di usabilità.

### Affordance e mapping
- Definisci affordance e distingui le sue tipologie.
- Spiega il mapping e la relazione con l’affordance.
- Spiega la differenza tra mapping arbitrario, convenzionale, naturale e diretto.
- Spiega vincoli strutturali e funzionali e il problema del workaround.

### Valutazione
- Spiega la valutazione euristica e il suo output.
- Differenza tra valutazione olistica e task-oriented.
- Come si costruisce un buon task per una valutazione di usabilità?
- Spiega la scala di severità Nielsen.
- Spiega la matrice problemi/valutatori.

### Questionari e statistica
- Che cosa sono i questionari psicometrici e a cosa servono?
- Confronta SUMI, SUS, UEQ e NPS.
- Che differenza c’è tra variabili ordinali, continue e discrete nella valutazione?
- Quando usare Mann-Whitney, Wilcoxon, Kruskal-Wallis o test binomiale?

### Persuasione e dark patterns
- Definisci captologia.
- Differenza tra persuasione, coercizione e inganno.
- Spiega macrosuasione e microsuasione.
- Descrivi almeno cinque dark patterns.

### Semiotica
- Definisci semiotica e i suoi tre ambiti: sintassi, semantica e pragmatica.
- Spiega il modello di Saussure.
- Spiega il modello di Peirce.
- Differenza tra simbolo, icona e indice.
- Spiega l’ingegneria semiotica.
```

### Flashcard consigliate

Aggiungere flashcard concise nel formato già usato dalla repo. Se non esiste un formato standard, usare:

```md
## Appunti IUM 2022

Q: Che cos’è l’usabilità?
A: Il grado con cui un prodotto può essere usato da determinati utenti per raggiungere determinati obiettivi con efficacia, efficienza e soddisfazione in un determinato contesto d’uso.

Q: Perché l’usabilità non è una proprietà intrinseca?
A: Perché dipende da utenti, obiettivi, attività e contesto d’uso.

Q: Che cos’è l’automation bias?
A: Eccessiva fiducia nel supporto decisionale automatico, che può causare errori di omissione o commissione quando il sistema è imperfetto.
```

---

## Aggiornamento glossario

Aggiornare:

```text
knowledge_base/99_Glossario/
```

Aggiungere o verificare voci:

```text
abduzione
accessibilità
affordance
automation bias
CASA
captologia
complacency
constraint
dark pattern
designer's deputy
efficacia
efficienza
ethopoeia
feedback
indice
interfaccia
learnability
mapping
memorability
microsuasione
macrosuasione
overconfidence
overdependence
overreliance
pragmatica
semantica
semiosi
semiotica
significante
significato
simbolo
sintassi
sistema interattivo
sistema socio-tecnico
skeuomorfismo
task
usabilità
workaround
```

Ogni voce deve avere:

```md
## Termine

Definizione breve.

Collegamenti:
- [[Nota principale]]
```

---

## Aggiornare gli index

Aggiornare almeno:

```text
knowledge_base/00_Index.md
exam_prep/00_Index.md
```

Aggiungere i nuovi link senza duplicare note già esistenti.

### Controlli Obsidian

Dopo l’aggiornamento:

1. Nessun wikilink rotto.
2. Nessun doppione concettuale evidente.
3. Titoli H1 coerenti con il concetto.
4. Note leggibili anche fuori da GitHub.
5. Callout Obsidian validi:
   - `[!info]`
   - `[!warning]`
   - `[!danger]`
   - `[!success]`
   - `[!question]`
   - `[!example]`

---

## Aggiornamento conflict log

Aggiornare:

```text
analysis/conflict_log.md
```

Aggiungere:

```md
CFL-004 | Numeri progetto 2022 | [[AppuntiIUM2022]] | Numeri di partecipanti, scadenze, punti e modalità progettuali sono legati all’anno 2022 e possono non valere per l’esame attuale. | Alta | Aperto | Separare teoria d’esame e progetto.
```

Aggiungere:

```md
CFL-005 | SUS e score psicometrici | [[AppuntiIUM2022]] | Lo score SUS è descritto ma anche criticato perché tratta dati ordinali con trasformazioni numeriche; mantenere la critica metodologica nella nota. | Media | Aperto | Da confrontare con appunti collettivi recenti.
```

Aggiornare `CFL-003` come indicato nella sezione semiotica.

---

## Aggiornamento pending questions

Aggiornare:

```text
analysis/pending_questions.md
```

Aggiungere domande da verificare con fonti successive:

```md
## Da verificare con appunti collettivi recenti e domande note

- La terminologia preferita dal professore è "semiotica" o "semeiotica"?
- Quanto sono richiesti nello scritto i dettagli numerici del progetto?
- Le tipologie di dark patterns sono richieste come elenco completo o solo come esempi?
- I questionari psicometrici richiesti nello scritto includono SUS, SUMI, UEQ, AttrakDiff e NPS o solo alcuni?
- La parte di statistica va conosciuta teoricamente o solo per il progetto?
- La distinzione tra macrosuasione e microsuasione è presente anche nelle domande note?
- Il metodo di ispezione semiotica viene chiesto nello scritto o è solo concetto avanzato?
```

---

## Informazioni progettuali potenzialmente obsolete

Aggiornare:

```text
analysis/info_progetto_potenzialmente_obsolete.md
```

Inserire una sezione `AppuntiIUM2022` con:

```md
## AppuntiIUM2022

Informazioni utili per capire il contesto del corso/progetto, ma non da usare automaticamente per l’esame scritto teorico attuale:

- modalità d’esame 2022;
- punti scritto/progetto/orale;
- scadenze e consegne;
- numero partecipanti indicato per progetto;
- composizione gruppi;
- indicazioni su slide/report;
- strumenti o questionari preferiti dal docente nel 2022;
- eventuali esempi legati a specifica edizione del corso.
```

---

## Regole di consolidamento

### Quando aggiornare una nota esistente

Aggiornare una nota esistente se il concetto è già presente, ma il file 2022:

- conferma la definizione;
- aggiunge esempi;
- chiarisce una distinzione;
- corregge una formulazione incerta;
- introduce terminologia più precisa.

### Quando creare una nuova nota

Creare una nuova nota solo se:

- il concetto è autonomo;
- potrebbe essere chiesto come domanda aperta;
- ha molte relazioni con altri concetti;
- il suo contenuto non entra bene in una nota già esistente.

### Quando non creare una nota

Non creare una nota per:

- esempi singoli troppo specifici;
- numeri legati al progetto;
- citazioni sparse;
- URL di strumenti;
- dettagli di calendario o modalità d’esame;
- frasi colloquiali degli appunti.

---

## Definition of Done

Codex deve terminare solo quando:

- [ ] `AppuntiIUM2022.pdf` è presente in `assets/raw/appunti-studenti/`.
- [ ] È stato creato/aggiornato `analysis/appunti_ium_2022_source.md`.
- [ ] È stato creato `analysis/reports/05_appunti_ium_2022.md`.
- [ ] `analysis/source_registry.md` marca `SRC-APP-003` come `Analizzato`.
- [ ] `README.md` non dichiara più fonti non analizzate come già integrate.
- [ ] Le note confermate da 2021+2022 sono marcate come confermate.
- [ ] I concetti nuovi 2022 sono marcati come da verificare.
- [ ] Le informazioni progettuali sono separate dalla teoria dello scritto.
- [ ] `analysis/conflict_log.md` è aggiornato.
- [ ] `analysis/pending_questions.md` è aggiornato.
- [ ] `analysis/info_progetto_potenzialmente_obsolete.md` è aggiornato.
- [ ] `knowledge_base/00_Index.md` include i nuovi concetti principali.
- [ ] `exam_prep/` contiene domande e flashcard derivate dal 2022.
- [ ] Non ci sono wikilink rotti.
- [ ] Non ci sono duplicati ovvi tra note.
- [ ] Accenti e italiano leggibile sono stati corretti nei testi principali.

---

## Commit suggerito

```bash
git add .
git commit -m "Integrate Appunti IUM 2022 into theory knowledge base"
```

Prima del commit, eseguire una review manuale dei file più importanti:

```text
README.md
knowledge_base/00_Index.md
analysis/source_registry.md
analysis/conflict_log.md
analysis/reports/05_appunti_ium_2022.md
exam_prep/checklist_ripasso.md
```
