"""Figures of section 4 (components)."""
import math
from figlib import *

COPPER = '#B4682A'
LIGHTWATER = '#BAE6FD'
DEEPWATER = '#0284C7'


def zigzag(f, x, y, color=AMBER):
    """Horizontal resistor symbol, 120 wide, starting at x."""
    f.path(f'M{x} {y} l10 -16 l20 32 l20 -32 l20 32 l20 -32 l20 32 l10 -16', stroke=color, w=4)


def darrow(f, x1, x2, y, color):
    """Double-headed horizontal arrow."""
    m = (x1 + x2) / 2
    f.line(m, y, x1, y, stroke=color, w=4, arrow=True)
    f.line(m, y, x2, y, stroke=color, w=4, arrow=True)


# 1 ── colour code ─────────────────────────────────────────────────────────
f = Fig('s04-codigo-colores', 560, 'El código de colores de las resistencias')
f.text(320, 42, 'Cómo se lee una resistencia', size=22, weight='bold')
f.line(60, 115, 170, 115, stroke='#9CA3AF', w=6)
f.line(470, 115, 580, 115, stroke='#9CA3AF', w=6)
f.rect(170, 78, 300, 74, fill='#E8D3A9', stroke=INK, sw=3, rx=30)
bands = [(214, '#FACC15', '4'), (264, '#7C3AED', '7'), (314, '#DC2626', '00'), (414, '#C9A227', '± 5 %')]
for x, col, lab in bands:
    f.rect(x - 12, 79.5, 24, 71, fill=col, stroke=INK, sw=1.5, rx=0)
    f.line(x, 156, x, 178, stroke=MUTED, w=2)
    f.text(x, 204, lab, size=24 if lab != '± 5 %' else 20, weight='bold')
f.text(214, 230, 'cifra', size=18, fill=MUTED)
f.text(264, 230, 'cifra', size=18, fill=MUTED)
f.text(322, 230, 'ceros', size=18, fill=MUTED)
f.text(424, 230, 'tolerancia', size=18, fill=MUTED)
f.text(320, 280, '4 · 7 · 00  →  4.700 Ω  =  4,7 kΩ', size=24, weight='bold', fill=GREEN)
f.line(60, 304, 580, 304, stroke=PAPER_EDGE, w=2)
cols = [('#111111', 'negro'), ('#7B4A1E', 'marrón'), ('#DC2626', 'rojo'), ('#F97316', 'naranja'), ('#FACC15', 'amarillo'),
        ('#16A34A', 'verde'), ('#2563EB', 'azul'), ('#7C3AED', 'violeta'), ('#9CA3AF', 'gris'), ('#FFFFFF', 'blanco')]
