"""Figures of section 3 (alternating current, frequency, wavelength, harmonics, decibels)."""
import math
from figlib import *


def wave(f, x0, y0, width, amp, fn, stroke=BLUE, w=4, dash=None, n=240):
    """Plot fn(t) for t in [0,1] as a path: x0..x0+width, centred on y0, height ±amp."""
    pts = []
    for k in range(n + 1):
        t = k / n
        pts.append(f'{x0 + width * t:.1f} {y0 - amp * fn(t):.1f}')
    f.path('M' + ' L'.join(pts), stroke=stroke, w=w, dash=dash)


def axis(f, x0, y0, width, label='tiempo', top=None, bottom=None):
    f.line(x0, y0, x0 + width + 14, y0, stroke=MUTED, w=2, arrow=True)
    if top is not None:
        f.line(x0, top, x0, bottom, stroke=MUTED, w=2)
    if label:
        f.text(x0 + width + 14, y0 + 26, label, size=18, anchor='end', fill=MUTED)


sin = lambda cycles, ph=0.0: (lambda t: math.sin(2 * math.pi * (cycles * t) + ph))

# 1 ── DC vs AC ────────────────────────────────────────────────────────────
f = Fig('s03-continua-y-alterna', 560, 'Corriente continua y corriente alterna')
f.text(320, 42, 'Continua: siempre igual', size=22, weight='bold')
axis(f, 90, 170, 500, top=70, bottom=230)
f.text(74, 100, '+', size=24, weight='bold', fill=RED, anchor='end')
f.text(74, 177, '0', size=20, fill=MUTED, anchor='end')
f.text(74, 228, '−', size=24, weight='bold', fill=BLUE, anchor='end')
f.line(90, 105, 540, 105, stroke=AMBER, w=5)
f.text(325, 92, 'la tensión no cambia', size=19, fill=AMBER)
f.line(50, 262, 590, 262, stroke=PAPER_EDGE, w=2)
f.text(320, 300, 'Alterna: va y viene', size=22, weight='bold')
axis(f, 90, 410, 500, top=320, bottom=500)
f.text(74, 348, '+', size=24, weight='bold', fill=RED, anchor='end')
f.text(74, 417, '0', size=20, fill=MUTED, anchor='end')
f.text(74, 486, '−', size=24, weight='bold', fill=BLUE, anchor='end')
wave(f, 90, 410, 450, 70, sin(2.5), stroke=AMBER, w=5)
f.text(320, 534, 'Por encima del cero empuja en un sentido; por debajo, en el otro', size=18, fill=MUTED)
f.save()

# 2 ── cycle and period ────────────────────────────────────────────────────
f = Fig('s03-ciclo-y-periodo', 400, 'Ciclo y periodo de una senoide')
f.text(320, 42, 'Un ciclo y su duración: el periodo', size=22, weight='bold')
X0, W, Y0, A = 70, 440, 220, 80
cyc = W / 2
f.rect(X0 + cyc / 4, Y0 - A - 34, cyc, 2 * A + 56, fill='#FDE68A', rx=10)
axis(f, X0, Y0, W + 70, top=Y0 - A - 20, bottom=Y0 + A + 20)
wave(f, X0, Y0, W, A, sin(2), stroke=BLUE, w=5)
xa, xb = X0 + cyc / 4, X0 + cyc / 4 + cyc
f.line(xa + 4, Y0 - A - 18, xb - 4, Y0 - A - 18, stroke=INK, w=3, arrow=True)
f.line(xb - 4, Y0 - A - 18, xa + 4, Y0 - A - 18, stroke=INK, w=3, arrow=True)
f.text((xa + xb) / 2, Y0 - A - 30, 'periodo T (un ciclo)', size=20, weight='bold')
f.circle(xa, Y0 - A, 6, fill=RED, stroke=RED); f.circle(xb, Y0 - A, 6, fill=RED, stroke=RED)
f.text(xb + 14, Y0 - A - 4, 'cresta', size=18, anchor='start', fill=RED)
f.circle(X0 + cyc * 0.75, Y0 + A, 6, fill=BLUE, stroke=BLUE)
f.text(X0 + cyc * 0.75, Y0 + A + 30, 'valle', size=18, fill=BLUE)
f.text(X0 - 8, Y0 + 7, '0', size=20, anchor='end', fill=MUTED)
f.text(320, 376, 'De una cresta a la siguiente: un ciclo completo', size=19, fill=MUTED)
f.save()

