"""Figures of section 2 (basic electricity)."""
import random
from figlib import *

# 1 ── free electrons: disorder vs current ─────────────────────────────────
f = Fig('s02-electrones-libres', 470, 'Electrones libres en un cable: desorden y corriente')
random.seed(7)
for panel, (y0, title) in enumerate([(20, 'Sin pila: cada electrón va por su lado'),
                                      (245, 'Con pila: todos avanzan en el mismo sentido')]):
    f.text(320, y0 + 26, title, size=21, weight='bold')
    f.rect(40, y0 + 44, 560, 130, fill='#F2C894', stroke='#B4682A', sw=3, rx=22)
    for i in range(7):
        for j in range(2):
            ax, ay = 85 + i * 78, y0 + 78 + j * 62
            f.circle(ax, ay, 15, fill='#FFF7ED', stroke='#B4682A', sw=2)
            f.text(ax, ay + 7, '+', size=20, weight='bold', fill='#B4682A')
    for i in range(6):
        for j in range(3):
            ex, ey = 124 + i * 78 + random.randint(-7, 3), y0 + 78 + j * 31 + random.randint(-4, 4)
            if panel == 0:
                ang = random.uniform(0, 2 * math.pi)
                dx, dy = 19 * math.cos(ang), 12 * math.sin(ang)
            else:
                dx, dy = 21, 0
            f.line(ex, ey, ex + dx, ey + dy, stroke=BLUE, w=3, arrow=True)
            f.circle(ex, ey, 7, fill=BLUE, stroke='#FFFFFF', sw=2)
    if panel == 1:
        f.text(22, y0 + 118, '−', size=30, weight='bold', fill=BLUE)
        f.text(620, y0 + 118, '+', size=30, weight='bold', fill=RED)
f.circle(60, 446, 7, fill=BLUE, stroke='#FFFFFF', sw=2)
f.text(76, 453, 'electrón libre', size=18, anchor='start', fill=MUTED)
f.circle(260, 446, 12, fill='#FFF7ED', stroke='#B4682A', sw=2)
f.text(280, 453, 'átomo de cobre (no se mueve de su sitio)', size=18, anchor='start', fill=MUTED)
f.save()

# 2 ── circuit and heating loop ────────────────────────────────────────────
f = Fig('s02-circuito-y-calefaccion', 640, 'Un circuito eléctrico y su equivalente con agua')
# electric
f.text(320, 44, 'El circuito de Vicente', size=22, weight='bold')
L, R, T, B = 130, 450, 90, 270
f.path(f'M{L} {T+40} V{T} H250', )           # left up, to switch
f.path(f'M330 {T} H{R} V{T+62}')             # switch to bulb
f.path(f'M{R} {T+118} V{B} H{L} V{T+132}')   # bulb down and back
f.battery(L, T + 40, h=100, label='pila')
f.circle(250, T, 6, fill=WIRE, stroke=WIRE)
f.circle(330, T, 6, fill=WIRE, stroke=WIRE)
f.line(250, T, 326, T - 4, stroke=WIRE, w=5)
f.text(290, T - 22, 'interruptor', size=19, fill=MUTED)
f.bulb(R, T + 90, r=28)
f.text(R + 40, T + 97, 'bombilla', size=20, anchor='start', weight='bold')
f.text(L + 14, T + 162, 'cable', size=19, anchor='start', fill=MUTED)
# electron flow arrows: from − (bottom) along bottom wire to bulb, back on top to +
f.line(220, B + 18, 370, B + 18, stroke=BLUE, w=4, arrow=True)
f.line(430, T + 20, 360, T + 20, stroke=BLUE, w=4, arrow=True)
f.text(320, B + 46, 'los electrones dan la vuelta completa', size=19, fill=BLUE)
# divider
f.line(60, 338, 580, 338, stroke=PAPER_EDGE, w=2)
# water
f.text(320, 378, 'Lo mismo, con agua', size=22, weight='bold')
T2, B2 = 424, 590
PIPE = dict(stroke=WATER, w=16)
f.path(f'M{L} {T2+52} V{T2} H{R-0} V{T2+50}', **PIPE)
f.path(f'M{R} {T2+120} V{B2} H{L} V{T2+108}', **PIPE)
f.circle(L, T2 + 80, 30, fill='#FFFFFF', stroke=INK, sw=3)
f.path(f'M{L-12} {T2+68} L{L} {T2+96} L{L+12} {T2+68} Z', stroke=INK, w=3, fill=WATER)
f.text(L - 42, T2 + 87, 'bomba', size=20, anchor='end', weight='bold')
# valve
f.rect(272, T2 - 14, 36, 28, fill='#FFFFFF', stroke=INK, sw=3, rx=4)
f.line(290, T2 - 14, 290, T2 - 32, stroke=INK, w=4)
f.line(274, T2 - 32, 306, T2 - 32, stroke=INK, w=5)
f.text(290, T2 + 40, 'llave', size=19, fill=MUTED)
# paddle wheel
f.circle(R, T2 + 85, 34, fill='#FFFFFF', stroke=INK, sw=3)
for k in range(8):
    ang = k * math.pi / 4
    f.line(R + 8 * math.cos(ang), T2 + 85 + 8 * math.sin(ang), R + 44 * math.cos(ang), T2 + 85 + 44 * math.sin(ang), stroke=AMBER, w=5)
