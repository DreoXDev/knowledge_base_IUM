# Piano Codex - Iterazione 03 Knowledge Base IUM

## Obiettivo

Aggiornare la repo `knowledge_base_IUM` dopo l'integrazione del report sugli appunti 2022 e preparare l'integrazione del nuovo asset:

`IUM __ Appunti collettivi collaborativi 2024-25.pdf`

Questa iterazione deve fare due cose:

1. correggere le incoerenze rimaste nella repo dopo la seconda iterazione;
2. integrare il file 2024-25 come fonte recente, senza duplicare inutilmente concetti già presenti.

Il focus resta la preparazione dello scritto teorico di Interazione Uomo-Macchina, non il progetto pratico da consegnare.

---

## Stato osservato della repo

La repo ha già una struttura corretta per un vault Obsidian:

```text
analysis/
assets/
exam_prep/
knowledge_base/
templates/
workflows/
```

La `knowledge_base/` è già divisa in macro-sezioni teoriche:

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

La cartella `analysis/reports/` contiene già:

```text
00_template_asset_report.md
04_appunti_ium_2021.md
05_appunti_ium_2022.md
README.md
index.md
```

Problema principale: alcuni file di stato non sono allineati con i report già presenti.

---

## Fix obbligatori prima di integrare il nuovo asset

### 1. Sistemare `analysis/source_registry.md`

Attualmente il registro non è una vera tabella Markdown e contiene stati non allineati.

Convertire il contenuto in tabella Markdown valida:

```md
| ID Fonte | Nome file | Tipo | Anno | Stato analisi | Attendibilità | Report collegato | Note |
|---|---|---|---|---|---|---|---|
```

Aggiornare gli stati così:

```md
| SRC-DOM-001 | Domande IUM.pdf | domande note | 2020-2021 | Da analizzare | Media-bassa |  | Risposte non affidabili da verificare |
| SRC-APP-001 | Appunti Collettivi 2025-2026.md | appunti collettivi | 2025-2026 | Da analizzare | Media-alta |  | Fonte più recente |
| SRC-APP-002 | Appunti IUM 2021.pdf | appunti studenti | 2020-2021 | Analizzato | Media-bassa | [[reports/04_appunti_ium_2021]] | Prima fonte integrata |
| SRC-APP-003 | AppuntiIUM2022.pdf | appunti studenti | 2022 | Analizzato | Media | [[reports/05_appunti_ium_2022]] | Fonte ampia già integrata |
| SRC-APP-004 | IUM __ Appunti collettivi collaborativi 2024-25.pdf | appunti collettivi | 2024-2025 | In analisi | Media-alta | [[reports/02_appunti_collettivi_2024_2025]] | Fonte recente da integrare in questa iterazione |
```

Dopo aver completato l'integrazione, cambiare `SRC-APP-004` da `In analisi` ad `Analizzato`.

---

### 2. Correggere `README.md`

Il README non deve dichiarare come "integrate" fonti che non sono ancora state analizzate.

Sostituire la sezione `Stato knowledge base` con una struttura più precisa:

```md
## Stato knowledge base

### Fonti analizzate

- Appunti IUM 2021
- Appunti IUM 2022

### Fonti in corso

- Appunti collettivi collaborativi 2024-25

### Fonti previste

- Appunti Collettivi 2025-2026.md
- Domande IUM.pdf

### Metodo di lavoro

Ogni fonte viene analizzata separatamente. Le informazioni vengono prima inserite come `DA VERIFICARE`, poi consolidate quando confermate da più fonti o dalle domande note.
```

Dopo questa iterazione, spostare `Appunti collettivi collaborativi 2024-25` da `Fonti in corso` a `Fonti analizzate`.

---

### 3. Correggere `analysis/reports/index.md`

L'indice report ha già il placeholder:

```md
| `02_appunti_collettivi_2024_2025` | IUM - Appunti collettivi collaborativi 2024-25.pdf | SRC-APP-004 | Da creare |
```

Aggiornarlo così:

```md
| [[02_appunti_collettivi_2024_2025]] | IUM __ Appunti collettivi collaborativi 2024-25.pdf | SRC-APP-004 | Creato |
```

