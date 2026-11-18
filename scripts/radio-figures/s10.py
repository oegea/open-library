"""Figures of section 10 (measurements, safety and EMC)."""
import random
from figlib import *

BROWN = '#92400E'    # phase wire
NEUTRAL = '#2563EB'  # neutral wire
EARTHW = '#16A34A'   # protective earth
EARTH = '#D9C7A3'
EARTH_EDGE = '#8A6D3B'


def box(f, x, y, w, h, label, fill='#FFFFFF', stroke=INK, size=19, weight='bold', sub=None):
    f.rect(x, y, w, h, fill=fill, stroke=stroke, sw=3, rx=10)
    if sub:
        f.text(x + w / 2, y + h / 2 - 2, label, size=size, weight=weight)
        f.text(x + w / 2, y + h / 2 + 22, sub, size=18, fill=MUTED)
    else:
        f.text(x + w / 2, y + h / 2 + 7, label, size=size, weight=weight)


def zigzag(f, x, y, color=INK):
    """Horizontal resistor 120 wide starting at (x, y)."""
    f.path(f'M{x} {y} l10 -16 l20 32 l20 -32 l20 32 l20 -32 l20 32 l10 -16', stroke=color, w=4)


# 1 ── multimeter: three connections ───────────────────────────────────────
f = Fig('s10-polimetro-tres-conexiones', 760, 'Las tres conexiones del polímetro')
f.text(320, 40, 'El polímetro, de tres maneras', size=22, weight='bold')
panels = [('Voltímetro: en paralelo', GREEN, 'toca dos puntos, sin cortar nada'),
          ('Amperímetro: en serie', AMBER, 'se abre el circuito y se intercala'),
          ('Ohmímetro: sin tensión', BLUE, 'la pieza suelta, sin pila ni enchufe')]
for k, (title, col, note) in enumerate(panels):
    y0 = 60 + k * 230
    f.rect(24, y0, 592, 216, fill=SOFT, rx=14)
    f.text(320, y0 + 32, title, size=21, weight='bold', fill=col)
    T, B = y0 + 70, y0 + 170
    if k == 0:
        L, R = 110, 330
        f.path(f'M{L} {T + 12} V{T} H{R} V{T + 26}')
        f.path(f'M{R} {T + 74} V{B} H{L} V{T + 94}')
        f.battery(L, T + 8, h=86)
        f.bulb(R, T + 50, r=24)
        f.path(f'M{R} {T} H470 V{T + 24}', stroke=col, w=4)
        f.path(f'M{R} {B} H470 V{B - 24}', stroke=col, w=4)
        f.circle(R, T, 6, fill=col, stroke=col); f.circle(R, B, 6, fill=col, stroke=col)
        f.meter(470, T + 50, 'V', '', color=col)
    elif k == 1:
        L, R = 110, 470
        f.path(f'M{L} {T + 12} V{T} H264')
        f.path(f'M316 {T} H{R} V{T + 26}')
        f.path(f'M{R} {T + 74} V{B} H{L} V{T + 94}')
        f.battery(L, T + 8, h=86)
        f.bulb(R, T + 50, r=24)
        f.meter(290, T, 'A', '', color=col)
    else:
        zigzag(f, 150, T + 50)
        f.path(f'M150 {T + 50} H110 V{T} H410 V{T + 24}', stroke=col, w=4)
        f.path(f'M270 {T + 50} H330 V{B} H410 V{B - 24}', stroke=col, w=4)
        f.meter(410, T + 50, 'Ω', '', color=col)
        f.text(210, T + 96, 'pieza', size=18, fill=MUTED)
    f.text(320, y0 + 202, note, size=19, fill=MUTED)
f.save()

# 2 ── measuring chain ─────────────────────────────────────────────────────
f = Fig('s10-cadena-de-medida', 420, 'La cadena de medida entre el transmisor y la antena')
f.text(320, 40, 'Medir entre el transmisor y la antena', size=22, weight='bold')
box(f, 30, 150, 150, 70, 'transmisor')
box(f, 250, 140, 170, 90, 'medidor', sub='ROE y vatios', stroke=AMBER)
f.line(180, 185, 250, 185, stroke=WIRE, w=7)
f.path('M420 185 H470 V110 H520', stroke=WIRE, w=7)
f.path('M470 185 V290 H500', stroke=WIRE, w=7, dash='12 8')
# antenna
f.line(548, 124, 548, 70, stroke=INK, w=5)
f.path('M524 62 L548 96 L572 62', stroke=INK, w=5)
f.text(548, 150, 'antena', size=20, weight='bold')
# dummy load
box(f, 500, 258, 116, 66, 'carga', sub='50 Ω', stroke=GREEN)
f.text(456, 316, 'o bien', size=18, fill=MUTED, anchor='end')
f.line(196, 256, 236, 256, stroke=AMBER, w=4, arrow=True)
f.text(120, 262, 'directa', size=19, fill=AMBER, weight='bold')
f.line(236, 292, 196, 292, stroke=RED, w=4, arrow=True)
f.text(118, 298, 'reflejada', size=19, fill=RED, weight='bold')
f.text(215, 132, 'coaxial', size=18, fill=MUTED)
f.text(320, 372, 'El medidor se intercala en el cable coaxial', size=19, fill=MUTED)
f.text(320, 398, 'Con la carga artificial se prueba sin emitir', size=19, fill=MUTED)
f.save()

