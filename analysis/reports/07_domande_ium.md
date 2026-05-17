# Report 07 — Domande IUM

> [!info] Asset
> Fonte: `Domande IUM.pdf`  
> Tipo: domande note da esami passati  
> Attendibilità risposte originali: media-bassa  
> Uso principale: generazione flashcard e controllo copertura KB

## Sintesi

Il documento PDF raccoglie 82 domande a risposta chiusa e 3 domande a risposta aperta estratte o ricordate dagli studenti negli appelli passati di IUM. Le risposte originali presenti nel file erano in alcuni casi errate (es. la definizione di p-value rispetto ad alpha), ambigue, o costituite da frammenti di appunti incompleti. Questo report certifica l'estrazione e la validazione totale delle domande rispetto alla Knowledge Base teorica.

## Sezioni individuate

| Sezione | Range domande | Tema |
|---|---:|---|
| Concetti di base | 1-24 | HCI, ergonomia, usabilità, affordance, mapping, constraint, STS |
| Concetti avanzati | 25-33 | CASA, captologia, ethopoeia, semiotica |
| Valutazioni qualitative | 34-39 | Valutazione euristica, undo, sistemi modali |
| Valutazioni quantitative | 40-73 | UX, usabilità ISO, inferenza statistica, p-value, NPS, Likert, low use |
| Dark patterns | 74-76 | Trappola per insetti, forced continuity, bait and switch |
| Tecnologie persuasive | 77-82 | Credibilità, Hook model, Fogg behavior model |
| Domande aperte | QA1-QA3 | Usabilità ISO, p-value, intervallo di confidenza |

## Copertura rispetto alla KB

| Tema | Note KB usate | Copertura | Azione |
|---|---|---|---|
| HCI, STS e Base | `Human-Computer Interaction`, `Sistema socio-tecnico`, `Affordance`, `Constraints`, `Bias` | Alta | Riformulate le risposte in modo discorsivo. |
| Questionari e Statistica | `Significativita statistica e pratica`, `NPS`, `Valutazione quantitativa` | Media-Alta | Corretti errori grossolani del PDF (p-value, ABX, stime). |
| Persuasione | `Tecnologie persuasive`, `Dark patterns` | Alta | Confermato. |
| Use consistent | `Low Use` | Bassa | Trovato concetto ambiguo "use consistent" che probabilmente si riferiva al Low Use. |

## Domande problematiche

- **Q033 (Motivazioni intrinseche mobile)**: Non era adeguatamente coperta dalla KB originaria in quei termini esatti, per cui è stata estrapolata la Self-Determination Theory dalle slide generali. Marcata `DA VERIFICARE`.
- **Q045 / QA02 (p-value)**: Il PDF confondeva il p-value con l'errore di Tipo I (alfa). Riscritto interamente basandosi sulle definizioni statistiche rigorose per evitare bocciature.
- **Q068 (Problemi non trovati)**: L'esempio di formula è stato espanso e chiarito matematicamente per dimostrare il limite tendente a 0.
- **Q072 (Use consistent)**: Riferimento non standard, mappato sul Low Use e tenuto in standby.

## Decisioni di integrazione

Per ogni domanda è stata creata una nota di risposta estesa validata in `exam_prep/domande/domande_note_validate.md`. Contestualmente, per facilitare il ripasso, sono state autogenerate 85 flashcard in `exam_prep/flashcards/IUM_domande_flashcards.md` e convertite nel formato TSV compatibile con l'importazione rapida per Anki (`exam_prep/flashcards/IUM_domande_flashcards_anki.tsv`).
