"""Figures of section 9 (propagation)."""
import math, random
from figlib import *

EARTH = '#D9C7A3'
EARTH_EDGE = '#8A6D3B'
IONO = '#DDD6FE'
IONO_EDGE = '#7C3AED'
SEA = '#BAE6FD'


def ground_y(x, y_edge=370, y_ctrl=300):
    """Height of the curved ground (a quadratic Bezier from x=0 to x=640)."""
    t = x / 640
    return (1 - t) ** 2 * y_edge + 2 * t * (1 - t) * y_ctrl + t * t * y_edge


def ground(f, y_edge=370, y_ctrl=300, fill=EARTH, edge=EARTH_EDGE):
    f.path(f'M2 {y_edge} Q320 {y_ctrl} 638 {y_edge} L638 {f.h - 4} L2 {f.h - 4} Z', stroke=edge, w=3, fill=fill)


def antenna(f, x, base, h=34):
    f.line(x, base, x, base - h, stroke=INK, w=4)
    f.line(x - 10, base - h, x + 10, base - h, stroke=INK, w=4)
    return x, base - h


def iono_band(f, y, h, label=True):
    f.rect(20, y, 600, h, fill=IONO, stroke=IONO_EDGE, sw=2, rx=14)
    if label:
        f.text(600, y + h / 2 + 7, 'ionosfera', size=19, anchor='end', fill=IONO_EDGE, weight='bold')


def hop(f, x1, y1, x2, y2, top=106, ctrl=60, **kw):
    """One ionospheric hop drawn as two straight legs joined by a smooth turn inside the layer."""
    xa = (x1 + x2) / 2
    rise = ((y1 + y2) / 2) - top
    d = (top - ctrl) * (xa - x1) / (rise + (top - ctrl))
    f.path(f'M{x1} {y1} L{xa - d:.1f} {top} Q{xa} {ctrl} {xa + d:.1f} {top} L{x2} {y2}', arrow=True, **kw)


# 1 ── three paths ─────────────────────────────────────────────────────────
f = Fig('s09-tres-caminos', 470, 'Los tres caminos de una onda de radio')
f.text(320, 40, 'Los tres caminos de una onda', size=22, weight='bold')
iono_band(f, 62, 40)
ground(f)
ax, ay = antenna(f, 110, ground_y(110))
rx, ry = antenna(f, 400, ground_y(400))
# sky wave
hop(f, ax, ay, 560, ground_y(560) - 6, top=104, ctrl=60, stroke=BLUE, w=4)
f.text(462, 196, 'onda ionosférica', size=19, anchor='start', fill=BLUE, weight='bold')
# direct wave
f.line(ax, ay, rx - 6, ry, stroke=AMBER, w=4, arrow=True)
f.text(255, ay - 12, 'onda directa', size=19, fill=AMBER, weight='bold')
# surface wave
f.path(f'M{ax + 4} {ground_y(110) - 8} Q190 {ground_y(190) - 12} 268 {ground_y(268) - 8}', stroke=GREEN, w=4, arrow=True, dash='10 7')
f.text(196, 400, 'onda de superficie', size=19, fill=GREEN, weight='bold')
f.text(196, 424, '(pegada al suelo)', size=18, fill=MUTED)
f.text(500, 424, 'la Tierra es curva', size=18, fill=MUTED)
f.save()

