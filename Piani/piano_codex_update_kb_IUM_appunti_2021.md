# Piano Codex — Aggiornamento Knowledge Base IUM da `Appunti IUM 2021.pdf`

> Obiettivo: aggiornare la knowledge base Obsidian dell'esame scritto teorico di **Interazione Uomo-Macchina (IUM)** usando il file `Appunti IUM 2021.pdf` come **prima fonte raw analizzata**.
>
> Importante: questo piano non chiede a Codex di “studiare tutto a caso”, ma di trasformare il PDF in note Markdown atomiche, collegate, verificabili e utili per ripasso/esame.

---

## 0. Contesto operativo

La repo è una knowledge base universitaria pensata per essere:

- leggibile direttamente come vault Obsidian;
- mantenibile da AI/Codex;
- basata su fonti raw versionate;
- costruita progressivamente, un file alla volta;
- orientata allo studio dello scritto teorico, non al progetto pratico di IUM.

Il file da integrare ora è:

```text
raw/assets/Appunti IUM 2021.pdf
```

Se il file non è ancora presente nella repo, Codex deve:

1. creare la cartella `raw/assets/` se manca;
2. copiare o aspettarsi il PDF in quella posizione;
3. registrarlo nel file indice delle fonti;
4. non modificare direttamente il PDF.

---

## 1. Regole fondamentali per Codex

### 1.1 Non sovrascrivere la knowledge base in modo distruttivo

Codex deve aggiornare o creare file Markdown in modo incrementale.

Prima di modificare una nota già esistente:

1. leggere il contenuto attuale;
2. capire se il nuovo contenuto conferma, aggiunge dettagli, corregge informazioni o crea conflitti;
3. applicare modifiche minime e tracciabili.

### 1.2 Separare fonte, sintesi e verifica

Ogni informazione importante deve avere una distinzione chiara tra:

- contenuto estratto dalla fonte;
- sintesi rielaborata per lo studio;
- stato di affidabilità.

Gli appunti 2021 contengono un disclaimer di possibile incompletezza/imprecisione, quindi non devono essere trattati come fonte definitiva.

Usare questi stati:

```text
status: raw
status: da-verificare
status: verificato-da-piu-fonti
status: consolidato
```

### 1.3 Formato Obsidian

Tutti i file generati devono essere Markdown pulito e leggibile in Obsidian.

Usare:

- wikilink `[[Nome nota]]`;
- tag coerenti;
- callout Obsidian;
- tabelle Markdown solo quando utili;
- titoli gerarchici;
- niente emoji;
- matematica in LaTeX solo dove serve.

Esempi di callout ammessi:

```md
> [!note] Sintesi
> Testo sintetico del concetto.

> [!warning] Da verificare
> Informazione presente negli appunti 2021 ma da controllare con fonti successive/domande note.

> [!question] Possibile domanda d'esame
> Domanda formulata a partire dal concetto.
```

---

## 2. Struttura repo da aggiornare

Codex deve verificare che la repo abbia una struttura simile. Se mancano cartelle/file, crearli.

```text
.
├── README.md
├── ai/
│   ├── codex_instructions.md
│   ├── workflow_analisi_fonti.md
│   └── reports/
│       └── 2021_appunti_ium_analysis_report.md
├── raw/
│   ├── assets/
│   │   └── Appunti IUM 2021.pdf
│   └── extracted/
│       └── appunti_ium_2021_extracted.md
├── kb/
│   ├── 00_Index.md
│   ├── 01_Mappe/
│   │   └── Mappa concetti IUM.md
│   ├── 02_Concetti/
│   ├── 03_Metodi/
│   ├── 04_Euristiche/
│   ├── 05_Domande_Esame/
│   ├── 06_Glossario/
│   │   └── Glossario IUM.md
│   └── 99_Da_Verificare/
│       └── Dubbi e conflitti fonti.md
├── sources/
│   ├── Fonti.md
│   └── Appunti IUM 2021.md
└── templates/
    ├── template_concetto.md
    ├── template_metodo.md
    ├── template_domanda.md
    └── template_report_fonte.md
```

Se la struttura reale della repo è diversa, Codex deve adattare i path mantenendo comunque questi ruoli logici.

---

