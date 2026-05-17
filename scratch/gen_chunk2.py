import os

data = [
    {"id": "Q025", "tema": "Semiotica e Persuasione", "q": "La teoria CASA riguarda?", "a": "Computers Are Social Actors (CASA): la teoria secondo cui gli esseri umani tendono in modo naturale e inconsapevole a considerare i computer e le interfacce come attori sociali autonomi, trattandoli con cortesia o rabbia, senza pensare di star comunicando con gli sviluppatori.", "kb": "[[CASA]]", "tag": "ium flashcard concetti-avanzati persuasione casa"},
    {"id": "Q026", "tema": "Semiotica e Persuasione", "q": "La captologia (o captology) riguarda...", "a": "Lo studio dei computer come tecnologie persuasive. Include l'analisi, la progettazione e la teoria di come i sistemi informatici possano essere utilizzati per cambiare deliberatamente le attitudini e i comportamenti degli utenti.", "kb": "[[Captologia]]", "tag": "ium flashcard concetti-avanzati persuasione captologia"},
    {"id": "Q027", "tema": "Semiotica e Persuasione", "q": "Cos'è l'ethopoeia?", "a": "È l'attribuzione diretta di attitudini, intenzioni, disposizioni e comportamenti tipicamente umani alle macchine. Si distingue dall'antropomorfizzazione perché l'ethopoeia riguarda il comportamento, non necessariamente la forma fisica o visiva.", "kb": "[[Ethopoeia]]", "tag": "ium flashcard concetti-avanzati persuasione ethopoeia"},
    {"id": "Q028", "tema": "Semiotica e Persuasione", "q": "In semiotica, il livello pragmatico è quello...", "a": "Che si concentra sulla relazione tra i segni e gli effetti che essi producono nel mondo reale o sulle persone. Studia il segno come prassi (l'intenzione comunicativa e l'effetto dell'interazione).", "kb": "[[Sintassi semantica pragmatica]], [[Semiotica]]", "tag": "ium flashcard concetti-avanzati semiotica pragmatica"},
    {"id": "Q029", "tema": "Semiotica e Persuasione", "q": "In semiotica un simbolo è...", "a": "Un segno in cui la relazione tra il significante (la forma percepibile) e il significato (il concetto) è completamente arbitraria e convenzionale, non basata sulla somiglianza. Deve quindi essere appresa culturalmente (es. la parola 'cane' o un semaforo rosso).", "kb": "[[Segno simbolo icona indice]]", "tag": "ium flashcard concetti-avanzati semiotica simbolo"},
    {"id": "Q030", "tema": "Semiotica e Persuasione", "q": "In semiotica una deﬁnizione suﬃcientemente precisa di icona è...", "a": "Un segno in cui il significante è percepito come una chiara imitazione del significato, mantenendo una somiglianza visiva, sonora o fisica (es. l'icona di una stampante o della lente di ingrandimento).", "kb": "[[Segno simbolo icona indice]]", "tag": "ium flashcard concetti-avanzati semiotica icona"},
    {"id": "Q031", "tema": "Semiotica e Persuasione", "q": "In semiotica l'abduzione è:", "a": "Il ragionamento abduttivo è il processo attraverso il quale gli individui generano la migliore ipotesi possibile per interpretare elementi o segni incompleti della realtà che li circonda.", "kb": "[[Abduzione]]", "tag": "ium flashcard concetti-avanzati semiotica abduzione"},
    {"id": "Q032", "tema": "Semiotica e Persuasione", "q": "Per Peirce, la semiosi è...", "a": "Il processo infinito attraverso cui un segno produce significato. Implica un ragionamento abduttivo continuo in cui generiamo ipotesi per interpretare la realtà, le mettiamo alla prova e, se confermate, diventano regole generali; altrimenti rivediamo le nostre convinzioni.", "kb": "[[Semiosi]], [[Peirce]]", "tag": "ium flashcard concetti-avanzati semiotica semiosi"},
    {"id": "Q033", "tema": "Semiotica e Persuasione", "q": "Quali sono le motivazioni intrinseche e umane supportate da una tecnologia mobile?", "a": "Solitamente, l'uso in mobilità supporta motivazioni psicologiche intrinseche (come autonomia, competenza e relazionalità previste dalla Self-Determination Theory) o bisogni fondamentali di socialità e reperimento di informazioni on-the-go.", "kb": "[[Tecnologie persuasive]]", "tag": "ium flashcard concetti-avanzati persuasione"},
    {"id": "Q034", "tema": "Valutazione Qualitativa", "q": "Il paradosso dell'utente attivo (active user paradox) si veriﬁca quando...", "a": "L'utente desidera concentrarsi immediatamente sul proprio task procedendo per tentativi ed errori (learning by doing), rifiutandosi attivamente di spendere tempo per leggere manuali o studiare preventivamente il funzionamento del sistema.", "kb": "[[Usabilità]]", "tag": "ium flashcard valutazione-qualitativa paradosso"},
    {"id": "Q035", "tema": "Valutazione Qualitativa", "q": "Riguardo alla valutazione qualitativa dell'usabilità di un sistema operativo, quale affermazione è corretta?", "a": "Nella valutazione euristica il risultato atteso è un elenco di problemi di usabilità, pesati per livello di gravità (severità) e collegati al principio o euristica che è stata violata.", "kb": "[[Valutazione euristica]]", "tag": "ium flashcard valutazione-qualitativa euristica"},
    {"id": "Q036", "tema": "Valutazione Qualitativa", "q": "Se il sistema offre il comando di FLIP-UNDO cosa succede?", "a": "Un comando di Flip-Undo tratta l'azione di 'Undo' come qualsiasi altro comando modificabile. Quindi, eseguire un 'Undo' subito dopo un altro 'Undo' annulla l'effetto del primo, ripristinando di fatto l'azione originale (funziona come un Redo involontario).", "kb": "[[Valutazione euristica]]", "tag": "ium flashcard valutazione-qualitativa undo"},
    {"id": "Q037", "tema": "Valutazione Qualitativa", "q": "Diffusione del fenomeno del daltonismo", "a": "Il daltonismo colpisce circa il 2-8% della popolazione (principalmente maschile). Per questo, in base alle regole di accessibilità e usabilità, è fondamentale non usare il solo colore come mezzo per trasmettere informazioni critiche o distinguere stati.", "kb": "[[Usabilità]], [[Accessibilità]]", "tag": "ium flashcard valutazione-qualitativa accessibilita"},
    {"id": "Q038", "tema": "Valutazione Qualitativa", "q": "Un sistema modale è un sistema che...", "a": "A fronte di una stessa azione o comando compiuto da un utente (es. premere un tasto), reagisce in modo diverso a seconda del 'modo' (stato o modalità) in cui il sistema si trova in quel momento (es. CAPS LOCK attivato).", "kb": "[[Valutazione euristica]]", "tag": "ium flashcard valutazione-qualitativa sistema modale"},
    {"id": "Q039", "tema": "Valutazione Qualitativa", "q": "L'output di una valutazione euristica è un elenco di...", "a": "Un elenco di problemi di usabilità identificati dagli ispettori, categorizzati in base all'euristica violata e prioritizzati assegnando loro un grado di severità (impatto, frequenza, persistenza).", "kb": "[[Valutazione euristica]], [[Prioritizzazione problemi di usabilità]]", "tag": "ium flashcard valutazione-qualitativa output"}
]

with open('exam_prep/domande/domande_note_validate.md', 'a', encoding='utf-8') as fd, \
     open('exam_prep/flashcards/IUM_domande_flashcards.md', 'a', encoding='utf-8') as ff, \
     open('exam_prep/flashcards/IUM_domande_flashcards_anki.tsv', 'a', encoding='utf-8') as fa:

    for item in data:
        fd.write(f"## {item['id']} — {item['tema']}\n\n")
        fd.write(f"> [!Question]\n> {item['q']}\n\n")
        if item['id'] == 'Q033':
            fd.write(f"**Risposta validata:**  \n{item['a']}\n\n")
            fd.write("**Stato:** da verificare / copertura parziale nella KB\n\n")
        else:
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

print("Chunk 2 written successfully.")