# 2 ── refraction ──────────────────────────────────────────────────────────
f = Fig('s09-refraccion', 470, 'La ionosfera curva las ondas: refracción')
f.text(320, 40, 'La ionosfera no refleja: curva', size=22, weight='bold')
f.rect(20, 190, 600, 50, fill='#EDE9FE', rx=0)
f.rect(20, 145, 600, 45, fill='#DDD6FE', rx=0)
f.rect(20, 110, 600, 35, fill='#C4B5FD', rx=0)
f.rect(20, 110, 600, 130, fill='none', stroke=IONO_EDGE, sw=2, rx=10)
f.text(604, 136, 'más ionización', size=18, anchor='end', fill=IONO_EDGE, weight='bold')
f.text(604, 230, 'menos ionización', size=18, anchor='end', fill=IONO_EDGE)
f.line(20, 410, 620, 410, stroke=EARTH_EDGE, w=4)
# returning ray
f.path('M90 410 L250 240 C300 188, 350 188, 400 240 L556 406', stroke=BLUE, w=4, arrow=True)
f.text(500, 302, 'vuelve', size=19, anchor='start', fill=BLUE, weight='bold')
f.text(500, 326, 'a tierra', size=19, anchor='start', fill=BLUE, weight='bold')
# escaping ray (higher frequency)
f.path('M90 410 L236 240 C262 208, 296 160, 330 110 L352 72', stroke=RED, w=4, arrow=True, dash='10 7')
f.text(372, 74, 'frecuencia muy alta:', size=18, anchor='start', fill=RED, weight='bold')
f.text(372, 96, 'se escapa', size=18, anchor='start', fill=RED, weight='bold')
f.text(320, 448, 'La trayectoria se va doblando poco a poco', size=19, fill=MUTED)
f.save()

# 3 ── layers day / night ──────────────────────────────────────────────────
f = Fig('s09-capas-dia-noche', 520, 'Las capas de la ionosfera, de día y de noche')
f.text(320, 38, 'Las capas, de día y de noche', size=22, weight='bold')
for col, (x0, title) in enumerate([(30, 'De día'), (330, 'De noche')]):
    night = col == 1
    f.rect(x0, 56, 280, 410, fill='#1E293B' if night else '#E0F2FE', rx=14)
    tcol = '#FFFFFF' if night else INK
    f.text(x0 + 140, 86, title, size=21, weight='bold', fill=tcol)
    if night:
        f.circle(x0 + 240, 80, 14, fill='#F8FAFC', stroke='#F8FAFC')
        f.circle(x0 + 247, 75, 12, fill='#1E293B', stroke='#1E293B')
    else:
        f.circle(x0 + 240, 80, 14, fill='#FBBF24', stroke='#F59E0B')
    bands = ([('F', '130–400 km', 104, 150, '#C4B5FD', False),
              ('E', 'muy débil', 268, 50, '#DDD6FE', True),
              ('D', 'ha desaparecido', 332, 50, 'none', True)] if night else
             [('F2', '200–400 km', 104, 80, '#C4B5FD', False),
              ('F1', '130–200 km', 194, 60, '#D8CCFE', False),
              ('E', '90–130 km', 264, 54, '#E4DCFE', False),
              ('D', '60–90 km: absorbe', 328, 54, '#FECACA', False)])
    for name, note, y, h, fill, dashed in bands:
        if dashed:
            f.add(f'<rect x="{x0 + 16}" y="{y}" width="248" height="{h}" rx="10" fill="{fill if fill != "none" else "none"}" '
                  f'fill-opacity="0.35" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="8 6"/>')
        else:
            f.rect(x0 + 16, y, 248, h, fill=fill, stroke=IONO_EDGE if name != 'D' else RED, sw=2, rx=10)
        lc = '#E2E8F0' if (night and dashed) else INK
        f.text(x0 + 32, y + h / 2 + 8, name, size=24, anchor='start', weight='bold', fill=lc)
        f.text(x0 + 252, y + h / 2 + 7, note, size=18, anchor='end', fill=lc)
    f.rect(x0 + 16, 404, 248, 46, fill=EARTH, stroke=EARTH_EDGE, sw=2, rx=10)
    f.text(x0 + 140, 434, 'suelo', size=18)
f.text(320, 498, 'De noche solo queda la capa F: el espejo sin el secante', size=19, fill=MUTED)
f.save()

