"""Figures of section 11 (operating procedures)."""
from figlib import *

VIOLET = '#7C3AED'
GREY = '#9CA3AF'


def box(f, x, y, w, h, lines, fill='#FFFFFF', stroke=INK, size=19, weight='normal', color=INK, lh=24):
    """Rounded box with centred lines of text."""
    f.rect(x, y, w, h, fill=fill, stroke=stroke, sw=2.5, rx=12)
    y0 = y + h / 2 - (len(lines) - 1) * lh / 2 + size * 0.35
    for i, s in enumerate(lines):
        f.text(x + w / 2, y0 + i * lh, s, size=size, weight=weight if i == 0 else 'normal', fill=color)


# 1 ── anatomy of a QSO ─────────────────────────────────────────────────────
f = Fig('s11-anatomia-qso', 640, 'Un contacto de principio a fin, como secuencia entre dos estaciones')
f.text(320, 40, 'Un contacto, paso a paso', size=22, weight='bold')
XL, XR = 90, 550
f.rect(20, 56, 140, 40, fill='#DBEAFE', stroke=BLUE, sw=2.5, rx=10)
f.text(XL, 83, 'EA5RKV', size=20, weight='bold', fill=BLUE)
f.rect(480, 56, 140, 40, fill='#FEF3C7', stroke=AMBER, sw=2.5, rx=10)
f.text(XR, 83, 'EA1XYZ', size=20, weight='bold', fill=AMBER)
f.line(XL, 96, XL, 600, stroke=BLUE, w=3, dash='6 7')
f.line(XR, 96, XR, 600, stroke=AMBER, w=3, dash='6 7')
# minimum QSO highlight
f.rect(34, 262, 572, 336, fill='#DCFCE7', stroke=GREEN, sw=2, rx=14)
steps = [
    (150, '1', '¿Está en uso la frecuencia?', True, BLUE),
    (220, '2', 'CQ, CQ, CQ… llama CQ y escucha', True, BLUE),
    (310, '3', 'EA5RKV, aquí EA1XYZ. Cambio.', False, AMBER),
    (380, '4', 'Te recibo 59 · nombre · lugar', True, BLUE),
    (450, '5', 'Te recibo 57 · nombre · lugar', False, AMBER),
    (560, '6', '«Gracias por el informe» · 73', True, BLUE),
]
for y, n, label, right, col in steps:
    if right:
        f.line(XL + 8, y, XR - 12, y, stroke=col, w=4, arrow=True)
    else:
        f.line(XR - 8, y, XL + 12, y, stroke=col, w=4, arrow=True)
    f.circle(130 if right else 510, y - 22, 13, fill=col, stroke=col, sw=1)
    f.add(f'<text x="{130 if right else 510}" y="{y - 15}" font-size="19" text-anchor="middle" '
          f'font-weight="bold" fill="#FFFFFF">{n}</text>')
    f.text(320, y - 14, label, size=19, weight='bold')
f.text(320, 506, 'contacto mínimo: indicativos, informes y acuse', size=18, fill='#166534', weight='bold')
f.line(XR - 8, 584, XL + 12, 584, stroke=AMBER, w=4, arrow=True)
f.text(320, 624, 'Primero el indicativo del otro; después, el tuyo', size=18, fill=MUTED)
f.save()

