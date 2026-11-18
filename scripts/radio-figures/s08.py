"""Figures of section 8 (antennas and transmission lines)."""
import math
from figlib import *


def wave_path(x0, x1, y, amp, cycles, phase=0.0, steps=120):
    pts = []
    for k in range(steps + 1):
        t = k / steps
        x = x0 + (x1 - x0) * t
        pts.append((x, y - amp * math.sin(2 * math.pi * cycles * t + phase)))
    return 'M' + ' L'.join(f'{x:.1f} {yy:.1f}' for x, yy in pts)


def half_sine(x0, x1, y, amp, steps=60, fn=math.sin):
    pts = []
    for k in range(steps + 1):
        t = k / steps
        pts.append((x0 + (x1 - x0) * t, y - amp * fn(math.pi * t)))
    return 'M' + ' L'.join(f'{x:.1f} {yy:.1f}' for x, yy in pts)


# 1 ── standing wave on a rope ─────────────────────────────────────────────
f = Fig('s08-cuerda-estacionaria', 380, 'Onda estacionaria en una cuerda sujeta por los dos extremos')
f.text(320, 44, 'La cuerda de la comba: una onda estacionaria', size=21, weight='bold')
Y = 190
f.rect(52, Y - 60, 16, 120, fill=INK, rx=4)
f.rect(572, Y - 60, 16, 120, fill=INK, rx=4)
f.path(half_sine(68, 572, Y, 78), stroke=AMBER, w=5)
f.path(half_sine(68, 572, Y, -78), stroke=AMBER, w=3, dash='8 8')
f.path(half_sine(68, 572, Y, 40), stroke=AMBER, w=2, dash='4 8')
f.path(half_sine(68, 572, Y, -40), stroke=AMBER, w=2, dash='4 8')
f.line(320, Y - 70, 320, Y + 70, stroke=BLUE, w=3, arrow=True)
f.line(320, Y + 70, 320, Y - 70, stroke=BLUE, w=3, arrow=True)
f.text(336, Y + 8, 'máximo vaivén', size=19, anchor='start', fill=BLUE, weight='bold')
f.text(84, Y - 76, 'quieto', size=19, anchor='start', fill=MUTED)
f.text(556, Y - 76, 'quieto', size=19, anchor='end', fill=MUTED)
f.line(68, 316, 572, 316, stroke=GREEN, w=3, arrow=True)
f.line(572, 316, 68, 316, stroke=GREEN, w=3, arrow=True)
f.text(320, 350, 'entre los dos extremos cabe media onda', size=20, weight='bold', fill=GREEN)
f.save()

# 2 ── current and voltage along a half-wave wire ──────────────────────────
f = Fig('s08-corriente-y-tension', 440, 'Corriente y tensión a lo largo de un hilo de media onda')
f.text(320, 44, 'Corriente y tensión en un hilo de media onda', size=21, weight='bold')
Y = 250
f.line(70, Y, 570, Y, stroke=WIRE, w=6)
f.circle(320, Y, 8, fill=PAPER, stroke=INK, sw=3)
# current: half sine, max in centre
f.path(half_sine(70, 570, Y, 120), stroke=BLUE, w=4)
# voltage magnitude: |cos|, max at tips
pts = []
for k in range(81):
    t = k / 80
    pts.append((70 + 500 * t, Y - 120 * abs(math.cos(math.pi * t))))