# 4 ── skip and silent zone ────────────────────────────────────────────────
f = Fig('s09-salto-y-zona-de-silencio', 500, 'El salto ionosférico y la zona de silencio')
f.text(320, 38, 'Saltos y zona de silencio', size=22, weight='bold')
iono_band(f, 58, 40)
ground(f, y_edge=372, y_ctrl=316)
gy = lambda x: ground_y(x, 372, 316)
ax, ay = antenna(f, 60, gy(60))
# too steep ray escapes
f.path(f'M{ax} {ay} L104 100 Q110 76 124 44', stroke=RED, w=3, arrow=True, dash='8 6')
# first hop
hop(f, ax, ay, 396, gy(396) - 5, top=102, ctrl=58, stroke=BLUE, w=4)
# second hop
hop(f, 396, gy(396) - 5, 604, gy(604) - 5, top=102, ctrl=58, stroke=BLUE, w=4)
f.text(228, 262, '1.er salto', size=19, fill=BLUE, weight='bold')
f.text(500, 262, '2.º salto', size=19, fill=BLUE, weight='bold')
# surface wave
f.path(f'M{ax + 6} {gy(60) - 8} L138 {gy(138) - 10}', stroke=GREEN, w=4, arrow=True, dash='8 6')
# brackets under the ground line
f.line(64, 408, 140, 408, stroke=GREEN, w=5)
f.text(102, 434, 'superficie', size=18, fill=GREEN, weight='bold')
f.line(152, 408, 384, 408, stroke=RED, w=5)
f.text(268, 434, 'zona de silencio', size=20, fill=RED, weight='bold')
f.text(268, 458, '(aquí no llega nada)', size=18, fill=MUTED)
f.line(396, 408, 620, 408, stroke=BLUE, w=5)
f.text(508, 434, 'se recibe', size=18, fill=BLUE, weight='bold')
f.text(130, 126, 'se escapa', size=18, anchor='start', fill=RED, weight='bold')
f.save()

# 5 ── MUF / LUF window ────────────────────────────────────────────────────
f = Fig('s09-ventana-muf-luf', 400, 'La ventana de frecuencias útiles entre la LUF y la MUF')
f.text(320, 40, 'La ventana de frecuencias útiles', size=22, weight='bold')
f.rect(40, 110, 170, 150, fill='#FECACA', stroke=RED, sw=2, rx=10)
f.rect(210, 110, 240, 150, fill='#BBF7D0', stroke=GREEN, sw=2, rx=10)
f.rect(450, 110, 150, 150, fill='#E5E7EB', stroke=MUTED, sw=2, rx=10)
f.text(125, 170, 'la capa D', size=19, fill=RED, weight='bold')
f.text(125, 196, 'la absorbe', size=19, fill=RED, weight='bold')
f.text(330, 158, 'VENTANA ÚTIL', size=21, fill=GREEN, weight='bold')
f.text(330, 196, 'lo mejor: cerca', size=19)
f.text(330, 220, 'de la MUF  →', size=19)
f.text(525, 170, 'se escapa', size=19, fill=MUTED, weight='bold')
f.text(525, 196, 'al espacio', size=19, fill=MUTED, weight='bold')
for x, name in [(210, 'LUF'), (450, 'MUF')]:
    f.line(x, 80, x, 290, stroke=INK, w=4)
    f.text(x, 72, name, size=22, weight='bold')
f.line(40, 320, 600, 320, stroke=INK, w=4, arrow=True)
f.text(320, 352, 'frecuencia: de más baja a más alta', size=19, fill=MUTED)
f.text(320, 382, 'LUF: frecuencia mínima utilizable · MUF: máxima', size=18, fill=MUTED)
f.save()

# 6 ── solar cycle ─────────────────────────────────────────────────────────
f = Fig('s09-ciclo-solar', 420, 'El ciclo solar de unos once años')
f.text(320, 40, 'El ciclo solar', size=22, weight='bold')
x0, x1, base, per = 70, 610, 300, 270
UP, DOWN = 4.5, 6.5   # years rising / falling

def cycle_shape(u):
    if u < UP:
        return math.sin(math.pi / 2 * u / UP) ** 2
    return math.cos(math.pi / 2 * (u - UP) / DOWN) ** 2

pts = []
for x in range(x0, x1 + 1, 5):
    years = (x - x0) / per * 11
    amp = 175 if years < 11 else 120
    y = base - amp * cycle_shape(years % 11)
    pts.append(f'{x} {y:.1f}')