# 2 ── RST scales ───────────────────────────────────────────────────────────
f = Fig('s11-escala-rst', 560, 'Las tres cifras del informe de señal RST')
f.text(320, 40, 'El informe RST: tres cifras, tres preguntas', size=22, weight='bold')
rows = [
    ('R', '¿Cuánto se entiende?', 5, GREEN, 'ininteligible', 'perfecto', 70),
    ('S', '¿Con cuánta fuerza llega?', 9, BLUE, 'apenas se nota', 'muy fuerte', 210),
    ('T', '¿Cómo de limpio es el tono?', 9, GREY, 'áspero', 'puro', 350),
]
for letter, q, n, col, lo, hi, y in rows:
    f.circle(60, y + 44, 30, fill=col, stroke=col, sw=1)
    f.add(f'<text x="60" y="{y + 56}" font-size="34" text-anchor="middle" font-weight="bold" fill="#FFFFFF">{letter}</text>')
    f.text(110, y + 22, q, size=20, anchor='start', weight='bold')
    w = 54
    for i in range(n):
        x = 110 + i * w
        op = 0.25 + 0.75 * (i + 1) / n
        f.add(f'<rect x="{x}" y="{y + 36}" width="{w - 6}" height="40" rx="7" fill="{col}" fill-opacity="{op:.2f}" '
              f'stroke="{col}" stroke-width="2"/>')
        f.text(x + (w - 6) / 2, y + 63, str(i + 1), size=20, weight='bold')
    f.text(110, y + 102, '1: ' + lo, size=18, anchor='start', fill=MUTED)
    f.text(110 + n * w - 6, y + 102, f'{n}: ' + hi, size=18, anchor='end', fill=MUTED)
f.text(350, 312, 'cada punto: 6 dB', size=18, fill=BLUE, weight='bold')
f.text(350, 452, 'solo en telegrafía', size=18, fill='#4B5563', weight='bold')
f.rect(40, 478, 270, 60, fill=SOFT, rx=12)
f.text(175, 516, 'En voz: «cinco nueve»', size=20, weight='bold')
f.rect(330, 478, 270, 60, fill=SOFT, rx=12)
f.text(465, 516, 'En telegrafía: 579', size=20, weight='bold')
f.save()

# 3 ── split ────────────────────────────────────────────────────────────────
f = Fig('s11-split', 430, 'Operación en split: la estación de DX transmite en una frecuencia y escucha en otra')
f.text(320, 40, 'Split: transmite aquí, escucha allí', size=22, weight='bold')
base = 300
f.line(40, base, 606, base, stroke=INK, w=3, arrow=True)
# DX
f.rect(118, 120, 34, base - 120, fill=BLUE, rx=5)
f.text(40, 112, 'estación de DX', size=19, weight='bold', fill=BLUE, anchor='start')
f.text(135, base + 28, '14.195 kHz', size=19, weight='bold')
# pile
import random
random.seed(4)
f.rect(352, 96, 200, base - 96, fill='#FEF3C7', stroke=AMBER, sw=2, rx=10)
for i in range(8):
    x = 364 + i * 23
    h = random.randint(40, 120)
    f.rect(x, base - h, 14, h, fill=AMBER, rx=3)
f.text(452, 124, 'los que llaman', size=19, weight='bold', fill='#92400E')
f.text(452, base + 28, '14.200 – 14.205 kHz', size=19, weight='bold')
# arrow DX listens
f.path(f'M156 150 C230 70, 290 70, 348 140', stroke=GREEN, w=4, arrow=True, dash='9 6')
f.text(262, 82, 'escucha «de 5 a 10 arriba»', size=18, fill=GREEN, weight='bold')
f.rect(40, 350, 560, 56, fill='#FEE2E2', stroke=RED, sw=2, rx=12)
f.text(320, 385, 'Nunca transmitas en la frecuencia de la estación de DX', size=19, weight='bold', fill='#991B1B')
f.save()

# 4 ── repeater ─────────────────────────────────────────────────────────────
f = Fig('s11-repetidor', 520, 'Un repetidor: recibe en una frecuencia y retransmite a la vez en otra')
f.text(320, 40, 'El repetidor: dos frecuencias y una llave', size=22, weight='bold')
G = 400
f.path(f'M2 {G} L150 {G} L320 150 L490 {G} L638 {G} L638 516 L2 516 Z', stroke='#8A6D3B', w=3, fill='#D9C7A3')
# repeater mast
f.line(320, 150, 320, 92, stroke=INK, w=5)
f.line(304, 92, 336, 92, stroke=INK, w=5)
f.rect(296, 150, 48, 30, fill='#FFFFFF', stroke=INK, sw=3, rx=5)
f.text(320, 78, 'repetidor', size=19, weight='bold')
# handhelds
for x, col in [(70, BLUE), (570, GREEN)]:
    f.rect(x - 11, G - 44, 22, 44, fill='#FFFFFF', stroke=INK, sw=3, rx=4)
    f.line(x + 5, G - 44, x + 5, G - 74, stroke=INK, w=4)