f.path('M' + ' L'.join(f'{x:.1f} {yy:.1f}' for x, yy in pts), stroke=RED, w=4, dash='10 7')
f.text(320, 112, 'corriente máxima', size=19, fill=BLUE, weight='bold')
f.text(74, 86, 'tensión', size=19, anchor='start', fill=RED, weight='bold')
f.text(74, 108, 'máxima', size=19, anchor='start', fill=RED, weight='bold')
f.text(566, 86, 'tensión', size=19, anchor='end', fill=RED, weight='bold')
f.text(566, 108, 'máxima', size=19, anchor='end', fill=RED, weight='bold')
f.text(70, Y + 34, 'punta', size=19, fill=MUTED)
f.text(570, Y + 34, 'punta', size=19, fill=MUTED)
f.text(320, Y + 34, 'centro', size=19, fill=MUTED)
f.line(60, 330, 110, 330, stroke=BLUE, w=4)
f.text(120, 337, 'corriente: cero en las puntas, máxima en el centro', size=18, anchor='start', fill=INK)
f.line(60, 366, 110, 366, stroke=RED, w=4, dash='10 7')
f.text(120, 373, 'tensión: máxima en las puntas, mínima en el centro', size=18, anchor='start', fill=INK)
f.text(320, 412, 'El cable se conecta en el centro; las puntas no se tocan', size=18, fill=MUTED)
f.save()

# 3 ── parts of a dipole ───────────────────────────────────────────────────
f = Fig('s08-dipolo-partes', 470, 'Partes y medidas de un dipolo de media onda')
f.text(320, 44, 'El dipolo de media onda', size=22, weight='bold')
Y = 150
f.rect(40, Y - 50, 12, 250, fill=INK, rx=3)
f.rect(588, Y - 50, 12, 250, fill=INK, rx=3)
f.line(52, Y, 96, Y, stroke=MUTED, w=2, dash='5 5')
f.line(544, Y, 588, Y, stroke=MUTED, w=2, dash='5 5')
f.rect(96, Y - 7, 22, 14, fill='#FFFFFF', stroke=INK, sw=2, rx=4)
f.rect(522, Y - 7, 22, 14, fill='#FFFFFF', stroke=INK, sw=2, rx=4)
f.line(118, Y, 306, Y, stroke=AMBER, w=5)
f.line(334, Y, 522, Y, stroke=AMBER, w=5)
f.rect(306, Y - 12, 28, 24, fill='#FFFFFF', stroke=INK, sw=3, rx=5)
f.path(f'M320 {Y+12} V{Y+170}', stroke=WIRE, w=6)
f.text(212, Y - 20, 'brazo', size=19, fill=AMBER, weight='bold')
f.text(428, Y - 20, 'brazo', size=19, fill=AMBER, weight='bold')
f.text(320, Y - 26, 'aislador central', size=18, fill=MUTED)
f.text(107, Y + 36, 'aislador', size=18, fill=MUTED)
f.text(533, Y + 36, 'aislador', size=18, fill=MUTED)
f.text(336, Y + 120, 'cable de bajada', size=19, anchor='start', fill=MUTED)
f.text(336, Y + 144, 'hacia el equipo', size=19, anchor='start', fill=MUTED)
# dimensions
f.line(118, Y + 62, 306, Y + 62, stroke=BLUE, w=3, arrow=True)
f.line(306, Y + 62, 118, Y + 62, stroke=BLUE, w=3, arrow=True)
f.text(212, Y + 88, 'un cuarto de onda', size=18, fill=BLUE)
f.line(118, 380, 522, 380, stroke=GREEN, w=3, arrow=True)
f.line(522, 380, 118, 380, stroke=GREEN, w=3, arrow=True)
f.rect(150, 392, 340, 56, fill=PAPER, rx=6)
f.text(320, 414, 'media onda en total:', size=19, fill=GREEN)
f.text(320, 442, '142,5 / f (MHz) metros', size=22, fill=GREEN, weight='bold')
f.save()