f.circle(R, T2 + 85, 7, fill=INK, stroke=INK)
f.text(R + 56, T2 + 80, 'rueda de', size=20, anchor='start', weight='bold')
f.text(R + 56, T2 + 104, 'paletas', size=20, anchor='start', weight='bold')
f.text(L + 20, T2 + 140, 'tubería', size=19, anchor='start', fill=MUTED)
f.line(220, B2 + 24, 370, B2 + 24, stroke='#0284C7', w=4, arrow=True)
f.line(430, T2 + 26, 360, T2 + 26, stroke='#0284C7', w=4, arrow=True)
f.save()

# 2b ── voltage drop in a long cable ──────────────────────────────────────
f = Fig('s02-caida-de-tension', 520, 'Caída de tensión en un cable largo')
f.text(320, 42, 'El cable se queda con parte de la tensión', size=22, weight='bold')
for k, (title, i, drop, left, col) in enumerate([('Escuchando: 0,8 A', '0,8 A', '0,4 V', '11,6 V', GREEN),
                                                  ('Transmitiendo: 10 A', '10 A', '5 V', '7 V', RED)]):
    y = 76 + k * 220
    f.rect(30, y, 580, 200, fill=SOFT, rx=14)
    f.text(320, y + 34, title, size=21, weight='bold', fill=col)
    # battery
    f.rect(54, y + 70, 96, 70, fill='#FFFFFF', stroke=INK, sw=3, rx=8)
    f.text(102, y + 100, 'batería', size=18, fill=MUTED)
    f.text(102, y + 126, '12 V', size=22, weight='bold')
    # cable (resistor zig-zag)
    f.line(150, y + 105, 196, y + 105)
    f.path(f'M196 {y+105} l10 -16 l20 32 l20 -32 l20 32 l20 -32 l20 32 l10 -16', stroke=AMBER, w=4)
    f.line(316, y + 105, 366, y + 105)
    f.text(256, y + 72, 'cable: 0,5 Ω', size=19, fill=AMBER, weight='bold')
    f.text(256, y + 158, 'se queda ' + drop, size=20, weight='bold', fill=AMBER)
    # radio
    f.rect(366, y + 70, 110, 70, fill='#FFFFFF', stroke=INK, sw=3, rx=8)
    f.text(421, y + 113, 'emisora', size=20, weight='bold')
    f.text(540, y + 100, 'le llegan', size=18, fill=MUTED)
    f.text(540, y + 128, left, size=24, weight='bold', fill=col)
    f.text(421, y + 176, '12 − ' + drop.replace(' V', '') + ' = ' + left, size=19, fill=MUTED)
f.save()

# 3 ── batteries in series / parallel ──────────────────────────────────────
def hbat(f, x, y, w=120, h=50):
    f.rect(x, y, w, h, fill='#FFFFFF', stroke=INK, sw=3, rx=8)
    f.rect(x + w, y + h / 2 - 10, 9, 20, fill=INK, rx=3)
    f.text(x + 16, y + h / 2 + 9, '−', size=26, weight='bold', fill=BLUE)
    f.text(x + w - 16, y + h / 2 + 9, '+', size=26, weight='bold', fill=RED)
    f.text(x + w / 2, y + h / 2 + 7, '1,5 V', size=19, fill=MUTED)