# uplink
f.line(84, G - 80, 300, 104, stroke=BLUE, w=4, arrow=True)
f.text(40, 190, 'entrada', size=19, anchor='start', weight='bold', fill=BLUE)
f.text(40, 214, '145,000 MHz', size=19, anchor='start', weight='bold', fill=BLUE)
f.text(40, 238, '+ subtono', size=18, anchor='start', fill=BLUE)
f.text(40, 260, '88,5 Hz', size=18, anchor='start', fill=BLUE)
# downlink
f.line(340, 104, 556, G - 80, stroke=GREEN, w=4, arrow=True)
f.text(600, 190, 'salida', size=19, anchor='end', weight='bold', fill=GREEN)
f.text(600, 214, '145,600 MHz', size=19, anchor='end', weight='bold', fill=GREEN)
f.text(600, 238, '(600 kHz', size=18, anchor='end', fill=GREEN)
f.text(600, 260, 'más arriba)', size=18, anchor='end', fill=GREEN)
# blocked direct path
f.line(96, G - 60, 216, G - 60, stroke=RED, w=3, dash='8 6')
f.text(232, G - 52, '×', size=30, weight='bold', fill=RED)
f.text(320, G - 20, 'la montaña corta el camino directo', size=18, fill='#7C2D12', weight='bold')
f.text(70, G + 34, 'transmite', size=19, weight='bold')
f.text(570, G + 34, 'escucha', size=19, weight='bold')
f.text(320, 480, 'Tú escuchas la salida y transmites en la entrada', size=19, weight='bold')
f.save()


# band strips ────────────────────────────────────────────────────────────────
def strip(f, y, lo, hi, segs, x0=40, x1=600, h=56):
    """Draw numbered coloured segments; returns scale function."""
    sc = lambda v: x0 + (v - lo) * (x1 - x0) / (hi - lo)
    for n, (a, b, col, _) in enumerate(segs, start=1):
        xa, xb = sc(a), sc(b)
        f.add(f'<rect x="{xa:.1f}" y="{y}" width="{xb - xa:.1f}" height="{h}" fill="{col}" stroke="#FFFFFF" stroke-width="2"/>')
        f.add(f'<text x="{(xa + xb) / 2:.1f}" y="{y + h / 2 + 7}" font-size="20" text-anchor="middle" '
              f'font-weight="bold" fill="#FFFFFF">{n}</text>')
    f.rect(x0, y, x1 - x0, h, fill='none', stroke=INK, sw=2.5, rx=0)
    return sc


def legend(f, y, segs, lh=30):
    for n, (a, b, col, label) in enumerate(segs, start=1):
        yy = y + (n - 1) * lh
        f.rect(40, yy - 18, 28, 24, fill=col, rx=5)
        f.add(f'<text x="54" y="{yy}" font-size="18" text-anchor="middle" font-weight="bold" fill="#FFFFFF">{n}</text>')
        f.text(80, yy, label, size=18, anchor='start')


# 5 ── 40 m band plan ───────────────────────────────────────────────────────
f = Fig('s11-plan-40m', 470, 'Plan de la banda de 40 metros en la Región 1 de la IARU')
f.text(320, 40, 'La banda de 40 metros, por tramos', size=22, weight='bold')
segs = [
    (7000, 7040, '#1D4ED8', '7.000 – 7.040   Telegrafía'),
    (7040, 7050, '#7C3AED', '7.040 – 7.050   Digitales estrechos'),
    (7050, 7060, '#0E7490', '7.050 – 7.060   Todos los modos (digitales)'),
    (7060, 7200, '#B45309', '7.060 – 7.200   Todos los modos: aquí se habla'),
]
sc = strip(f, 110, 7000, 7200, segs)
for v in (7000, 7050, 7100, 7150, 7200):
    f.line(sc(v), 166, sc(v), 176, stroke=INK, w=2.5)
