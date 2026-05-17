import os

data = [
    {"id": "Q074", "tema": "Dark Patterns", "q": "Il dark pattern 'trappola per insetti' (Roach Motel) cosa prevede?", "a": "È un design che rende facilissimo entrare in una situazione (es. sottoscrivere un abbonamento, creare un account) ma rende intenzionalmente molto difficile e frustrante uscirne (nascondendo pulsanti, richiedendo email, iterazioni infinite).", "kb": "[[Dark patterns]]", "tag": "ium flashcard dark-patterns roach-motel"},
    {"id": "Q075", "tema": "Dark Patterns", "q": "Il Dark Pattern “Forced Continuity” (continuazione forzata) prevede...", "a": "L'utente accetta una prova gratuita fornendo la carta di credito. Al termine della prova, il sistema fa scattare l'addebito ricorrente silenziosamente, senza un avviso o un promemoria chiaro e tempestivo, sperando nell'inerzia e dimenticanza dell'utente.", "kb": "[[Dark patterns]]", "tag": "ium flashcard dark-patterns forced-continuity"},
    {"id": "Q076", "tema": "Dark Patterns", "q": "Bait and switch", "a": "L'utente compie un'azione nota aspettandosi un certo risultato (l'esca/bait), ma il sistema esegue un'azione completamente diversa e indesiderata (lo scambio/switch). Esempio classico: premere la X per chiudere la finestra e, invece, installare o accettare l'aggiornamento.", "kb": "[[Dark patterns]]", "tag": "ium flashcard dark-patterns bait-and-switch"},
    {"id": "Q077", "tema": "Tecnologie Persuasive", "q": "I 4 tipi di credibilità", "a": "Secondo BJ Fogg: Presunta (assunzioni generali, es. un brand noto), Di superficie o Surface (giudizio immediato basato su estetica e design), Reputazione o Reputed (giudizio di terzi, es. recensioni) e Guadagnata o Earned (basata sull'esperienza diretta positiva passata).", "kb": "[[Credibilità]], [[Captologia]]", "tag": "ium flashcard tecnologie-persuasive credibilita"},
    {"id": "Q078", "tema": "Tecnologie Persuasive", "q": "Fasi e ordine dell'Hook model", "a": "Il ciclo delle abitudini nei prodotti è composto da 4 fasi: 1. Trigger (Innesco), 2. Action (Azione semplice), 3. Variable Reward (Ricompensa variabile), 4. Investment (Investimento di tempo, dati o sforzo che porta a un nuovo innesco).", "kb": "[[Tecnologie persuasive]]", "tag": "ium flashcard tecnologie-persuasive hook-model"},
    {"id": "Q079", "tema": "Tecnologie Persuasive", "q": "Quale è il signiﬁcato di trigger nel modello Hook?", "a": "È l'innesco o attuatore che spinge l'utente a compiere l'azione (il motore dell'abitudine). Può essere esterno (notifiche, email, CTA) o, con il tempo, diventare puramente interno (stati emotivi, routine).", "kb": "[[Tecnologie persuasive]]", "tag": "ium flashcard tecnologie-persuasive trigger"},
    {"id": "Q080", "tema": "Tecnologie Persuasive", "q": "Secondo il modello di Hook i trigger interni...", "a": "Sono inneschi psicologici in cui l'utente inizia ad associare automaticamente (senza pensiero consapevole) il prodotto al sollievo da uno stato d'animo negativo o di noia. L'abitudine si consolida quando l'emozione stessa diventa il prompt all'azione.", "kb": "[[Tecnologie persuasive]]", "tag": "ium flashcard tecnologie-persuasive trigger interni"},
    {"id": "Q081", "tema": "Tecnologie Persuasive", "q": "Secondo il modello di Fogg l'esame persuasivo ha maggior effetto quando ci concentriamo...", "a": "Nel rendere il comportamento atteso più semplice da eseguire (riduzione dell'attrito). Per Fogg è molto più efficace e veloce facilitare l'abilità (Ability) piuttosto che tentare di aumentare artificialmente la motivazione dell'utente.", "kb": "[[Tecnologie persuasive]]", "tag": "ium flashcard tecnologie-persuasive fogg"},
    {"id": "Q082", "tema": "Tecnologie Persuasive", "q": "Secondo il modello di Fogg, tre variabili devono convergere perché un comportamento target si veriﬁchi, quali?", "a": "Motivazione (volontà), Abilità (capacità o facilità di esecuzione) e un Trigger (l'innesco che suggerisce l'azione). Se manca anche solo uno di questi elementi o si trovano sotto la 'linea di attivazione', il comportamento non avviene.", "kb": "[[Tecnologie persuasive]]", "tag": "ium flashcard tecnologie-persuasive fogg"},
    {"id": "QA01", "tema": "Domande Aperte", "q": "Deﬁnizione di usabilità secondo lo standard ISO 9241", "a": "L'usabilità è definita come il grado con cui un prodotto può essere usato da utenti specificati per raggiungere obiettivi specificati con Efficacia (correttezza e completezza, basso tasso errori), Efficienza (risorse spese) e Soddisfazione (assenza di disagio e atteggiamento positivo) in un determinato contesto d'uso.", "kb": "[[Usabilità]]", "tag": "ium flashcard domande-aperte usabilita"},
    {"id": "QA02", "tema": "Domande Aperte", "q": "Deﬁnizione di p-value di un test di veriﬁca di ipotesi statistica e suo ruolo nelle valutazioni", "a": "Il p-value è il livello di significatività osservato, ovvero la probabilità di ottenere risultati pari o più estremi qualora l'ipotesi nulla fosse vera. Se p-value < alfa (es. 5%), si rigetta H0 in favore di H1. Nell'HCI serve a valutare oggettivamente se le differenze misurate tra due sistemi A e B sono reali, oppure frutto esclusivo del caso.", "kb": "[[Significativita statistica e pratica]]", "tag": "ium flashcard domande-aperte statistica p-value"},
    {"id": "QA03", "tema": "Domande Aperte", "q": "Deﬁnizione di intervallo di conﬁdenza e sua rilevanza nella valutazione di usabilità", "a": "L'intervallo di confidenza è l'intervallo di valori che ha un'alta probabilità fissata (es. 95%) di contenere il vero parametro della popolazione intera, partendo dai dati del nostro campione ristretto. In usabilità è fondamentale perché, potendo testare solo 15-20 utenti, serve a stimare la reale performance globale (margin of error) del sistema e la stabilità del risultato.", "kb": "[[Intervallo di confidenza]], [[Significativita statistica e pratica]]", "tag": "ium flashcard domande-aperte statistica intervalli"}
]