# 4 ── figure-of-eight pattern ─────────────────────────────────────────────
f = Fig('s08-diagrama-ocho', 500, 'Diagrama de radiación en ocho de un dipolo, visto desde arriba')
f.text(320, 44, 'El dipolo visto desde arriba: radia en ocho', size=21, weight='bold')
cx, cy, r = 320, 250, 95
f.circle(cx - r, cy, r, fill='#DBEAFE', stroke=BLUE, sw=4)
f.circle(cx + r, cy, r, fill='#DBEAFE', stroke=BLUE, sw=4)
f.line(cx, cy - 130, cx, cy + 130, stroke=AMBER, w=7)
f.text(cx, cy - 144, 'norte', size=19, fill=MUTED)
f.text(cx + 14, cy - 100, 'el hilo', size=19, anchor='start', fill=AMBER, weight='bold')
f.text(cx - 2 * r - 14, cy + 7, 'oeste', size=19, anchor='end', fill=MUTED)
f.text(cx + 2 * r + 14, cy + 7, 'este', size=19, anchor='start', fill=MUTED)
f.line(cx - 40, cy, cx - 2 * r + 14, cy, stroke=BLUE, w=4, arrow=True)
f.line(cx + 40, cy, cx + 2 * r - 14, cy, stroke=BLUE, w=4, arrow=True)
f.text(cx - r, cy - 28, 'máximo', size=20, fill=BLUE, weight='bold')
f.text(cx + r, cy - 28, 'máximo', size=20, fill=BLUE, weight='bold')
f.text(cx, cy + 156, 'sur', size=19, fill=MUTED)
f.text(cx, cy + 184, 'casi nada hacia las puntas (norte y sur)', size=19, fill=MUTED)
f.text(320, 472, 'Radia de frente y de espaldas al hilo', size=20, weight='bold')
f.save()

# 5 ── quarter-wave vertical and its mirror image ──────────────────────────
f = Fig('s08-vertical-espejo', 500, 'Vertical de cuarto de onda con radiales y su imagen en el plano de tierra')
f.text(320, 44, 'La vertical: media antena y un espejo', size=22, weight='bold')
G = 270
f.rect(40, G, 560, 190, fill='#E9DFC8', rx=0)
f.line(40, G, 600, G, stroke='#8B7B55', w=4)
f.line(320, G - 6, 320, G - 170, stroke=AMBER, w=7)
f.line(320, G + 8, 320, G + 170, stroke=AMBER, w=5, dash='10 9')
for dx in (-240, -150, 150, 240):
    f.line(320, G, 320 + dx, G + (16 if abs(dx) < 200 else 6), stroke=BLUE, w=4)
f.circle(320, G, 9, fill='#FFFFFF', stroke=INK, sw=3)
f.text(340, G - 110, 'varilla de un', size=19, anchor='start', fill=AMBER, weight='bold')
f.text(340, G - 86, 'cuarto de onda', size=19, anchor='start', fill=AMBER, weight='bold')
f.text(340, G + 104, 'imagen: el brazo', size=19, anchor='start', fill=MUTED)
f.text(340, G + 128, 'que «pone» el espejo', size=19, anchor='start', fill=MUTED)
f.text(120, G - 16, 'radiales', size=19, fill=BLUE, weight='bold')
f.text(120, G + 60, 'plano de tierra', size=19, fill='#6B5B35', weight='bold')
f.line(290, G - 6, 290, G - 170, stroke=GREEN, w=3, arrow=True)
f.line(290, G - 170, 290, G - 6, stroke=GREEN, w=3, arrow=True)
f.text(278, G - 84, '71,25 / f', size=19, anchor='end', fill=GREEN, weight='bold')
f.text(320, 486, 'Radia como un dipolo del que solo se ha construido la mitad', size=18, fill=MUTED)
f.save()

# 6 ── isotropic / dipole / yagi patterns ──────────────────────────────────
f = Fig('s08-isotropica-dipolo-yagi', 400, 'Diagramas de la antena isotrópica, el dipolo y la yagi')
f.text(320, 44, 'La misma potencia, repartida de tres maneras', size=21, weight='bold')
cy = 180
# isotropic
f.circle(115, cy, 52, fill='#DBEAFE', stroke=BLUE, sw=4)
f.circle(115, cy, 5, fill=INK, stroke=INK)
# dipole
f.circle(320 - 42, cy, 42, fill='#DBEAFE', stroke=BLUE, sw=4)
f.circle(320 + 42, cy, 42, fill='#DBEAFE', stroke=BLUE, sw=4)
f.line(320, cy - 62, 320, cy + 62, stroke=AMBER, w=6)
# yagi lobe pointing up
f.path(f'M525 {cy+70} C460 {cy+20}, 470 {cy-110}, 525 {cy-110} C580 {cy-110}, 590 {cy+20}, 525 {cy+70} Z',
       stroke=BLUE, w=4, fill='#DBEAFE')