Non creare un nuovo `06_...` se il placeholder `02_...` esiste già: usa il nome già previsto per evitare ulteriore disordine.

---

### 4. Verificare che i raw asset siano presenti

Controllare che il PDF sia salvato in una cartella coerente, ad esempio:

```text
assets/raw/appunti-collettivi/IUM_Appunti_collettivi_collaborativi_2024-25.pdf
```

Se il file ha spazi, doppio underscore o caratteri problematici, mantenere pure il file originale ma aggiungere una nota nel report con il path reale.

Non modificare il contenuto dei raw asset.

---

### 5. Verificare accenti e stile italiano

Fare una passata veloce sui file Markdown modificati in questa iterazione e correggere almeno gli errori ricorrenti:

```text
piu -> più
perche -> perché
proprieta -> proprietà
usabilita -> usabilità
affidabilita -> affidabilità
validita -> validità
qualita -> qualità
attivita -> attività
```

Non fare refactor stilistici enormi su tutta la repo in questa iterazione: correggere solo i file toccati.

---

### 6. Verificare wikilink principali

Dopo l'integrazione, controllare che i link presenti in `knowledge_base/00_Index.md` puntino a note realmente esistenti.

Se un link punta a una nota inesistente ma il concetto è già presente in un'altra nota con nome diverso:

- non creare duplicati;
- aggiungere alias/frontmatter o correggere il link;
- mantenere un nome nota stabile e leggibile.

Esempio: mantenere `Skeuomorfismo` come nota principale, ma aggiungere alias `scheumorfismo` se utile.

---

## Nuovo report da creare

Creare:

```text
analysis/reports/02_appunti_collettivi_2024_2025.md
```

Struttura obbligatoria:

```md
# Report analisi - Appunti collettivi collaborativi 2024-25

Data analisi: 2026-05-17
Asset analizzato: `assets/raw/appunti-collettivi/IUM_Appunti_collettivi_collaborativi_2024-25.pdf`
Tipo asset: `appunti collettivi`
Stato report: `COMPLETO`
Fonte: `SRC-APP-004`

## 1. Sintesi fonte

## 2. Concetti confermati rispetto alle fonti 2021 e 2022

## 3. Concetti da consolidare o aggiornare nella KB

## 4. Concetti nuovi o più precisi

## 5. Informazioni progettuali o amministrative da separare

## 6. Note da creare o aggiornare

## 7. Domande d'esame / flashcard da aggiungere

## 8. Dubbi, conflitti e punti da verificare

## 9. Azioni eseguite da Codex
```

---

## Analisi del nuovo asset 2024-25

Il file 2024-25 è più sintetico e pulito dei PDF 2021/2022. Va trattato come fonte recente e utile per consolidare definizioni già presenti.

Non va copiato integralmente nella KB. Va usato per:

- confermare concetti già presenti;
- correggere formulazioni troppo grezze;
- aggiungere dettagli mancanti;
- aumentare l'attendibilità dei concetti presenti anche in 2021/2022;
- creare domande/flashcard su punti esplicitamente segnalati come rilevanti per scritto.

---

## Note da aggiornare nella knowledge base

### 1. Fondamenti HCI

Cartella:

```text
knowledge_base/01_Fondamenti_HCI/
```

Aggiornare o verificare:

```text
Human-Computer Interaction.md
Ergonomia cognitiva.md
Sistema interattivo.md
Interfaccia.md
Task.md
IUUMM.md
```

Azioni:

- aggiungere/raffinare definizione di HCI come disciplina che si occupa di progettazione, realizzazione e valutazione di sistemi interattivi con capacità computazionale destinati all'uso umano;
- evidenziare che i sistemi reali sono usati da persone reali in attività reali;
- aggiungere o consolidare `IUUMM`: Interazione Uomo-Uomo Mediata dalla Macchina;
- aggiungere origini HCI: anni Ottanta, diffusione personal computer, IBM PC 1981, Apple Macintosh 1984, ACM CHI 1983;
- rafforzare interdisciplinarità: scienza dei computer, scienze della progettazione, scienze dell'uomo;
- aggiornare ergonomia cognitiva con processi cognitivi coinvolti: percezione, attenzione, memoria, pensiero, linguaggio, emozioni;
- aggiungere nota su introspezione del progettista: il progettista non è l'utente e non può progettare solo immaginando se stesso.

