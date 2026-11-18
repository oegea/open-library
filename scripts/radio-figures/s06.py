"""Figures of section 6 (waves and modulation)."""
import math
from figlib import *


def poly(pts):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)


def wave(x0, x1, y0, fn, n=600):
    """Polyline of y0 - fn(t) for t in 0..1 mapped onto x0..x1."""
    return poly([(x0 + (x1 - x0) * k / n, y0 - fn(k / n)) for k in range(n + 1)])


TAU = 2 * math.pi

# 1 ── electromagnetic wave ────────────────────────────────────────────────
f = Fig('s06-onda-electromagnetica', 420, 'Una onda electromagnética: campos E y H perpendiculares')
f.text(320, 42, 'Una onda electromagnética', size=22, weight='bold')
X0, X1, Y = 90, 520, 220
cyc = 2
# field "ribs"
for k in range(0, 41):
    t = k / 40
    x = X0 + (X1 - X0) * t
    s = math.sin(TAU * cyc * t)
    f.line(x, Y, x, Y - 85 * s, stroke='#F3A6A6', w=2)
    f.line(x, Y, x - 38 * s, Y + 38 * s, stroke='#A9C2F5', w=2)
f.path(wave(X0, X1, Y, lambda t: 85 * math.sin(TAU * cyc * t)), stroke=RED, w=4)
f.path(poly([(X0 + (X1 - X0) * k / 400 - 38 * math.sin(TAU * cyc * k / 400),
              Y + 38 * math.sin(TAU * cyc * k / 400)) for k in range(401)]), stroke=BLUE, w=4)
f.line(60, Y, 590, Y, stroke=INK, w=3, arrow=True)
f.text(590, Y - 14, 'avance', size=19, anchor='end', fill=INK)
f.text(150, 100, 'E', size=30, weight='bold', fill=RED)
f.text(250, 334, 'H', size=30, weight='bold', fill=BLUE)
f.text(320, 372, 'E: campo eléctrico, aquí en vertical', size=19, fill=RED)
f.text(320, 400, 'H: campo magnético, perpendicular a E', size=19, fill=BLUE)
f.save()

# 2 ── polarisation ────────────────────────────────────────────────────────
f = Fig('s06-polarizacion', 470, 'Polarización: antenas alineadas y antenas cruzadas')
f.text(320, 42, 'La polarización tiene que coincidir', size=22, weight='bold')
for k, (title, col, crossed) in enumerate([('Las dos verticales: buena señal', GREEN, False),
                                            ('Cruzadas: se pierde casi todo (hasta 20 dB)', RED, True)]):
    y = 70 + k * 198
    f.rect(30, y, 580, 182, fill=SOFT, rx=14)
    f.text(320, y + 32, title, size=20, weight='bold', fill=col)
    cy = y + 108
    # transmitting vertical antenna
    f.line(90, cy - 52, 90, cy + 52, stroke=INK, w=6)
    f.text(90, y + 176, 'emite', size=18, fill=MUTED)
    # wave with vertical E
    f.path(wave(130, 470, cy, lambda t: 34 * math.sin(TAU * 5 * t)), stroke=RED, w=3)
    f.line(130, cy, 480, cy, stroke=MUTED, w=2, arrow=True, dash='6 6')
    if crossed:
        f.line(506, cy, 594, cy, stroke=INK, w=6)
    else:
        f.line(550, cy - 52, 550, cy + 52, stroke=INK, w=6)
    f.text(550, y + 176, 'recibe', size=18, fill=MUTED)
f.save()

# 3 ── inverse-square dilution ─────────────────────────────────────────────
f = Fig('s06-dilucion-con-la-distancia', 430, 'La energía se reparte con el cuadrado de la distancia')
f.text(320, 42, 'La misma energía, cada vez más repartida', size=22, weight='bold')
AX, AY = 50, 215
f.line(AX, AY, 600, AY - 86, stroke=AMBER, w=2, dash='7 6')
f.line(AX, AY, 600, AY + 86, stroke=AMBER, w=2, dash='7 6')
f.line(AX, AY - 34, AX, AY + 34, stroke=INK, w=6)
f.text(AX + 6, AY + 62, 'antena', size=18, fill=MUTED)
for n, cx in [(1, 210), (2, 370), (3, 530)]:
    cell = 50
    side = cell * n
    x0, y0 = cx - side / 2, AY - side / 2
    for i in range(n):
        for j in range(n):
            f.rect(x0 + i * cell, y0 + j * cell, cell, cell, fill='#FDE68A' if (i, j) == (0, 0) else '#FFFFFF',
                   stroke=INK, sw=2, rx=0)
    f.text(cx, 340, f'distancia × {n}', size=19, weight='bold')
    f.text(cx, 368, ['toda la potencia', '1/4 en cada uno', '1/9 en cada uno'][n - 1], size=18, fill=MUTED)
