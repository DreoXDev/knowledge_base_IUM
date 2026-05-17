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

# Complessità strutturale, funzionale e d'uso

> [!info] Definizione
> Tre dimensioni diverse della complessità di un sistema interattivo che il progettista deve bilanciare.

## Spiegazione

Aggiungere funzioni a un sistema aumenta inesorabilmente la sua complessità. La progettazione IUM mira a far sì che un aumento di funzioni non corrisponda a un aumento lineare della difficoltà per l'utente.
In tal senso, **l'interfaccia funge da filtro semplificatore**: riduce la complessità d'uso percepita senza necessariamente alterare la reale complessità strutturale o funzionale del software sottostante.

## Dettagli importanti

- **Complessità strutturale**: numero di componenti interni, moduli, database e le loro relazioni architettoniche.
- **Complessità funzionale**: numero di task e operazioni che il sistema permette di svolgere (es. word processor vs blocco note).
- **Complessità d'uso**: quanto è difficile e oneroso (cognitivamente e fisicamente) per l'utente accedere e utilizzare quelle funzioni.

Un rischio progettuale noto è lo **"show off"**: esporre la complessità strutturale o l'abbondanza funzionale all'utente solo per mostrare "quanto è potente" il sistema, peggiorando così la complessità d'uso e portando a fenomeni come il *low use*.

## Collegamenti

- [[Multifunzionalita]]
- [[Low use]]
- [[Interfaccia]]

## Possibili domande d'esame

> [!question] Domanda
> Qual è la differenza tra complessità funzionale e d'uso?

Risposta attesa:

La complessità funzionale è la quantità di cose che il sistema può fare. La complessità d'uso è lo sforzo richiesto all'utente per farle. Una buona interfaccia filtra la complessità funzionale, mantenendo bassa la complessità d'uso (es. nascondendo funzioni avanzate dietro menu contestuali).

## Conferma e consolidamento

> [!success] Stato
> Concetto confermato da `Appunti IUM 2021`, `AppuntiIUM2022` e `Appunti collettivi 2024-25`.

## Fonti interne

- [[Appunti IUM 2021]]
- [[04_appunti_ium_2021]]
- [[05_appunti_ium_2022]]
- [[02_appunti_collettivi_2024_2025]]