Se `IUUMM.md` non esiste, crearla.

---

### 2. Sistemi socio-tecnici

Cartella:

```text
knowledge_base/02_Sistemi_Socio_Tecnici/
```

Aggiornare:

```text
Sistema socio-tecnico.md
STS thinking.md
Proprieta emergenti.md
Conseguenze inattese.md
Effetto Peltzman.md
```

Azioni:

- consolidare la definizione di sistema socio-tecnico come insieme di elementi interrelati e mutualmente dipendenti che appaiono come entità unitaria ma collettiva;
- chiarire il ruolo dell'osservatore nel definire il perimetro del sistema;
- aggiungere componente sociale e componente tecnica:
  - persone: ergonomia, dimensione sociale, conoscenza tacita, convenzioni, unwritten rules;
  - tecniche/tecnologie: procedure, protocolli, divisione del lavoro, written rules;
- consolidare proprietà emergenti funzionali e non funzionali;
- rafforzare STS thinking come joint optimization tra componente sociale e tecnica;
- aggiornare conseguenze inattese con effetto Peltzman/effetto cobra e risk compensation.

---

### 3. Automazione, bias e conseguenze inattese

Cartella:

```text
knowledge_base/10_Automazione_Bias_e_Conseguenze_Inattese/
```

Aggiornare o creare:

```text
Overreliance.md
Overdependence.md
Overconfidence.md
Automation bias.md
Automation-related complacency.md
Complacency.md
```

Azioni:

- verificare se `Complacency` e `Automation-related complacency` sono duplicati;
- se duplicati, usare una nota principale e alias;
- distinguere chiaramente:
  - overreliance come sovraffidamento generale;
  - overdependence / automation bias come dipendenza eccessiva dal supporto decisionale;
  - overconfidence / automation-related complacency come fiducia che il sistema funzioni sempre correttamente;
- aggiungere esempi brevi solo se utili allo studio, senza appesantire.

---

### 4. Usabilità e UX

Cartella:

```text
knowledge_base/03_Usabilita/
```

Aggiornare:

```text
Usabilita.md
Efficacia.md
Efficienza.md
Soddisfazione.md
Bassa usabilita.md
Low use.md
User experience.md
Potenziale usabilita.md
Robustezza.md
Apprendibilita.md
Ricordabilita.md
```

Azioni:

- consolidare definizione ISO di usabilità:
  - determinati utenti;
  - determinati obiettivi;
  - efficacia, efficienza, soddisfazione;
  - determinato contesto d'uso;
- ribadire che non ha senso parlare di usabilità assoluta di un sistema in sé, ma solo in un contesto d'uso;
- se manca, creare `Potenziale usabilita.md`;
- chiarire UX come esperienza soggettiva e dinamica;
- distinguere utile / usabile / usato;
- aggiungere estensioni:
  - robustezza;
  - apprendibilità;
  - ricordabilità;
- aggiungere trade-off tra learnability/soddisfazione e robustezza/efficienza;
- aggiornare Low Use con formula dello Use Index se già presente, altrimenti crearla.

---

### 5. Affordance, mapping, constraints e complessità

Cartella:

```text
knowledge_base/04_Affordance_Mapping_Constraints/
```

Aggiornare:

```text
Affordance.md
Mapping.md
Constraints.md
Workaround.md
Skeuomorfismo.md
User-created affordances.md
Multifunzionalita.md
Complessita d'uso strutturale funzionale.md
Legge di Fitts.md
Errori di giustapposizione.md
Dispositivi per l'interazione.md
```

Azioni:

- consolidare definizioni Gibson e Norman di affordance;
- esplicitare che l'affordance non è puramente intrinseca, ma dipende anche da capacità, competenze e contesto dell'utente;
- distinguere affordance:
  - cognitive;
  - fisiche;
  - sensoriali;
  - funzionali;
  - emozionali;
  - sociali;
