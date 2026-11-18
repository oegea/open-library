"""Figures of section 5 (circuits)."""
import math
from figlib import *

SIN = lambda t: math.sin(2 * math.pi * t)


# ── local helpers ──────────────────────────────────────────────────────────
def res_h(f, x, y, w=80, label=None, sub=None, subcol=RED):
    f.rect(x, y - 15, w, 30, fill='#FFFFFF', stroke=INK, sw=3, rx=4)
    if label:
        f.text(x + w / 2, y - 26, label, size=20, weight='bold')
    if sub:
        f.text(x + w / 2, y + 44, sub, size=20, weight='bold', fill=subcol)


def res_v(f, x, y, h=80, label=None, sub=None, subcol=RED, side=1):
    f.rect(x - 15, y, 30, h, fill='#FFFFFF', stroke=INK, sw=3, rx=4)
    anchor = 'start' if side > 0 else 'end'
    if label:
        f.text(x + side * 26, y + h / 2 - 6, label, size=20, weight='bold', anchor=anchor)
    if sub:
        f.text(x + side * 26, y + h / 2 + 20, sub, size=20, weight='bold', fill=subcol, anchor=anchor)


def cap_v(f, x, y, color=INK):
    """Capacitor on a vertical wire, centred at (x, y)."""
    f.line(x - 22, y - 7, x + 22, y - 7, stroke=color, w=5)
    f.line(x - 22, y + 7, x + 22, y + 7, stroke=color, w=5)


def cap_h(f, x, y, color=INK):
    f.line(x - 7, y - 22, x - 7, y + 22, stroke=color, w=5)
    f.line(x + 7, y - 22, x + 7, y + 22, stroke=color, w=5)


def coil_h(f, x, y, n=4, r=11, color=INK):
    d = f'M{x} {y}' + ''.join(f' a{r} {r} 0 0 1 {2*r} 0' for _ in range(n))
    f.path(d, stroke=color, w=4)
    return x + 2 * r * n


def coil_v(f, x, y, n=4, r=11, color=INK):
    d = f'M{x} {y}' + ''.join(f' a{r} {r} 0 0 1 0 {2*r}' for _ in range(n))
    f.path(d, stroke=color, w=4)
    return y + 2 * r * n


def gnd(f, x, y):
    f.line(x - 18, y, x + 18, y, stroke=INK, w=4)
    f.line(x - 11, y + 8, x + 11, y + 8, stroke=INK, w=4)
    f.line(x - 4, y + 16, x + 4, y + 16, stroke=INK, w=4)


def wave(f, x0, ymid, w, amp, fn, color=BLUE, sw=4, n=240, dash=None, t0=0.0, t1=1.0):
    pts = []
    for k in range(n + 1):
        t = t0 + (t1 - t0) * k / n
        pts.append(f'{x0 + w * k / n:.1f} {ymid - amp * fn(t):.1f}')
    f.path('M' + ' L'.join(pts), stroke=color, w=sw, dash=dash)


def axes(f, x0, y0, w, h, xlabel=None, ylabel=None):
    f.line(x0, y0, x0, y0 - h, stroke=INK, w=3, arrow=True)
    f.line(x0, y0, x0 + w, y0, stroke=INK, w=3, arrow=True)
    if xlabel:
        f.text(x0 + w, y0 + 28, xlabel, size=18, anchor='end', fill=MUTED)
    if ylabel:
        f.text(x0 + 8, y0 - h - 8, ylabel, size=18, anchor='start', fill=MUTED)