# 3 ── RCD ─────────────────────────────────────────────────────────────────
def person(f, x, y):
    f.circle(x, y, 11, fill='#FFFFFF', stroke=INK, sw=3)
    f.line(x, y + 11, x, y + 46, stroke=INK, w=3)
    f.line(x - 14, y + 26, x + 14, y + 26, stroke=INK, w=3)
    f.line(x, y + 46, x - 12, y + 70, stroke=INK, w=3)
    f.line(x, y + 46, x + 12, y + 70, stroke=INK, w=3)

f = Fig('s10-diferencial', 620, 'Cómo funciona el interruptor diferencial')
f.text(320, 40, 'El diferencial compara la ida y la vuelta', size=22, weight='bold')
for k in range(2):
    y0 = 60 + k * 270
    leak = k == 1
    f.rect(24, y0, 592, 256 if leak else 190, fill=SOFT, rx=14)
    box(f, 44, y0 + 50, 140, 100, 'diferencial', stroke=RED if leak else GREEN, size=19)
    box(f, 440, y0 + 50, 150, 100, 'aparato')
    f.line(184, y0 + 76, 440, y0 + 76, stroke=BROWN, w=5, arrow=True)
    f.line(440, y0 + 126, 186, y0 + 126, stroke=NEUTRAL, w=5, arrow=True)
    f.text(312, y0 + 64, ('fase: van 5,05 A' if leak else 'fase: van 5 A'), size=19, fill=BROWN, weight='bold')
    f.text(312, y0 + 116, 'neutro: vuelven 5 A', size=19, fill=NEUTRAL, weight='bold')
    if leak:
        person(f, 515, y0 + 162)
        f.line(515, y0 + 150, 515, y0 + 152, stroke=RED, w=3)
        f.line(470, y0 + 236, 560, y0 + 236, stroke=EARTH_EDGE, w=5)
        f.text(400, y0 + 204, '0,05 A se fugan', size=19, fill=RED, weight='bold', anchor='end')
        f.text(400, y0 + 228, 'a tierra por la persona', size=18, fill=RED, anchor='end')
        f.text(114, y0 + 186, 'faltan 50 mA:', size=19, fill=RED, weight='bold')
        f.text(114, y0 + 210, 'CORTA', size=22, fill=RED, weight='bold')
    else:
        f.text(320, y0 + 176, 'Iguales: no hay fuga y no actúa', size=19, fill=GREEN, weight='bold')
f.save()

# 4 ── storm protection (antenna on a block of flats) ──────────────────────
f = Fig('s10-proteccion-tormentas', 560, 'Antena en un edificio: mástil, descargador y equipo unidos a la tierra del edificio')
f.text(320, 40, 'En un edificio: todo a la misma tierra', size=22, weight='bold')
GY = 440
f.rect(2, GY, 636, 116, fill=EARTH, stroke=EARTH_EDGE, sw=2, rx=0)
# building
f.rect(270, 160, 330, 280, fill='#FFFFFF', stroke=INK, sw=3, rx=4)
for wy in (190, 270):
    for wx in (470, 530):
        f.rect(wx, wy, 36, 44, fill='#E0F2FE', stroke=MUTED, sw=2, rx=3)
# mast and antenna on the roof
f.line(290, 160, 290, 84, stroke=INK, w=6)
f.line(214, 84, 366, 84, stroke=INK, w=5)
f.text(290, 72, 'antena', size=19, weight='bold')
# earth conductor: mast -> down the facade -> building earth
f.path(f'M290 160 H258 V{GY + 44}', stroke=EARTHW, w=7)
f.line(200, GY + 44, 600, GY + 44, stroke=EARTHW, w=8)
f.text(400, GY + 78, 'red de tierra del edificio', size=20, weight='bold', fill='#166534')
f.text(400, GY + 102, '(la conexión la hace un instalador)', size=18, fill='#166534')
# coax: antenna -> down -> arrester at the entry point
f.path('M300 92 V146 H226 V318', stroke=WIRE, w=4)
f.rect(210, 318, 32, 32, fill='#FDE68A', stroke=AMBER, sw=3, rx=6)
f.line(242, 334, 256, 334, stroke=EARTHW, w=5)
f.path('M226 350 V372 H240', stroke=WIRE, w=4)
f.circle(242, 372, 5, fill=WIRE, stroke=WIRE)
# inside: loose gap, then cable to the rig
f.circle(300, 372, 5, fill=WIRE, stroke=WIRE)
f.path('M300 372 H380', stroke=WIRE, w=4)
box(f, 380, 346, 110, 54, 'equipo')
f.text(350, 312, 'con tormenta:', size=18, fill=RED, weight='bold', anchor='middle')
f.text(350, 334, 'desconectado', size=18, fill=RED, weight='bold', anchor='middle')
# mains earth of the rig
f.line(470, 400, 470, GY + 40, stroke=EARTHW, w=4, dash='9 6')
f.text(482, 418, 'tierra del', size=18, fill='#166534', anchor='start')
f.text(482, 436, 'enchufe', size=18, fill='#166534', anchor='start')
# labels on the left
f.text(196, 328, 'descargador', size=19, anchor='end', fill=AMBER, weight='bold')
f.text(196, 352, 'de gas', size=19, anchor='end', fill=AMBER, weight='bold')
f.text(212, 196, 'bajada a tierra:', size=19, anchor='end', fill='#166534', weight='bold')
f.text(212, 220, 'corta, gruesa', size=19, anchor='end', fill='#166534')
f.text(212, 244, 'y recta', size=19, anchor='end', fill='#166534')
f.save()