## 3. Registrazione della fonte

Creare o aggiornare:

```text
sources/Appunti IUM 2021.md
```

Contenuto minimo:

```md
---
type: fonte
source_kind: appunti_studenti
course: Interazione Uomo-Macchina
year: 2020-2021
reliability: media-bassa
status: raw
processed: false
---

# Appunti IUM 2021

## Descrizione

Appunti degli studenti del corso di Interazione Uomo-Macchina 2020-2021.

> [!warning] Affidabilità
> La fonte stessa contiene un disclaimer: gli appunti possono includere imprecisioni, errori o parti incomplete. Usarli come base di estrazione concetti, ma non come autorità finale.

## Stato lavorazione

- [ ] PDF importato in `raw/assets/`
- [ ] Testo estratto in `raw/extracted/`
- [ ] Concetti principali identificati
- [ ] Note atomiche create
- [ ] Domande d'esame derivate
- [ ] Dubbi/conflitti registrati
- [ ] Report finale generato

## Collegamenti

- File raw: `raw/assets/Appunti IUM 2021.pdf`
- Estrazione testo: `raw/extracted/appunti_ium_2021_extracted.md`
- Report analisi: `ai/reports/2021_appunti_ium_analysis_report.md`
```

Aggiornare anche:

```text
sources/Fonti.md
```

aggiungendo una riga in tabella:

```md
| Fonte | Tipo | Anno | Stato | Affidabilità | Note |
|---|---|---:|---|---|---|
| [[Appunti IUM 2021]] | Appunti studenti | 2020-2021 | raw | media-bassa | Prima fonte storica da integrare; contiene disclaimer interno |
```

---

## 4. Estrazione controllata del contenuto

Codex deve creare:

```text
raw/extracted/appunti_ium_2021_extracted.md
```

Questo file deve contenere una trascrizione o estrazione pulita del PDF, mantenendo la struttura per sezioni.

Non deve essere una nota di studio finale, ma una base di lavoro.

Formato consigliato:

```md
# Estrazione — Appunti IUM 2021

Fonte: [[Appunti IUM 2021]]

## Pagine 1-2 — Metadati e indice

...

## Sezione — L'interazione Uomo-Macchina

...

## Sezione — Sistema socio-tecnico

...
```

Regole:

- preservare i titoli principali;
- correggere solo errori OCR evidenti;
- non rielaborare pesantemente;
- non eliminare esempi importanti;
- marcare immagini/diagrammi non trascritti con:

```md
> [!info] Figura da valutare
> Nel PDF è presente una figura utile a supporto del concetto. Valutare se ricrearla come schema testuale.
```

---

## 5. Macro-argomenti da estrarre dal PDF

Il PDF contiene un indice già utile. Codex deve usarlo come base per la tassonomia iniziale.

### 5.1 Concetti base HCI

Cartella:

```text
kb/02_Concetti/
```

Note da creare/aggiornare:

```text
HCI - Interazione Uomo-Macchina.md
Ergonomia cognitiva.md
Sistema interattivo.md
Interfaccia.md
Usabilità.md
Sistema socio-tecnico.md
Conseguenze inattese.md
Overreliance.md
Overdependence.md
Overconfidence.md
Complacency.md
Automation bias.md
Affordance.md
Mapping.md
Constraint.md
Workaround.md
Multifunzionalità.md
Complessità d'uso strutturale funzionale.md
Skeuomorfismo.md
User-created affordances.md
Errori di giustapposizione.md
Low use.md
UX - User Experience.md
```

### 5.2 Metodi e valutazione

Cartella:

```text
kb/03_Metodi/
```

Note da creare/aggiornare:

```text
Valutazione di usabilità.md
Valutazione euristica.md
User test.md
Protocollo think-aloud.md
Valutazione quantitativa.md
Confronto longitudinale.md
Confronto trasversale.md
Prioritizzazione problemi di usabilità.md
Severità problemi di usabilità.md
Matrice problemi valutatori.md
Rapporto finale valutazione euristica.md
```

### 5.3 Euristiche e principi di design

Cartella:

```text
kb/04_Euristiche/
```

Note da creare/aggiornare:

```text
Euristiche di Nielsen.md
IXD Checklist.md
ISO 9241-110.md
Principi linee guida standard regole di progetto.md
Alert Identify Direct.md
Prevenzione degli errori.md
Feedback.md
Consistency.md
Simplicity.md
Accessibility.md
Tolerance.md
```

### 5.4 Semiotica, persuasione e temi avanzati

Cartella:

```text
kb/02_Concetti/
```

Note da creare/aggiornare:

```text
Dark patterns.md
Tecnologie persuasive.md
Captologia.md
Semiotica.md
Segno simbolo icona indice.md
Significante significato oggetto.md
Ingegneria semiotica.md
Metacomunicazione.md
Deputy del progettista.md
CASA.md
Ethopoeia.md
```

Creare queste note anche se nel primo passaggio sono solo scheletri da completare, perché il PDF 2021 include questi argomenti nell'indice e probabilmente nelle sezioni finali.

---

## 6. Template per ogni nota concettuale

Ogni nota in `kb/02_Concetti/` deve seguire questo formato.

```md
---
type: concetto
course: IUM
status: da-verificare
sources:
  - "[[Appunti IUM 2021]]"
tags:
  - ium
  - concetto
---

# Nome concetto

> [!note] Definizione breve
> Definizione sintetica in 2-4 righe.

## Spiegazione

Spiegazione rielaborata in modo chiaro, adatta al ripasso.

## Dettagli importanti

- Punto importante 1
- Punto importante 2
- Punto importante 3

## Esempi

- Esempio tratto dagli appunti 2021.
- Eventuale esempio riformulato.

## Collegamenti

- [[Concetto correlato 1]]
- [[Concetto correlato 2]]

## Possibili domande d'esame

> [!question] Domanda
> Domanda teorica plausibile.

Risposta sintetica:

...

## Stato di verifica

> [!warning] Da verificare
> Contenuto basato sugli appunti 2021. Verificare con appunti collettivi più recenti e domande note.

## Fonti

- [[Appunti IUM 2021]]
```

---

## 7. Template per metodi/procedure

Ogni nota in `kb/03_Metodi/` deve seguire questo formato.

```md
---
type: metodo
course: IUM
status: da-verificare
sources:
  - "[[Appunti IUM 2021]]"
tags:
  - ium
  - metodo
---

# Nome metodo

## Obiettivo

A cosa serve il metodo.

## Quando si usa

Contesto d'uso.

## Procedura

1. Primo passo
2. Secondo passo
3. Terzo passo

## Output atteso

- Output 1
- Output 2

## Errori da evitare

- Errore 1
- Errore 2

## Collegamenti

- [[Concetto correlato]]
- [[Metodo correlato]]

## Possibili domande d'esame

> [!question] Domanda
> ...

## Fonti

- [[Appunti IUM 2021]]
```

---

## 8. Aggiornamento mappa concettuale

Aggiornare:

```text
kb/01_Mappe/Mappa concetti IUM.md
```

Struttura consigliata:

```md
# Mappa concetti IUM

## Fondamenti

- [[HCI - Interazione Uomo-Macchina]]
- [[Ergonomia cognitiva]]
- [[Sistema interattivo]]
- [[Interfaccia]]
- [[Usabilità]]

## Progettazione dell'interazione

- [[Affordance]]
- [[Mapping]]
- [[Constraint]]
- [[Workaround]]
- [[Skeuomorfismo]]
- [[Multifunzionalità]]

## Sistemi socio-tecnici e conseguenze inattese

- [[Sistema socio-tecnico]]
- [[Conseguenze inattese]]
- [[Overreliance]]
- [[Overdependence]]
- [[Overconfidence]]
- [[Complacency]]
- [[Automation bias]]

## Valutazione

- [[Valutazione di usabilità]]
- [[Valutazione euristica]]
- [[User test]]
- [[Valutazione quantitativa]]
- [[Severità problemi di usabilità]]
- [[Prioritizzazione problemi di usabilità]]

## Euristiche

- [[Euristiche di Nielsen]]
- [[IXD Checklist]]
- [[ISO 9241-110]]
- [[Prevenzione degli errori]]
- [[Alert Identify Direct]]

## Temi avanzati

- [[Dark patterns]]
- [[Tecnologie persuasive]]
- [[Captologia]]
- [[Semiotica]]
- [[Ingegneria semiotica]]
```