f.text(320, 406, 'Al doble de distancia, la cuarta parte: −6 dB', size=20, weight='bold', fill=AMBER)
f.save()

# 4 ── voice and carrier ───────────────────────────────────────────────────
f = Fig('s06-voz-y-portadora', 420, 'La voz, lenta, y la portadora, rapidísima')
f.text(320, 42, 'Dos ondas, cada una para una cosa', size=22, weight='bold')
f.rect(30, 62, 580, 160, fill=SOFT, rx=14)
f.text(320, 92, 'La voz: lenta e irregular (cientos o miles de Hz)', size=19, weight='bold', fill=BLUE)
voice = lambda t: 34 * (0.6 * math.sin(TAU * 2 * t) + 0.35 * math.sin(TAU * 5 * t + 1) + 0.2 * math.sin(TAU * 9 * t + 2))
f.line(60, 160, 580, 160, stroke=MUTED, w=1)
f.path(wave(60, 580, 160, voice), stroke=BLUE, w=4)
f.rect(30, 236, 580, 160, fill=SOFT, rx=14)
f.text(320, 266, 'La portadora: rapidísima y siempre igual (millones de Hz)', size=19, weight='bold', fill=RED)
f.line(60, 334, 580, 334, stroke=MUTED, w=1)
f.path(wave(60, 580, 334, lambda t: 36 * math.sin(TAU * 44 * t), n=1600), stroke=RED, w=2)
f.save()

# 5 ── CW keying ───────────────────────────────────────────────────────────
f = Fig('s06-cw-manipulacion', 320, 'Una portadora manipulada en morse: la letra R')
f.text(320, 42, 'La letra R en morse: punto, raya, punto', size=22, weight='bold')
Y = 160
f.line(50, Y, 590, Y, stroke=MUTED, w=2)
for x0, x1, name in [(110, 160, 'punto'), (230, 380, 'raya'), (450, 500, 'punto')]:
    ncyc = (x1 - x0) / 9
    f.path(wave(x0, x1, Y, lambda t, n=ncyc: 52 * math.sin(TAU * n * t), n=int((x1 - x0) * 4)), stroke=RED, w=2)
    f.text((x0 + x1) / 2, Y + 92, name, size=20, weight='bold')
f.text(320, 296, 'Portadora encendida o apagada: nada más', size=19, fill=MUTED)
f.save()

# 6 ── beat ────────────────────────────────────────────────────────────────
f = Fig('s06-batido', 500, 'El batido de dos ondas de frecuencias parecidas')
f.text(320, 42, 'El batido: dos ondas casi iguales, sumadas', size=22, weight='bold')
X0, X1 = 60, 580
f1, f2 = 22, 24
f.text(320, 82, 'Dos ondas de frecuencias parecidas', size=19, fill=MUTED)
f.path(wave(X0, X1, 150, lambda t: 44 * math.cos(TAU * f1 * t), n=1400), stroke=RED, w=2)
f.path(wave(X0, X1, 150, lambda t: 44 * math.cos(TAU * f2 * t), n=1400), stroke=BLUE, w=2)
f.text(320, 238, 'Su suma: el tamaño sube y baja', size=19, fill=MUTED)
ssum = lambda t: 44 * (math.cos(TAU * f1 * t) + math.cos(TAU * f2 * t))
env = lambda t: 88 * abs(math.cos(math.pi * (f2 - f1) * t))
f.path(wave(X0, X1, 340, ssum, n=1600), stroke=INK, w=2)
f.path(wave(X0, X1, 340, env), stroke=AMBER, w=3, dash='7 6')
f.path(wave(X0, X1, 340, lambda t: -env(t)), stroke=AMBER, w=3, dash='7 6')
for t, lab, col in [(0.25, 'se anulan', RED), (0.5, 'se refuerzan', GREEN), (0.75, 'se anulan', RED)]:
    f.text(X0 + (X1 - X0) * t, 462, lab, size=19, weight='bold', fill=col)