# 3 ── frequency ───────────────────────────────────────────────────────────
f = Fig('s03-frecuencia', 550, 'Frecuencia: ciclos por segundo')
f.text(320, 42, 'Los mismos segundos, distinto ritmo', size=22, weight='bold')
for k, (n, lab, per) in enumerate([(2, '2 ciclos en 1 segundo: 2 Hz', 'T = medio segundo'),
                                   (6, '6 ciclos en 1 segundo: 6 Hz', 'T = un sexto de segundo')]):
    y = 160 + k * 240
    f.rect(40, y - 94, 560, 216, fill=SOFT, rx=14)
    f.text(320, y - 64, lab, size=21, weight='bold', fill=BLUE if k == 0 else RED)
    f.line(80, y + 20, 560, y + 20, stroke=MUTED, w=2)
    wave(f, 80, y + 20, 480, 44, sin(n), stroke=BLUE if k == 0 else RED, w=4)
    f.line(84, y + 82, 556, y + 82, stroke=INK, w=2, arrow=True)
    f.line(556, y + 82, 84, y + 82, stroke=INK, w=2, arrow=True)
    f.text(320, y + 106, '1 segundo', size=18, fill=MUTED)
    pw = 480 / n
    f.line(80 + pw / 4 + 3, y - 34, 80 + pw / 4 + pw - 3, y - 34, stroke=AMBER, w=3, arrow=True)
    f.line(80 + pw / 4 + pw - 3, y - 34, 80 + pw / 4 + 3, y - 34, stroke=AMBER, w=3, arrow=True)
    f.text(80 + pw / 4 + pw + 10, y - 28, per, size=18, fill=AMBER, anchor='start', weight='bold')
f.save()

# 4 ── peak, peak-to-peak, RMS ─────────────────────────────────────────────
f = Fig('s03-pico-y-eficaz', 490, 'Valor de pico, de pico a pico y eficaz')
f.text(320, 42, 'Tres maneras de medir la misma onda', size=22, weight='bold')
X0, W, Y0, A = 150, 330, 230, 120
f.line(X0, Y0, X0 + W + 10, Y0, stroke=MUTED, w=2)
wave(f, X0, Y0, W, A, sin(1.5), stroke=BLUE, w=5)
f.text(X0 - 10, Y0 + 7, '0', size=20, anchor='end', fill=MUTED)
# RMS line
f.line(X0, Y0 - 0.707 * A, X0 + W + 10, Y0 - 0.707 * A, stroke=GREEN, w=3, dash='8 7')
f.text(X0 + W + 16, Y0 - 0.707 * A - 12, 'eficaz', size=20, weight='bold', fill=GREEN, anchor='start')
f.text(X0 + W + 16, Y0 - 0.707 * A + 12, '0,707 × pico', size=18, fill=GREEN, anchor='start')
# peak arrow (at first crest x = X0 + W/6)
xc = X0 + W / 6
f.line(xc, Y0 - 4, xc, Y0 - A + 6, stroke=RED, w=3, arrow=True)
f.line(xc, Y0 - A + 6, xc, Y0 - 4, stroke=RED, w=3, arrow=True)
f.text(xc + 10, Y0 - A / 2 + 16, 'pico', size=19, weight='bold', fill=RED, anchor='start')
# peak-to-peak arrow at left
f.line(60, Y0 - A, X0 + W / 6, Y0 - A, stroke=MUTED, w=2, dash='4 6')
f.line(60, Y0 + A, X0 + W / 2, Y0 + A, stroke=MUTED, w=2, dash='4 6')
f.line(70, Y0 - A + 6, 70, Y0 + A - 6, stroke=AMBER, w=3, arrow=True)
f.line(70, Y0 + A - 6, 70, Y0 - A + 6, stroke=AMBER, w=3, arrow=True)
f.text(52, Y0 + 6, 'pico a pico', size=20, weight='bold', fill=AMBER, rotate=-90)
f.text(320, 400, 'pico a pico = 2 × pico', size=20, weight='bold')
f.text(320, 434, 'eficaz = 0,707 × pico', size=20, weight='bold', fill=GREEN)
f.text(320, 466, 'pico = 1,414 × eficaz', size=20, weight='bold', fill=RED)
f.save()