for v, anchor in ((7000, 'start'), (7100, 'middle'), (7200, 'end')):
    f.text(sc(v), 198, f'{v:,}'.replace(',', '.'), size=18, anchor=anchor, fill=MUTED)
f.text(320, 222, 'kHz', size=18, fill=MUTED)
# markers above
for v, lab, col, ty in ((7030, 'QRP', '#1D4ED8', 76), (7090, 'QRP voz', '#B45309', 76), (7110, 'emergencias', RED, 76)):
    f.line(sc(v), 108, sc(v), ty + 6, stroke=col, w=3)
    f.circle(sc(v), 108, 5, fill=col, stroke=col, sw=1)
f.text(40, 72, '7.030 QRP', size=18, fill='#1D4ED8', weight='bold', anchor='start')
f.text(sc(7090) + 8, 72, '7.090 QRP voz', size=18, fill='#B45309', weight='bold', anchor='end')
f.text(sc(7110) - 8, 72, '7.110 emergencias', size=18, fill=RED, weight='bold', anchor='start')
legend(f, 270, segs, lh=34)
f.text(320, 430, 'De abajo arriba: de lo más estrecho a lo más ancho', size=19, weight='bold')
f.save()

# 6 ── 2 m band plan ────────────────────────────────────────────────────────
f = Fig('s11-plan-2m', 590, 'Plan de la banda de 2 metros en la Región 1 de la IARU')
f.text(320, 40, 'La banda de 2 metros, por tramos', size=22, weight='bold')
segs = [
    (144.000, 144.400, '#1D4ED8', '144,025 – 144,400   Telegrafía y SSB (señales débiles)'),
    (144.400, 144.500, '#DC2626', '144,400 – 144,490   Balizas: no se transmite'),
    (144.500, 144.794, '#0E7490', '144,500 – 144,794   Todos los modos'),
    (144.794, 144.975, '#7C3AED', '144,794 – 144,9625   Digitales (APRS: 144,800)'),
    (144.975, 145.200, '#B45309', '144,975 – 145,194   Entradas de repetidores'),
    (145.200, 145.575, '#059669', '145,206 – 145,5625   FM símplex (llamada: 145,500)'),
    (145.575, 145.800, '#92400E', '145,575 – 145,794   Salidas de repetidores'),
    (145.800, 146.000, '#4B5563', '145,806 – 146,000   Satélites: sin contactos terrestres'),
]
sc = strip(f, 150, 144.0, 146.0, segs)
for v in (144.0, 144.5, 145.0, 145.5, 146.0):
    f.line(sc(v), 206, sc(v), 216, stroke=INK, w=2.5)
for v, anchor in ((144.0, 'start'), (145.0, 'middle'), (146.0, 'end')):
    f.text(sc(v), 238, f'{v:.1f}'.replace('.', ',') + (' MHz' if v == 144.0 else ''), size=18, anchor=anchor, fill=MUTED)
# shift bracket
xa, xb = sc(145.0875), sc(145.6875)
f.path(f'M{xa:.0f} 146 V112 H{xb:.0f} V140', stroke=INK, w=3, arrow=True)
f.text((xa + xb) / 2, 100, '600 kHz', size=19, weight='bold')
f.text(xa - 10, 130, 'transmites', size=18, anchor='end', fill='#B45309', weight='bold')
f.text(xb + 10, 100, 'escuchas', size=18, anchor='start', fill='#92400E', weight='bold')
legend(f, 286, segs, lh=33)
f.text(320, 566, 'De 144,000 a 144,025: bajada de satélites', size=18, fill=MUTED)
f.save()