with open('exam_prep/domande/domande_note_validate.md', 'a', encoding='utf-8') as fd, \
     open('exam_prep/flashcards/IUM_domande_flashcards.md', 'a', encoding='utf-8') as ff, \
     open('exam_prep/flashcards/IUM_domande_flashcards_anki.tsv', 'a', encoding='utf-8') as fa:

    for item in data:
        fd.write(f"## {item['id']} — {item['tema']}\n\n")
        fd.write(f"> [!Question]\n> {item['q']}\n\n")
        fd.write(f"**Risposta validata:**  \n{item['a']}\n\n")
        fd.write(f"**Stato:** validata\n\n")
        fd.write(f"**Note KB collegate:**\n")
        for kb in item['kb'].split(", "):
            fd.write(f"- {kb}\n")
        fd.write("---\n\n")

        ff.write(f"## FC-{item['id']} — {item['tema']}\n\n")
        ff.write(f"**Domanda**  \n{item['q']}\n\n")
        ff.write(f"**Risposta**  \n{item['a']}\n\n")
        ff.write(f"**Tag:** {' '.join(['#'+t for t in item['tag'].split()])}\n\n---\n\n")

        q_br = item['q'].replace('\n', '<br>')
        a_br = item['a'].replace('\n', '<br>')
        fa.write(f"{item['id']}\t{q_br}\t{a_br}\t{item['tag']}\n")

print("Chunk 4 written successfully.")