f.save()

# 7 ── AM envelope ─────────────────────────────────────────────────────────
f = Fig('s06-am-envolvente', 470, 'AM: la envolvente de la portadora dibuja el audio')
f.text(320, 42, 'AM: el tamaño de la portadora dibuja la voz', size=22, weight='bold')
aud = lambda t: math.sin(TAU * 2 * t)
f.text(320, 82, 'La señal de audio', size=19, fill=BLUE, weight='bold')
f.line(X0, 130, X1, 130, stroke=MUTED, w=1)
f.path(wave(X0, X1, 130, lambda t: 34 * aud(t)), stroke=BLUE, w=4)
f.text(320, 206, 'La portadora, modulada en amplitud', size=19, fill=RED, weight='bold')
A = 56
am = lambda t: A * (1 + 0.75 * aud(t)) * math.sin(TAU * 46 * t)
e1 = lambda t: A * (1 + 0.75 * aud(t))
f.line(X0, 320, X1, 320, stroke=MUTED, w=1)
f.path(wave(X0, X1, 320, am, n=1800), stroke=RED, w=2)
f.path(wave(X0, X1, 320, e1), stroke=AMBER, w=3, dash='7 6')
f.path(wave(X0, X1, 320, lambda t: -e1(t)), stroke=AMBER, w=3, dash='7 6')
f.text(320, 448, 'La línea de puntos es la envolvente: tiene la forma del audio', size=19, fill=AMBER)
f.save()


# spectrum helpers ──────────────────────────────────────────────────────────
def axis(f, y, x0=50, x1=590, label='frecuencia'):
    f.line(x0, y, x1, y, stroke=INK, w=3, arrow=True)
    f.text(x1, y + 52, label, size=18, anchor='end', fill=MUTED)


def tick(f, x, y, lab):
    f.line(x, y, x, y + 8, stroke=INK, w=2)
    f.text(x, y + 30, lab, size=19)


def hump(f, xa, xb, y, h, fill, stroke=INK, dash=None, high_at='b'):
    """Voice-shaped sideband between xa and xb; taller towards `high_at`."""
    if high_at == 'b':
        d = f'M{xa} {y} L{xa} {y - h * 0.45} L{xb} {y - h} L{xb} {y} Z'
    else:
        d = f'M{xa} {y} L{xa} {y - h} L{xb} {y - h * 0.45} L{xb} {y} Z'
    f.path(d, stroke=stroke, w=3, fill=fill, dash=dash)


# 8 ── AM with a single tone ───────────────────────────────────────────────
f = Fig('s06-am-tono', 400, 'Portadora de 7.000 kHz modulada con un tono de 1 kHz: tres señales')
f.text(320, 42, 'Un tono de 1 kHz sobre 7.000 kHz: tres señales', size=22, weight='bold')
Y = 290
axis(f, Y, label='kHz')
for x, h, lab, col, name in [(180, 90, '6.999', BLUE, 'nueva'), (320, 180, '7.000', RED, 'portadora'), (460, 90, '7.001', BLUE, 'nueva')]:
    f.line(x, Y, x, Y - h, stroke=col, w=8, cap='butt')
    tick(f, x, Y, lab)
    f.text(x, Y - h - 14, name, size=19, weight='bold', fill=col)
f.line(188, Y - 140, 312, Y - 140, stroke=MUTED, w=2, arrow=True)
f.line(312, Y - 140, 190, Y - 140, stroke=MUTED, w=2, arrow=True)
f.text(250, Y - 152, '1 kHz', size=18, fill=MUTED)
f.line(328, Y - 140, 452, Y - 140, stroke=MUTED, w=2, arrow=True)
f.line(452, Y - 140, 330, Y - 140, stroke=MUTED, w=2, arrow=True)
f.text(390, Y - 152, '1 kHz', size=18, fill=MUTED)
f.text(320, 376, 'Entre ellas no hay nada: son tres señales separadas', size=19, fill=MUTED)
f.save()

