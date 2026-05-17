import os

os.makedirs('exam_prep/domande', exist_ok=True)
os.makedirs('exam_prep/flashcards', exist_ok=True)

data = [
    {"id": "Q001", "tema": "Fondamenti HCI", "q": "Una deﬁnizione accettabile di ergonomia può essere?", "a": "L'ergonomia è lo studio delle attività umane e dell'interazione tra persone e strumenti per l'elaborazione dell'informazione. L'ergonomia cognitiva considera processi come percezione, attenzione, memoria e pensiero per progettare strumenti adatti alle capacità e ai limiti degli utenti.", "kb": "[[Ergonomia cognitiva]], [[Human-Computer Interaction]]", "tag": "ium flashcard concetti-base ergonomia"},
    {"id": "Q002", "tema": "Fondamenti HCI", "q": "L'usabilità di un sistema...", "a": "È il grado in cui un prodotto può essere usato da determinati utenti per raggiungere determinati obiettivi con efficacia, efficienza e soddisfazione in uno specifico contesto d'uso. Non è una proprietà intrinseca del sistema ma dipende dall'interazione reale.", "kb": "[[Usabilità]]", "tag": "ium flashcard concetti-base usabilita"},
    {"id": "Q003", "tema": "Fondamenti HCI", "q": "A cosa si riferisce l'ISO 9241 quando parla dell'insieme di componenti di un sistema interattivo che forniscono all'utente informazioni e gli permettono di effettuare specifici compiti?", "a": "All'interfaccia. Essa funge da punto di incontro e comunicazione bidirezionale tra l'utente (che ha degli obiettivi) e il sistema computazionale.", "kb": "[[Interfaccia]], [[Sistema interattivo]]", "tag": "ium flashcard concetti-base interfaccia"},
    {"id": "Q004", "tema": "Affordance e Mapping", "q": "Un mapping è...", "a": "La relazione progettuale (mappatura) tra un controllo, l'azione che esso 'afforda' (suggerisce di fare) e l'effetto che tale azione avrà nel mondo reale o applicativo.", "kb": "[[Mapping]]", "tag": "ium flashcard concetti-base mapping"},
    {"id": "Q005", "tema": "Affordance e Mapping", "q": "Il concetto di affordance indica...", "a": "Una qualsiasi proprietà fisica o percepita di un oggetto che ne definisce i possibili usi o invita una persona all'azione, suggerendo chiaramente come dovrebbe essere usato.", "kb": "[[Affordance]]", "tag": "ium flashcard concetti-base affordance"},
    {"id": "Q006", "tema": "Affordance e Mapping", "q": "Come abbiamo deﬁnito una affordance?", "a": "Oltre a invitare visivamente o simbolicamente a un'azione, un'affordance ben progettata suggerisce anche il possibile effetto che quell'azione avrà sul mondo (rendendo chiaro a cosa serve).", "kb": "[[Affordance]]", "tag": "ium flashcard concetti-base affordance"},
    {"id": "Q007", "tema": "Affordance e Mapping", "q": "Un constraint è...", "a": "Un vincolo progettuale che limita l'azione dell'utente guidandolo verso l'uso corretto. Può essere fisico, logico, semantico o culturale, e serve a prevenire errori chiudendo percorsi errati.", "kb": "[[Constraints]]", "tag": "ium flashcard concetti-base constraint"},
    {"id": "Q008", "tema": "Affordance e Mapping", "q": "Un'interfaccia skeuomorﬁca è...", "a": "Un'interfaccia grafica progettata con elementi ornamentali e visivi che ricordano pesantemente le strutture e i materiali degli oggetti fisici corrispondenti (es. una calcolatrice digitale con ombre ed effetto metallo, o una cartella di finta pelle).", "kb": "[[Skeuomorfismo]]", "tag": "ium flashcard concetti-base skeuomorfismo"},
    {"id": "Q009", "tema": "Affordance e Mapping", "q": "Una affordance cognitiva dipende...", "a": "È un tipo di affordance progettata per aiutare gli utenti nelle loro azioni cognitive, facilitando processi come pensare, decidere, imparare o ricordare.", "kb": "[[Affordance]]", "tag": "ium flashcard concetti-base affordance cognitiva"},
    {"id": "Q010", "tema": "Bias e Automazione", "q": "Quale frase è più corretta riguardo all'automation bias?", "a": "L'automation bias è l'eccessiva fiducia riposta nelle risposte di un supporto automatico. Porta a errori di omissione (non notare un problema) e di commissione (seguire attivamente un consiglio sbagliato della macchina).", "kb": "[[Automation bias]]", "tag": "ium flashcard concetti-base automazione"},
    {"id": "Q011", "tema": "Bias e Automazione", "q": "L'overconﬁdence è...", "a": "La sovraconfidenza, ovvero pensare che il sistema non andrà mai giù, non produrrà mai output scorretti o che dal suo uso non deriverà mai un danno.", "kb": "[[Overconfidence]]", "tag": "ium flashcard concetti-base bias"},
    {"id": "Q012", "tema": "Usabilità e Design", "q": "Gli errori di giustapposizione sono...", "a": "Errori di usabilità causati da un errato design dell'interfaccia che posiziona comandi opposti o critici troppo vicini tra loro, favorendo clic accidentali (es. pulsante 'Salva' adiacente a 'Elimina').", "kb": "[[Errori di giustapposizione]]", "tag": "ium flashcard concetti-base errori"},
    {"id": "Q013", "tema": "Bias e Automazione", "q": "Se un utente è convinto che il sistema che sta usando non potrà mai andare giù o produrre output scorretti, di quale bias si parla?", "a": "Overconfidence (sovraconfidenza).", "kb": "[[Overconfidence]]", "tag": "ium flashcard concetti-base bias"},
    {"id": "Q014", "tema": "Bias e Automazione", "q": "Se la maggior parte delle persone non sapesse eseguire un compito qualora il supporto smettesse di funzionare si parlerebbe di...", "a": "Overdependence (sovradipendenza), un fenomeno che porta alla perdita progressiva di abilità umane (deskilling) per eccessivo affidamento alla macchina.", "kb": "[[Overdependence]]", "tag": "ium flashcard concetti-base bias"},
    {"id": "Q015", "tema": "Bias e Automazione", "q": "La complacency riguarda...", "a": "Il rilassamento dell'attenzione. L'utente dà per scontato che il sistema funzionerà sempre correttamente e smette di vigilare per individuare eventuali anomalie.", "kb": "[[Complacency]]", "tag": "ium flashcard concetti-base bias"},
    {"id": "Q016", "tema": "Usabilità e Design", "q": "La toilette di Floyd è il caso in cui...", "a": "Si tende a complicare un'operazione semplice, pretendendo che basti scrivere una lunga procedura testuale per renderla ovvia all'utente, ignorando le carenze di base del design.", "kb": "[[Floyd toilet]]", "tag": "ium flashcard concetti-base usabilita"},
    {"id": "Q017", "tema": "Usabilità e Design", "q": "Una porta di Norman è...", "a": "Un oggetto progettato male la cui affordance visiva invita a compiere l'azione opposta a quella richiesta (es. una maniglione da tirare che in realtà va spinto), costringendo a usare cartelli compensativi.", "kb": "[[Norman doors]]", "tag": "ium flashcard concetti-base usabilita"},
    {"id": "Q018", "tema": "Usabilità e Design", "q": "I sistemi “wake up and use” sono quelli che...", "a": "Sono così auto-esplicativi che un utente può usarli in modo efficace fin dalla primissima volta, senza alcun addestramento o lettura di manuali.", "kb": "[[Usabilità]]", "tag": "ium flashcard concetti-base usabilita"},
    {"id": "Q019", "tema": "Complessità", "q": "Un coltellino svizzero ha...", "a": "Alta complessità funzionale (fa tantissime cose), bassa complessità strutturale (è facile capire come è fatto meccanicamente) e alta complessità d'uso (usarlo è scomodo rispetto allo strumento dedicato).", "kb": "[[Complessita d'uso strutturale funzionale]]", "tag": "ium flashcard concetti-base complessita"},
    {"id": "Q020", "tema": "Complessità", "q": "Un orologio meccanico da parete ha...", "a": "Alta complessità strutturale (tantissimi ingranaggi interdipendenti), bassa complessità funzionale (segna solo l'ora) e bassa complessità d'uso (basta guardarlo).", "kb": "[[Complessita d'uso strutturale funzionale]]", "tag": "ium flashcard concetti-base complessita"},
    {"id": "Q021", "tema": "Sistemi Socio-Tecnici", "q": "Un sistema socio-tecnico è:", "a": "Un sistema in cui la componente umana/sociale e quella tecnica sono inestricabilmente legate. L'interazione tra queste componenti genera proprietà emergenti e conseguenze imprevedibili che non appartengono alle singole parti.", "kb": "[[Sistema socio-tecnico]], [[Proprietà emergenti]]", "tag": "ium flashcard concetti-base socio-tecnico"},
    {"id": "Q022", "tema": "Affordance e Mapping", "q": "L'affordance cognitiva sono quelle che...", "a": "Aiutano gli utenti nelle loro azioni cognitive (pensare, decidere, imparare, ricordare).", "kb": "[[Affordance]]", "tag": "ium flashcard concetti-base affordance"},
    {"id": "Q023", "tema": "Usabilità e Design", "q": "Nel paradigma “alert, identify, direct”, alert signiﬁca...", "a": "Costituisce il primo livello di feedback e avverte semplicemente l'utente che 'qualcosa non va', notificando la presenza di un errore o stato anomalo.", "kb": "[[Feedback]]", "tag": "ium flashcard concetti-base feedback"},
    {"id": "Q024", "tema": "Usabilità e Design", "q": "Nel paradigma “alert, identify, direct”, direct signiﬁca...", "a": "È l'ultimo livello di gestione dell'errore: fornisce all'utente le istruzioni o l'azione diretta ('fai questo') per risolvere attivamente il problema appena identificato.", "kb": "[[Feedback]]", "tag": "ium flashcard concetti-base feedback"}
]

