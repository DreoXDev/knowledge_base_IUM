---
type: concetto
course: IUM
status: confermato
sources:
  - "[[Appunti IUM 2021]]"
  - "[[Appunti IUM 2022]]"
  - "[[02_appunti_collettivi_2024_2025]]"
tags:
  - ium
  - concetto
---

# Prioritizzazione problemi di usabilità

> [!info] Definizione
> Processo per stimare la gravità dei problemi riscontrati e decidere l'ordine in cui devono essere risolti dal team di sviluppo.

## Spiegazione

Non tutti i problemi hanno lo stesso peso. In IUM la severità è classicamente misurata su una scala 0-4.

## Dettagli importanti

La severità si stima considerando tre fattori:
- **Frequenza**: quanti utenti incontreranno il problema.
- **Impatto**: quanto il problema ostacola il task (es. fastidio vs blocco totale).
- **Persistenza**: l'utente impara a superare il problema o ci ricasca ogni volta?

### Scala di Severità 0-4 (Nielsen)
- 0: Non è un problema di usabilità
- 1: Problema cosmetico (risolvere se c'è tempo)
- 2: Problema minore (bassa priorità)
- 3: Problema maggiore (alta priorità)
- 4: Catastrofe di usabilità (da risolvere tassativamente prima del rilascio)

### Elaborazione statistica
Ogni valutatore assegna la sua severità. Per aggregarle **non si usa la media** se si considera la scala come puramente ordinale, ma si preferiscono **mediana**, **moda**, **range interquartile** (per vedere la dispersione del disaccordo).

### Regola Rank 1224
Una tecnica per la prioritizzazione prevede di assegnare pesi. Spesso si risolve circa il 20% dei problemi più gravi (legge di Pareto) che causano l'80% del disagio. Nelle fasi di valutazione assoluta (passa/non passa) si può usare il **test binomiale** per stabilire statisticamente se la percentuale di task completati senza catastrofi supera la soglia accettabile.

## Collegamenti

- [[Valutazione euristica]]
- [[Test binomiale]]
- [[Severita problemi di usabilita]]

## Possibili domande d'esame

> [!question] Domanda
> Su quali fattori si basa la stima della severità di un problema di usabilità?

Risposta attesa:

Sulla frequenza con cui si verifica, sull'impatto che ha sul completamento del task e sulla persistenza nel tempo per l'utente.

## Conferma e consolidamento

> [!success] Stato
> Concetto confermato da fonti 2021, 2022 e 2024-25.

## Fonti interne

- [[Appunti IUM 2021]]
- [[04_appunti_ium_2021]]
- [[05_appunti_ium_2022]]
- [[02_appunti_collettivi_2024_2025]]