f = Fig('s02-pilas-serie-paralelo', 560, 'Pilas en serie y en paralelo')
f.text(320, 44, 'En serie: una detrás de otra', size=22, weight='bold')
hbat(f, 150, 76); hbat(f, 290, 76)
f.path('M150 101 H110 V170', w=4); f.path('M419 101 H470 V170', w=4)
f.line(110, 190, 470, 190, stroke=GREEN, w=3, arrow=True)
f.line(470, 190, 112, 190, stroke=GREEN, w=3, arrow=True)
f.text(290, 224, '1,5 + 1,5 = 3 V', size=24, weight='bold', fill=GREEN)
f.text(320, 256, 'Las tensiones se suman', size=20, fill=MUTED)
f.line(60, 284, 580, 284, stroke=PAPER_EDGE, w=2)
f.text(320, 324, 'En paralelo: una al lado de otra', size=22, weight='bold')
hbat(f, 220, 350); hbat(f, 220, 420)
f.path('M220 375 H170 V445 H220', w=4); f.path('M349 375 H400 V445 H349', w=4)
f.path('M170 410 H110 V470', w=4); f.path('M400 410 H470 V470', w=4)
f.line(110, 490, 470, 490, stroke=GREEN, w=3, arrow=True)
f.line(470, 490, 112, 490, stroke=GREEN, w=3, arrow=True)
f.text(290, 524, '1,5 V, pero dura el doble', size=24, weight='bold', fill=GREEN)
f.save()

# 4 ── voltmeter in parallel ───────────────────────────────────────────────
f = Fig('s02-voltimetro-en-paralelo', 400, 'El voltímetro se conecta en paralelo')
f.text(320, 44, 'Voltímetro: en paralelo, sin cortar nada', size=22, weight='bold')
L, R, T, B = 300, 540, 100, 300
f.path(f'M{L} {T+50} V{T} H{R} V{T+72}')
f.path(f'M{R} {T+128} V{B} H{L} V{T+142}')
f.battery(L, T + 50, h=100)
f.bulb(R, T + 100, r=28)
# meter
f.rect(50, 150, 130, 100, fill='#FFFFFF', stroke=GREEN, sw=4, rx=12)
f.rect(64, 162, 102, 40, fill='#ECFDF5', stroke=GREEN, sw=2, rx=6)
f.text(115, 191, '4,5 V', size=24, weight='bold', fill=GREEN)
f.text(115, 236, 'voltímetro', size=18, fill=MUTED)
f.path(f'M150 150 C150 90, 220 {T}, {L-6} {T}', stroke=RED, w=4)
f.path(f'M150 250 C150 {B+20}, 220 {B}, {L-6} {B}', stroke=INK, w=4)
f.circle(L, T, 7, fill=RED, stroke=RED); f.circle(L, B, 7, fill=INK, stroke=INK)
f.text(320, 356, 'Sus dos puntas tocan dos puntos; el circuito sigue igual', size=19, fill=MUTED)
f.save()

# 5 ── same current everywhere ─────────────────────────────────────────────
f = Fig('s02-misma-corriente', 430, 'La corriente es la misma antes y después de la bombilla')
f.text(320, 44, 'La corriente que entra es la que sale', size=22, weight='bold')
L, R, T, B = 130, 520, 110, 310
f.path(f'M{L} {T+50} V{T} H294'); f.path(f'M346 {T} H{R} V{T+72}')
f.path(f'M{R} {T+128} V{B} H346'); f.path(f'M294 {B} H{L} V{T+142}')
f.battery(L, T + 50, h=100)
f.bulb(R, T + 100, r=28)
f.meter(320, T, 'A', '0,3 A', color=AMBER); f.meter(320, B, 'A', '0,3 A', color=AMBER)
f.text(320, T + 56, '0,3 A', size=24, weight='bold', fill=AMBER)
f.text(320, B - 40, '0,3 A', size=24, weight='bold', fill=AMBER)
f.line(390, T - 22, 470, T - 22, stroke=AMBER, w=4, arrow=True)
f.line(250, B + 24, 180, B + 24, stroke=AMBER, w=4, arrow=True)
f.text(430, T - 34, 'ida', size=19, fill=MUTED); f.text(215, B + 50, 'vuelta', size=19, fill=MUTED)
f.text(320, 404, 'Los amperímetros van en serie: intercalados en el camino', size=19, fill=MUTED)
f.save()