- aggiornare mapping come caratteristica dell'affordance;
- mantenere distinzione tra mapping diretto/naturale e arbitrario/convenzionale;
- ribadire formula concettuale: non puoi avere mapping senza affordance, ma puoi avere affordance senza mapping;
- aggiornare constraints:
  - passivi/strutturali;
  - attivi/funzionali;
- aggiornare workaround come segnale utile per capire dove il sistema non supporta bene l'uso reale;
- creare o aggiornare `Dispositivi per l'interazione.md` con input/output:
  - output: vista, udito, tatto;
  - input: mani, voce, sguardo, postura;
- consolidare complessità:
  - funzionale;
  - strutturale;
  - d'uso;
- aggiungere idea dell'interfaccia come filtro semplificatore che riduce la complessità d'uso senza cambiare necessariamente complessità funzionale/strutturale;
- aggiungere `show off` come rischio progettuale se non già presente.

---

### 6. Valutazione di usabilità

Cartella:

```text
knowledge_base/05_Valutazione_Usabilita/
```

Aggiornare:

```text
Valutazione di usabilita.md
User test.md
Protocollo think-aloud.md
Confronto longitudinale.md
Confronto trasversale.md
Valutazione qualitativa.md
Valutazione quantitativa.md
```

Azioni:

- chiarire confronto longitudinale: due versioni dello stesso sistema;
- chiarire confronto trasversale: due sistemi diversi;
- aggiungere valutazione formativa / riassuntiva se manca;
- aggiungere valutazione assoluta / comparativa se manca;
- consolidare caratteristiche della valutazione:
  - empirica;
  - concreta;
  - sistematica;
- mantenere separati i dettagli del progetto pratico da quelli teorici.

---

### 7. Valutazione euristica

Cartella:

```text
knowledge_base/06_Valutazione_Euristica/
```

Aggiornare:

```text
Valutazione euristica.md
Valutazione olistica.md
Valutazione task-oriented.md
Euristiche di Nielsen.md
IXD Checklist.md
ISO 9241-110.md
Principi linee guida standard regole di progetto.md
Matrice problemi valutatori.md
Severita problemi usabilita.md
Prioritizzazione problemi usabilita.md
Walk-up-and-use system.md
```

Azioni:

- verificare se esistono note equivalenti con nomi diversi prima di creare nuovi file;
- aggiungere/rafforzare distinzione:
  - principi;
  - linee guida/design pattern;
  - regole di progetto;
  - standard;
- aggiungere assi: generalità e prescrittività;
- aggiungere livelli di autorevolezza A/B/C/D;
- consolidare ISO 9241-110 con i sette principi:
  1. Adeguatezza al compito
  2. Autodescrizione
  3. Conformità alle aspettative dell'utente
  4. Adeguatezza all'apprendimento
  5. Controllabilità
  6. Tolleranza verso gli errori
  7. Adeguatezza alla personalizzazione
- consolidare Nielsen/Mussio:
  - percezione;
  - cognizione;
  - errori;
- aggiornare metodo:
  - valutazione sistematica;
  - ispezione predittiva;
  - olistica vs task-oriented;
  - con/senza osservatori;
  - valutatori esperti di usabilità e/o dominio;
  - think-aloud;
  - estrazione problemi;
  - accorpamento;
  - associazione a euristiche;
  - valutazione severità;
- creare/aggiornare `Matrice problemi valutatori.md`;
- creare/aggiornare `Prioritizzazione problemi usabilita.md` con:
  - scala severità 0-4;
  - frequenza, impatto, persistenza;
  - rank 1224;
  - prima fascia circa 20%;
  - test binomiale;
  - media/mediana/deviazione standard/range interquartile;
- aggiungere errori frequenti:
  - aggregare problemi;
  - proporre soluzioni durante la valutazione;
  - partire dai principi invece che dai problemi;
  - mischiare problemi e soluzioni.

---

### 8. Valutazione quantitativa e statistica inferenziale

Cartella:

```text
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/
```

Aggiornare o creare:

```text
Valutazione quantitativa.md
Misura e metrica.md
Variabili e scale di misura.md
Intervallo di confidenza.md
Significativita statistica e pratica.md
Test statistici per IUM.md
Mann-Whitney.md
Kruskal-Wallis.md
Test binomiale.md
Chi quadro.md
T di Student.md
ANOVA.md
Boxplot e violin plot.md
```

