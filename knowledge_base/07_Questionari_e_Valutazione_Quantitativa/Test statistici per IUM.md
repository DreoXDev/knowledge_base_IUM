---
type: concetto
course: IUM
status: confermato
sources:
  - "[[02_appunti_collettivi_2024_2025]]"
tags:
  - ium
  - concetto
  - statistica
---

# Test statistici per IUM

> [!info] Definizione
> Guida operativa per la selezione del test d'ipotesi corretto in base al tipo di dati raccolti durante la valutazione quantitativa.

## Spiegazione

Negli appunti 2024-25 la scelta del test dipende strettamente dalle **scale di misura** delle variabili.

### Tipi di variabili e scale
- **Categorica / Nominale**: i valori sono etichette senza ordine (es. colore preferito).
- **Ordinale**: i valori hanno un ordine ma la distanza tra loro non è quantificabile in modo oggettivo (es. scale Likert, basso/medio/alto).
- **Numerica a Intervalli**: la differenza tra valori è misurabile, ma lo zero è arbitrario (es. temperatura).
- **Numerica a Rapporti**: zero assoluto, si possono fare rapporti (es. tempo di completamento, numero di errori).

> [!warning] Avviso
> In IUM, non si dovrebbe calcolare la media di variabili ordinali (es. Likert 1-5) a meno che non vi sia una forte giustificazione. È preferibile usare la **mediana** o la **moda**.

## Tabella Operativa dei Test

| Tipo di variabile dipendente | Confronto tra 2 gruppi indipendenti | Confronto tra 3+ gruppi indipendenti |
| :--- | :--- | :--- |
| **Numerica (Continua)** | T di Student | ANOVA |
| **Ordinale** | Mann-Whitney (o Wilcoxon se dati appaiati) | Kruskal-Wallis (o Friedman se dati appaiati) |
| **Discreta/Dicotomica/Nominale** | Chi quadro (o test binomiale se 2 categorie) | Chi quadro |

*Nota: per la valutazione assoluta su scala psicometrica (passa/non passa) si confrontano risposte positive/negative con test binomiale o si confrontano gli **intervalli di confidenza**.*

## Collegamenti

- [[Intervallo di confidenza]]
- [[Significativita statistica e pratica]]
- [[Valutazione quantitativa]]

## Conferma e consolidamento

> [!success] Stato
> Concetto estratto da `Appunti collettivi 2024-25`.

## Fonti interne

- [[02_appunti_collettivi_2024_2025]]