for k, (col, name) in enumerate(cols):
    cx = 84 + (k % 5) * 118
    y = 330 + (k // 5) * 112
    f.rect(cx - 44, y, 44, 44, fill=col, stroke=INK, sw=2, rx=8)
    f.text(cx + 22, y + 33, str(k), size=30, weight='bold')
    f.text(cx - 6, y + 72, name, size=19, fill=MUTED)
f.save()

# 2 ── LED with series resistor ────────────────────────────────────────────
f = Fig('s04-led-con-resistencia', 380, 'Un LED con su resistencia en serie')
f.text(320, 42, 'El LED y su resistencia, en fila', size=22, weight='bold')
L, R, T, B = 110, 530, 120, 300
f.path(f'M{L} {T+40} V{T} H230')
zigzag(f, 230, T)
f.path(f'M350 {T} H{R} V{T+60}')
f.path(f'M{R} {T+98} V{B} H{L} V{T+132}')
f.battery(L, T + 40, h=100)
f.text(L + 44, T + 96, '12 V', size=22, anchor='start', weight='bold')
f.text(290, T - 30, '560 Ω', size=22, weight='bold', fill=AMBER)
f.text(290, T + 52, 'se queda 10 V', size=20, weight='bold', fill=AMBER)
# LED (pointing down)
f.path(f'M{R-20} {T+60} L{R+20} {T+60} L{R} {T+96} Z', stroke=INK, w=3, fill='#FCA5A5')
f.line(R - 20, T + 98, R + 20, T + 98, stroke=INK, w=4)
f.line(R + 28, T + 66, R + 50, T + 54, stroke=RED, w=3, arrow=True)
f.line(R + 28, T + 84, R + 50, T + 72, stroke=RED, w=3, arrow=True)
f.text(R - 34, T + 76, 'LED', size=22, anchor='end', weight='bold')
f.text(R - 34, T + 102, 'se queda 2 V', size=20, anchor='end', weight='bold', fill=RED)
f.line(380, T - 20, 470, T - 20, stroke=BLUE, w=4, arrow=True)
f.text(425, T - 34, '18 mA', size=20, weight='bold', fill=BLUE)
f.text(320, 348, '10 V + 2 V = 12 V · la misma corriente por los dos', size=19, fill=MUTED)
f.save()

# 3 ── capacitor and rubber membrane ───────────────────────────────────────
f = Fig('s04-condensador-y-membrana', 580, 'Un condensador cargado y su equivalente con agua')
f.text(320, 42, 'Un condensador cargado', size=22, weight='bold')
f.line(110, 150, 290, 150); f.line(350, 150, 530, 150)
f.rect(295, 88, 50, 124, fill='#E0E7FF', rx=0)
f.rect(284, 84, 12, 132, fill=INK, rx=2); f.rect(344, 84, 12, 132, fill=INK, rx=2)
for k in range(4):
    y = 110 + k * 30
    f.text(264, y, '−', size=26, weight='bold', fill=BLUE)
    f.text(376, y, '+', size=26, weight='bold', fill=RED)
f.text(170, 118, 'sobran electrones', size=18, fill=BLUE)
f.text(476, 118, 'faltan electrones', size=18, fill=RED)
f.text(170, 190, 'placa', size=19, fill=MUTED); f.text(476, 190, 'placa', size=19, fill=MUTED)
f.text(320, 246, 'en medio, un aislante (dieléctrico)', size=19, fill=MUTED)
f.line(60, 278, 580, 278, stroke=PAPER_EDGE, w=2)
f.text(320, 318, 'Con agua: una membrana de goma', size=22, weight='bold')
f.rect(70, 350, 500, 110, fill=LIGHTWATER, stroke=DEEPWATER, sw=3, rx=8)
f.path('M320 351 Q396 405 320 459', stroke=RED, w=7)
f.line(110, 405, 230, 405, stroke=DEEPWATER, w=5, arrow=True)
f.text(170, 388, 'presión', size=19, fill=DEEPWATER, weight='bold')
f.text(470, 412, 'el agua no pasa', size=19, fill=DEEPWATER)
f.text(320, 494, 'membrana abombada: guarda la presión', size=19, fill=RED, weight='bold')
f.text(320, 546, 'Nada la cruza, pero el agua se desplaza a los dos lados', size=18, fill=MUTED)
f.save()

# 4 ── charging curve ──────────────────────────────────────────────────────
f = Fig('s04-carga-condensador', 450, 'Carga de un condensador a través de una resistencia')
f.text(320, 42, 'Así se carga un condensador', size=22, weight='bold')
X0, Y0, H, TAU = 80, 350, 240, 96
f.line(X0, Y0, 590, Y0, stroke=INK, w=3, arrow=True)
f.line(X0, Y0, X0, 80, stroke=INK, w=3, arrow=True)
f.line(X0, Y0 - H, 580, Y0 - H, stroke=MUTED, w=2, dash='6 6')
f.text(585, Y0 - H - 10, 'tensión de la batería', size=18, anchor='end', fill=MUTED)
up = ' '.join(f'{"M" if t == 0 else "L"}{X0 + t} {Y0 - H * (1 - math.exp(-t / TAU)):.1f}' for t in range(0, 481, 6))
dn = ' '.join(f'{"M" if t == 0 else "L"}{X0 + t} {Y0 - H * math.exp(-t / TAU):.1f}' for t in range(0, 481, 6))
f.path(dn, stroke=RED, w=4, dash='10 7')
f.path(up, stroke=BLUE, w=5)
y63 = Y0 - H * 0.632
f.line(X0 + TAU, Y0, X0 + TAU, y63, stroke=MUTED, w=2, dash='4 5')
f.circle(X0 + TAU, y63, 6, fill=BLUE, stroke=BLUE)
f.text(X0 + TAU + 14, y63 + 26, '63 %', size=20, anchor='start', weight='bold', fill=BLUE)
f.text(X0 + TAU, Y0 + 28, 'R × C', size=20, weight='bold')
f.text(X0 + 5 * TAU, Y0 + 28, '5 × R × C', size=20, weight='bold')
f.text(330, Y0 + 62, 'tiempo', size=19, fill=MUTED)
f.text(400, 168, 'tensión en el condensador', size=19, weight='bold', fill=BLUE)
f.text(330, 300, 'corriente', size=19, weight='bold', fill=RED)
f.save()

# 5 ── capacitor with DC and AC ────────────────────────────────────────────
f = Fig('s04-condensador-cc-ca', 470, 'La membrana con corriente continua y con alterna')
f.text(320, 42, 'Con continua: se abomba y el agua se para', size=21, weight='bold')
f.rect(90, 70, 460, 90, fill=LIGHTWATER, stroke=DEEPWATER, sw=3, rx=8)
f.path('M320 71 Q392 115 320 159', stroke=RED, w=7)
f.line(120, 115, 220, 115, stroke=DEEPWATER, w=5, arrow=True)
f.text(455, 122, 'parada', size=20, weight='bold', fill=MUTED)
f.text(320, 196, 'La bomba empuja siempre hacia el mismo lado', size=18, fill=MUTED)
f.line(60, 224, 580, 224, stroke=PAPER_EDGE, w=2)
f.text(320, 264, 'Con alterna: oscila y el agua va y viene', size=21, weight='bold')
f.rect(90, 292, 460, 90, fill=LIGHTWATER, stroke=DEEPWATER, sw=3, rx=8)
f.path('M320 293 Q392 337 320 381', stroke=RED, w=7)
f.path('M320 293 Q248 337 320 381', stroke=RED, w=5, dash='8 7')
darrow(f, 115, 225, 337, DEEPWATER)
darrow(f, 415, 525, 337, DEEPWATER)
f.text(320, 418, 'El émbolo empuja y tira, sin parar', size=18, fill=MUTED)
f.text(320, 446, 'Ni una gota cruza la membrana', size=18, fill=MUTED)
f.save()

# 6 ── coil and its field ──────────────────────────────────────────────────
f = Fig('s04-bobina-y-campo', 420, 'Una bobina y su campo magnético')
f.text(320, 42, 'Una bobina y su campo magnético', size=22, weight='bold')
f.path('M470 178 C 640 70, 0 70, 170 178', stroke=BLUE, w=3, dash='9 7')
f.path('M470 242 C 640 350, 0 350, 170 242', stroke=BLUE, w=3, dash='9 7')
f.line(110, 210, 532, 210, stroke=BLUE, w=4, arrow=True, dash='9 7')
for k in range(6):
    cx = 200 + k * 48
    f.add(f'<ellipse cx="{cx}" cy="210" rx="20" ry="58" fill="none" stroke="{COPPER}" stroke-width="6"/>')
f.path('M180 210 C150 300, 120 330, 80 350', stroke=COPPER, w=6)
f.path('M460 210 C490 300, 520 330, 560 350', stroke=COPPER, w=6)
f.text(320, 92, 'campo magnético', size=20, weight='bold', fill=BLUE)
f.text(96, 384, 'entra la corriente', size=18, fill=MUTED)
f.text(544, 384, 'sale la corriente', size=18, fill=MUTED)
f.text(320, 316, 'espiras de hilo', size=19, fill=COPPER, weight='bold')
f.save()

# 7 ── reactances vs frequency ─────────────────────────────────────────────
f = Fig('s04-reactancias', 440, 'Reactancia de la bobina y del condensador según la frecuencia')
f.text(320, 42, 'Lo que estorba cada uno, según la frecuencia', size=21, weight='bold')
X0, Y0 = 90, 350
f.line(X0, Y0, 590, Y0, stroke=INK, w=3, arrow=True)
f.line(X0, Y0, X0, 76, stroke=INK, w=3, arrow=True)
f.line(X0, Y0, X0 + 480, Y0 - 240, stroke=BLUE, w=5)
xc = ' '.join(f'{"M" if t == 100 else "L"}{X0 + t} {Y0 - 27000 / t:.1f}' for t in range(100, 481, 5))
f.path(xc, stroke=RED, w=5)
tx = math.sqrt(54000)
f.circle(X0 + tx, Y0 - tx / 2, 9, fill='#FFFFFF', stroke=INK, sw=3)
f.text(X0 + tx + 40, Y0 - tx / 2 + 86, 'aquí estorban lo mismo', size=18, anchor='start', fill=MUTED)
f.line(X0 + tx + 36, Y0 - tx / 2 + 76, X0 + tx + 8, Y0 - tx / 2 + 10, stroke=MUTED, w=2)
f.text(560, 96, 'bobina: sube', size=20, anchor='end', weight='bold', fill=BLUE)
f.text(206, 96, 'condensador: baja', size=20, anchor='start', weight='bold', fill=RED)
f.text(340, Y0 + 34, 'frecuencia', size=19, fill=MUTED)
f.text(96, 416, 'baja', size=18, fill=MUTED); f.text(566, 416, 'alta', size=18, fill=MUTED)
f.text(52, 220, 'oposición (ohmios)', size=19, fill=MUTED, rotate=-90)
f.save()

# 8 ── transformer ─────────────────────────────────────────────────────────
f = Fig('s04-transformador', 440, 'Un transformador y su relación de espiras')
f.text(320, 42, 'Un transformador', size=22, weight='bold')
f.rect(238, 96, 164, 216, fill='none', stroke='#6B7280', sw=22, rx=6)
f.rect(262, 120, 116, 168, fill='none', stroke=BLUE, sw=3, rx=30)
for k in range(13):
    y = 132 + k * 12
    f.line(222, y + 5, 254, y - 5, stroke=COPPER, w=4)
for k in range(4):
    y = 174 + k * 20
    f.line(386, y + 6, 418, y - 6, stroke=COPPER, w=7)
f.path('M222 137 H150', stroke=COPPER, w=4); f.path('M222 281 H150', stroke=COPPER, w=4)
f.path('M418 168 H490', stroke=COPPER, w=6); f.path('M418 240 H490', stroke=COPPER, w=6)
f.text(104, 110, 'primario', size=20, weight='bold')
f.text(104, 196, '920', size=24, weight='bold', fill=COPPER); f.text(104, 220, 'espiras', size=18, fill=COPPER)
f.text(104, 268, '230 V', size=26, weight='bold', fill=RED)
f.text(536, 110, 'secundario', size=20, weight='bold')
f.text(536, 196, '48', size=24, weight='bold', fill=COPPER); f.text(536, 220, 'espiras', size=18, fill=COPPER)
f.text(536, 268, '12 V', size=26, weight='bold', fill=GREEN)
f.text(320, 212, 'campo', size=18, fill=BLUE); f.text(320, 234, 'magnético', size=18, fill=BLUE)
f.text(320, 360, 'núcleo de hierro: las bobinas no se tocan', size=19, fill=MUTED)
f.text(320, 404, '230 / 920 = 0,25 V por espira · 48 × 0,25 = 12 V', size=19, weight='bold')
f.save()

# 9 ── PN junction ─────────────────────────────────────────────────────────
f = Fig('s04-union-pn', 560, 'La unión PN en directa y en inversa')
f.text(320, 42, 'La unión PN', size=22, weight='bold')
for k, (half, lsign, rsign, cap, col) in enumerate([(5, '+', '−', 'Directa: la barrera se cierra y la corriente pasa', GREEN),
                                                     (42, '−', '+', 'Inversa: la barrera se ensancha y no pasa nada', RED)]):
    y = 70 + k * 170
    f.line(100, y + 45, 170, y + 45); f.line(470, y + 45, 540, y + 45)
    f.rect(170, y, 150 - half, 90, fill='#FECACA', stroke=INK, sw=3, rx=0)
    f.rect(320 + half, y, 150 - half, 90, fill='#BFDBFE', stroke=INK, sw=3, rx=0)
    f.rect(320 - half, y, 2 * half, 90, fill='#E5E7EB', stroke=INK, sw=3, rx=0)
    f.text(215, y + 56, 'P', size=30, weight='bold', fill='#991B1B')
    f.text(425, y + 56, 'N', size=30, weight='bold', fill='#1E3A8A')
    f.text(76, y + 56, lsign, size=34, weight='bold', fill=RED if lsign == '+' else BLUE)
    f.text(564, y + 56, rsign, size=34, weight='bold', fill=RED if rsign == '+' else BLUE)
    if k == 0:
        f.line(250, y + 74, 390, y + 74, stroke=GREEN, w=5, arrow=True)
    else:
        f.text(320, y + 54, 'barrera', size=18, fill=MUTED)
    f.text(320, y + 124, cap, size=19, weight='bold', fill=col)
f.line(60, 384, 580, 384, stroke=PAPER_EDGE, w=2)
f.text(320, 420, 'El símbolo del diodo', size=20, weight='bold')
f.line(200, 470, 290, 470); f.line(330, 470, 430, 470)
f.path('M290 448 L290 492 L330 470 Z', stroke=INK, w=3, fill='#FFFFFF')
f.line(332, 446, 332, 494, stroke=INK, w=5)
f.text(188, 477, 'ánodo (P)', size=20, anchor='end', weight='bold')
f.text(442, 477, 'cátodo (N)', size=20, anchor='start', weight='bold')
f.text(320, 532, 'La flecha indica por dónde puede pasar la corriente', size=18, fill=MUTED)
f.save()

# 10 ── half-wave rectification ────────────────────────────────────────────
f = Fig('s04-rectificacion', 380, 'Rectificación de media onda con un diodo')
f.text(320, 42, 'Rectificar: dejar pasar solo un sentido', size=22, weight='bold')
YM, A = 180, 62
def wave(x0, half=False):
    pts = []
    for i in range(0, 201, 4):
        v = math.sin(i / 200 * 4 * math.pi)
        if half:
            v = max(v, 0)
        pts.append(f'{"M" if i == 0 else "L"}{x0 + i} {YM - A * v:.1f}')
    return ' '.join(pts)
f.line(40, YM, 250, YM, stroke=MUTED, w=2, dash='5 6')
f.line(390, YM, 600, YM, stroke=MUTED, w=2, dash='5 6')
f.path(wave(45), stroke=BLUE, w=5)
f.path(wave(395, half=True), stroke=GREEN, w=5)
f.line(262, YM, 300, YM); f.line(340, YM, 378, YM)
f.path(f'M300 {YM-22} L300 {YM+22} L340 {YM} Z', stroke=INK, w=3, fill='#FFFFFF')
f.line(342, YM - 24, 342, YM + 24, stroke=INK, w=5)
f.text(320, YM - 40, 'diodo', size=19, weight='bold')
f.text(145, 290, 'entra: alterna', size=20, weight='bold', fill=BLUE)
f.text(145, 316, '(va y viene)', size=18, fill=MUTED)
f.text(495, 290, 'sale: un solo sentido', size=20, weight='bold', fill=GREEN)
f.text(495, 316, '(a impulsos)', size=18, fill=MUTED)
f.text(495, YM + 34, 'bloqueado', size=18, fill=MUTED)
f.save()

# 11 ── transistor as a tap ────────────────────────────────────────────────
f = Fig('s04-transistor-y-grifo', 560, 'Un grifo y un transistor')
f.text(320, 42, 'Un grifo…', size=22, weight='bold')
f.rect(90, 120, 460, 44, fill=LIGHTWATER, stroke=DEEPWATER, sw=3, rx=6)
f.rect(296, 108, 48, 68, fill='#FFFFFF', stroke=INK, sw=3, rx=6)
f.line(320, 108, 320, 78, stroke=INK, w=5); f.line(292, 78, 348, 78, stroke=INK, w=7)
f.text(362, 86, 'manecilla: poco esfuerzo', size=19, anchor='start', weight='bold', fill=BLUE)
f.line(120, 142, 270, 142, stroke=DEEPWATER, w=6, arrow=True)
f.line(370, 142, 520, 142, stroke=DEEPWATER, w=6, arrow=True)
f.text(320, 206, 'caudal grande, que mueve la bomba', size=19, weight='bold', fill=DEEPWATER)
f.line(60, 234, 580, 234, stroke=PAPER_EDGE, w=2)
f.text(320, 274, '…y un transistor', size=22, weight='bold')
CX, CY = 300, 400
f.circle(CX, CY, 52, fill='#FFFFFF', stroke=INK, sw=3)
f.line(CX - 16, CY - 28, CX - 16, CY + 28, stroke=INK, w=6)
f.line(CX - 16, CY, CX - 130, CY)
f.path(f'M{CX-16} {CY-12} L{CX+20} {CY-40} V{CY-100}')
f.path(f'M{CX-16} {CY+12} L{CX+20} {CY+40}', arrow=True)
f.line(CX + 20, CY + 40, CX + 20, CY + 100)
f.text(CX + 34, CY - 84, 'colector', size=20, anchor='start', weight='bold')
f.text(CX + 34, CY + 98, 'emisor', size=20, anchor='start', weight='bold')
f.text(CX - 136, CY - 12, 'base', size=20, anchor='end', weight='bold')
f.line(CX - 120, CY + 20, CX - 40, CY + 20, stroke=BLUE, w=3, arrow=True)
f.text(CX - 130, CY + 54, 'corriente pequeña', size=18, fill=BLUE, weight='bold')
f.line(470, CY - 96, 470, CY + 96, stroke=AMBER, w=9, arrow=True)
f.text(540, CY - 6, 'corriente', size=19, weight='bold', fill=AMBER)
f.text(540, CY + 18, 'grande', size=19, weight='bold', fill=AMBER)
f.text(320, 536, 'La base manda; la energía la pone la fuente', size=19, fill=MUTED)
f.save()

# 12 ── schematic symbols of the section ───────────────────────────────────
def _hump(cx, cy, n=4, r=8, up=True):
    x0 = cx - n * r
    sweep = 1 if up else 0
    return f'M{x0} {cy} ' + ' '.join(f'a{r} {r} 0 0 {sweep} {2*r} 0' for _ in range(n))

def sym_res(f, cx, cy):
    f.line(cx - 60, cy, cx - 30, cy, w=3); f.line(cx + 30, cy, cx + 60, cy, w=3)
    f.path(f'M{cx-30} {cy} l5 -10 l10 20 l10 -20 l10 20 l10 -20 l10 20 l5 -10', stroke=INK, w=3)

def sym_pot(f, cx, cy):
    sym_res(f, cx, cy)
    f.line(cx, cy - 40, cx, cy - 14, stroke=INK, w=3, arrow=True)

def sym_cap(f, cx, cy, plus=False, var=False):
    f.line(cx - 60, cy, cx - 7, cy, w=3); f.line(cx + 7, cy, cx + 60, cy, w=3)
    f.line(cx - 7, cy - 22, cx - 7, cy + 22, stroke=INK, w=4); f.line(cx + 7, cy - 22, cx + 7, cy + 22, stroke=INK, w=4)
    if plus:
        f.text(cx - 26, cy - 10, '+', size=22, weight='bold')
    if var:
        f.line(cx - 28, cy + 28, cx + 28, cy - 28, stroke=INK, w=3, arrow=True)

def sym_coil(f, cx, cy, core=False):
    f.line(cx - 60, cy, cx - 32, cy, w=3); f.line(cx + 32, cy, cx + 60, cy, w=3)
    f.path(_hump(cx, cy), stroke=INK, w=3)
    if core:
        f.line(cx - 32, cy - 18, cx + 32, cy - 18, stroke=INK, w=3); f.line(cx - 32, cy - 25, cx + 32, cy - 25, stroke=INK, w=3)

def sym_trafo(f, cx, cy):
    f.path(_hump(cx, cy - 12, up=True), stroke=INK, w=3)
    f.path(_hump(cx, cy + 12, up=False), stroke=INK, w=3)
    f.line(cx - 32, cy - 3, cx + 32, cy - 3, stroke=INK, w=3); f.line(cx - 32, cy + 3, cx + 32, cy + 3, stroke=INK, w=3)
    for sx in (-1, 1):
        f.path(f'M{cx+sx*32} {cy-12} V{cy-34}', stroke=INK, w=3); f.path(f'M{cx+sx*32} {cy+12} V{cy+34}', stroke=INK, w=3)

def sym_diode(f, cx, cy, kind='d'):
    f.line(cx - 60, cy, cx - 14, cy, w=3)
    f.path(f'M{cx-14} {cy-17} L{cx-14} {cy+17} L{cx+14} {cy} Z', stroke=INK, w=3, fill='#FFFFFF')
    if kind == 'z':
        f.path(f'M{cx+7} {cy-23} L{cx+15} {cy-18} V{cy+18} L{cx+23} {cy+23}', stroke=INK, w=4)
    else:
        f.line(cx + 15, cy - 18, cx + 15, cy + 18, stroke=INK, w=4)
    if kind == 'v':
        f.line(cx + 25, cy - 18, cx + 25, cy + 18, stroke=INK, w=4)
        f.line(cx + 25, cy, cx + 60, cy, w=3)
    else:
        f.line(cx + 15, cy, cx + 60, cy, w=3)
    if kind == 'l':
        f.line(cx + 2, cy - 24, cx + 18, cy - 42, stroke=INK, w=3, arrow=True)
        f.line(cx + 18, cy - 22, cx + 34, cy - 40, stroke=INK, w=3, arrow=True)

def sym_bjt(f, cx, cy, npn=True):
    f.circle(cx, cy, 30, fill='#FFFFFF', stroke=INK, sw=3)
    f.line(cx - 10, cy - 18, cx - 10, cy + 18, stroke=INK, w=5)
    f.line(cx - 60, cy, cx - 10, cy, w=3)
    f.path(f'M{cx-10} {cy-8} L{cx+14} {cy-24} V{cy-46}', stroke=INK, w=3)
    if npn:
        f.path(f'M{cx-10} {cy+8} L{cx+14} {cy+24}', stroke=INK, w=3, arrow=True)
    else:
        f.path(f'M{cx+14} {cy+24} L{cx-7} {cy+10}', stroke=INK, w=3, arrow=True)
    f.line(cx + 14, cy + 24, cx + 14, cy + 46, w=3)

def sym_fet(f, cx, cy):
    f.circle(cx, cy, 30, fill='#FFFFFF', stroke=INK, sw=3)
    f.line(cx - 6, cy - 20, cx - 6, cy + 20, stroke=INK, w=5)
    f.line(cx - 60, cy, cx - 9, cy, stroke=INK, w=3, arrow=True)
    f.path(f'M{cx-6} {cy-12} H{cx+14} V{cy-46}', stroke=INK, w=3)
    f.path(f'M{cx-6} {cy+12} H{cx+14} V{cy+46}', stroke=INK, w=3)

f = Fig('s04-simbolos', 800, 'Símbolos de los componentes de la sección')
f.text(320, 42, 'Los símbolos de los componentes', size=22, weight='bold')
cells = [
    (sym_res, {}, 'resistencia', ''),
    (sym_pot, {}, 'potenciómetro', ''),
    (sym_cap, {}, 'condensador', ''),
    (sym_cap, {'plus': True}, 'condensador', 'electrolítico'),
    (sym_cap, {'var': True}, 'condensador', 'variable'),
    (sym_coil, {}, 'bobina', ''),
    (sym_coil, {'core': True}, 'bobina', 'con núcleo'),
    (sym_trafo, {}, 'transformador', ''),
    (sym_diode, {}, 'diodo', ''),
    (sym_diode, {'kind': 'l'}, 'LED', ''),
    (sym_diode, {'kind': 'z'}, 'zéner', ''),
    (sym_diode, {'kind': 'v'}, 'varicap', ''),
    (sym_bjt, {'npn': True}, 'transistor NPN', ''),
    (sym_bjt, {'npn': False}, 'transistor PNP', ''),
    (sym_fet, {}, 'transistor FET', ''),
]
for k, (fn, kw, l1, l2) in enumerate(cells):
    cx = 110 + (k % 3) * 210
    top = 62 + (k // 3) * 146
    f.rect(cx - 98, top, 196, 136, fill=SOFT, rx=12)
    fn(f, cx, top + 54, **kw)
    if l2:
        f.text(cx, top + 108, l1, size=18, weight='bold'); f.text(cx, top + 128, l2, size=18, weight='bold')
    else:
        f.text(cx, top + 122, l1, size=19, weight='bold')
f.save()