# 6 ── Ohm experiment ──────────────────────────────────────────────────────
f = Fig('s02-experimento-ohm', 430, 'Misma batería, distinta resistencia, distinta corriente')
f.text(320, 44, 'La misma batería de 12 V, tres bombillas', size=22, weight='bold')
f.text(120, 86, 'Resistencia', size=19, fill=MUTED); f.text(400, 86, 'Corriente que circula', size=19, fill=MUTED)
for k, (r, i) in enumerate([(6, 2), (12, 1), (24, 0.5)]):
    y = 140 + k * 92
    f.bulb(70, y, r=24)
    f.text(110, y + 9, f'{r} Ω', size=26, anchor='start', weight='bold')
    w = 170 * i
    f.rect(220, y - 22, w, 44, fill=BLUE, rx=8)
    f.text(220 + w + 14, y + 9, (str(i).replace('.', ',')) + ' A', size=26, anchor='start', weight='bold', fill=BLUE)
f.text(320, 400, 'A doble resistencia, mitad de corriente:  I = U / R', size=20, weight='bold')
f.save()

# 7 ── Ohm triangle ────────────────────────────────────────────────────────
def tri(f, cx, top, size, hide=None, big=False):
    half = size * 0.62
    y2 = top + size
    f.path(f'M{cx} {top} L{cx+half} {y2} L{cx-half} {y2} Z', stroke=INK, w=3, fill='#FFFFFF')
    ym = top + size * 0.5
    f.line(cx - half * 0.5, ym, cx + half * 0.5, ym, stroke=INK, w=3)
    f.line(cx, ym, cx, y2, stroke=INK, w=3)
    fs = 44 if big else 26
    pos = {'U': (cx, ym - size * 0.08), 'I': (cx - half * 0.42, y2 - size * 0.12), 'R': (cx + half * 0.42, y2 - size * 0.12)}
    for k, (x, y) in pos.items():
        if k == hide:
            f.circle(x, y - fs * 0.33, fs * 0.62, fill=AMBER, stroke=AMBER)
            f.text(x, y, '?', size=fs, weight='bold', fill='#FFFFFF')
        else:
            f.text(x, y, k, size=fs, weight='bold', fill={'U': RED, 'I': BLUE, 'R': INK}[k])

f = Fig('s02-triangulo-ohm', 640, 'El triángulo de la ley de Ohm')
f.text(320, 44, 'El triángulo de Ohm', size=22, weight='bold')
tri(f, 320, 66, 190, big=True)
f.text(320, 290, 'Tapa la letra que buscas y lee lo que queda', size=20, fill=MUTED)
for k, (hide, formula, expl) in enumerate([('I', 'I = U / R', 'U encima de R: se dividen'),
                                            ('R', 'R = U / I', 'U encima de I: se dividen'),
                                            ('U', 'U = I × R', 'I al lado de R: se multiplican')]):
    y = 318 + k * 104
    f.rect(50, y, 540, 92, fill=SOFT, rx=14)
    tri(f, 120, y + 10, 72, hide=hide)
    f.text(200, y + 42, formula, size=28, anchor='start', weight='bold')
    f.text(200, y + 72, expl, size=19, anchor='start', fill=MUTED)
f.save()

# 8 ── prefix ladder ───────────────────────────────────────────────────────
f = Fig('s02-escalera-prefijos', 600, 'La escalera de los prefijos')
f.text(320, 44, 'La escalera de los mil', size=22, weight='bold')
rows = [('G', 'giga', 'mil millones'), ('M', 'mega', 'un millón'), ('k', 'kilo', 'mil'),
        ('', 'unidad', 'V, A, Ω, Hz…'), ('m', 'mili', 'una milésima'), ('µ', 'micro', 'una millonésima'),
        ('n', 'nano', 'una milmillonésima'), ('p', 'pico', 'una billonésima')]
for k, (sym, name, what) in enumerate(rows):
    y = 70 + k * 58
    base = k == 3
    f.rect(150, y, 340, 48, fill='#FDE68A' if base else '#FFFFFF', stroke=INK, sw=2, rx=10)
    f.text(182, y + 33, sym, size=28, weight='bold', fill=AMBER)
    f.text(214, y + 32, name, size=22, anchor='start', weight='bold')
    f.text(476, y + 31, what, size=18, anchor='end', fill=MUTED)
f.line(100, 84, 100, 520, stroke=BLUE, w=5, arrow=True)
f.text(78, 300, 'bajar: × 1.000', size=20, weight='bold', fill=BLUE, rotate=-90)
f.line(540, 520, 540, 84, stroke=RED, w=5, arrow=True)
f.text(574, 300, 'subir: ÷ 1.000', size=20, weight='bold', fill=RED, rotate=-90)
f.text(320, 566, 'Cada peldaño: la coma se mueve tres lugares', size=20, fill=MUTED)
f.save()