---

## 9. Aggiornamento glossario

Aggiornare:

```text
kb/06_Glossario/Glossario IUM.md
```

Aggiungere definizioni brevi per almeno questi termini:

```text
HCI
IUUMM
Ergonomia
Ergonomia cognitiva
Sistema interattivo
Interfaccia
Task
Usabilità
Efficacia
Efficienza
Soddisfazione
Sistema socio-tecnico
STS thinking
Proprietà emergenti
Conseguenze inattese
Effetto Peltzman
Overreliance
Overdependence
Overconfidence
Complacency
Automation bias
Affordance
Mapping
Constraint
Workaround
Skeuomorfismo
User-created affordance
Legge di Fitts
Errori di giustapposizione
Multifunzionalità
Low use
Euristica
Valutazione euristica
Valutazione olistica
Valutazione task-oriented
Think-aloud protocol
Severità
Prioritizzazione
Dark pattern
Captologia
Semiotica
Segno
Simbolo
Icona
Indice
Significante
Significato
Metacomunicazione
```

Formato:

```md
## Termine

Definizione breve.

Fonte: [[Appunti IUM 2021]]

Stato: `da-verificare`
```

---

## 10. Domande d'esame derivate

Creare o aggiornare:

```text
kb/05_Domande_Esame/Domande derivate da Appunti IUM 2021.md
```

Le domande devono essere generate a partire dai concetti, senza inventare risposte non supportate.

Formato:

```md
---
type: domande
course: IUM
source: "[[Appunti IUM 2021]]"
status: da-verificare
tags:
  - ium
  - domande-esame
---

# Domande derivate da Appunti IUM 2021

## Concetti base

### Che cos'è l'Interazione Uomo-Macchina?

> [!answer] Risposta sintetica
> ...

Fonte: [[HCI - Interazione Uomo-Macchina]]

---

### Perché l'usabilità non è una proprietà intrinseca del sistema?

> [!answer] Risposta sintetica
> ...

Fonte: [[Usabilità]]
```

Codex deve produrre almeno:

- 10 domande sui concetti base;
- 10 domande su affordance/mapping/constraint/usabilità;
- 10 domande su valutazione euristica e quantitativa;
- 5 domande su sistemi socio-tecnici e conseguenze inattese;
- 5 domande su semiotica/persuasione/dark patterns, anche se marcate come da completare.

---

## 11. Gestione conflitti e informazioni incerte

Creare o aggiornare:

```text
kb/99_Da_Verificare/Dubbi e conflitti fonti.md
```

Ogni dubbio deve essere registrato così:

```md
## Titolo dubbio

- Fonte: [[Appunti IUM 2021]]
- Concetto collegato: [[Nome concetto]]
- Tipo: definizione incompleta / possibile errore / conflitto futuro / esempio poco chiaro
- Descrizione: ...
- Azione richiesta: verificare con appunti collettivi 2024-25, appunti 2022 o domande note.
```

Possibili elementi da marcare subito come da verificare:

- definizioni molto colloquiali o poco formali;
- esempi storici o numerici;
- formule riportate senza contesto;
- parti specifiche del progetto d'esame 2020-2021, perché potrebbero non valere più per l'esame attuale;
- nomi di standard/principi se riportati in modo incompleto;
- temi avanzati presenti solo nell'indice ma non ancora ben sviluppati.

---

## 12. Separazione tra esame scritto e progetto

Poiché questa repo serve allo **scritto teorico**, Codex deve distinguere chiaramente:

1. concetti teorici utili per l'esame;
2. dettagli pratici del progetto 2020-2021;
3. procedure di valutazione utili sia per progetto che per teoria;
4. informazioni obsolete sul progetto.

Creare eventualmente:

```text
kb/99_Da_Verificare/Info progetto potenzialmente obsolete.md
```

E spostarci/registrare lì informazioni come:

- numeri specifici di partecipanti richiesti nel 2020-2021;
- istruzioni di consegna del progetto di quell'anno;
- indicazioni legate a slide o relazione di progetto;
- riferimenti a modalità d'esame/progetto non più attuali.