# 1 ── series and parallel ─────────────────────────────────────────────────
f = Fig('s05-serie-y-paralelo', 640, 'Resistencias en serie y en paralelo')
f.text(320, 42, 'En serie: un solo camino', size=22, weight='bold')
L, T, B, Rr = 90, 100, 250, 550
f.path(f'M{L} {T+30} V{T} H210'); f.line(290, T, 370, T); f.path(f'M450 {T} H{Rr} V{B} H{L} V{T+122}')
f.battery(L, T + 30, h=100)
f.text(L - 34, T + 86, '12 V', size=20, weight='bold', anchor='end')
res_h(f, 210, T, label='4 Ω', sub='4 V'); res_h(f, 370, T, label='8 Ω', sub='8 V')
f.line(250, B + 22, 400, B + 22, stroke=BLUE, w=4, arrow=True)
f.text(325, B - 14, '1 A en todo el circuito', size=20, weight='bold', fill=BLUE)
f.text(320, 306, 'Misma corriente. La tensión se reparte: 4 + 8 = 12 V', size=19, fill=MUTED)
f.line(60, 326, 580, 326, stroke=PAPER_EDGE, w=2)
f.text(320, 364, 'En paralelo: dos caminos', size=22, weight='bold')
T2, B2 = 410, 570
f.path(f'M{L} {T2+26} V{T2} H470 V{T2+40}'); f.path(f'M470 {T2+120} V{B2} H{L} V{T2+118}')
f.path(f'M310 {T2} V{T2+40}'); f.path(f'M310 {T2+120} V{B2}')
f.battery(L, T2 + 26, h=100)
f.text(L - 34, T2 + 82, '12 V', size=20, weight='bold', anchor='end')
res_v(f, 310, T2 + 40, label='4 Ω', sub='3 A', subcol=BLUE); res_v(f, 470, T2 + 40, label='8 Ω', sub='1,5 A', subcol=BLUE)
f.circle(310, T2, 6, fill=WIRE, stroke=WIRE); f.circle(310, B2, 6, fill=WIRE, stroke=WIRE)
f.line(140, T2 - 18, 230, T2 - 18, stroke=BLUE, w=4, arrow=True)
f.text(185, T2 + 30, '4,5 A', size=20, weight='bold', fill=BLUE)
f.text(320, 616, 'Misma tensión. La corriente se reparte: 3 + 1,5 = 4,5 A', size=19, fill=MUTED)
f.save()

# 2 ── Dani's series bulb ──────────────────────────────────────────────────
f = Fig('s05-bombilla-en-serie', 500, 'El truco de la bombilla en serie')
f.text(320, 42, 'La bombilla en serie con el aparato', size=22, weight='bold')
for k, (title, lit, vb, va, note, col) in enumerate([
        ('Aparato sano', False, 'unos 20 V', 'unos 210 V', 'La bombilla apenas luce', GREEN),
        ('Aparato en cortocircuito', True, 'casi 230 V', 'casi 0 V', 'Brilla a tope: máximo 0,26 A', RED)]):
    y = 70 + k * 210
    f.rect(30, y, 580, 196, fill=SOFT, rx=14)
    f.text(320, y + 32, title, size=21, weight='bold', fill=col)
    f.rect(52, y + 66, 104, 60, fill='#FFFFFF', stroke=INK, sw=3, rx=8)
    f.text(104, y + 92, 'enchufe', size=18, fill=MUTED); f.text(104, y + 116, '230 V', size=20, weight='bold')
    f.line(156, y + 96, 256, y + 96); f.line(304, y + 96, 400, y + 96)
    f.bulb(280, y + 96, r=24, lit=lit)
    if lit:
        for a in range(0, 360, 45):
            ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
            f.line(280 + 30 * ca, y + 96 + 30 * sa, 280 + 40 * ca, y + 96 + 40 * sa, stroke=AMBER, w=3)
    f.rect(400, y + 66, 150, 60, fill='#FFFFFF', stroke=INK, sw=3, rx=8)
    f.text(475, y + 103, 'aparato', size=20, weight='bold')
    f.text(280, y + 158, vb, size=20, weight='bold', fill=AMBER)
    f.text(475, y + 158, va, size=20, weight='bold', fill=AMBER)
    f.text(320, y + 186, note, size=19, fill=MUTED)
f.save()

# 3 ── voltage divider ─────────────────────────────────────────────────────
f = Fig('s05-divisor-de-tension', 440, 'Un divisor de tensión')
f.text(320, 42, 'El divisor de tensión', size=22, weight='bold')
L, X, T, B = 130, 330, 90, 380
f.path(f'M{L} {T+90} V{T} H{X} V{T+20}'); f.line(X, T + 100, X, T + 170); f.path(f'M{X} {T+250} V{B} H{L} V{T+182}')
f.battery(L, T + 90, h=100)
f.text(L - 34, T + 146, '9 V', size=20, weight='bold', anchor='end')
res_v(f, X, T + 20, label='R1 = 1 kΩ', sub='3 V', side=-1)
res_v(f, X, T + 170, label='R2 = 2 kΩ', sub='6 V', side=-1)
f.circle(X, T + 135, 6, fill=WIRE, stroke=WIRE)
f.line(X, T + 135, 470, T + 135, stroke=GREEN, w=4); f.line(X, B, 470, B, stroke=GREEN, w=4)
f.circle(476, T + 135, 7, fill='#FFFFFF', stroke=GREEN, sw=4); f.circle(476, B, 7, fill='#FFFFFF', stroke=GREEN, sw=4)
f.line(500, T + 145, 500, B - 10, stroke=GREEN, w=3, arrow=True); f.line(500, B - 10, 500, T + 147, stroke=GREEN, w=3, arrow=True)
f.text(516, T + 210, 'salida', size=19, anchor='start', fill=MUTED)
f.text(516, T + 238, '6 V', size=24, anchor='start', weight='bold', fill=GREEN)
f.text(320, 422, 'R2 es dos tercios del total: se lleva dos tercios de 9 V', size=19, fill=MUTED)
f.save()