Azioni:

- creare una nota sintetica `Test statistici per IUM.md` con tabella operativa:
  - variabili continue -> T di Student / ANOVA;
  - variabili ordinali -> Mann-Whitney/Wilcoxon, Kruskal-Wallis/Friedman;
  - variabili discrete/dicotomiche -> Chi quadro o test binomiale;
  - valutazione assoluta su scala psicometrica -> confronto risposte positive/negative, test binomiale o intervalli di confidenza;
- aggiungere o rafforzare:
  - variabile numerica;
  - variabile ordinale;
  - variabile categorica/nominale;
  - scala a rapporti;
  - scala a intervalli;
- aggiungere avviso: non calcolare la media di variabili ordinali se non è giustificato; preferire mediana/moda secondo il tipo di dato;
- aggiungere definizione di intervallo di confidenza come domanda da scritto;
- distinguere:
  - differenza statisticamente significativa;
  - differenza praticamente significativa;
- spiegare approccio di Neyman: confronto intervalli di confidenza;
- spiegare approccio di Fisher: test di ipotesi e ipotesi nulla;
- mantenere tono da appunto teorico, non da corso di statistica avanzata.

---

### 9. Questionari psicometrici

Cartella:

```text
knowledge_base/07_Questionari_e_Valutazione_Quantitativa/
```

Aggiornare o creare:

```text
Questionari psicometrici.md
Scala Likert.md
Bias di risposta.md
NPS.md
SUMI.md
AttrakDiff.md
UEQ.md
SUS.md
Fatigue bias.md
Acquiescence bias.md
Central tendency bias.md
```

Azioni:

- aggiornare `Scala Likert.md` con svantaggi:
  - acquiescence bias;
  - central tendency bias;
- aggiornare `NPS.md`:
  - detrattori 0-6;
  - passivi 7-8;
  - promotori 9-10;
  - formula NPS = % promotori - % detrattori;
  - criticità italiana: confusione con voto scolastico 0-10;
  - possibile correzione: probabilità 0%-100%;
- aggiornare `SUMI.md`:
  - 50 item;
  - tre valori di risposta;
  - cinque sottodimensioni: efficiency, affect, helpfulness, controllability, learnability;
  - vantaggi e svantaggi;
- aggiornare `AttrakDiff.md`:
  - differenziale semantico;
  - UX;
  - qualità pragmatica/edonica se già presente dalle fonti precedenti;
- aggiornare `UEQ.md`:
  - 26 item;
  - sei sottoscale: attractiveness, perspicuity, efficiency, dependability, stimulation, novelty;
  - vantaggi: documentazione, tool, benchmark, traduzioni;
  - svantaggi: central tendency bias e trattamento numerico;
- aggiornare `SUS.md`:
  - 10 item;
  - 5 livelli;
  - calcolo score con item dispari/pari;
  - moltiplicazione per 2.5;
  - interpretazione soglia 68;
  - aggiungere attenzione agli errori di calcolo.

---

### 10. Domande d'esame e flashcard

Cartelle:

```text
exam_prep/domande_note/
exam_prep/flashcards/
exam_prep/checklist_ripasso.md
```

Creare o aggiornare:

```text
exam_prep/domande_note/domande_appunti_collettivi_2024_2025.md
exam_prep/flashcards/flashcards_appunti_collettivi_2024_2025.md
```

Aggiungere domande aperte brevi, ad esempio:

```md
## Domande da appunti collettivi 2024-25

### Che cos'è l'HCI?

### Perché l'usabilità non è una caratteristica intrinseca del sistema?

### Che cos'è un sistema socio-tecnico?

### Che cosa sono le proprietà emergenti?

### Differenza tra overdependence e overconfidence.

### Che cosa significa progettare per l'uso?

### Che differenza c'è tra affordance e mapping?

### Che cosa sono i constraints strutturali e funzionali?

### Che cos'è un workaround e perché è utile per il progettista?

### Che differenza c'è tra confronto longitudinale e trasversale?

### Che cos'è una valutazione euristica?

### Differenza tra valutazione olistica e task-oriented.

### Che cosa sono generalità e prescrittività nelle indicazioni di design?

### Differenza tra principi, linee guida, standard e regole di progetto.

### Che cos'è l'intervallo di confidenza?

### Differenza tra significatività statistica e significatività pratica.

### Quando usare Mann-Whitney, Kruskal-Wallis, test binomiale e Chi quadro?

### Che cos'è il Net Promoter Score?

### Vantaggi e svantaggi di SUMI, UEQ, SUS e AttrakDiff.
```

Aggiornare `exam_prep/checklist_ripasso.md` aggiungendo una sezione:

```md
## Da saper spiegare bene dopo Appunti collettivi 2024-25

- [ ] HCI e IUUMM
- [ ] Sistema socio-tecnico
- [ ] Conseguenze inattese e overreliance
- [ ] Affordance, mapping, constraints, workaround
- [ ] Complessità funzionale, strutturale e d'uso
- [ ] Valutazione euristica
- [ ] Euristiche Nielsen/Mussio
- [ ] ISO 9241-110
- [ ] Intervallo di confidenza
- [ ] Test statistici principali per IUM
- [ ] Questionari SUMI, UEQ, SUS, AttrakDiff, NPS
```

---

## Informazioni da NON integrare nella KB teorica principale

Il file contiene anche indicazioni legate al progetto d'esame e alla relazione.

Non inserirle nelle note teoriche principali se sono operative/progettuali.

Spostarle o sintetizzarle in:

```text
analysis/info_progetto_potenzialmente_obsolete.md
```

oppure, se utili al progetto ma non allo scritto:

```text
analysis/project_notes_from_sources.md
```

Esempi di contenuti da separare:

- numeri esatti di utenti per progetto;
- richieste specifiche della relazione;
- grafici consigliati per la presentazione;
- indicazioni su deliverable;
- workflow pratico per progetto.

La knowledge base per lo scritto deve rimanere pulita e teorica.

---

## Regole di consolidamento

Quando un concetto è presente in 2021, 2022 e 2024-25:

- rimuovere `DA VERIFICARE`;
- impostare stato come `confermato`;
- aggiungere nel frontmatter o nella sezione fonte:
  - `SRC-APP-002`
  - `SRC-APP-003`
  - `SRC-APP-004`

Quando un concetto è presente solo in 2024-25:

- inserirlo come `DA VERIFICARE`;
- collegarlo solo a `SRC-APP-004`;
- aggiungere eventualmente a `analysis/pending_questions.md`.

Quando 2024-25 corregge o chiarisce 2021/2022:

- aggiornare la nota consolidata;
- aggiungere una riga in `analysis/conflict_log.md`;
- non mantenere due versioni incompatibili nella KB principale.

---

## Controlli finali richiesti a Codex

Alla fine dell'iterazione eseguire questi controlli:

1. `analysis/source_registry.md` è una tabella Markdown valida.
2. `SRC-APP-003` risulta `Analizzato`.
3. `SRC-APP-004` risulta `Analizzato`.
4. Esiste `analysis/reports/02_appunti_collettivi_2024_2025.md`.
5. `analysis/reports/index.md` punta al nuovo report.
6. Il README non dichiara integrate fonti ancora non analizzate.
7. Non sono state create note duplicate per concetti già presenti.
8. `knowledge_base/00_Index.md` linka le nuove note create.
9. `exam_prep/checklist_ripasso.md` include i punti del nuovo asset.
10. Le informazioni di progetto sono separate dalle note teoriche.
11. I file modificati usano accenti corretti in italiano.
12. Le note sono leggibili in Obsidian senza plugin obbligatori.

---

## Output atteso da Codex

Alla fine Codex deve produrre un breve riepilogo in chat con:

```md
## Iterazione 03 completata

### File aggiornati
- ...

### File creati
- ...

### Concetti consolidati
- ...

### Concetti nuovi inseriti
- ...

### Problemi/fix applicati
- ...

### Dubbi rimasti
- ...
```

Non deve fare commit automatici se non esplicitamente richiesto.
