# Codex Instructions

## Regole fondamentali

1. Non modificare mai i file in `assets/raw/`.
2. Non integrare contenuti nella knowledge base senza un report in `analysis/reports/`.
3. Quando aggiorni una nota, mantieni lo stile Obsidian.
4. Usa link interni `[[...]]` tra concetti correlati.
5. Non duplicare lo stesso contenuto in piu note: crea una nota principale e collegala.
6. Se due fonti sono in conflitto, aggiorna `analysis/conflict_log.md` invece di scegliere arbitrariamente.
7. Se una risposta a una domanda nota non e verificata, marcarla come `DA VERIFICARE`.
8. Ogni nota concettuale deve contenere almeno:
   - definizione;
   - spiegazione breve;
   - esempio;
   - collegamenti;
   - possibili domande d'esame.
9. Non usare emoji nei file Markdown.
10. Scrivi in italiano chiaro, con tono da appunti universitari.

## Stile Markdown

Usa callout Obsidian quando utili:

```md
> [!info] Definizione
> Testo della definizione.

> [!example] Esempio
> Esempio pratico.

> [!warning] Attenzione d'esame
> Errore comune o distinzione importante.

> [!question] Possibile domanda d'esame
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
