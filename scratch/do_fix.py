import os
import sys
sys.path.append('scratch')
import importlib.util

# 1. Load data
all_data = []
for i in range(1, 5):
    file_path = f'scratch/gen_chunk{i}.py'
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    # Remove file writing part to prevent duplication
    code = code.split("with open(")[0]
    exec(code)
    all_data.extend(data)

# Ensure directories exist
os.makedirs('exam_prep/domande_note', exist_ok=True)
os.makedirs('exam_prep/flashcards', exist_ok=True)
os.makedirs('analysis/reports', exist_ok=True)

# 2. Write domande_chiuse.md and domande_aperte.md
with open('exam_prep/domande_note/domande_chiuse.md', 'w', encoding='utf-8') as fc, \
     open('exam_prep/domande_note/domande_aperte.md', 'w', encoding='utf-8') as fa, \
     open('exam_prep/flashcards/IUM_domande_flashcards.md', 'w', encoding='utf-8') as ff:

    fc.write("# Domande Chiuse\n\n")
    fa.write("# Domande Aperte\n\n")
    ff.write("# Flashcards IUM (Domande Note)\n\n")

    for item in all_data:
        is_open = item['id'].startswith('QA')
        file_target = fa if is_open else fc
        target_file_name = "domande_aperte" if is_open else "domande_chiuse"
        
        # ID reformatting (e.g. Q001 -> Q-001, QA01 -> Q-A01)
        if is_open:
            new_id = "Q-A" + item['id'][2:]
        else:
            new_id = "Q-" + item['id'][1:]

        # Handle stato
        stato = "VALIDATA"
        if item['id'] == 'Q033':
            stato = "DA VERIFICARE"
            note = "La risposta originale mancava, usata teoria parziale da KB."
        elif item['id'] == 'Q072':
            stato = "DA VERIFICARE"
            note = "Termine 'use consistent' non standard, ricondotto al Low Use."
        else:
            note = "Risposta validata contro la KB consolidata."

        if item['id'] in ['Q045', 'Q046', 'Q066', 'Q068', 'Q069', 'Q070', 'QA02']:
            note += " Risposta originale potenzialmente incompleta o errata, corretta con la KB."

        # Markdown Domanda
        file_target.write(f"## {new_id} — {item['tema']}\n\n")
        file_target.write(f"**Tipo:** {'aperta' if is_open else 'chiusa'}  \n")
        file_target.write(f"**Fonte:** SRC-DOM-001  \n")
        if not is_open:
            file_target.write(f"**Macroarea:** {item['tema']}  \n")
        file_target.write(f"**Stato risposta:** {stato}  \n")
        file_target.write(f"**Concetti collegati:** {item['kb']}\n\n")
        file_target.write(f"### Domanda\n\n{item['q']}\n\n")
        file_target.write(f"### Risposta corretta\n\n{item['a']}\n\n")
        file_target.write(f"### Spiegazione\n\nConcetto derivato dalle note della KB.\n\n")
        file_target.write(f"### Note di validazione\n\n{note}\n\n---\n\n")

        # Markdown Flashcard
        ff.write(f"## FC-{new_id} — {item['tema']}\n\n")
        ff.write(f"**Domanda:** {item['q']}\n\n")
        ff.write(f"**Risposta:** {item['a']}\n\n")
        ff.write(f"**Collegata a:** [[domande_note/{target_file_name}#{new_id} — {item['tema']}]]\n\n---\n\n")

print("Files generated successfully.")
