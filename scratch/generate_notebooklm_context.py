import os
import re

os.makedirs('notebooklm_context', exist_ok=True)

# Helper function to strip Obsidian links: [[Concept|Alias]] -> Alias, [[Concept]] -> Concept
def clean_obsidian_links(text):
    # [[Path/To/File#Header|Link Text]] -> Link Text
    text = re.sub(r'\[\[[^\]|]*\|([^\]]*)\]\]', r'\1', text)
    # [[Path/To/File#Header]] -> Header (or last part)
    def repl(match):
        content = match.group(1)
        if '#' in content:
            content = content.split('#')[-1]
        if '/' in content:
            content = content.split('/')[-1]
        return content
    text = re.sub(r'\[\[([^\]]*)\]\]', repl, text)
    return text

# 1. Consolidate Theory
kb_dir = 'knowledge_base'
theory_subdirs = sorted([d for d in os.listdir(kb_dir) if os.path.isdir(os.path.join(kb_dir, d)) and d != '99_Glossario'])

consolidated_theory = []
consolidated_theory.append("# CORSO DI INTERAZIONE UOMO-MACCHINA (IUM) - TEORIA COMPLETA\n")
consolidated_theory.append("Questo documento raccoglie la teoria ufficiale del corso di Interazione Uomo-Macchina (IUM), organizzata per moduli tematici. È ottimizzato per lo studio tramite modelli linguistici e NotebookLM.\n\n---\n")

for subdir in theory_subdirs:
    dir_path = os.path.join(kb_dir, subdir)
    module_title = subdir.replace('_', ' ')
    # Remove leading numbers from module title if any
    module_title = re.sub(r'^\d+\s+', '', module_title)
    module_title = module_title.title()
    
    consolidated_theory.append(f"\n# MODULO: {module_title}\n\n")
    
    files = sorted([f for f in os.listdir(dir_path) if f.endswith('.md')])
    for file in files:
        file_path = os.path.join(dir_path, file)
        note_title = file[:-3].replace('_', ' ')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove yaml frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
                
        cleaned_content = clean_obsidian_links(content.strip())
        
        consolidated_theory.append(f"## {note_title}\n\n")
        consolidated_theory.append(cleaned_content)
        consolidated_theory.append("\n\n---\n")

with open('notebooklm_context/01_Teoria_Completa_IUM.md', 'w', encoding='utf-8') as out_f:
    out_f.write('\n'.join(consolidated_theory))

print("01_Teoria_Completa_IUM.md generated.")

# 2. Consolidate Questions
questions_data = []

# Read domande_chiuse.md
chiuse_path = 'exam_prep/domande_note/domande_chiuse.md'
if os.path.exists(chiuse_path):
    with open(chiuse_path, 'r', encoding='utf-8') as f:
        chiuse_content = f.read()
else:
    chiuse_content = ""

# Read domande_aperte.md
aperte_path = 'exam_prep/domande_note/domande_aperte.md'
if os.path.exists(aperte_path):
    with open(aperte_path, 'r', encoding='utf-8') as f:
        aperte_content = f.read()
else:
    aperte_content = ""

def parse_domande(content):
    parsed = []
    # Find all ## Q-... sections
    sections = re.split(r'##\s+(Q-A?\d+)\s+—\s+([^\n]+)', content)
    # sections[0] is header before first question
    # then triplets: id, title, content
    i = 1
    while i < len(sections):
        qid = sections[i]
        title = sections[i+1]
        body = sections[i+2]
        i += 3
        
        # Extract Question, Correct Answer, Explanation
        q_match = re.search(r'### Domanda\s*\n*(.*?)\n*(?=###|$)', body, re.DOTALL)
        a_match = re.search(r'### Risposta (?:corretta|da esame)\s*\n*(.*?)\n*(?=###|$)', body, re.DOTALL)
        exp_match = re.search(r'### Spiegazione\s*\n*(.*?)\n*(?=###|$)', body, re.DOTALL)
        
        q = q_match.group(1).strip() if q_match else ""
        a = a_match.group(1).strip() if a_match else ""
        exp = exp_match.group(1).strip() if exp_match else ""
        
        parsed.append({
            "id": qid,
            "title": title,
            "q": q,
            "a": a,
            "exp": exp
        })
    return parsed

chiuse_list = parse_domande(chiuse_content)
aperte_list = parse_domande(aperte_content)

consolidated_questions = []
consolidated_questions.append("# DOMANDE D'ESAME E RISPOSTE VALIDATE DI IUM\n")
consolidated_questions.append("Questo documento raccoglie 82 domande chiuse e 3 domande aperte tratte dagli esami passati del corso di Interazione Uomo-Macchina. Ogni domanda ha una risposta validata e una spiegazione concettuale.\n\n---\n")

consolidated_questions.append("\n## SEZIONE 1: DOMANDE A RISPOSTA CHIUSA\n\n")
for item in chiuse_list:
    consolidated_questions.append(f"### {item['id']}: {item['title']}\n")
    consolidated_questions.append(f"**DOMANDA:**\n{item['q']}\n\n")
    consolidated_questions.append(f"**RISPOSTA CORRETTA (VALIDATA):**\n{item['a']}\n\n")
    if item['exp']:
        consolidated_questions.append(f"**SPIEGAZIONE:**\n{item['exp']}\n\n")
    consolidated_questions.append("---\n\n")

consolidated_questions.append("\n## SEZIONE 2: DOMANDE A RISPOSTA APERTA\n\n")
for item in aperte_list:
    consolidated_questions.append(f"### {item['id']}: {item['title']}\n")
    consolidated_questions.append(f"**DOMANDA:**\n{item['q']}\n\n")
    consolidated_questions.append(f"**RISPOSTA DA ESAME (VALIDATA):**\n{item['a']}\n\n")
    if item['exp']:
        consolidated_questions.append(f"**SPIEGAZIONE:**\n{item['exp']}\n\n")
    consolidated_questions.append("---\n\n")

with open('notebooklm_context/02_Domande_ed_Esercizi_Esame.md', 'w', encoding='utf-8') as out_f:
    out_f.write(clean_obsidian_links('\n'.join(consolidated_questions)))

print("02_Domande_ed_Esercizi_Esame.md generated.")