# 9 ── AM spectrum with voice ──────────────────────────────────────────────
f = Fig('s06-am-espectro', 430, 'Espectro de una señal de AM con voz')
f.text(320, 42, 'AM con voz: las tres jorobas de Dani', size=22, weight='bold')
Y = 290
axis(f, Y, label='kHz')
hump(f, 140, 302, Y, 90, '#BFDBFE', high_at='b')
hump(f, 338, 500, Y, 90, '#BFDBFE', high_at='a')
f.line(320, Y, 320, Y - 190, stroke=RED, w=8, cap='butt')
f.text(320, Y - 202, 'portadora', size=19, weight='bold', fill=RED)
f.text(190, Y - 136, 'banda lateral', size=19, weight='bold', fill=BLUE)
f.text(190, Y - 112, 'inferior (LSB)', size=19, weight='bold', fill=BLUE)
f.text(456, Y - 136, 'banda lateral', size=19, weight='bold', fill=BLUE)
f.text(456, Y - 112, 'superior (USB)', size=19, weight='bold', fill=BLUE)
tick(f, 140, Y, '6.997'); tick(f, 320, Y, '7.000'); tick(f, 500, Y, '7.003')
f.line(142, 372, 498, 372, stroke=AMBER, w=3, arrow=True)
f.line(498, 372, 144, 372, stroke=AMBER, w=3, arrow=True)
f.text(320, 404, 'ancho de banda: 6 kHz (2 × 3 kHz)', size=20, weight='bold', fill=AMBER)
f.save()

# 10 ── SSB spectrum ───────────────────────────────────────────────────────
f = Fig('s06-ssb-espectro', 560, 'De AM a banda lateral única')
f.text(320, 42, 'De AM a banda lateral única', size=22, weight='bold')
Y = 230
f.text(70, 84, 'AM', size=22, weight='bold', anchor='start')
axis(f, Y, label='kHz')
hump(f, 140, 302, Y, 80, '#BFDBFE', high_at='b')
hump(f, 338, 500, Y, 80, '#BFDBFE', high_at='a')
f.line(320, Y, 320, Y - 150, stroke=RED, w=8, cap='butt')
tick(f, 140, Y, '7.097'); tick(f, 320, Y, '7.100'); tick(f, 500, Y, '7.103')
f.text(540, 110, '6 kHz', size=22, weight='bold', fill=AMBER, anchor='end')
f.line(50, 296, 590, 296, stroke=PAPER_EDGE, w=2)
Y = 480
f.text(70, 334, 'SSB (banda inferior)', size=22, weight='bold', anchor='start')
axis(f, Y, label='kHz')
hump(f, 140, 302, Y, 80, '#BFDBFE', high_at='b')
hump(f, 338, 500, Y, 80, 'none', stroke=MUTED, dash='6 6', high_at='a')
f.line(320, Y, 320, Y - 150, stroke=MUTED, w=4, dash='6 6', cap='butt')
for cx, cy in [(320, Y - 110), (420, Y - 44)]:
    f.line(cx - 16, cy - 16, cx + 16, cy + 16, stroke=RED, w=5)
    f.line(cx - 16, cy + 16, cx + 16, cy - 16, stroke=RED, w=5)
f.text(326, Y - 160, 'sin portadora', size=18, fill=MUTED, anchor='start')
f.text(440, Y - 100, 'sin esta copia', size=18, fill=MUTED)
tick(f, 140, Y, '7.097'); tick(f, 320, Y, '7.100'); tick(f, 500, Y, '7.103')
f.text(200, Y - 100, '2,7 kHz', size=22, weight='bold', fill=AMBER)
f.save()

# 11 ── FM waveform ────────────────────────────────────────────────────────
f = Fig('s06-fm-onda', 450, 'FM: amplitud constante, frecuencia variable')
f.text(320, 42, 'FM: el tamaño no cambia, cambia el ritmo', size=22, weight='bold')
f.text(320, 82, 'La señal de audio', size=19, fill=BLUE, weight='bold')
f.line(X0, 130, X1, 130, stroke=MUTED, w=1)
f.path(wave(X0, X1, 130, lambda t: 34 * math.sin(TAU * 2 * t)), stroke=BLUE, w=4)
f.text(320, 206, 'La portadora, modulada en frecuencia', size=19, fill=RED, weight='bold')
f.line(X0, 300, X1, 300, stroke=MUTED, w=1)
N = 2400
phase, pts = 0.0, []
for k in range(N + 1):
    t = k / N
    inst = 30 + 17 * math.sin(TAU * 2 * t)      # instantaneous cycles across the width
    phase += TAU * inst / N
    pts.append((X0 + (X1 - X0) * t, 300 - 56 * math.sin(phase)))