with open('exam_prep/domande/domande_note_validate.md', 'a', encoding='utf-8') as fd, \
     open('exam_prep/flashcards/IUM_domande_flashcards.md', 'a', encoding='utf-8') as ff, \
     open('exam_prep/flashcards/IUM_domande_flashcards_anki.tsv', 'a', encoding='utf-8') as fa:

    for item in data:
        # Domande
        fd.write(f"## {item['id']} — {item['tema']}\n\n")
        fd.write(f"> [!Question]\n> {item['q']}\n\n")
        fd.write(f"**Risposta validata:**  \n{item['a']}\n\n")
        fd.write(f"**Note KB collegate:**\n")
        for kb in item['kb'].split(", "):
            fd.write(f"- {kb}\n")
        fd.write("\n**Stato:** validata\n\n---\n\n")

        # Flashcards
        ff.write(f"## FC-{item['id']} — {item['tema']}\n\n")
        ff.write(f"**Domanda**  \n{item['q']}\n\n")
        ff.write(f"**Risposta**  \n{item['a']}\n\n")
        ff.write(f"**Tag:** {' '.join(['#'+t for t in item['tag'].split()])}\n\n---\n\n")

        # TSV
        q_br = item['q'].replace('\n', '<br>')
        a_br = item['a'].replace('\n', '<br>')
        fa.write(f"{item['id']}\t{q_br}\t{a_br}\t{item['tag']}\n")

print("Chunk 1 written successfully.")