# 5 ── LC energy exchange in four frames ───────────────────────────────────
f = Fig('s05-vaiven-lc', 696, 'El vaivén de energía en un circuito LC')
f.text(320, 42, 'El vaivén entre condensador y bobina', size=22, weight='bold')
frames = [('1', 'Condensador cargado', 'Energía: en el condensador', ('+', '−'), 0),
          ('2', 'Corriente máxima', 'Energía: en la bobina', None, 1),
          ('3', 'Cargado al revés', 'Energía: en el condensador', ('−', '+'), 0),
          ('4', 'Corriente al revés', 'Energía: en la bobina', None, -1)]
for k, (num, t1, t2, signs, cur) in enumerate(frames):
    x = 20 + (k % 2) * 305; y = 66 + (k // 2) * 300
    f.rect(x, y, 295, 284, fill=SOFT, rx=14)
    f.circle(x + 30, y + 32, 17, fill=AMBER, stroke=AMBER); f.text(x + 30, y + 40, num, size=22, weight='bold', fill='#FFFFFF')
    f.text(x + 56, y + 39, t1, size=19, weight='bold', anchor='start')
    cx, cl, top, bot = x + 85, x + 215, y + 80, y + 210
    capcol = RED if signs else INK; coilcol = BLUE if cur else INK
    f.path(f'M{cx} {y+138} V{top} H{cl} V{y+101}'); f.path(f'M{cl} {y+189} V{bot} H{cx} V{y+152}')
    cap_v(f, cx, y + 145, color=capcol)
    coil_v(f, cl, y + 101, color=coilcol)
    if signs:
        f.text(cx - 40, y + 142, signs[0], size=26, weight='bold', fill=RED if signs[0] == '+' else BLUE)
        f.text(cx - 40, y + 172, signs[1], size=26, weight='bold', fill=RED if signs[1] == '+' else BLUE)
    if cur == 1:
        f.line(cx + 20, top - 14, cl - 20, top - 14, stroke=BLUE, w=4, arrow=True)
    if cur == -1:
        f.line(cl - 20, top - 14, cx + 20, top - 14, stroke=BLUE, w=4, arrow=True)
    f.text(x + 147, y + 256, t2, size=19, fill=RED if signs else BLUE, weight='bold')
f.text(320, 676, 'Después del 4 vuelve al 1, y así una y otra vez', size=19, fill=MUTED)
f.save()

# 6 ── reactances crossing ─────────────────────────────────────────────────
f = Fig('s05-cruce-de-reactancias', 440, 'Las reactancias se cruzan en la frecuencia de resonancia')
f.text(320, 42, 'Donde las dos reactancias se igualan', size=22, weight='bold')
x0, y0, w, h = 80, 370, 500, 270
axes(f, x0, y0, w + 30, h + 20, xlabel='frecuencia', ylabel='reactancia (ohmios)')
wave(f, x0, y0, w, h, lambda t: 0.9 * t, color=BLUE, sw=5)
wave(f, x0 + 0.2 * w, y0, 0.8 * w, h, lambda t: min(1.0, 0.2025 / max(t, 1e-3)), color=RED, sw=5, t0=0.2)
xc = x0 + w * 0.4743; yc = y0 - h * 0.9 * 0.4743
f.line(xc, y0, xc, yc, stroke=AMBER, w=3, dash='5 5'); f.circle(xc, yc, 8, fill=AMBER, stroke=AMBER)
f.text(x0 + w - 6, y0 - h * 0.9 + 96, 'bobina: sube', size=20, anchor='end', weight='bold', fill=BLUE)
f.text(x0 + w * 0.32, y0 - h * 0.86, 'condensador: baja', size=20, anchor='start', weight='bold', fill=RED)
f.text(xc, y0 + 30, 'frecuencia de resonancia', size=19, weight='bold', fill=AMBER)
f.save()

# 7 ── Q factor ────────────────────────────────────────────────────────────
f = Fig('s05-factor-q', 440, 'Curvas de resonancia con Q alto y Q bajo')
f.text(320, 42, 'El mismo columpio, más o menos fino', size=22, weight='bold')
x0, y0, w, h = 80, 370, 500, 270
axes(f, x0, y0, w + 30, h + 20, xlabel='frecuencia', ylabel='respuesta')
lor = lambda q, a: (lambda t: a / math.sqrt(1 + (q * (t - 0.5)) ** 2))
wave(f, x0, y0, w, h, lor(6, 0.42), color=BLUE, sw=5)
wave(f, x0, y0, w, h, lor(40, 0.95), color=AMBER, sw=5)
f.line(x0 + w / 2, y0, x0 + w / 2, y0 - h, stroke=MUTED, w=2, dash='5 5')
f.text(x0 + w / 2 + 44, y0 - h * 0.8, 'Q alto: estrecho,', size=20, anchor='start', weight='bold', fill=AMBER)
f.text(x0 + w / 2 + 44, y0 - h * 0.8 + 26, 'muy selectivo', size=20, anchor='start', weight='bold', fill=AMBER)
f.text(x0 + 14, y0 - h * 0.42, 'Q bajo: ancho,', size=20, anchor='start', weight='bold', fill=BLUE)
f.text(x0 + 14, y0 - h * 0.42 + 26, 'poco selectivo', size=20, anchor='start', weight='bold', fill=BLUE)
f.text(x0 + w / 2, y0 + 30, 'frecuencia de resonancia', size=19, fill=MUTED)
f.save()

# 8 ── four filter responses ───────────────────────────────────────────────
f = Fig('s05-cuatro-filtros', 660, 'Respuesta de los cuatro tipos de filtro')
f.text(320, 42, 'Los cuatro filtros: qué deja pasar cada uno', size=22, weight='bold')
lp = lambda t: 1 / math.sqrt(1 + (t / 0.45) ** 10)
hp = lambda t: 1 / math.sqrt(1 + (0.55 / max(t, 1e-3)) ** 10)
bp = lambda t: 1 / math.sqrt(1 + (12 * (t - 0.5)) ** 6)
bs = lambda t: 1 - bp(t)
for k, (name, fn, note) in enumerate([('Paso bajo', lp, 'pasa lo de abajo'), ('Paso alto', hp, 'pasa lo de arriba'),
                                      ('Paso banda', bp, 'pasa una franja'), ('Rechazo de banda', bs, 'pasa todo menos una franja')]):
    x = 20 + (k % 2) * 305; y = 66 + (k // 2) * 290
    f.rect(x, y, 295, 276, fill=SOFT, rx=14)
    f.text(x + 147, y + 34, name, size=21, weight='bold')
    px, py, pw, ph = x + 36, y + 206, 226, 130
    pts = [f'{px + pw * i / 120:.1f} {py - ph * fn(i / 120):.1f}' for i in range(121)]
    f.add(f'<path d="M{px} {py} L' + ' L'.join(pts) + f' L{px+pw} {py} Z" fill="{GREEN}" fill-opacity="0.25"/>')
    wave(f, px, py, pw, ph, fn, color=GREEN, sw=5)
    axes(f, px, py, pw + 14, ph + 24)
    f.text(x + 147, y + 232, 'frecuencia →', size=18, fill=MUTED)
    f.text(x + 147, y + 260, note, size=19, weight='bold', fill=GREEN)
f.text(320, 646, 'La zona verde es lo que sale del filtro', size=19, fill=MUTED)
f.save()

# 9 ── LC low-pass and high-pass ───────────────────────────────────────────
f = Fig('s05-filtros-lc', 520, 'Filtros paso bajo y paso alto con bobina y condensador')
f.text(320, 42, 'Con una bobina y un condensador', size=22, weight='bold')
for k, name in enumerate(['Paso bajo: bobina en el camino, condensador a masa',
                          'Paso alto: condensador en el camino, bobina a masa']):
    y = 66 + k * 224
    f.rect(30, y, 580, 210, fill=SOFT, rx=14)
    f.text(320, y + 32, name, size=19, weight='bold')
    yy = y + 90
    f.circle(92, yy, 7, fill='#FFFFFF', stroke=INK, sw=3); f.circle(548, yy, 7, fill='#FFFFFF', stroke=INK, sw=3)
    f.text(92, yy - 22, 'entrada', size=18, fill=MUTED); f.text(548, yy - 22, 'salida', size=18, fill=MUTED)
    if k == 0:
        f.line(99, yy, 230, yy); end = coil_h(f, 230, yy, color=BLUE); f.line(end, yy, 541, yy)
        f.text(274, yy - 22, 'bobina', size=18, fill=BLUE, weight='bold')
        f.line(420, yy, 420, yy + 33); cap_v(f, 420, yy + 40, color=RED); f.line(420, yy + 47, 420, yy + 76); gnd(f, 420, yy + 76)
        f.text(452, yy + 48, 'condensador', size=18, anchor='start', fill=RED, weight='bold')
    else:
        f.line(99, yy, 263, yy); cap_h(f, 270, yy, color=RED); f.line(277, yy, 541, yy)
        f.text(270, yy - 30, 'condensador', size=18, fill=RED, weight='bold')
        f.line(420, yy, 420, yy + 8); e = coil_v(f, 420, yy + 8, n=3, color=BLUE); f.line(420, e, 420, e + 6); gnd(f, 420, e + 6)
        f.text(452, yy + 48, 'bobina', size=18, anchor='start', fill=BLUE, weight='bold')
    f.circle(420, yy, 6, fill=WIRE, stroke=WIRE)
    f.text(396, yy + 100, 'masa', size=18, anchor='end', fill=MUTED)
f.save()

# 10 ── power supply stages with waveforms ─────────────────────────────────
def ripple(t, _c={}):
    if 'v' not in _c:
        v, out = 0.0, []
        for i in range(2401):
            v = max(abs(math.sin(2 * math.pi * 2 * i / 1200)), v - 0.0009)
            out.append(v)
        _c['v'] = out
    return _c['v'][1200 + int(t * 1200)]

f = Fig('s05-fuente-etapas', 826, 'Las cuatro etapas de una fuente de alimentación')
f.text(320, 42, 'Del enchufe a la emisora: las cuatro aduanas', size=22, weight='bold')
rows = [('Enchufe', '230 V alterna', lambda t: math.sin(4 * math.pi * t), 1.0, RED, True),
        ('1. Transformador', 'baja la tensión', lambda t: 0.45 * math.sin(4 * math.pi * t), 1.0, AMBER, True),
        ('2. Rectificador', 'un solo sentido', lambda t: 0.9 * abs(math.sin(4 * math.pi * t)) - 0.45, 1.0, AMBER, False),
        ('3. Filtro', 'rellena los valles', lambda t: 0.9 * ripple(t) - 0.45, 1.0, BLUE, False),
        ('4. Regulador', 'la deja clavada', lambda t: 0.22, 1.0, GREEN, False)]
for k, (name, sub, fn, sc, col, bip) in enumerate(rows):
    y = 66 + k * 144
    f.rect(30, y, 580, 126, fill=SOFT, rx=14)
    f.text(50, y + 54, name, size=21, weight='bold', anchor='start')
    f.text(50, y + 84, sub, size=19, anchor='start', fill=MUTED)
    px, pw, ym = 280, 300, y + 63
    f.rect(px - 10, y + 10, pw + 20, 106, fill='#FFFFFF', rx=10)
    base = ym if bip else ym + 0.45 * 44
    f.line(px, base, px + pw, base, stroke=MUTED, w=2, dash='4 5')
    wave(f, px, ym, pw, 44, fn, color=col, sw=4)
    if k < 4:
        f.line(140, y + 128, 140, y + 142, stroke=INK, w=4, arrow=True)
f.text(320, 804, 'La línea de puntos es el cero. La ondulación de la etapa 3 es el rizado', size=18, fill=MUTED)
f.save()

# 11 ── rectification ──────────────────────────────────────────────────────
f = Fig('s05-rectificacion', 600, 'Rectificación de media onda y de onda completa')
f.text(320, 42, 'Rectificar: media onda y onda completa', size=22, weight='bold')
rows = [('Entra: alterna', lambda t: math.sin(4 * math.pi * t), RED, ''),
        ('Un diodo: media onda', lambda t: max(0, math.sin(4 * math.pi * t)), AMBER, '50 pulsos por segundo'),
        ('Puente de cuatro diodos: onda completa', lambda t: abs(math.sin(4 * math.pi * t)), GREEN, '100 pulsos por segundo')]
for k, (name, fn, col, note) in enumerate(rows):
    y = 66 + k * 176
    f.rect(30, y, 580, 162, fill=SOFT, rx=14)
    f.text(50, y + 32, name, size=20, weight='bold', anchor='start')
    px, pw, ym = 60, 520, y + 96
    f.line(px, ym, px + pw, ym, stroke=MUTED, w=2, dash='4 5')
    wave(f, px, ym, pw, 40, fn, color=col, sw=5)
    if note:
        f.text(590, y + 152, note, size=18, anchor='end', fill=MUTED)
f.save()

# 12 ── amplifier classes ──────────────────────────────────────────────────
f = Fig('s05-clases-de-amplificador', 720, 'Clases de amplificador según el tiempo de conducción')
f.text(320, 42, 'Cuánto del ciclo conduce el transistor', size=22, weight='bold')
rows = [('Clase A', 'todo el ciclo', -2.0), ('Clase B', 'medio ciclo', 0.0),
        ('Clase AB', 'algo más de medio ciclo', -0.25), ('Clase C', 'un pulso breve', 0.6)]
for k, (name, sub, thr) in enumerate(rows):
    y = 66 + k * 156
    f.rect(30, y, 580, 142, fill=SOFT, rx=14)
    f.text(50, y + 60, name, size=24, weight='bold', anchor='start')
    px, pw, ym, amp = 250, 340, y + 60, 40
    f.text(px + pw / 2, y + 134, sub, size=19, weight='bold', fill=AMBER)
    f.rect(px - 10, y + 10, pw + 20, 100, fill='#FFFFFF', rx=10)
    fn = lambda t: math.sin(4 * math.pi * t)
    # shaded conduction region
    seg, n = [], 340
    for i in range(n + 1):
        t = i / n; v = fn(t)
        if v > thr:
            seg.append((px + pw * t, ym - amp * v))
        if (v <= thr or i == n) and seg:
            base = ym - amp * max(thr, -1.0)
            d = f'M{seg[0][0]:.1f} {base:.1f} L' + ' L'.join(f'{a:.1f} {b:.1f}' for a, b in seg) + f' L{seg[-1][0]:.1f} {base:.1f} Z'
            f.add(f'<path d="{d}" fill="{AMBER}" fill-opacity="0.45" stroke="{AMBER}" stroke-width="3"/>')
            seg = []
    wave(f, px, ym, pw, amp, fn, color=MUTED, sw=2, dash='5 5')
f.text(320, 706, 'Línea de puntos: la señal. En color: cuando conduce', size=18, fill=MUTED)
f.save()

# 13 ── saturation ─────────────────────────────────────────────────────────
f = Fig('s05-saturacion', 484, 'Señal limpia y señal recortada por saturación')
f.text(320, 42, 'Cuando se le pide demasiado', size=22, weight='bold')
for k, (name, fn, col) in enumerate([('Dentro de sus límites: senoide limpia', lambda t: 0.75 * math.sin(4 * math.pi * t), GREEN),
                                     ('Saturado: recorta. Armónicos e intermodulación', lambda t: max(-0.9, min(0.9, 1.3 * math.sin(4 * math.pi * t))), RED)]):
    y = 66 + k * 192
    f.rect(30, y, 580, 178, fill=SOFT, rx=14)
    f.text(320, y + 30, name, size=19, weight='bold', fill=col)
    px, pw, ym, amp = 60, 520, y + 106, 56
    f.line(px, ym - amp * 0.9, px + pw, ym - amp * 0.9, stroke=MUTED, w=2, dash='4 5')
    f.line(px, ym + amp * 0.9, px + pw, ym + amp * 0.9, stroke=MUTED, w=2, dash='4 5')
    wave(f, px, ym, pw, amp, fn, color=col, sw=5)
f.text(320, 464, 'Líneas de puntos: el tope que marca la alimentación', size=18, fill=MUTED)
f.save()

# 14 ── oscillator loop ────────────────────────────────────────────────────
f = Fig('s05-oscilador-lazo', 460, 'Un oscilador: amplificador realimentado a través de un circuito resonante')
f.text(320, 42, 'Un oscilador es un lazo', size=22, weight='bold')
ax, ay = 250, 150
f.path(f'M{ax} {ay-50} L{ax+110} {ay} L{ax} {ay+50} Z', stroke=INK, w=4, fill='#FFFFFF')
f.text(ax + 36, ay + 7, 'A', size=24, weight='bold')
f.text(ax + 55, ay - 64, 'amplificador', size=20, weight='bold')
f.text(ax + 55, ay + 80, 'repone las pérdidas', size=18, fill=MUTED)
f.path(f'M{ax+110} {ay} H480 V330 H430', stroke=BLUE, w=4, arrow=True)
f.rect(210, 296, 220, 68, fill='#FFFFFF', stroke=AMBER, sw=4, rx=10)
f.text(320, 326, 'circuito resonante', size=20, weight='bold', fill=AMBER)
f.text(320, 352, 'elige la frecuencia', size=18, fill=MUTED)
f.path(f'M210 330 H130 V{ay} H{ax-8}', stroke=BLUE, w=4, arrow=True)
f.text(92, 250, 'realimentación', size=19, fill=BLUE, weight='bold', rotate=-90)
f.circle(480, ay, 6, fill=BLUE, stroke=BLUE)
f.line(480, ay, 570, ay, stroke=GREEN, w=4, arrow=True)
f.text(540, ay - 16, 'salida', size=20, weight='bold', fill=GREEN)
f.text(320, 420, 'La señal da vueltas: vuelve a favor y con ganancia suficiente', size=19, fill=MUTED)
f.save()

# 15 ── receiver chain ─────────────────────────────────────────────────────
f = Fig('s05-cadena-receptor', 520, 'La cadena de bloques de un receptor')
f.text(320, 42, 'El receptor, leído de izquierda a derecha', size=22, weight='bold')
def block(x, y, l1, l2=None, col=INK, w=138):
    f.rect(x, y, w, 70, fill='#FFFFFF', stroke=col, sw=3, rx=10)
    if l2:
        f.text(x + w / 2, y + 30, l1, size=18, weight='bold', fill=col); f.text(x + w / 2, y + 54, l2, size=18, weight='bold', fill=col)
    else:
        f.text(x + w / 2, y + 42, l1, size=18, weight='bold', fill=col)
xs = [11, 171, 331, 491]
r1 = [('Antena', None, INK), ('Filtro', 'paso banda', AMBER), ('Amplificador', None, BLUE), ('Mezclador', None, MUTED)]
for x, (a, b, c) in zip(xs, r1):
    block(x, 80, a, b, c)
for x in xs[:3]:
    f.line(x + 140, 115, x + 156, 115, stroke=INK, w=4, arrow=True)
block(331, 196, 'Oscilador', None, GREEN)
f.path('M469 231 H540 V158', stroke=GREEN, w=4, arrow=True)
f.text(322, 238, '(sección 7)', size=18, anchor='end', fill=MUTED)
f.path('M600 150 V288 H80 V304', stroke=INK, w=3, dash='5 5', arrow=True)
r2 = [('Filtro', 'estrecho', AMBER), ('Amplificador', None, BLUE), ('Detector', None, RED), ('Audio y', 'altavoz', INK)]
for x, (a, b, c) in zip(xs, r2):
    block(x, 310, a, b, c)
for x in xs[:3]:
    f.line(x + 140, 345, x + 156, 345, stroke=INK, w=4, arrow=True)
f.rect(11, 420, 618, 56, fill='#FDE68A', stroke=INK, sw=3, rx=10)
f.text(320, 455, 'Fuente de alimentación: alimenta todas las etapas', size=19, weight='bold')
f.text(320, 504, 'El mezclador y su oscilador se explican en la sección 7', size=18, fill=MUTED)
f.save()


# 16 ── series and parallel LC ─────────────────────────────────────────────
f = Fig('s05-lc-serie-y-paralelo', 520, 'Circuito LC serie y circuito LC paralelo')
f.text(320, 42, 'La misma pareja, conectada de dos maneras', size=22, weight='bold')
f.rect(30, 66, 580, 196, fill=SOFT, rx=14)
f.text(320, 98, 'En serie: uno detrás de otro', size=21, weight='bold')
yy = 150
f.circle(92, yy, 7, fill='#FFFFFF', stroke=INK, sw=3); f.circle(548, yy, 7, fill='#FFFFFF', stroke=INK, sw=3)
f.line(99, yy, 200, yy); e = coil_h(f, 200, yy, color=BLUE); f.line(e, yy, 393, yy); cap_h(f, 400, yy, color=RED); f.line(407, yy, 541, yy)
f.text(320, 212, 'En resonancia: impedancia MÍNIMA', size=20, weight='bold', fill=GREEN)
f.text(320, 240, 'una puerta abierta para esa frecuencia', size=19, fill=MUTED)
f.rect(30, 276, 580, 230, fill=SOFT, rx=14)
f.text(320, 308, 'En paralelo: uno al lado del otro', size=21, weight='bold')
ty, by = 340, 416
my = (ty + by) / 2
f.circle(92, my, 7, fill='#FFFFFF', stroke=INK, sw=3); f.circle(548, my, 7, fill='#FFFFFF', stroke=INK, sw=3)
f.line(99, my, 230, my); f.line(410, my, 541, my)
f.line(230, ty, 230, by); f.line(410, ty, 410, by)
f.line(230, ty, 276, ty); e = coil_h(f, 276, ty, color=BLUE); f.line(e, ty, 410, ty)
f.line(230, by, 313, by); cap_h(f, 320, by, color=RED); f.line(327, by, 410, by)
f.text(320, 466, 'En resonancia: impedancia MÁXIMA', size=20, weight='bold', fill=AMBER)
f.text(320, 492, 'un tapón para esa frecuencia', size=19, fill=MUTED)
f.save()

# 17 ── pi and T low-pass filters ──────────────────────────────────────────
f = Fig('s05-filtros-pi-y-t', 500, 'Filtros paso bajo en pi y en T')
f.text(320, 42, 'Tres piezas: filtros en π y en T', size=22, weight='bold')
def shunt_cap(x, yy):
    f.circle(x, yy, 6, fill=WIRE, stroke=WIRE)
    f.line(x, yy, x, yy + 33); cap_v(f, x, yy + 40, color=RED); f.line(x, yy + 47, x, yy + 72); gnd(f, x, yy + 72)
for k, name in enumerate(['Paso bajo en π', 'Paso bajo en T']):
    y = 66 + k * 214
    f.rect(30, y, 580, 200, fill=SOFT, rx=14)
    f.text(320, y + 32, name, size=21, weight='bold')
    yy = y + 78
    f.circle(72, yy, 7, fill='#FFFFFF', stroke=INK, sw=3); f.circle(568, yy, 7, fill='#FFFFFF', stroke=INK, sw=3)
    if k == 0:
        f.line(79, yy, 276, yy); e = coil_h(f, 276, yy, color=BLUE); f.line(e, yy, 561, yy)
        shunt_cap(190, yy); shunt_cap(450, yy)
    else:
        f.line(79, yy, 150, yy); e = coil_h(f, 150, yy, color=BLUE); f.line(e, yy, 402, yy); e2 = coil_h(f, 402, yy, color=BLUE); f.line(e2, yy, 561, yy)
        shunt_cap(320, yy)
    f.text(72, yy + 34, 'entra', size=18, fill=MUTED); f.text(568, yy + 34, 'sale', size=18, fill=MUTED)
f.save()

# 18 ── bridge rectifier, both current paths ───────────────────────────────
def diode_v(f, x, y, color):
    f.path(f'M{x-15} {y+13} L{x+15} {y+13} L{x} {y-13} Z', stroke=color, w=3, fill=color if color != MUTED else '#FFFFFF')
    f.line(x - 15, y - 13, x + 15, y - 13, stroke=color, w=4)

f = Fig('s05-puente-rectificador', 720, 'El puente rectificador en los dos semiciclos')
f.text(320, 42, 'El puente de cuatro diodos', size=22, weight='bold')
for k in range(2):
    y = 66 + k * 314
    f.rect(30, y, 580, 300, fill=SOFT, rx=14)
    f.text(320, y + 32, 'Semiciclo positivo' if k == 0 else 'Semiciclo negativo', size=21, weight='bold')
    x1, x2, top, mid, bot, xl = 170, 330, y + 70, y + 160, y + 250, 500
    on = [(x1, 'u'), (x2, 'd')] if k == 0 else [(x2, 'u'), (x1, 'd')]
    def col(x, pos):
        return RED if (x, pos) in on else MUTED
    # rails and columns (grey base)
    for x in (x1, x2):
        f.line(x, top, x, bot, stroke=MUTED, w=3)
    f.path(f'M{x1} {top} H{xl} V{mid-34}', stroke=MUTED, w=3); f.path(f'M{xl} {mid+34} V{bot} H{x1}', stroke=MUTED, w=3)
    f.line(x1, mid, x2 - 92, mid, stroke=MUTED, w=3); f.line(x2 - 28, mid, x2, mid, stroke=MUTED, w=3)
    # active path in red
    xa, xb = (x1, x2) if k == 0 else (x2, x1)
    f.path(f'M{xa} {mid} V{top} H{xl} V{mid-34}', stroke=RED, w=5, arrow=True)
    f.path(f'M{xl} {mid+34} V{bot} H{xb} V{mid}', stroke=RED, w=5)
    if k == 0:
        f.line(x2, mid, x2 - 28, mid, stroke=RED, w=5); f.line(x2 - 92, mid, x1, mid, stroke=RED, w=5)
    else:
        f.line(x1, mid, x2 - 92, mid, stroke=RED, w=5); f.line(x2 - 28, mid, x2, mid, stroke=RED, w=5)
    for x in (x1, x2):
        diode_v(f, x, (top + mid) / 2, col(x, 'u')); diode_v(f, x, (mid + bot) / 2, col(x, 'd'))
        f.circle(x, mid, 6, fill=INK, stroke=INK)
    # source and load
    f.circle(x2 - 60, mid, 32, fill='#FFFFFF', stroke=INK, sw=3)
    f.text(x2 - 60, mid + 9, '∼', size=30, weight='bold')
    f.text(x2 - 60, mid + 60, 'del', size=18, fill=MUTED); f.text(x2 - 60, mid + 80, 'transformador', size=18, fill=MUTED)
    f.rect(xl - 44, mid - 34, 88, 68, fill='#FFFFFF', stroke=INK, sw=3, rx=8)
    f.text(xl, mid + 7, 'aparato', size=19, weight='bold')
    f.text(xl + 54, mid - 46, '+', size=26, weight='bold', fill=RED); f.text(xl + 54, mid + 62, '−', size=26, weight='bold', fill=BLUE)
    f.line(xl + 80, mid - 24, xl + 80, mid + 24, stroke=GREEN, w=4, arrow=True)
f.text(320, 704, 'En los dos casos, el aparato recibe la corriente en el mismo sentido', size=18, fill=MUTED)
f.save()