# 5 ── phase ───────────────────────────────────────────────────────────────
f = Fig('s03-fase', 640, 'Dos ondas en fase se refuerzan; en oposición de fase se anulan')
for k, (title, ph, res, restxt) in enumerate([('En fase (0°): se refuerzan', 0.0, 2, 'el doble'),
                                              ('En oposición de fase (180°): se anulan', math.pi, 0, 'cero')]):
    y = 20 + k * 310
    f.text(320, y + 26, title, size=22, weight='bold', fill=GREEN if k == 0 else RED)
    f.rect(40, y + 40, 560, 250, fill=SOFT, rx=14)
    ya, yb, ys = y + 78, y + 134, y + 226
    for yy in (ya, yb, ys):
        f.line(170, yy, 580, yy, stroke=MUTED, w=2)
    wave(f, 170, ya, 410, 20, sin(2), stroke=BLUE, w=4)
    wave(f, 170, yb, 410, 20, sin(2, ph), stroke=AMBER, w=4)
    wave(f, 170, ys, 410, 20 * res, sin(2), stroke=GREEN if k == 0 else RED, w=5)
    f.text(156, ya + 7, 'onda A', size=19, anchor='end', fill=BLUE, weight='bold')
    f.text(156, yb + 7, 'onda B', size=19, anchor='end', fill=AMBER, weight='bold')
    f.text(156, ys + 7, 'A + B', size=19, anchor='end', weight='bold')
    f.line(60, y + 168, 580, y + 168, stroke=PAPER_EDGE, w=2)
    f.text(156, ys + 32, restxt, size=18, anchor='end', fill=MUTED)
f.save()

# 6 ── wavelength ──────────────────────────────────────────────────────────
f = Fig('s03-longitud-de-onda', 420, 'Longitud de onda: la distancia entre dos crestas')
f.text(320, 42, 'La longitud de onda es una distancia', size=22, weight='bold')
# antenna
f.line(80, 130, 80, 300, stroke=INK, w=6)
f.line(56, 300, 104, 300, stroke=INK, w=5)
f.text(80, 116, 'antena', size=19, fill=MUTED)
X0, W, Y0, A = 110, 440, 215, 60
wave(f, X0, Y0, W, A, sin(2.75), stroke=BLUE, w=5)
f.line(X0, Y0, X0 + W + 14, Y0, stroke=MUTED, w=2)
cyc = W / 2.75
xa, xb = X0 + cyc * 0.25, X0 + cyc * 1.25
f.line(xa, Y0 - A - 8, xa, Y0 - A - 44, stroke=INK, w=2); f.line(xb, Y0 - A - 8, xb, Y0 - A - 44, stroke=INK, w=2)
f.line(xa + 5, Y0 - A - 30, xb - 5, Y0 - A - 30, stroke=RED, w=4, arrow=True)
f.line(xb - 5, Y0 - A - 30, xa + 5, Y0 - A - 30, stroke=RED, w=4, arrow=True)
f.text((xa + xb) / 2, Y0 - A - 44, 'longitud de onda λ', size=20, weight='bold', fill=RED)
f.line(150, 320, 520, 320, stroke=INK, w=3, arrow=True)
f.text(335, 348, 'distancia (metros): la onda se aleja', size=19, fill=MUTED)
f.text(320, 392, 'λ (metros) = 300 / f (MHz)', size=24, weight='bold')
f.save()

# 7 ── Amparo's ruler ──────────────────────────────────────────────────────
f = Fig('s03-regla-de-amparo', 446, 'La regla de Amparo: megahercios y metros')
f.text(320, 42, 'La regla de Amparo', size=22, weight='bold')
f.rect(30, 90, 580, 230, fill='#FBE9A9', stroke='#C9A227', sw=3, rx=10)
pairs = [('1,8', '160'), ('3,5', '80'), ('7', '40'), ('14', '20'), ('28', '10'), ('50', '6'), ('144', '2'), ('430', '0,7')]
f.text(48, 124, 'MHz', size=20, weight='bold', anchor='start', fill=BLUE)
f.text(48, 304, 'metros', size=20, weight='bold', anchor='start', fill=RED)
f.line(48, 205, 592, 205, stroke='#C9A227', w=3)
for k, (mhz, m) in enumerate(pairs):
    x = 78 + k * 69
    f.line(x, 180, x, 230, stroke=INK, w=3)
    f.text(x, 168, mhz, size=20, weight='bold', fill=BLUE)
    f.text(x, 258, m, size=20, weight='bold', fill=RED)