f.circle(525, cy + 86, 12, fill='#DBEAFE', stroke=BLUE, sw=3)
for k, (yy, w) in enumerate([(cy + 78, 54), (cy + 60, 48), (cy + 42, 42)]):
    f.line(525 - w / 2, yy, 525 + w / 2, yy, stroke=AMBER, w=5)
for x, name, g1, g2 in [(115, 'isotrópica', '0 dBi', '(no existe)'), (320, 'dipolo', '2,15 dBi', '= 0 dBd'),
                        (525, 'yagi', 'unos 8 dBi', '= unos 6 dBd')]:
    f.text(x, 306, name, size=20, weight='bold')
    f.text(x, 336, g1, size=20, fill=BLUE, weight='bold')
    f.text(x, 362, g2, size=18, fill=MUTED)
f.save()

# 7 ── yagi elements ───────────────────────────────────────────────────────
f = Fig('s08-yagi', 440, 'Elementos de una antena yagi')
f.text(320, 44, 'La yagi, vista desde arriba', size=22, weight='bold')
Y = 215
f.line(90, Y, 520, Y, stroke=MUTED, w=6)
els = [(120, 150, 'reflector', 'el más largo', INK), (240, 136, 'dipolo activo', 'aquí va el cable', AMBER),
       (360, 122, 'director', 'más corto', INK), (480, 110, 'director', 'más corto aún', INK)]
for x, h, n1, n2, col in els:
    f.line(x, Y - h / 2, x, Y + h / 2, stroke=col, w=7)
f.circle(240, Y, 9, fill='#FFFFFF', stroke=INK, sw=3)
f.text(120, Y + 106, 'reflector', size=19, weight='bold')
f.text(120, Y + 130, '(el más largo)', size=18, fill=MUTED)
f.text(240, Y - 92, 'dipolo activo', size=19, weight='bold', fill=AMBER)
f.text(240, Y - 116, 'el cable va aquí:', size=18, fill=MUTED)
f.text(420, Y + 106, 'directores', size=19, weight='bold')
f.text(420, Y + 130, '(más cortos)', size=18, fill=MUTED)
f.line(535, Y, 610, Y, stroke=BLUE, w=6, arrow=True)
f.text(572, Y - 18, 'radia', size=19, fill=BLUE, weight='bold')
f.text(60, Y + 7, 'atrás', size=18, fill=MUTED, anchor='middle')
f.text(320, 412, 'Solo el dipolo está conectado; los demás son parásitos', size=19, fill=MUTED)
f.save()

# 8 ── ropes: matched vs mismatched junction ───────────────────────────────
def bump(x, y, w, h):
    return f'M{x} {y} C{x + w * 0.3} {y}, {x + w * 0.3} {y - h}, {x + w * 0.5} {y - h} C{x + w * 0.7} {y - h}, {x + w * 0.7} {y}, {x + w} {y}'

f = Fig('s08-cuerdas-y-rebote', 550, 'Una onda en una unión entre cuerdas iguales y entre cuerdas distintas')
f.text(320, 42, 'Qué le pasa a una onda al llegar a un nudo', size=21, weight='bold')
for k in range(2):
    y0 = 70 + k * 220
    f.rect(30, y0, 580, 200 + 40 * k, fill=SOFT, rx=14)