# 7 ── UTC ──────────────────────────────────────────────────────────────────
f = Fig('s11-hora-utc', 490, 'Conversión de la hora peninsular española a hora UTC')
f.text(320, 40, 'De tu reloj a la hora UTC', size=22, weight='bold')
f.text(150, 84, 'tu reloj (península)', size=19, weight='bold', fill=MUTED)
f.text(490, 84, 'hora UTC', size=19, weight='bold', fill=MUTED)
rows = [
    ('Invierno', '19:30', '', '− 1 h', '18:30', '', BLUE),
    ('Verano', '19:30', '', '− 2 h', '17:30', '', AMBER),
    ('Verano, madrugada del día 15', '00:40', 'x', '− 2 h', '22:40', 'día 14', RED),
]
for i, (name, loc, d1, op, utc, d2, col) in enumerate(rows):
    y = 104 + i * 116
    f.rect(24, y, 592, 100, fill=SOFT, rx=14)
    f.text(44, y + 28, name, size=19, anchor='start', weight='bold', fill=col)
    f.rect(70, y + 40, 160, 50, fill='#1F2933', rx=8)
    f.add(f'<text x="150" y="{y + 76}" font-size="32" text-anchor="middle" font-weight="bold" fill="#FDE68A">{loc}</text>')
    f.rect(410, y + 40, 160, 50, fill='#1F2933', rx=8)
    f.add(f'<text x="490" y="{y + 76}" font-size="32" text-anchor="middle" font-weight="bold" fill="#86EFAC">{utc}</text>')
    f.line(244, y + 65, 394, y + 65, stroke=col, w=4, arrow=True)
    f.text(320, y + 56, op, size=20, weight='bold', fill=col)
    if d1:
        f.text(596, y + 28, '¡es el ' + d2 + '!', size=18, anchor='end', fill=RED, weight='bold')
f.text(320, 470, 'Canarias: una hora menos que la península', size=18, fill=MUTED)
f.save()

# 8 ── distress flowchart ───────────────────────────────────────────────────
f = Fig('s11-socorro', 760, 'Qué hacer al oír una llamada de socorro')
f.text(320, 40, 'Si oyes una llamada de socorro', size=22, weight='bold')
box(f, 60, 62, 520, 104, ['1. No transmitas: escucha y apunta', 'hora, frecuencia, quién, dónde, qué ha pasado,', 'cuántas personas y qué necesitan'],
    fill='#DBEAFE', stroke=BLUE, weight='bold')
f.line(320, 166, 320, 196, stroke=INK, w=4, arrow=True)
# decision
f.path('M320 200 L500 250 L320 300 L140 250 Z', stroke=AMBER, w=3, fill='#FEF3C7')
f.text(320, 244, '2. ¿Contesta', size=19, weight='bold')
f.text(320, 268, 'otra estación?', size=19, weight='bold')
# yes branch (right)
f.path('M500 250 H560 V330', stroke=INK, w=4, arrow=True)
f.text(566, 240, 'sí', size=19, weight='bold', anchor='start', fill=GREEN)
box(f, 400, 334, 220, 104, ['Sigue a la escucha', 'en silencio', 'y apuntando'], fill='#DCFCE7', stroke=GREEN, weight='bold')
# no branch (down-left)
f.path('M140 250 H90 V330', stroke=INK, w=4, arrow=True)
f.text(84, 240, 'no', size=19, weight='bold', anchor='end', fill=RED)
box(f, 20, 334, 340, 104, ['3. Contesta tú', 'con calma; completa los datos', 'y léelos de vuelta'], fill='#FFFFFF', stroke=INK, weight='bold')
f.line(190, 438, 190, 470, stroke=INK, w=4, arrow=True)
box(f, 20, 474, 600, 104, ['4. Avisa al 112', 'di que eres radioaficionado y pasa los datos', 'tal como los has apuntado'],
    fill='#FEE2E2', stroke=RED, weight='bold')
f.line(320, 578, 320, 610, stroke=INK, w=4, arrow=True)
box(f, 20, 614, 600, 104, ['5. Vuelve a la frecuencia y quédate', 'confirma que el aviso está dado', 'y mantén la frecuencia limpia'],
    fill='#FFFFFF', stroke=INK, weight='bold')
f.text(320, 744, 'El socorro tiene prioridad sobre cualquier otra comunicación', size=18, fill=MUTED)
f.save()