f.line(200, 132, 560, 132, stroke=BLUE, w=3, arrow=True)
f.text(380, 124, 'crece', size=18, fill=BLUE)
f.line(560, 290, 200, 290, stroke=RED, w=3, arrow=True)
f.text(380, 312, 'crece', size=18, fill=RED)
f.text(320, 360, 'MHz × metros ≈ 300', size=22, weight='bold')
f.text(320, 390, '(los nombres de las bandas son redondeos)', size=18, fill=MUTED)
f.text(320, 420, 'Si una escala sube, la otra baja', size=19, fill=MUTED)
f.save()

# 8 ── spectrum ────────────────────────────────────────────────────────────
f = Fig('s03-espectro', 620, 'Los tramos del espectro radioeléctrico')
f.text(320, 42, 'El espectro, tramo a tramo', size=22, weight='bold')
rows = [('VLF', '3 a 30 kHz', '100 a 10 km', False), ('LF', '30 a 300 kHz', '10 a 1 km', False),
        ('MF', '300 kHz a 3 MHz', '1.000 a 100 m', False), ('HF', '3 a 30 MHz', '100 a 10 m', True),
        ('VHF', '30 a 300 MHz', '10 a 1 m', True), ('UHF', '300 MHz a 3 GHz', '1 m a 10 cm', True),
        ('SHF', '3 a 30 GHz', '10 a 1 cm', False), ('EHF', '30 a 300 GHz', '1 cm a 1 mm', False)]
f.text(130, 78, 'tramo', size=18, fill=MUTED); f.text(300, 78, 'frecuencias', size=18, fill=MUTED)
f.text(500, 78, 'longitud de onda', size=18, fill=MUTED)
for k, (s, fr, wl, hot) in enumerate(rows):
    y = 92 + k * 58
    f.rect(84, y, 500, 48, fill='#FDE68A' if hot else '#FFFFFF', stroke=INK, sw=2, rx=10)
    f.text(130, y + 33, s, size=24, weight='bold', fill='#9A3412' if hot else INK)
    f.text(300, y + 32, fr, size=20, weight='bold' if hot else 'normal')
    f.text(500, y + 32, wl, size=19, fill=MUTED)
f.line(48, 100, 48, 548, stroke=BLUE, w=5, arrow=True)
f.text(34, 324, 'más frecuencia', size=19, weight='bold', fill=BLUE, rotate=-90)
f.text(320, 592, 'Cada tramo: diez veces más frecuencia que el anterior', size=19, fill=MUTED)
f.save()

# 9 ── sum of harmonics ────────────────────────────────────────────────────
f = Fig('s03-suma-de-armonicos', 640, 'Sumando senoides se construye una onda cuadrada')
f.text(320, 42, 'Sumar senoides cambia la forma de la onda', size=22, weight='bold')
h1 = lambda t: math.sin(2 * math.pi * 2 * t)
h3 = lambda t: h1(t) + math.sin(2 * math.pi * 6 * t) / 3
h5 = lambda t: h3(t) + math.sin(2 * math.pi * 10 * t) / 5
sq = lambda t: (math.pi / 4) * (1 if math.sin(2 * math.pi * 2 * t) >= 0 else -1)
for k, (fn, lab) in enumerate([(h1, 'Solo la fundamental'), (h3, 'Fundamental + 3.er armónico'),
                               (h5, 'Fundamental + 3.º + 5.º armónico')]):
    y = 150 + k * 180
    f.rect(40, y - 84, 560, 166, fill=SOFT, rx=14)
    f.text(320, y - 56, lab, size=20, weight='bold')
    f.line(70, y + 14, 570, y + 14, stroke=MUTED, w=2)
    if k == 2:
        pts = []
        n = 400
        for i in range(n + 1):
            t = i / n
            pts.append(f'{70 + 500 * t:.1f} {y + 14 - 52 * sq(t):.1f}')
        f.path('M' + ' L'.join(pts), stroke=RED, w=3, dash='6 6')
    wave(f, 70, y + 14, 500, 52, fn, stroke=BLUE, w=4, n=400)