f.path(poly(pts), stroke=RED, w=2)
f.text(190, 396, 'audio alto:', size=18, fill=MUTED); f.text(190, 420, 'más apretada', size=19, weight='bold')
f.text(450, 396, 'audio bajo:', size=18, fill=MUTED); f.text(450, 420, 'más separada', size=19, weight='bold')
f.save()

# 12 ── waterfall ──────────────────────────────────────────────────────────
f = Fig('s06-cascada', 480, 'Las huellas de AM, SSB, CW y FT8 en una cascada')
f.text(320, 42, 'Cómo se ve cada modo en la cascada', size=22, weight='bold')
PX, PY, PW, PH = 70, 96, 540, 300
f.rect(PX, PY, PW, PH, fill='#0B2545', rx=8)
f.text(PX + PW / 2, 84, 'frecuencia →', size=18, fill=MUTED)
f.text(40, PY + PH / 2, 'tiempo', size=18, fill=MUTED, rotate=-90)
f.line(56, PY + 20, 56, PY + PH - 20, stroke=MUTED, w=3, arrow=True)
# AM
f.rect(96, PY, 120, PH, fill='#F59E0B', rx=0)
f.add(f'<rect x="96" y="{PY}" width="120" height="{PH}" fill="#0B2545" opacity="0.45"/>')
f.rect(152, PY, 8, PH, fill='#FEF3C7', rx=0)
# SSB: one-sided blobs with gaps
for y0, h, w in [(PY + 6, 44, 62), (PY + 62, 28, 50), (PY + 104, 60, 66), (PY + 186, 34, 56), (PY + 236, 52, 64)]:
    f.rect(322 - w, y0, w, h, fill='#FBBF24', rx=3)
# CW dashes
y = PY + 8
for h in [10, 30, 10, 10, 30, 30, 10, 30, 10]:
    f.rect(385, y, 5, h, fill='#FEF3C7', rx=0)
    y += h + 12
assert y - 12 <= PY + PH - 6
# FT8 blocks
import random
random.seed(3)
for b in range(4):
    y0 = PY + 8 + b * 73
    for x in random.sample(range(452, 588, 9), 7):
        f.rect(x, y0, 4, 56, fill='#FDE68A', rx=0)
for x, lab in [(156, 'AM'), (290, 'SSB'), (388, 'CW'), (520, 'FT8')]:
    f.text(x, PY + PH + 30, lab, size=22, weight='bold')
f.text(320, 460, 'Cada modo deja su huella: es su espectro, visto desde arriba', size=18, fill=MUTED)
f.save()

# 13 ── bandwidth comparison ───────────────────────────────────────────────
f = Fig('s06-anchos-de-banda', 420, 'El ancho de banda de cada modo, a escala')
f.text(320, 42, 'Cuánto dial ocupa cada modo (a escala)', size=22, weight='bold')
rows = [('FT8', 0.05, '50 Hz'), ('CW', 0.15, '150 Hz'), ('SSB', 2.7, '2,7 kHz'), ('AM', 6, '6 kHz'), ('FM', 16, '16 kHz')]
for k, (name, khz, lab) in enumerate(rows):
    y = 84 + k * 60
    w = max(2, 380 * khz / 16)
    f.text(96, y + 27, name, size=22, weight='bold', anchor='end')
    f.rect(112, y, w, 38, fill=[GREEN, GREEN, BLUE, AMBER, RED][k], rx=0 if w < 8 else 6)
    f.text(112 + w + 12, y + 27, lab, size=20, anchor='start', weight='bold' if khz < 1 else 'normal')
f.text(320, 400, 'El morse y el FT8 son alfileres: apenas se ven', size=19, fill=MUTED)
f.save()