Y = 190
f.text(320, 104, 'Cuerdas iguales: pasa entera', size=20, weight='bold', fill=GREEN)
f.line(60, Y, 580, Y, stroke=WIRE, w=5)
f.circle(320, Y, 8, fill=INK, stroke=INK)
f.path(bump(400, Y, 110, 56), stroke=GREEN, w=6)
f.line(440, Y - 78, 520, Y - 78, stroke=GREEN, w=4, arrow=True)
f.text(320, Y + 34, 'nudo', size=18, fill=MUTED)
f.text(320, Y + 62, 'igual impedancia: toda la energía sigue adelante', size=18, fill=MUTED)
Y = 450
f.text(320, 326, 'Cuerdas distintas: una parte rebota', size=20, weight='bold', fill=RED)
f.line(60, Y, 320, Y, stroke=WIRE, w=4)
f.line(320, Y, 580, Y, stroke=WIRE, w=13)
f.circle(320, Y, 9, fill=INK, stroke=INK)
f.path(bump(400, Y - 6, 110, 34), stroke=GREEN, w=6)
f.line(440, Y - 62, 520, Y - 62, stroke=GREEN, w=4, arrow=True)
f.path(bump(120, Y, 110, 38), stroke=RED, w=6)
f.line(210, Y - 62, 130, Y - 62, stroke=RED, w=4, arrow=True)
f.text(170, Y - 76, 'rebota', size=19, fill=RED, weight='bold')
f.text(480, Y - 76, 'sigue', size=19, fill=GREEN, weight='bold')
f.text(320, Y + 34, 'nudo', size=18, fill=MUTED)
f.text(320, Y + 62, 'distinta impedancia: parte de la energía vuelve', size=18, fill=MUTED)
f.save()

# 9 ── standing waves on the line for three SWR values ─────────────────────
f = Fig('s08-ondas-estacionarias-en-la-linea', 520, 'Tensión a lo largo del cable para ROE 1, 2 y 5')
f.text(320, 42, 'La tensión a lo largo del cable', size=22, weight='bold')
for k, (swr, col, note) in enumerate([(1, GREEN, 'plana: nada rebota'), (2, AMBER, 'máximo = 2 × mínimo'),
                                      (5, RED, 'máximo = 5 × mínimo')]):
    y0 = 70 + k * 146
    f.rect(30, y0, 580, 132, fill=SOFT, rx=14)
    f.text(60, y0 + 40, f'ROE {swr}', size=24, weight='bold', fill=col, anchor='start')
    f.text(60, y0 + 70, note, size=18, fill=MUTED, anchor='start')
    base = y0 + 116
    f.line(280, base, 590, base, stroke=MUTED, w=2)
    rho = (swr - 1) / (swr + 1)
    vmax = 1 + rho
    scale = 92 / 1.667
    pts = []
    for i in range(121):
        t = i / 120
        x = 280 + 310 * t
        v = math.sqrt(1 + rho * rho + 2 * rho * math.cos(4 * math.pi * 1.5 * t))
        pts.append((x, base - v * scale))
    f.path('M' + ' L'.join(f'{x:.1f} {yy:.1f}' for x, yy in pts), stroke=col, w=4)
f.save()

# 10 ── SWR curve from the analyser ────────────────────────────────────────
f = Fig('s08-curva-de-roe', 460, 'Curva de ROE de una antena en función de la frecuencia')
f.text(320, 42, 'Lo que dibuja el analizador', size=22, weight='bold')
X0, X1, Y0, Y1 = 90, 590, 360, 80   # Y0 = ROE 1, Y1 = ROE 4
def yy(s): return Y0 - (s - 1) / 3 * (Y0 - Y1)
def xx(fr): return X0 + (fr - 6.88) / 0.44 * (X1 - X0)
FR = 7.10
f.line(X0, Y0, X1, Y0, stroke=INK, w=3)
f.line(X0, Y0, X0, Y1 - 10, stroke=INK, w=3)
for s in (1, 2, 3, 4):
    f.text(X0 - 12, yy(s) + 7, str(s), size=19, anchor='end')
f.text(46, 62, 'ROE', size=19, weight='bold', anchor='middle')
for fr, lab in ((6.95, '6,95'), (7.10, '7,10'), (7.25, '7,25')):
    f.text(xx(fr), Y0 + 30, lab, size=19)