f.text(320, 620, 'Línea de puntos: la onda cuadrada a la que se va acercando', size=18, fill=MUTED)
f.save()

# 10 ── clipped wave and its spectrum ──────────────────────────────────────
f = Fig('s03-onda-recortada', 560, 'Una onda recortada contiene armónicos')
f.text(320, 42, 'Deformar la onda hace aparecer armónicos', size=22, weight='bold')
clip = lambda t: min(0.45, math.sin(2 * math.pi * 2 * t))
for k, (fn, lab, bars) in enumerate([(sin(2), 'Senoide limpia', [1, 0, 0, 0]),
                                     (clip, 'Cresta recortada', [1, 0.36, 0.2, 0.1])]):
    y = 70 + k * 245
    f.rect(30, y, 580, 225, fill=SOFT, rx=14)
    f.text(160, y + 34, lab, size=20, weight='bold', fill=GREEN if k == 0 else RED)
    f.text(450, y + 34, 'frecuencias que contiene', size=18, fill=MUTED)
    f.line(50, y + 115, 280, y + 115, stroke=MUTED, w=2)
    wave(f, 50, y + 115, 230, 56, fn, stroke=GREEN if k == 0 else RED, w=4)
    f.line(330, y + 170, 590, y + 170, stroke=INK, w=2)
    for j, (b, mhz) in enumerate(zip(bars, ['7', '14', '21', '28'])):
        x = 350 + j * 60
        if b:
            f.rect(x, y + 170 - 110 * b, 34, 110 * b, fill=BLUE if j == 0 else RED, rx=4)
        f.text(x + 17, y + 196, mhz, size=19, weight='bold' if b else 'normal', fill=INK if b else MUTED)
    f.text(460, y + 216, 'MHz', size=18, fill=MUTED)
f.save()

# 11 ── decibel ladder ─────────────────────────────────────────────────────
f = Fig('s03-escalera-decibelios', 640, 'La escalera de los decibelios')
f.text(320, 42, 'Decibelios y potencia', size=22, weight='bold')
rows = [('+30 dB', '× 1.000'), ('+20 dB', '× 100'), ('+10 dB', '× 10'), ('+6 dB', '× 4'), ('+3 dB', '× 2'),
        ('0 dB', 'no cambia'), ('−3 dB', '÷ 2'), ('−6 dB', '÷ 4'), ('−10 dB', '÷ 10'), ('−20 dB', '÷ 100'),
        ('−30 dB', '÷ 1.000')]
for k, (db, x) in enumerate(rows):
    y = 62 + k * 48
    mid = k == 5
    col = GREEN if k < 5 else (INK if mid else RED)
    key = db in ('+10 dB', '+3 dB', '−3 dB', '−10 dB')
    f.rect(150, y, 340, 40, fill='#FDE68A' if mid else '#FFFFFF', stroke=INK, sw=3 if key else 2, rx=10)
    f.text(250, y + 29, db, size=23, weight='bold', fill=col)
    f.text(400, y + 29, x, size=23, weight='bold' if key or mid else 'normal')
f.line(100, 296, 100, 70, stroke=GREEN, w=5, arrow=True)
f.text(78, 184, 'ganancia', size=20, weight='bold', fill=GREEN, rotate=-90)
f.line(100, 350, 100, 580, stroke=RED, w=5, arrow=True)
f.text(78, 466, 'pérdida', size=20, weight='bold', fill=RED, rotate=-90)
f.text(562, 318, 'sumar dB', size=18, fill=MUTED); f.text(562, 342, '= multiplicar', size=18, fill=MUTED)
f.text(320, 618, '3 dB: el doble. 10 dB: diez veces', size=20, weight='bold')
f.save()

# 12 ── station chain in dB ────────────────────────────────────────────────
f = Fig('s03-cadena-en-decibelios', 480, 'La cadena de una estación en decibelios')
f.text(320, 42, 'Una estación, sumando decibelios', size=22, weight='bold')
boxes = [(40, 'transmisor', '', INK), (240, 'cable', '−3 dB', RED), (440, 'antena', '+6 dB', GREEN)]
for x, name, db, col in boxes:
    f.rect(x, 90, 160, 96, fill='#FFFFFF', stroke=col, sw=4, rx=12)
    f.text(x + 80, 132, name, size=21, weight='bold')
    if db:
        f.text(x + 80, 166, db, size=24, weight='bold', fill=col)