Non eliminarle completamente: possono essere utili come contesto, ma non devono confondersi con la teoria da ricordare.

---

## 13. Report finale dell'analisi del file

Creare:

```text
ai/reports/2021_appunti_ium_analysis_report.md
```

Formato:

```md
---
type: report_ai
source: "[[Appunti IUM 2021]]"
status: completed
---

# Report analisi — Appunti IUM 2021

## Fonte analizzata

- Nome: Appunti IUM 2021
- Tipo: appunti studenti
- Anno: 2020-2021
- Affidabilità: media-bassa
- Stato: prima integrazione

## Sintesi contenuto

Breve sintesi dei macro-argomenti coperti.

## Note create

| Nota | Tipo | Stato |
|---|---|---|
| [[HCI - Interazione Uomo-Macchina]] | concetto | da-verificare |
| ... | ... | ... |

## Note aggiornate

| Nota | Modifica |
|---|---|
| ... | ... |

## Domande generate

| Sezione | Numero domande |
|---|---:|
| Concetti base | ... |
| Valutazione | ... |

## Dubbi registrati

| Dubbio | Azione richiesta |
|---|---|
| ... | ... |

## Prossimo step consigliato

Analizzare il prossimo asset e confrontarlo con le note create da questa fonte.
```

---

## 14. Aggiornamento README

Aggiornare `README.md` con una sezione:

```md
## Stato knowledge base

### Fonti integrate

- [x] Appunti IUM 2021 — prima estrazione e creazione note base
- [ ] Appunti IUM 2022
- [ ] Appunti collettivi 2024-25
- [ ] Appunti collettivi 2025-26
- [ ] Domande note

### Metodo di lavoro

Ogni fonte viene analizzata separatamente. Le informazioni vengono prima inserite come `da-verificare`, poi consolidate quando confermate da più fonti o dalle domande note.
```

---

## 15. Checklist finale per Codex

Prima di terminare, Codex deve verificare:

- [ ] `sources/Appunti IUM 2021.md` creato/aggiornato
- [ ] `sources/Fonti.md` aggiornato
- [ ] `raw/extracted/appunti_ium_2021_extracted.md` creato
- [ ] note concettuali principali create in `kb/02_Concetti/`
- [ ] note metodo create in `kb/03_Metodi/`
- [ ] note euristiche create in `kb/04_Euristiche/`
- [ ] glossario aggiornato
- [ ] mappa concetti aggiornata
- [ ] domande derivate create
- [ ] dubbi/conflitti registrati
- [ ] informazioni pratiche/obsolete del progetto separate dalla teoria
- [ ] report finale creato in `ai/reports/`
- [ ] README aggiornato
- [ ] nessuna fonte raw modificata
- [ ] nessuna nota contiene testo copiato in blocco senza rielaborazione
- [ ] tutti i file Markdown sono leggibili in Obsidian

---

## 16. Prompt operativo consigliato per Codex

Usare questo prompt nella repo:

```text
Analizza il file raw/assets/Appunti IUM 2021.pdf e aggiorna la knowledge base Obsidian seguendo il piano in questo documento.

Obiettivo:
- creare una prima base teorica dell'esame scritto di Interazione Uomo-Macchina;
- estrarre concetti, definizioni, metodi, euristiche e domande potenziali;
- mantenere separati contenuti teorici e dettagli pratici del progetto 2020-2021;
- marcare tutto come da-verificare, dato che la fonte è un appunto studenti con disclaimer;
- produrre un report finale dell'analisi.

Non sovrascrivere contenuti esistenti senza integrarli in modo ragionato.
Non trattare gli appunti 2021 come fonte definitiva.
Mantieni tutti i file Markdown leggibili in Obsidian.
```

---

## 17. Risultato atteso

Alla fine di questo step la repo deve avere:

1. una prima tassonomia completa dei concetti IUM;
2. note atomiche collegate tra loro;
3. una base di domande teoriche per lo scritto;
4. un glossario iniziale;
5. una mappa concettuale navigabile;
6. un registro delle incertezze;
7. un report di cosa è stato fatto.

Questo permetterà, nei prossimi step, di analizzare gli altri file uno per volta e consolidare progressivamente la knowledge base.
