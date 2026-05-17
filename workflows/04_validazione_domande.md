# Workflow - Validazione Domande

## Obiettivo

Validare progressivamente le risposte alle domande note usando la knowledge base consolidata.

## Stati risposta

- `VALIDATA`: risposta coerente con note consolidate e fonti attendibili.
- `PROBABILE`: risposta plausibile ma non ancora verificata completamente.
- `DA VERIFICARE`: risposta assente, incompleta o non controllata.
- `POTENZIALMENTE ERRATA`: risposta in conflitto con report o note consolidate.

## Procedura

1. Partire da `exam_prep/domande_note/domande_da_verificare.md`.
2. Collegare ogni domanda ai concetti rilevanti.
3. Confrontare la risposta con le note in `knowledge_base/`.
4. Aggiornare lo stato.
5. Registrare dubbi o conflitti se la validazione non e possibile.
