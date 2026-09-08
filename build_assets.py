from pathlib import Path
from html import escape

# Self-contained SVG/CSS motion; respects prefers-reduced-motion.

ROOT = Path(__file__).parent
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
def write(name, body, height, title):
    (ASSETS / name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
{body}
</svg>''')

write('hero.svg', '''
<defs>
  <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#14121f"/><stop offset="1" stop-color="#30203e"/></linearGradient>
  <linearGradient id="orb" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#b8ffd9"/><stop offset=".5" stop-color="#c2b3ff"/><stop offset="1" stop-color="#e69cc9"/></linearGradient>
  <radialGradient id="halo"><stop stop-color="#be91e9" stop-opacity=".23"/><stop offset="1" stop-color="#be91e9" stop-opacity="0"/></radialGradient>
  <clipPath id="name"><text x="41" y="241" font-family="DejaVu Sans,Arial,sans-serif" font-size="106" font-weight="700" letter-spacing="-6">Sharina.</text></clipPath>
  <linearGradient id="sheen"><stop stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity=".045"/></pattern>
</defs>
<style>
@keyframes breathe { 0%,100%{opacity:.4}50%{opacity:1} }
@keyframes signal { to {stroke-dashoffset:-96} }
@keyframes spin { to {transform:rotate(360deg)} }
@keyframes float { 0%,100%{transform:translateY(0)}50%{transform:translateY(-15px)} }
@keyframes shine { 0%,10%{transform:translateX(-240px)}75%,100%{transform:translateX(640px)} }
.spin{animation:spin 15s linear infinite}.reverse{animation:spin 21s linear infinite reverse}
.satellite{animation:spin 6s linear infinite}.floating{animation:float 5s ease-in-out infinite}
.float2{animation:float 6s ease-in-out -2s infinite}.shine{animation:shine 5s ease-in-out infinite}
.signal{animation:signal 6s linear infinite}.beacon{animation:breathe 4s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.shine{display:none}}
</style>
<rect width="1200" height="460" rx="24" fill="url(#bg)"/>
<rect width="1200" height="460" rx="24" fill="url(#grid)"/>
<circle cx="945" cy="210" r="265" fill="url(#halo)" class="beacon"/>
<g font-family="DejaVu Sans,Arial,sans-serif">
<rect x="48" y="36" width="44" height="38" rx="10" fill="#b8ffd9"/>
<text x="57" y="63" fill="#181522" font-size="23" font-weight="700">s/</text>
<text x="106" y="61" fill="#e9e4f4" font-size="17" letter-spacing="2">NRSHARINA</text>
<circle cx="991" cy="54" r="4" fill="#b8ffd9" class="beacon"/>
<text x="1006" y="60" fill="#c4b9d3" font-size="15" letter-spacing="2">MALAYSIA</text>
<text x="48" y="132" fill="#b8ffd9" font-size="16" letter-spacing="3">INTERN / LEARNING BY BUILDING</text>
<text x="41" y="241" fill="#f7f1ff" font-size="106" font-weight="700" letter-spacing="-6">Sharina<tspan fill="#b8ffd9">.</tspan></text>
<g clip-path="url(#name)"><rect x="0" y="145" width="220" height="115" fill="url(#sheen)" class="shine"/></g>
<text x="48" y="298" fill="#f4ecfb" font-size="30">Real problems. Thoughtful software.</text>
<text x="48" y="338" fill="#c4b9d3" font-size="19">Web applications · Solar tech · Geospatial tools</text>
<path d="M48 390H1152" stroke="#786685" stroke-opacity=".45"/>
<text x="48" y="428" fill="#b8ffd9" font-size="14" letter-spacing="2">UNDERSTAND → BUILD → REFINE</text>
<text x="855" y="428" fill="#c4b9d3" font-size="14" letter-spacing="2">ALWAYS A WORK IN PROGRESS</text>
</g>
<!-- Imaginary orbital coding lab; decorative artwork, not an architecture diagram. -->
<g transform="translate(957 356)" fill="none" stroke="#b8ffd9" stroke-opacity=".25">
<path d="M-115 0L0-35L115 0L0 27Z" fill="#233638" fill-opacity=".7"/>
<path d="M-77 9L38-23M-38 18L77-12M-77-12L38 18M-38-23L77 9"/>
<path d="M-115 0L0 27L115 0" stroke-opacity=".8" stroke-dasharray="16 32" class="signal"/>
</g>
<g transform="translate(761 154)"><g class="float2">
<rect x="-33" y="-26" width="66" height="52" rx="14" fill="#30263f" stroke="#9e7eba"/>
<text y="9" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-size="27" fill="#ddc6ff">{ }</text>
</g></g>
<g transform="translate(1122 316)"><g class="float2">
<rect x="-27" y="-27" width="54" height="54" rx="14" fill="#203c33" stroke="#8ecead"/>
<path d="M0 16C-19-5-13-17 0-17C13-17 19-5 0 16Z" fill="none" stroke="#b8ffd9" stroke-width="2"/><circle cy="-5" r="4" fill="#b8ffd9"/>
</g></g>
<g transform="translate(957 222)"><g class="floating">
<circle r="117" fill="none" stroke="#af92cb" stroke-opacity=".28"/>
<circle r="82" fill="none" stroke="#af92cb" stroke-opacity=".22"/>
<g class="spin"><ellipse rx="168" ry="56" transform="rotate(-34)" fill="none" stroke="url(#orb)" stroke-width="2"/></g>
<g class="reverse"><ellipse rx="165" ry="61" transform="rotate(38)" fill="none" stroke="#b8ffd9" stroke-opacity=".6"/></g>
<circle r="142" fill="none" stroke="#b8ffd9" stroke-opacity=".3" stroke-dasharray="2 14" class="signal"/>
<path d="M0-75C8-22 22-8 75 0C22 8 8 22 0 75C-8 22-22 8-75 0C-22-8-8-22 0-75Z" fill="url(#orb)"/>
<rect x="-28" y="-20" width="56" height="40" rx="12" fill="#211a30"/>
<text x="0" y="8" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-size="23" font-weight="700" fill="#f5f0fc">&lt;/&gt;</text>
<g class="satellite"><circle cy="-142" r="12" fill="#b8ffd9" fill-opacity=".13"/><circle cy="-142" r="6" fill="#caffdf"/><circle cy="142" r="4" fill="#fba3d1"/></g>


</g></g>
''', 460, 'Sharina. Real problems. Thoughtful software. Web applications, solar tech and geospatial tools. Based in Malaysia.')

chips = [('PHP','01'),('Laravel','02'),('Tailwind CSS','03'),('SQLite','04'),('QGIS','05'),('QField','06'),('Git','07'),('GitHub','08'),('VS Code','09')]
body = '<style>@keyframes active{0%,17%,100%{stroke:#45364f;fill:#282134}5%,11%{stroke:#b8ffd9;fill:#294138}}.chip{animation:active 13.5s ease-in-out infinite}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style><rect width="1200" height="206" rx="18" fill="#1b1727"/>'
for i,(label,num) in enumerate(chips):
    row, col = divmod(i,5)
    x,y = 24+col*232, 22+row*88
    body += f'''<rect x="{x}" y="{y}" width="224" height="74" rx="12" fill="#282134" stroke="#45364f" class="chip" style="animation-delay:{i*1.5}s"/>
<text x="{x+16}" y="{y+26}" font-family="DejaVu Sans,Arial,sans-serif" font-size="12" fill="#b8ffd9" letter-spacing="2">{num}</text>
<text x="{x+16}" y="{y+55}" font-family="DejaVu Sans,Arial,sans-serif" font-size="22" fill="#f4ecfb">{escape(label)}</text>'''
body += '<text x="969" y="155" font-family="DejaVu Sans,Arial,sans-serif" font-size="17" fill="#c5b8d2">TOOLS → IDEAS → CODE</text>'
write('toolkit.svg',body,206,'Toolkit: PHP, Laravel, Tailwind CSS, SQLite, QGIS, QField, Git, GitHub and VS Code.')

write('footer.svg','''<defs><linearGradient id="line"><stop stop-color="#b8ffd9"/><stop offset="1" stop-color="#bc91e4"/></linearGradient></defs>
<style>@keyframes trace{to{stroke-dashoffset:-1200}}.trace{animation:trace 10s linear infinite}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style>
<rect width="1200" height="124" rx="18" fill="#1b1727"/>
<path d="M28 2H1172" stroke="url(#line)" stroke-width="2" stroke-dasharray="140 1060" class="trace"/>
<rect x="28" y="27" width="4" height="70" rx="2" fill="url(#line)"/>
<text x="52" y="57" font-family="DejaVu Sans,Arial,sans-serif" font-size="15" letter-spacing="3" fill="#b8ffd9">THE APPROACH</text>
<text x="52" y="89" font-family="DejaVu Sans,Arial,sans-serif" font-size="23" fill="#f4ecfb">Make it useful. Make it clear. Make it better.</text>
<text x="978" y="77" font-family="DejaVu Sans,Arial,sans-serif" font-size="20" fill="#c5b8d2">&lt; / sharina &gt;</text>''',124,'The approach: Make it useful. Make it clear. Make it better.')

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    for path in ASSETS.glob('*.svg'):
        ET.parse(path)
        print(f'Validated {path.name}')
