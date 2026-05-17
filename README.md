# Knowledge Base IUM

Vault Obsidian per la preparazione della parte teorica dell'esame di Interazione Uomo-Macchina.

La repo separa:

- asset originali;
- report di analisi;
- knowledge base consolidata;
- materiale di ripasso per l'esame.

## Struttura principale

- `assets/raw/`: asset originali non modificabili.
- `analysis/reports/`: report prodotti dopo l'analisi di un singolo asset.
- `knowledge_base/`: note consolidate per lo studio.
- `exam_prep/`: domande, flashcard, simulazioni e checklist.
- `templates/`: modelli Markdown per mantenere coerenza.
- `workflows/`: procedure operative per AI e Codex.

## Uso in Obsidian

Aprire questa cartella come vault Obsidian. Le note usano link interni `[[...]]`, callout standard e Markdown semplice, senza dipendenze da plugin non essenziali.

## Workflow consigliato

1. Importare un asset in `assets/raw/`.
2. Analizzarlo con ChatGPT.
3. Salvare il report in `analysis/reports/`.
4. Usare Codex per aggiornare le note in `knowledge_base/`.
5. Aggiornare domande, flashcard e checklist in `exam_prep/`.

Gli asset raw non vanno modificati e non vanno copiati direttamente nella knowledge base senza un report di analisi.

## Stato knowledge base

### Fonti integrate

- [x] Appunti IUM 2021 - prima estrazione e creazione note base
- [x] Appunti IUM 2022 - conferma concetti 2021 e integrazione dettagli

### Fonti in lavorazione

- [ ] Nessuna

### Fonti da analizzare

- [ ] Appunti collettivi 2024-25
- [ ] Appunti collettivi 2025-26
- [ ] Domande note

### Metodo di lavoro

Ogni fonte viene analizzata separatamente. Le informazioni vengono prima inserite come `DA VERIFICARE`, poi consolidate quando confermate da più fonti o dalle domande note. I dettagli progettuali specifici di un anno vengono separati dalla teoria dello scritto.