f.line(202, 138, 236, 138, stroke=INK, w=4, arrow=True)
f.line(402, 138, 436, 138, stroke=INK, w=4, arrow=True)
for x, wtt, note in [(120, '100 W', 'sale'), (320, '50 W', 'llega a la antena'), (520, '200 W', 'equivalentes')]:
    f.line(x, 190, x, 228, stroke=MUTED, w=2, dash='4 5')
    f.text(x, 262, wtt, size=28, weight='bold', fill=BLUE)
    f.text(x, 290, note, size=18, fill=MUTED)
f.text(220, 250, '÷ 2', size=22, weight='bold', fill=RED)
f.text(420, 250, '× 4', size=22, weight='bold', fill=GREEN)
f.rect(60, 330, 520, 112, fill=SOFT, rx=14)
f.text(320, 372, '−3 dB + 6 dB = +3 dB', size=28, weight='bold')
f.text(320, 414, '+3 dB es el doble: 100 W → 200 W', size=21, fill=MUTED)
f.save()

# 13 ── mean power is half the peak power ──────────────────────────────────
f = Fig('s03-potencia-media', 560, 'La potencia media de una alterna es la mitad de la potencia de cresta')
f.text(320, 42, 'La potencia media es la mitad de la de cresta', size=22, weight='bold')
X0, W = 110, 440
f.text(X0, 84, 'tensión', size=19, weight='bold', fill=BLUE, anchor='start')
f.line(X0, 150, X0 + W, 150, stroke=MUTED, w=2)
wave(f, X0, 150, W, 50, sin(2), stroke=BLUE, w=4)
f.text(X0 - 10, 157, '0', size=20, anchor='end', fill=MUTED)
f.line(50, 222, 590, 222, stroke=PAPER_EDGE, w=2)
f.text(X0, 256, 'potencia (tensión al cuadrado)', size=19, weight='bold', fill=RED, anchor='start')
BASE, TOP = 470, 290
MID = (BASE + TOP) / 2
pw = lambda t: math.sin(2 * math.pi * 2 * t) ** 2
# fill: area above mid (amber) and gaps below mid (hatched light)
n = 400
up = ['M%.1f %.1f' % (X0, MID)]
for i in range(n + 1):
    t = i / n
    y = BASE - (BASE - TOP) * pw(t)
    up.append('L%.1f %.1f' % (X0 + W * t, min(y, MID)))
up.append('L%.1f %.1f Z' % (X0 + W, MID))
f.add('<path d="%s" fill="#FDBA74" stroke="none"/>' % ' '.join(up))
dn = ['M%.1f %.1f' % (X0, MID)]
for i in range(n + 1):
    t = i / n
    y = BASE - (BASE - TOP) * pw(t)
    dn.append('L%.1f %.1f' % (X0 + W * t, max(y, MID)))
dn.append('L%.1f %.1f Z' % (X0 + W, MID))
f.add('<path d="%s" fill="#FFFFFF" stroke="#FDBA74" stroke-width="2" stroke-dasharray="5 5"/>' % ' '.join(dn))
f.line(X0, BASE, X0 + W, BASE, stroke=MUTED, w=2)
pts = ['%.1f %.1f' % (X0 + W * i / n, BASE - (BASE - TOP) * pw(i / n)) for i in range(n + 1)]
f.path('M' + ' L'.join(pts), stroke=RED, w=4)
f.line(X0 - 6, MID, X0 + W + 6, MID, stroke=GREEN, w=3, dash='8 7')
f.text(X0 - 10, BASE + 7, '0', size=20, anchor='end', fill=MUTED)
f.text(X0 - 10, TOP + 7, 'cresta', size=18, anchor='end', fill=RED)
f.text(X0 - 10, MID + 7, 'mitad', size=18, anchor='end', fill=GREEN, weight='bold')
f.text(320, 510, 'Las cimas (naranja) encajan en los huecos (blanco):', size=19, fill=MUTED)
f.text(320, 538, 'la media queda justo a media altura', size=19, fill=MUTED)
f.save()
