import os
import re
import json

base_dir = r"c:\Users\spart\Streaming de Google Drive\Mi unidad\IFR\ECOEMS\Matemáticas"

files_to_parse = [
    "A) Números y operaciones 🔢.txt",
    "B) Jerarquía y cálculo algebraico básico 🧮.txt",
    "C) Proporcionalidad y porcentajes 💸.txt",
    "D) Álgebra 🧩.txt",
    "E) Ecuaciones y sistemas ✍️.txt",
    "F) Funciones, tablas y gráficas 📊.txt",
    "G) Geometría y medición 📐.txt",
    "H) Estadística y probabilidad 🎲.txt"
]

sections_data = []

exercise_pattern = re.compile(r'^(\d+)\)\s+(.*(\n.*)*?)(?=^\d+\)|\Z)', re.MULTILINE)
option_pattern = re.compile(r'^([a-eA-E])\)\s+(.*)', re.MULTILINE)
tip_pattern = re.compile(r'^Tip\s*(?:💡)?\s*:\s*(.*(?:\n.*)*)', re.MULTILINE)

current_id = 1

for file_name in files_to_parse:
    path = os.path.join(base_dir, file_name)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.strip().split('\n')
    section_name = lines[0].strip()
    section_name = re.sub(r'^[A-H]\)\s*', '', section_name)
    
    exercises = []
    
    blocks = re.split(r'^(\d+)\)\s+', content, flags=re.MULTILINE)
    
    for i in range(1, len(blocks), 2):
        ex_num = blocks[i]
        ex_text = blocks[i+1].strip()
        
        opts = option_pattern.findall(ex_text)
        if len(opts) < 2:
            continue
        
        opciones = []
        for opt_match in opts:
            opciones.append({
                "label": opt_match[0].upper(),
                "text": opt_match[1].strip()
            })
            
        question_text = re.sub(r'^[a-eA-E]\)\s+.*$', '', ex_text, flags=re.MULTILINE).strip()
        
        tip_match = tip_pattern.search(question_text)
        guia = ""
        if tip_match:
            guia = tip_match.group(1).strip()
            question_text = question_text[:tip_match.start()].strip()
            
        exercises.append({
            "tipo": f"Ejercicio {current_id}",
            "enunciado": question_text,
            "opciones": opciones,
            "guia": guia,
            "resultado": None,
            "quePide": "",
            "datos": "",
            "porQue": "",
            "verificacion": "",
            "errores": ""
        })
        current_id += 1
        
    # Match the [/ANTIGRAVITY | ANSWER_KEY] block
    answer_key_match = re.search(r'\[/?ANTIGRAVITY\s*\|\s*ANSWER_KEY\]\s*(.*?)\[/?ANTIGRAVITY\s*\|\s*ANSWER_KEY\]', content, flags=re.IGNORECASE | re.DOTALL)
    if not answer_key_match:
        # Fallback if no closing tag exists
        answer_key_match = re.search(r'\[/?ANTIGRAVITY\s*\|\s*ANSWER_KEY\]\s*(.*)', content, flags=re.IGNORECASE | re.DOTALL)
        
    if answer_key_match:
        answer_text = answer_key_match.group(1)
        reactivos = re.findall(r'-\s*Reactivo\s*(\d+).*?Correcta:\s*([a-eA-E])', answer_text, flags=re.IGNORECASE | re.DOTALL)
        # Reactivos usually start from 1 per file. Map them to the exercises list.
        for r_num_str, correct_opt in reactivos:
            r_idx = int(r_num_str) - 1
            if 0 <= r_idx < len(exercises):
                exercises[r_idx]["resultado"] = f"Opción {correct_opt.upper()}"
        
    sections_data.append({
        "name": section_name,
        "shortName": section_name.split()[0].replace('🔢', '').replace('🧮', ''),
        "description": "Ejercicios de " + section_name,
        "exercises": exercises
    })

hm_data = {
    "sections": sections_data
}

template_path = os.path.join(base_dir, "Habilidad matemática.html")
with open(template_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

json_str = json.dumps(hm_data, ensure_ascii=False, indent=2)
data_script = f"<script>\nwindow.HM_DATA = {json_str};\n</script>"

html_content = html_content.replace('<script src="ejercicios.js"></script>', data_script)

html_content = html_content.replace('<title>Instituto Fernando Ramírez · Habilidad Matemática</title>', '<title>Instituto Fernando Ramírez · Matemáticas</title>')
html_content = html_content.replace('<div class="brand__area">Habilidad Matemática</div>', '<div class="brand__area">Matemáticas</div>')

import re

style_injection = """
        /* Animations for Feedback */
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            20%, 60% { transform: translateX(-5px); }
            40%, 80% { transform: translateX(5px); }
        }
        @keyframes pop {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        
        .option-btn.selected.wrong {
            animation: shake 0.4s ease;
        }
        .option-btn.selected.correct {
            animation: pop 0.4s ease;
        }

        .svg-figure img {
            max-width: 300px !important;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
"""
html_content = html_content.replace('</style>', style_injection + '\n    </style>', 1)

svg_map_override = """        const SVG_MAP = {
            's2_e0': 'svg/ej41_harina_leche.svg',
            's2_e1': 'svg/ej42_equivalente.svg',
            's2_e2': 'svg/ej43_grupo.svg',
            's2_e3': 'svg/ej44_ecuacion.svg',
            's2_e4': 'svg/ej45_mezcla.svg',
            's2_e5': 'svg/ej46_cuadernos.svg',
            's2_e6': 'svg/ej47_auto.svg',
            's2_e7': 'svg/ej48_pintura.svg',
            's2_e8': 'svg/ej49_maquina.svg',
            's2_e9': 'svg/ej50_receta_arroz.svg'
        };"""
html_content = re.sub(r'const SVG_MAP = \{.*?\};', svg_map_override, html_content, flags=re.DOTALL)

# Remover textos innecesarios de las figuras base y los avisos de análisis
html_content = html_content.replace('<p>Analiza la imagen</p>', '')
html_content = html_content.replace('<p>Analiza la secuencia y determina qué figura sigue</p>', '')
html_content = html_content.replace('<div class="visual-note">📐 Ejercicio de análisis. Verifica tu respuesta abajo.</div>', '')

output_path = os.path.join(base_dir, "Matemáticas.html")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {output_path}")
