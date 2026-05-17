# Workflow - Import Asset

## Obiettivo

Inserire un nuovo asset nella repo senza alterarlo e renderlo tracciabile.

## Procedura

1. Copiare il file originale in una sottocartella di `assets/raw/`.
2. Non rinominare il file se il nome originale e utile per riconoscerlo.
3. Aggiungere o aggiornare una riga in `analysis/source_registry.md`.
4. Assegnare un ID fonte stabile.
5. Lasciare `Stato analisi` su `Da analizzare` finche non esiste un report.

## Regole

- Non modificare il contenuto degli asset raw.
- Non estrarre concetti direttamente dall'asset per la knowledge base.
- Se l'asset e duplicato o ambiguo, registrare il dubbio in `analysis/pending_questions.md`.
