# Workflow - Update Knowledge Base da Report

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
7. Aggiorna `analysis/source_registry.md` marcando l'asset come analizzato.
8. Aggiungi conflitti a `analysis/conflict_log.md`.
9. Aggiungi dubbi a `analysis/pending_questions.md`.
10. Aggiorna `exam_prep/domande_note/` solo se il report contiene domande.
11. Aggiorna `exam_prep/flashcards/ium_flashcards.md` solo con concetti gia consolidati o ad alta priorita.
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