f.text(340, Y0 + 62, 'frecuencia (MHz)', size=19, fill=MUTED)
pts = []
for i in range(101):
    fr = 6.88 + 0.44 * i / 100
    s = min(4.2, math.sqrt(1.2 ** 2 + ((fr - FR) / 0.062) ** 2))
    pts.append((xx(fr), yy(s)))
f.path('M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts), stroke=BLUE, w=5)
f.line(X0, yy(2), X1, yy(2), stroke=AMBER, w=3, dash='9 7')
f.text(X1, yy(2) + 26, 'ROE 2', size=18, anchor='end', fill=AMBER, weight='bold')
f.circle(xx(FR), yy(1.2), 8, fill=GREEN, stroke=GREEN)
f.text(xx(FR), yy(1.2) - 44, 'resonancia', size=19, fill=GREEN, weight='bold')
f.text(xx(FR), yy(1.2) - 20, 'ROE 1,2', size=19, fill=GREEN, weight='bold')
bw = 0.062 * math.sqrt(4 - 1.44)
f.line(xx(FR - bw) + 6, yy(2), xx(FR + bw) - 6, yy(2), stroke=GREEN, w=5, arrow=True)
f.line(xx(FR + bw) - 6, yy(2), xx(FR - bw) + 6, yy(2), stroke=GREEN, w=5, arrow=True)
f.circle(xx(FR - bw), yy(2), 6, fill=GREEN, stroke=GREEN)
f.circle(xx(FR + bw), yy(2), 6, fill=GREEN, stroke=GREEN)
f.text(xx(FR), yy(2) - 16, 'ancho de banda', size=19, fill=GREEN, weight='bold')
f.save()

# 11 ── coax cross-section ─────────────────────────────────────────────────
f = Fig('s08-coaxial-por-dentro', 400, 'Corte de un cable coaxial con sus cuatro capas')
f.text(320, 44, 'Un cable coaxial, cortado', size=22, weight='bold')
cx, cy = 170, 215
f.circle(cx, cy, 120, fill='#374151', stroke=INK, sw=3)
f.circle(cx, cy, 100, fill='#C98B4B', stroke=INK, sw=2)
f.circle(cx, cy, 86, fill='#FFFFFF', stroke=INK, sw=2)
f.circle(cx, cy, 22, fill='#D97706', stroke=INK, sw=2)
rows = [(22 * 0.3, 'conductor central (vivo)', '#B45309', 110), (60, 'dieléctrico (aislante)', MUTED, 175),
        (93, 'malla de cobre', '#8A5A22', 240), (110, 'cubierta de plástico', INK, 305)]
for rr, label, col, ly in rows:
    ang = math.radians(-35 + (ly - 110) / 195 * 70)
    px, py = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
    f.line(px, py, 330, ly, stroke=col, w=2)
    f.circle(px, py, 4, fill=col, stroke=col, sw=1)
    f.text(338, ly + 7, label, size=20, anchor='start', weight='bold', fill=col)
f.text(320, 378, 'La onda viaja encerrada entre el vivo y la malla', size=19, fill=MUTED)
f.save()

# 12 ── balun / common-mode current ────────────────────────────────────────
f = Fig('s08-balun', 500, 'Dipolo con y sin balun: la corriente por el exterior de la malla')
f.text(320, 42, 'Para qué sirve el balun', size=22, weight='bold')
for k, (cx, title, col) in enumerate([(165, 'Sin balun', RED), (475, 'Con balun', GREEN)]):
    f.rect(20 + k * 310, 64, 290, 420, fill=SOFT, rx=14)
    f.text(cx, 100, title, size=21, weight='bold', fill=col)
    Y = 160
    f.line(cx - 120, Y, cx - 12, Y, stroke=AMBER, w=5)
    f.line(cx + 12, Y, cx + 120, Y, stroke=AMBER, w=5)
    f.rect(cx - 12, Y - 10, 24, 20, fill='#FFFFFF', stroke=INK, sw=3, rx=4)
    f.line(cx, Y + 10, cx, 400, stroke=WIRE, w=7)
    f.rect(cx - 36, 400, 72, 44, fill='#FFFFFF', stroke=INK, sw=3, rx=6)
    f.text(cx, 430, 'equipo', size=18)
    for a in (-1, 1):
        f.path(f'M{cx + a*60} {Y-14} q0 -22 {a*14} -30', stroke=BLUE, w=3)
        f.path(f'M{cx + a*84} {Y-14} q0 -30 {a*20} -42', stroke=BLUE, w=3)
    if k == 0:
        for yy_ in (230, 290, 350):
            f.path(f'M{cx+16} {yy_} q22 -14 22 -34', stroke=RED, w=3)
            f.path(f'M{cx-16} {yy_} q-22 -14 -22 -34', stroke=RED, w=3)
            f.path(f'M{cx+30} {yy_+8} q34 -20 34 -52', stroke=RED, w=3)
            f.path(f'M{cx-30} {yy_+8} q-34 -20 -34 -52', stroke=RED, w=3)
        f.line(cx + 12, 200, cx + 12, 246, stroke=RED, w=4, arrow=True)
        f.text(cx, 468, 'el cable también radia', size=18, fill=RED, weight='bold')
    else:
        f.circle(cx, Y + 44, 20, fill='#FFFFFF', stroke=INK, sw=5)
        f.text(cx + 30, Y + 51, 'balun', size=19, anchor='start', weight='bold')
        f.text(cx, 468, 'solo radia la antena', size=18, fill=GREEN, weight='bold')
f.save()

# 13 ── take-off angle: low vs high dipole, side view ─────────────────────
f = Fig('s08-angulo-de-salida', 430, 'Ángulo de salida de un dipolo bajo y de un dipolo alto, vistos de lado')
f.text(320, 42, 'El dipolo visto de lado: la altura cambia el ángulo', size=20, weight='bold')
G = 330
f.rect(20, G, 600, 22, fill='#E9DFC8', rx=0)
f.line(20, G, 620, G, stroke='#8B7B55', w=4)
# low dipole: single lobe straight up
cx = 165
f.line(cx, G, cx, G - 26, stroke=MUTED, w=3)
f.circle(cx, G - 30, 7, fill=AMBER, stroke=AMBER)
f.path(f'M{cx} {G-38} C{cx-95} {G-110}, {cx-70} {G-250}, {cx} {G-250} C{cx+70} {G-250}, {cx+95} {G-110}, {cx} {G-38} Z',
       stroke=BLUE, w=4, fill='#DBEAFE')
f.line(cx, G - 70, cx, G - 215, stroke=BLUE, w=4, arrow=True)
f.text(cx, G + 52, 'bajo: sale hacia arriba', size=19, weight='bold')
f.text(cx, G + 78, '(vuelve a caer cerca)', size=18, fill=MUTED)
# high dipole: two lobes at ~30 degrees
cx = 465
f.line(cx, G, cx, G - 120, stroke=MUTED, w=3)
f.circle(cx, G - 124, 7, fill=AMBER, stroke=AMBER)
for sgn in (-1, 1):
    a = math.radians(30)
    ex, ey = cx + sgn * 150 * math.cos(a), G - 124 - 150 * math.sin(a) + 20
    px, py = -sgn * math.sin(a) * 34, -math.cos(a) * 34
    mx, my = (cx + ex) / 2, (G - 124 + ey) / 2
    f.path(f'M{cx} {G-124} Q{mx+px:.0f} {my+py:.0f} {ex:.0f} {ey:.0f} Q{mx-px:.0f} {my-py:.0f} {cx} {G-124} Z',
           stroke=BLUE, w=4, fill='#DBEAFE')
f.text(cx, G + 52, 'alto: sale rasante', size=19, weight='bold')
f.text(cx, G + 78, '(llega mucho más lejos)', size=18, fill=MUTED)
f.text(cx, G - 250, 'unos 30° del horizonte', size=18, fill=BLUE)
f.line(320, 70, 320, G - 6, stroke=PAPER_EDGE, w=2)
f.save()