f.path('M' + ' L'.join(pts) + f' L{x1} {base} L{x0} {base} Z', stroke='none', w=0, fill='#FDE68A')
f.path('M' + ' L'.join(pts), stroke=AMBER, w=5)
f.line(x0, base, x1, base, stroke=INK, w=3)
f.line(x0, base, x0, 100, stroke=INK, w=3)
f.text(44, 210, 'manchas solares', size=18, fill=MUTED, rotate=-90)
p1, p2 = x0 + per * UP / 11, x0 + per + per * UP / 11
f.text(p1, 114, 'máximo', size=19, weight='bold', fill=AMBER)
f.text(p2, 146, 'máximo', size=19, weight='bold', fill=AMBER)
f.text(p2, 168, '(más flojo)', size=18, fill=MUTED)
for xm in (x0 + 34, x0 + per, x1 - 34):
    f.text(xm, 326, 'mínimo', size=18, fill=MUTED)
f.line(p1, 84, p2, 84, stroke=INK, w=3, arrow=True)
f.line(p2, 84, p1 + 2, 84, stroke=INK, w=3, arrow=True)
f.text((p1 + p2) / 2, 74, 'unos 11 años', size=20, weight='bold')
f.text(320, 366, 'Sube en 4 o 5 años y baja en 6 o 7. No hay dos ciclos iguales', size=19)
f.text(320, 394, 'Máximo: bandas altas abiertas · Mínimo: cerradas', size=19, fill=MUTED)
f.save()

# 7 ── bands by day and night ──────────────────────────────────────────────
f = Fig('s09-bandas-dia-y-noche', 440, 'Las bandas de HF de día y de noche')
f.text(320, 40, 'Qué esperar de cada banda de HF', size=22, weight='bold')
f.text(84, 86, 'Banda', size=19, fill=MUTED)
f.text(280, 86, 'De día', size=19, weight='bold')
f.text(500, 86, 'De noche', size=19, weight='bold')
G, A, R = ('#BBF7D0', GREEN), ('#FDE68A', AMBER), ('#FECACA', RED)
rows = [('160 y 80 m', ('solo local', R), ('larga distancia', G)),
        ('40 m', ('media distancia', A), ('larga distancia', G)),
        ('20 m', ('larga distancia', G), ('a ratos', A)),
        ('17 a 10 m', ('larga, con sol activo', G), ('cerradas', R))]
for k, (band, day, night) in enumerate(rows):
    y = 104 + k * 70
    f.text(84, y + 37, band, size=20, weight='bold')
    for x, (txt, (fill, edge)) in ((170, day), (392, night)):
        f.rect(x, y, 210, 56, fill=fill, stroke=edge, sw=2, rx=10)
        f.text(x + 105, y + 35, txt, size=19)
f.text(320, 414, 'Bandas bajas, de noche. Bandas altas, de día.', size=20, weight='bold')
f.save()

# 8 ── tropospheric duct ───────────────────────────────────────────────────
f = Fig('s09-conducto-troposferico', 470, 'Un conducto troposférico sobre el mar')
f.text(320, 40, 'Conducto troposférico', size=22, weight='bold')
ground(f, y_edge=350, y_ctrl=290, fill=SEA, edge='#0284C7')
gy = lambda x: ground_y(x, 350, 290)
f.path('M24 232 Q320 172 616 232', stroke='#FB923C', w=22)
f.text(350, 160, 'aire caliente encima (inversión térmica)', size=19, fill='#C2410C', weight='bold')
f.text(320, 298, 'aire frío', size=18, fill=MUTED)
f.text(320, 388, 'mar', size=20, fill='#0369A1', weight='bold')
ax, ay = antenna(f, 50, gy(50))
rx, ry = antenna(f, 592, gy(592))
xs = [50, 140, 230, 320, 410, 500, 592]
d = f'M{ax} {ay}'
for i, x in enumerate(xs[1:], start=1):
    top = i % 2 == 1
    y = (gy(x) - 100) if top else (gy(x) - 8)
    if x == 592:
        y = ry
    d += f' L{x} {y:.0f}'
f.path(d, stroke=BLUE, w=4, arrow=True)
f.path(f'M{ax} {ay} L96 190 L112 96', stroke=RED, w=3, arrow=True, dash='8 6')
f.text(124, 100, 'sin conducto: se pierde', size=18, anchor='start', fill=RED)
f.text(320, 436, 'La onda viaja atrapada, mucho más allá del horizonte', size=19, fill='#0C4A6E')
f.save()