# 5 ── harmonic vs fundamental overload ────────────────────────────────────
f = Fig('s10-armonico-o-sobrecarga', 640, 'Emisión no deseada frente a sobrecarga por la fundamental')
f.text(320, 40, 'Dos formas de interferir', size=22, weight='bold')
for k in range(2):
    y0 = 60 + k * 286
    f.rect(24, y0, 592, 272, fill=SOFT, rx=14)
    base = y0 + 200
    f.text(320, y0 + 32, ('1. Tu transmisor emite un armónico' if k == 0 else '2. Tu señal es limpia, pero muy fuerte'),
           size=20, weight='bold', fill=RED if k == 0 else AMBER)
    f.rect(380, y0 + 70, 200, 130, fill='#DBEAFE', stroke=BLUE, sw=2, rx=8)
    f.text(480, y0 + 96, 'banda del televisor', size=18, fill=BLUE, weight='bold')
    f.line(50, base, 596, base, stroke=INK, w=3, arrow=True)
    f.text(590, base + 26, 'frecuencia', size=18, fill=MUTED, anchor='end')
    f.rect(120, y0 + 78, 26, base - (y0 + 78), fill=GREEN, rx=4)
    f.text(133, base + 26, 'tu señal', size=18, fill=GREEN, weight='bold')
    if k == 0:
        f.rect(470, base - 50, 22, 50, fill=RED, rx=4)
        f.text(481, base - 60, 'armónico', size=18, fill=RED, weight='bold')
        f.text(320, y0 + 256, 'Fallo en el transmisor: filtro paso bajo', size=19, weight='bold')
    else:
        f.path(f'M150 {y0 + 84} C240 {y0 + 46}, 330 {y0 + 60}, 388 {y0 + 130}', stroke=AMBER, w=4, arrow=True, dash='9 6')
        f.text(268, y0 + 128, 'se cuela por', size=18, fill=AMBER, weight='bold')
        f.text(268, y0 + 152, 'los cables', size=18, fill=AMBER, weight='bold')
        f.text(480, base - 30, 'sin armónicos', size=18, fill=MUTED)
        f.text(320, y0 + 256, 'Fallo en el televisor: ferritas y filtro paso alto', size=19, weight='bold')
f.save()

# 6 ── noise floor ─────────────────────────────────────────────────────────
f = Fig('s10-ruido-de-fondo', 440, 'El ruido de fondo entierra las señales débiles')
f.text(320, 40, 'El ruido de fondo decide qué se oye', size=22, weight='bold')
random.seed(11)
peaks = [(70, 170), (140, 100), (210, 55)]
for k, (x0, title, floor, col) in enumerate([(30, 'Lugar tranquilo', 26, GREEN), (330, 'Lugar ruidoso', 118, RED)]):
    f.rect(x0, 60, 280, 320, fill=SOFT, rx=14)
    f.text(x0 + 140, 92, title, size=21, weight='bold', fill=col)
    base = 350
    for px, ph in peaks:
        hidden = ph <= floor
        f.add(f'<rect x="{x0 + px - 9}" y="{base - ph}" width="18" height="{ph}" rx="4" fill="{BLUE}" '
              f'fill-opacity="{0.25 if hidden else 1}"/>')
    pts = [f'{x0 + 14} {base}']
    for x in range(14, 267, 9):
        pts.append(f'{x0 + x} {base - floor - random.randint(-7, 7)}')
    pts.append(f'{x0 + 266} {base}')
    f.path('M' + ' L'.join(pts) + ' Z', stroke='#6B7280', w=2, fill='#9CA3AF')
    f.line(x0 + 14, base, x0 + 266, base, stroke=INK, w=3)
    if floor > 40:
        f.text(x0 + 140, base - floor / 2 + 6, 'ruido de fondo', size=18, fill='#FFFFFF', weight='bold')
    else:
        f.text(x0 + 196, 214, 'ruido de', size=18, fill=MUTED, weight='bold')
        f.text(x0 + 196, 236, 'fondo: bajo', size=18, fill=MUTED, weight='bold')
f.text(170, 410, 'se oyen las tres señales', size=19, fill=GREEN, weight='bold')
f.text(470, 410, 'solo se oye la más fuerte', size=19, fill=RED, weight='bold')
f.save()
