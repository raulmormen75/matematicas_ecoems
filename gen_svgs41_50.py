import os

svg_dir = r'c:\Users\spart\Streaming de Google Drive\Mi unidad\IFR\ECOEMS\Matemáticas\svg'
os.makedirs(svg_dir, exist_ok=True)

svgs = {
    'ej41_harina_leche.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  <!-- Harina: 2 tazas -->
  <text x="80" y="30" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333" text-anchor="middle">Harina</text>
  <path d="M60,50 L65,90 L95,90 L100,50 Z" fill="#e0e0e0" stroke="#888" stroke-width="2"/>
  <path d="M20,50 L25,90 L55,90 L60,50 Z" fill="#e0e0e0" stroke="#888" stroke-width="2"/>
  
  <text x="150" y="65" font-family="sans-serif" font-size="24" font-weight="bold" fill="#333" text-anchor="middle">:</text>
  
  <!-- Leche: 3 tazas -->
  <text x="220" y="30" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333" text-anchor="middle">Leche</text>
  <path d="M170,50 L175,90 L205,90 L210,50 Z" fill="#d0e6f2" stroke="#4a90e2" stroke-width="2"/>
  <path d="M210,50 L215,90 L245,90 L250,50 Z" fill="#d0e6f2" stroke="#4a90e2" stroke-width="2"/>
  <path d="M250,50 L255,90 L285,90 L290,50 Z" fill="#d0e6f2" stroke="#4a90e2" stroke-width="2"/>
</svg>''',

    'ej42_equivalente.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  <text x="70" y="55" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">4</text>
  <line x1="50" y1="65" x2="90" y2="65" stroke="#333" stroke-width="3"/>
  <text x="70" y="95" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">7</text>
  
  <path d="M100,45 Q150,20 200,45" fill="none" stroke="#2196f3" stroke-width="2" marker-end="url(#arrowBlue)"/>
  <rect x="135" y="15" width="30" height="20" rx="4" fill="#2196f3"/>
  <text x="150" y="29" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">× n</text>
  
  <path d="M100,75 Q150,100 200,75" fill="none" stroke="#e91e63" stroke-width="2" marker-end="url(#arrowPink)"/>
  <rect x="135" y="85" width="30" height="20" rx="4" fill="#e91e63"/>
  <text x="150" y="99" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">× n</text>
  
  <text x="240" y="65" font-family="sans-serif" font-size="40" font-weight="bold" fill="#9c27b0" text-anchor="middle">?</text>
  
  <defs>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#2196f3"/>
    </marker>
    <marker id="arrowPink" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#e91e63"/>
    </marker>
  </defs>
</svg>''',

    'ej43_grupo.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <rect x="30" y="20" width="100" height="35" rx="5" fill="#e91e63"/>
  <text x="80" y="43" font-family="sans-serif" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">15 Mujeres</text>
  
  <line x1="30" y1="65" x2="130" y2="65" stroke="#333" stroke-width="3"/>
  
  <rect x="30" y="75" width="100" height="35" rx="5" fill="#2196f3"/>
  <text x="80" y="98" font-family="sans-serif" font-size="16" font-weight="bold" fill="#fff" text-anchor="middle">10 Hombres</text>

  <path d="M140,65 L170,65" stroke="#333" stroke-width="2" marker-end="url(#arrowSimple)"/>

  <text x="215" y="45" font-family="sans-serif" font-size="16" font-weight="bold" fill="#333" text-anchor="middle">÷ MCD</text>
  <line x1="180" y1="55" x2="250" y2="55" stroke="#333" stroke-width="2" stroke-dasharray="4"/>
  <text x="215" y="75" font-family="sans-serif" font-size="16" font-weight="bold" fill="#333" text-anchor="middle">÷ MCD</text>

  <text x="275" y="65" font-family="sans-serif" font-size="32" font-weight="bold" fill="#ab47bc" text-anchor="middle">?</text>

  <defs>
    <marker id="arrowSimple" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#333"/>
    </marker>
  </defs>
</svg>''',

    'ej44_ecuacion.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <!-- Left Fraction -->
  <text x="80" y="45" font-family="sans-serif" font-size="28" font-style="italic" font-weight="bold" fill="#333" text-anchor="middle">x</text>
  <line x1="50" y1="60" x2="110" y2="60" stroke="#333" stroke-width="3"/>
  <text x="80" y="95" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">12</text>
  
  <!-- Equal sign -->
  <text x="150" y="72" font-family="sans-serif" font-size="32" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  
  <!-- Right Fraction -->
  <text x="220" y="45" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">3</text>
  <line x1="190" y1="60" x2="250" y2="60" stroke="#333" stroke-width="3"/>
  <text x="220" y="95" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">4</text>
  
  <!-- Cross arrows -->
  <path d="M100,45 L200,85" stroke="#ff9800" stroke-width="3" stroke-linecap="round" stroke-dasharray="6" marker-end="url(#arrowOrange)"/>
  <path d="M100,85 L200,45" stroke="#4caf50" stroke-width="3" stroke-linecap="round" stroke-dasharray="6" marker-end="url(#arrowGreen)"/>
  
  <defs>
    <marker id="arrowOrange" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#ff9800"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#4caf50"/>
    </marker>
  </defs>
</svg>''',

    'ej45_mezcla.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <text x="60" y="45" font-family="sans-serif" font-size="16" font-weight="bold" fill="#795548" text-anchor="middle">Azúcar</text>
  <line x1="30" y1="60" x2="90" y2="60" stroke="#333" stroke-width="2"/>
  <text x="60" y="85" font-family="sans-serif" font-size="16" font-weight="bold" fill="#1976d2" text-anchor="middle">Agua</text>
  
  <text x="115" y="66" font-family="sans-serif" font-size="24" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  
  <text x="155" y="45" font-family="sans-serif" font-size="20" font-weight="bold" fill="#795548" text-anchor="middle">5</text>
  <line x1="140" y1="60" x2="170" y2="60" stroke="#333" stroke-width="2"/>
  <text x="155" y="85" font-family="sans-serif" font-size="20" font-weight="bold" fill="#1976d2" text-anchor="middle">8</text>

  <path d="M180,60 L200,60" fill="none" stroke="#333" stroke-width="2" marker-end="url(#arrowSimpleMix)"/>

  <text x="245" y="45" font-family="sans-serif" font-size="24" font-weight="bold" fill="#9c27b0" text-anchor="middle">?</text>
  <line x1="220" y1="60" x2="270" y2="60" stroke="#333" stroke-width="2"/>
  <text x="245" y="85" font-family="sans-serif" font-size="20" font-weight="bold" fill="#1976d2" text-anchor="middle">40</text>

  <path d="M165,85 Q200,110 235,90" fill="none" stroke="#4caf50" stroke-width="2" stroke-dasharray="4" marker-end="url(#arrowGreenMix)"/>
  <rect x="185" y="95" width="30" height="15" rx="3" fill="#4caf50"/>
  <text x="200" y="106" font-family="sans-serif" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">× n</text>

  <defs>
    <marker id="arrowSimpleMix" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#333"/>
    </marker>
    <marker id="arrowGreenMix" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#4caf50"/>
    </marker>
  </defs>
</svg>''',

    'ej46_cuadernos.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <!-- Group 1: 3 cuadernos -->
  <rect x="40" y="30" width="20" height="30" fill="#4caf50" rx="2"/>
  <rect x="50" y="30" width="20" height="30" fill="#43a047" rx="2"/>
  <rect x="60" y="30" width="20" height="30" fill="#388e3c" rx="2"/>
  <text x="60" y="80" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333" text-anchor="middle">3 u.</text>
  
  <text x="100" y="48" font-family="sans-serif" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  <text x="135" y="48" font-family="sans-serif" font-size="20" font-weight="bold" fill="#2e7d32" text-anchor="middle">$45</text>
  
  <path d="M100,65 L100,90" fill="none" stroke="#666" stroke-width="2" marker-end="url(#arrowSimpleBook)"/>
  <text x="135" y="85" font-family="sans-serif" font-size="16" font-weight="bold" fill="#9c27b0" text-anchor="middle">1 u = ?</text>
  
  <line x1="175" y1="20" x2="175" y2="100" stroke="#ccc" stroke-width="2" stroke-dasharray="4"/>
  
  <!-- Group 2: 5 cuadernos -->
  <rect x="195" y="30" width="20" height="30" fill="#4caf50" rx="2"/>
  <rect x="205" y="30" width="20" height="30" fill="#43a047" rx="2"/>
  <rect x="215" y="30" width="20" height="30" fill="#388e3c" rx="2"/>
  <rect x="225" y="30" width="20" height="30" fill="#2e7d32" rx="2"/>
  <rect x="235" y="30" width="20" height="30" fill="#1b5e20" rx="2"/>
  <text x="225" y="80" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333" text-anchor="middle">5 u.</text>

  <text x="270" y="48" font-family="sans-serif" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  <text x="285" y="48" font-family="sans-serif" font-size="24" font-weight="bold" fill="#9c27b0" text-anchor="middle">?</text>
  
  <defs>
    <marker id="arrowSimpleBook" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#666"/>
    </marker>
  </defs>
</svg>''',

    'ej47_auto.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <!-- Group 1: 3 hours -->
  <rect x="30" y="30" width="60" height="30" rx="4" fill="#2196f3"/>
  <text x="60" y="50" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle">3 horas</text>
  <text x="100" y="50" font-family="sans-serif" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  <text x="140" y="50" font-family="sans-serif" font-size="16" font-weight="bold" fill="#333" text-anchor="middle">120 km</text>
  
  <!-- Vertical Hint -->
  <path d="M60,65 L60,85" stroke="#9c27b0" stroke-width="2" marker-end="url(#arrowPurpleAuto)"/>
  <rect x="30" y="90" width="60" height="20" rx="4" fill="#f3e5f5" stroke="#ce93d8" stroke-width="1"/>
  <text x="60" y="104" font-family="sans-serif" font-size="12" font-weight="bold" fill="#9c27b0" text-anchor="middle">1 hora</text>
  
  <text x="100" y="104" font-family="sans-serif" font-size="18" font-weight="bold" fill="#9c27b0" text-anchor="middle">=</text>
  <text x="140" y="106" font-family="sans-serif" font-size="16" font-weight="bold" fill="#9c27b0" text-anchor="middle">? km</text>
  
  <!-- Divider -->
  <line x1="185" y1="15" x2="185" y2="105" stroke="#ccc" stroke-width="2" stroke-dasharray="4"/>
  
  <!-- Group 2: 5 hours -->
  <rect x="205" y="30" width="60" height="30" rx="4" fill="#4caf50"/>
  <text x="235" y="50" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle">5 horas</text>
  
  <text x="275" y="50" font-family="sans-serif" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  <text x="290" y="53" font-family="sans-serif" font-size="24" font-weight="bold" fill="#2e7d32" text-anchor="middle">?</text>
  
  <defs>
    <marker id="arrowPurpleAuto" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#9c27b0"/>
    </marker>
  </defs>
</svg>''',

    'ej48_pintura.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <rect x="15" y="20" width="80" height="30" rx="4" fill="#ef5350"/>
  <text x="55" y="40" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Colorante</text>
  
  <rect x="15" y="70" width="80" height="30" rx="4" fill="#9e9e9e"/>
  <text x="55" y="90" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Base</text>
  
  <!-- Left Fraction -->
  <text x="120" y="45" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">2</text>
  <line x1="100" y1="60" x2="140" y2="60" stroke="#333" stroke-width="3"/>
  <text x="120" y="95" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">7</text>
  
  <!-- Equal sign -->
  <text x="165" y="72" font-family="sans-serif" font-size="32" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  
  <!-- Right Fraction -->
  <text x="210" y="45" font-family="sans-serif" font-size="28" font-style="italic" font-weight="bold" fill="#ef5350" text-anchor="middle">x</text>
  <line x1="190" y1="60" x2="230" y2="60" stroke="#333" stroke-width="3"/>
  <text x="210" y="95" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">28</text>
  
  <!-- Cross arrows -->
  <path d="M130,45 L200,85" stroke="#4caf50" stroke-width="2" stroke-linecap="round" stroke-dasharray="4" marker-end="url(#arrowGreenPaint)"/>
  <path d="M130,85 L200,45" stroke="#ef5350" stroke-width="2" stroke-linecap="round" stroke-dasharray="4" marker-end="url(#arrowRedPaint)"/>
  
  <text x="270" y="72" font-family="sans-serif" font-size="24" font-weight="bold" fill="#9c27b0" text-anchor="middle">?</text>
  
  <defs>
    <marker id="arrowGreenPaint" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#4caf50"/>
    </marker>
    <marker id="arrowRedPaint" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#ef5350"/>
    </marker>
  </defs>
</svg>''',

    'ej49_maquina.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <!-- Left Side: 4 hours -->
  <rect x="30" y="30" width="60" height="30" rx="4" fill="#607d8b"/>
  <text x="60" y="50" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle">4 horas</text>
  
  <text x="100" y="50" font-family="sans-serif" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  
  <rect x="110" y="30" width="60" height="30" rx="4" fill="#ffb74d"/>
  <text x="140" y="50" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333" text-anchor="middle">36 pz</text>

  <!-- Hint -->
  <path d="M85,65 L85,85" stroke="#9c27b0" stroke-width="2" marker-end="url(#arrowPurpleMachine)"/>
  <text x="85" y="105" font-family="sans-serif" font-size="14" font-weight="bold" fill="#9c27b0" text-anchor="middle">1 hora = ?</text>
  
  <!-- Divider -->
  <line x1="185" y1="15" x2="185" y2="105" stroke="#ccc" stroke-width="2" stroke-dasharray="4"/>
  
  <!-- Right Side: 7 hours -->
  <rect x="205" y="30" width="60" height="30" rx="4" fill="#455a64"/>
  <text x="235" y="50" font-family="sans-serif" font-size="14" font-weight="bold" fill="#fff" text-anchor="middle">7 horas</text>
  
  <text x="275" y="50" font-family="sans-serif" font-size="18" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  
  <text x="290" y="53" font-family="sans-serif" font-size="24" font-weight="bold" fill="#e65100" text-anchor="middle">?</text>
  
  <defs>
    <marker id="arrowPurpleMachine" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#9c27b0"/>
    </marker>
  </defs>
</svg>''',

    'ej50_receta_arroz.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 120" fill="none">
  <rect width="300" height="120" rx="10" fill="#f5f5f5"/>
  
  <rect x="15" y="25" width="70" height="25" rx="4" fill="#5c6bc0"/>
  <text x="50" y="42" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Personas</text>
  
  <rect x="15" y="75" width="70" height="25" rx="4" fill="#8d6e63"/>
  <text x="50" y="92" font-family="sans-serif" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Gramos</text>
  
  <!-- Left Fraction -->
  <text x="120" y="48" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">6</text>
  <line x1="95" y1="60" x2="145" y2="60" stroke="#333" stroke-width="3"/>
  <text x="120" y="95" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">450</text>
  
  <!-- Equal sign -->
  <text x="175" y="72" font-family="sans-serif" font-size="32" font-weight="bold" fill="#333" text-anchor="middle">=</text>
  
  <!-- Right Fraction -->
  <text x="230" y="48" font-family="sans-serif" font-size="28" font-weight="bold" fill="#333" text-anchor="middle">10</text>
  <line x1="205" y1="60" x2="255" y2="60" stroke="#333" stroke-width="3"/>
  <text x="230" y="95" font-family="sans-serif" font-size="28" font-style="italic" font-weight="bold" fill="#d32f2f" text-anchor="middle">x</text>
  
  <!-- Cross arrows -->
  <path d="M135,45 L215,85" stroke="#9c27b0" stroke-width="2" stroke-linecap="round" stroke-dasharray="4" marker-end="url(#arrowRiceCross)"/>
  <path d="M135,85 L215,45" stroke="#009688" stroke-width="2" stroke-linecap="round" stroke-dasharray="4" marker-end="url(#arrowRiceCross2)"/>
  
  <text x="280" y="72" font-family="sans-serif" font-size="24" font-weight="bold" fill="#e65100" text-anchor="middle">?</text>
  
  <defs>
    <marker id="arrowRiceCross" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#9c27b0"/>
    </marker>
    <marker id="arrowRiceCross2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M0,0 L10,5 L0,10 Z" fill="#009688"/>
    </marker>
  </defs>
</svg>'''
}

for name, content in svgs.items():
    with open(os.path.join(svg_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)
print('SVGs generados!')
