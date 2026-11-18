"""Figures of section 7 (receivers and transmitters)."""
import random
from figlib import *

LIGHT_AMBER = '#FDE68A'


def darrow(f, x1, y, x2, color=MUTED, w=3):
    """Horizontal double-headed arrow."""
    m = (x1 + x2) / 2
    f.line(m, y, x2 - 2, y, stroke=color, w=w, arrow=True)
    f.line(m, y, x1 + 2, y, stroke=color, w=w, arrow=True)


def block(f, x, y, w, h, lines, fill='#FFFFFF', stroke=INK, size=20, bold=True, color=INK):
    f.rect(x, y, w, h, fill=fill, stroke=stroke, sw=3, rx=10)
    n = len(lines)
    for k, s in enumerate(lines):
        yy = y + h / 2 + 7 + (k - (n - 1) / 2) * 24
        f.text(x + w / 2, yy, s, size=size if k == 0 else 18, weight='bold' if (bold and k == 0) else 'normal',
               fill=color if k == 0 else MUTED)


def antenna(f, x, y):
    """Antenna symbol with its base at (x, y)."""
    f.line(x, y, x, y - 44, stroke=INK, w=4)
    f.line(x, y - 22, x - 20, y - 46, stroke=INK, w=4)
    f.line(x, y - 22, x + 20, y - 46, stroke=INK, w=4)


# 1 ── signal and noise ────────────────────────────────────────────────────
f = Fig('s07-senal-y-ruido', 420, 'Amplificar sube por igual la señal y el ruido')
f.text(320, 42, 'Amplificar no separa la señal del ruido', size=22, weight='bold')
random.seed(3)
for k, (x0, title, nh, sh) in enumerate([(40, 'Antes de amplificar', 22, 62), (340, 'Después de amplificar', 66, 186)]):
    base = 330
    f.text(x0 + 130, 84, title, size=20, weight='bold', fill=MUTED)
    pts = []
    for i in range(0, 261, 6):
        x = x0 + i
        if abs(i - 132) <= 6:
            y = base - sh
        else:
            y = base - random.uniform(nh * 0.45, nh)
        pts.append((x, y))
    d = f'M{x0} {base} ' + ' '.join(f'L{x:.0f} {y:.0f}' for x, y in pts) + f' L{x0 + 260} {base} Z'
    f.path(d, stroke=MUTED, w=2, fill='#D6D3CB')
    f.line(x0 + 132, base - nh, x0 + 132, base - sh, stroke=BLUE, w=8, cap='butt')
    f.line(x0, base, x0 + 260, base, stroke=INK, w=3)
    f.text(x0 + 148, base - sh + 14, 'señal', size=19, anchor='start', weight='bold', fill=BLUE)
    f.text(x0 + 40, base - nh - 8, 'ruido', size=19, weight='bold', fill=MUTED)
f.text(320, 384, 'Las dos crecen igual: la señal sobresale lo mismo', size=20, fill=INK)
f.save()

# 2 ── selectivity ─────────────────────────────────────────────────────────
f = Fig('s07-selectividad', 560, 'Filtro ancho y filtro estrecho')
for k, (title, x1, x2, col) in enumerate([('Filtro ancho: entran las dos', 190, 450, RED),
                                           ('Filtro estrecho: solo entra la deseada', 244, 316, GREEN)]):
    y0 = 20 + k * 268
    base = y0 + 200
    f.text(320, y0 + 28, title, size=21, weight='bold', fill=col)
    f.add(f'<rect x="{x1}" y="{y0 + 48}" width="{x2 - x1}" height="{base - y0 - 48}" rx="6" fill="{LIGHT_AMBER}" '
          f'stroke="{AMBER}" stroke-width="3" stroke-dasharray="8 6"/>')
    f.line(280, base, 280, base - 46, stroke=GREEN, w=12, cap='butt')
    f.line(380, base, 380, base - 140, stroke=RED, w=12, cap='butt')
    f.line(50, base, 590, base, stroke=INK, w=3, arrow=True)
    f.text(250, base + 28, 'deseada', size=19, weight='bold', fill=GREEN)
    f.text(400, base + 28, 'vecina fuerte', size=19, weight='bold', fill=RED)
    f.text(560, base + 28, 'frec.', size=18, fill=MUTED)
    f.text(120, y0 + 76, 'ventana', size=19, fill=AMBER, weight='bold')
    f.text(120, y0 + 100, 'del filtro', size=19, fill=AMBER, weight='bold')
f.line(60, 284, 580, 284, stroke=PAPER_EDGE, w=2)
f.save()

# 3 ── mixer ───────────────────────────────────────────────────────────────
f = Fig('s07-mezclador', 470, 'Un mezclador entrega la suma y la diferencia')
f.text(320, 42, 'El mezclador: suma y diferencia', size=22, weight='bold')
f.text(100, 100, 'Señal de antena', size=19, fill=MUTED)
f.text(100, 128, '7.100 kHz', size=22, weight='bold', fill=BLUE)
f.line(190, 114, 252, 114, stroke=BLUE, w=4, arrow=True)
f.circle(290, 114, 30, fill='#FFFFFF', stroke=INK, sw=4)
f.line(272, 96, 308, 132, stroke=INK, w=4); f.line(272, 132, 308, 96, stroke=INK, w=4)
f.text(290, 70, 'mezclador', size=19, weight='bold')
block(f, 180, 214, 220, 66, ['Oscilador local', '16.100 kHz'], fill=SOFT)
f.line(290, 214, 290, 152, stroke=INK, w=4, arrow=True)
f.line(322, 114, 372, 114, stroke=INK, w=4, arrow=True)
f.text(384, 100, 'suma: 23.200 kHz', size=19, anchor='start', fill=MUTED)
f.text(384, 130, 'diferencia: 9.000 kHz', size=19, anchor='start', weight='bold', fill=GREEN)
f.line(520, 146, 520, 300, stroke=INK, w=4, arrow=True)
block(f, 440, 304, 160, 56, ['Filtro'], fill=LIGHT_AMBER)
f.line(520, 360, 520, 400, stroke=GREEN, w=4, arrow=True)
f.text(520, 434, 'solo 9.000 kHz', size=22, weight='bold', fill=GREEN)
f.text(190, 420, 'El filtro elimina la suma', size=19, fill=MUTED)
f.text(190, 444, 'y deja pasar la diferencia', size=19, fill=MUTED)
f.save()

# 4 ── superheterodyne block diagram ───────────────────────────────────────
def chain(f, top, blocks, side, labels, bx=50, bw=330, bh=62, gap=40):
    """Vertical chain of blocks. side: {index: lines}; labels: {index: text after block}."""
    cx = bx + bw / 2
    y = top
    for k, (lines, fill) in enumerate(blocks):
        block(f, bx, y, bw, bh, lines, fill=fill)
        if k in side:
            block(f, 436, y - 4, 176, bh + 8, side[k], fill=SOFT, size=19)
            f.line(436, y + bh / 2, bx + bw + 6, y + bh / 2, stroke=INK, w=4, arrow=True)
        if k < len(blocks) - 1 or k in labels:
            f.line(cx, y + bh, cx, y + bh + gap - 5, stroke=INK, w=4, arrow=True)
            if k in labels:
                f.text(cx + 16, y + bh + gap / 2 + 6, labels[k], size=18, anchor='start', fill=BLUE, weight='bold')
        y += bh + gap
    return y


f = Fig('s07-superheterodino', 830, 'Esquema de bloques de un receptor superheterodino')
f.text(320, 40, 'El receptor superheterodino', size=22, weight='bold')
antenna(f, 215, 104)
f.text(250, 86, 'antena', size=19, anchor='start', fill=MUTED)
f.line(215, 104, 215, 123, stroke=INK, w=4, arrow=True)
end = chain(f, 128,
            [(['Filtro de entrada', 'y amplificador de RF'], '#FFFFFF'),
             (['Mezclador'], '#FFFFFF'),
             (['Filtro de FI', 'aquí está la selectividad'], LIGHT_AMBER),
             (['Amplificador de FI'], '#FFFFFF'),
             (['Demodulador'], '#FFFFFF'),
             (['Amplificador de audio'], '#FFFFFF')],
            side={1: ['Oscilador local', '16,1 MHz'], 4: ['BFO', 'en SSB y CW']},
            labels={0: '7,1 MHz', 1: '9 MHz (FI)', 2: '9 MHz', 3: '9 MHz', 4: 'audio', 5: 'audio'})
f.text(215, end + 22, 'Altavoz', size=22, weight='bold')
f.text(320, end + 62, 'El dial mueve el oscilador local; la FI no cambia nunca', size=19, fill=MUTED)
f.save()

# 5 ── image frequency ─────────────────────────────────────────────────────
f = Fig('s07-frecuencia-imagen', 430, 'La frecuencia imagen, al otro lado del oscilador local')
f.text(320, 42, 'La imagen: el reflejo al otro lado', size=22, weight='bold')
base = 270
f.line(40, base, 604, base, stroke=INK, w=3, arrow=True)
for x, h, col, name, freq in [(120, 64, GREEN, 'deseada', '7,1 MHz'), (520, 64, RED, 'imagen', '25,1 MHz')]:
    f.line(x, base, x, base - h, stroke=col, w=12, cap='butt')
    f.text(x, base - h - 14, name, size=20, weight='bold', fill=col)
    f.text(x, base + 30, freq, size=20, weight='bold', fill=col)
f.line(320, base + 6, 320, 84, stroke=INK, w=4, dash='10 7')
f.text(320, 76, 'oscilador local', size=20, weight='bold')
f.text(320, base + 30, '16,1 MHz', size=20, weight='bold')
darrow(f, 132, 136, 312, color=AMBER); darrow(f, 328, 136, 508, color=AMBER)
f.text(222, 124, '9 MHz', size=19, weight='bold', fill=AMBER)
f.text(420, 124, '9 MHz', size=19, weight='bold', fill=AMBER)
darrow(f, 120, 344, 520, color=INK)
f.text(320, 378, '18 MHz = 2 × FI', size=22, weight='bold')
f.text(320, 410, 'Las dos dan 9 MHz de diferencia con el oscilador', size=19, fill=MUTED)
f.save()

# 6 ── SSB transmitter block diagram ───────────────────────────────────────
f = Fig('s07-transmisor-ssb', 900, 'Esquema de bloques de un transmisor de SSB')
f.text(320, 40, 'El transmisor de SSB', size=22, weight='bold')
end = chain(f, 64,
            [(['Micrófono', 'y su amplificador'], '#FFFFFF'),
             (['Modulador balanceado', 'quita la portadora'], LIGHT_AMBER),
             (['Filtro de cristal', 'quita una banda lateral'], LIGHT_AMBER),
             (['Mezclador'], '#FFFFFF'),
             (['Filtro paso banda', 'quita la suma'], '#FFFFFF'),
             (['Excitador'], '#FFFFFF'),
             (['Amplificador de potencia', 'clase AB (lineal)'], '#FFFFFF'),
             (['Filtro paso bajo', 'quita los armónicos'], '#FFFFFF')],
            side={1: ['Oscilador', 'de portadora'], 3: ['Oscilador', 'variable']},
            labels={0: 'voz', 1: 'dos bandas, sin portadora', 2: 'una sola banda (SSB)',
                    3: 'suma y diferencia', 4: 'en la frecuencia de emisión', 6: 'con potencia', 7: 'limpia'},
            bh=58, gap=38)
antenna(f, 215, end + 46)
f.text(250, end + 24, 'antena', size=19, anchor='start', fill=MUTED)
f.save()

# 6b ── double-conversion receiver ─────────────────────────────────────────
f = Fig('s07-doble-conversion', 760, 'Esquema de bloques de un receptor de doble conversión')
f.text(320, 40, 'Receptor de doble conversión', size=22, weight='bold')
antenna(f, 215, 104)
f.text(250, 86, 'antena', size=19, anchor='start', fill=MUTED)
f.line(215, 104, 215, 123, stroke=INK, w=4, arrow=True)
end = chain(f, 128,
            [(['Filtro de entrada', 'y amplificador de RF'], '#FFFFFF'),
             (['Primer mezclador'], '#FFFFFF'),
             (['Filtro de 1.ª FI', 'aleja la imagen'], LIGHT_AMBER),
             (['Segundo mezclador'], '#FFFFFF'),
             (['Filtro de 2.ª FI', 'aquí está la selectividad'], LIGHT_AMBER),
             (['Amplificador de FI,', 'demodulador y audio'], '#FFFFFF')],
            side={1: ['1.er oscilador', 'variable: 52.100'], 3: ['2.º oscilador', 'fijo: 45.455']},
            labels={0: '7.100 kHz', 1: '45.000 kHz', 2: '45.000 kHz', 3: '455 kHz', 4: '455 kHz'},
            bh=60, gap=38)
f.text(320, end + 8, 'Frecuencias en kHz, para escuchar 7.100 kHz', size=19, fill=MUTED)
f.save()

# 7 ── low-pass filter and harmonics ───────────────────────────────────────
f = Fig('s07-filtro-paso-bajo', 580, 'El filtro paso bajo elimina los armónicos')
xs = [130, 270, 410, 550]
names = ['7,1', '14,2', '21,3', '28,4']
for k, (title, hs) in enumerate([('A la salida del amplificador', [130, 52, 36, 26]),
                                  ('Después del filtro paso bajo', [128, 6, 4, 3])]):
    y0 = 20 + k * 280
    base = y0 + 210
    f.text(320, y0 + 28, title, size=21, weight='bold')
    if k == 1:
        f.path(f'M60 {base - 150} H190 C240 {base - 150}, 240 {base - 10}, 300 {base - 8} H600',
               stroke=AMBER, w=4, dash='10 7')
        f.text(330, base - 120, 'curva del filtro', size=19, anchor='start', weight='bold', fill=AMBER)
    for j, (x, h) in enumerate(zip(xs, hs)):
        f.line(x, base, x, base - h, stroke=BLUE if j == 0 else RED, w=14, cap='butt')
        f.text(x, base + 28, names[j], size=19, weight='bold', fill=BLUE if j == 0 else RED)
    f.line(50, base, 606, base, stroke=INK, w=3, arrow=True)
    if k == 0:
        f.text(130, base - 142, 'tu señal', size=19, weight='bold', fill=BLUE)
        f.text(410, base - 70, 'armónicos', size=19, weight='bold', fill=RED)
    f.text(64, base + 28, 'MHz', size=18, fill=MUTED)
f.line(60, 292, 580, 292, stroke=PAPER_EDGE, w=2)
f.save()

# 8 ── PEP envelope ────────────────────────────────────────────────────────
f = Fig('s07-pep', 440, 'Potencia de cresta de la envolvente (PEP)')
f.text(225, 44, 'SSB: sube y baja con la voz', size=21, weight='bold')
mid = 250
env = [4, 20, 62, 96, 54, 70, 110, 76, 30, 6, 4, 34, 84, 58, 92, 110, 66, 40, 72, 28, 8, 4, 22, 60, 88, 46, 16, 4]
x0, step = 36, 14
top = ' '.join(f'L{x0 + i * step} {mid - a}' for i, a in enumerate(env))
bot = ' '.join(f'L{x0 + i * step} {mid + a}' for i, a in reversed(list(enumerate(env))))
f.path(f'M{x0} {mid} {top} {bot} Z', stroke=BLUE, w=3, fill='#BFDBFE')
f.line(30, mid - 110, 424, mid - 110, stroke=RED, w=3, dash='9 6')
f.text(36, mid - 120, '100 W PEP: los picos', size=19, anchor='start', weight='bold', fill=RED)
f.line(30, mid - 55, 424, mid - 55, stroke=GREEN, w=3, dash='4 6')
f.line(36, mid + 144, 76, mid + 144, stroke=GREEN, w=3, dash='4 6')
f.text(86, mid + 150, 'potencia media: unos 25 W', size=19, anchor='start', weight='bold', fill=GREEN)
f.line(440, 70, 440, 400, stroke=PAPER_EDGE, w=2)
f.text(535, 44, 'FM o CW', size=21, weight='bold')
f.rect(462, mid - 110, 146, 220, fill='#BFDBFE', stroke=BLUE, sw=3, rx=0)
f.text(535, mid + 150, 'constante', size=19, weight='bold', fill=BLUE)
f.text(320, 424, 'La silueta es la envolvente de la señal', size=18, fill=MUTED)
f.save()

# 9 ── splatter ────────────────────────────────────────────────────────────
f = Fig('s07-splatter', 560, 'Señal limpia y señal con splatter')
for k, (title, col) in enumerate([('Señal limpia: ocupa solo su sitio', GREEN),
                                   ('Sobremodulada: invade a las vecinas', RED)]):
    y0 = 20 + k * 270
    base = y0 + 210
    f.text(320, y0 + 28, title, size=21, weight='bold', fill=col)
    if k == 1:
        f.path(f'M100 {base} L270 {base - 80} L270 {base} Z', stroke=RED, w=2, fill='#FCA5A5')
        f.path(f'M540 {base} L370 {base - 80} L370 {base} Z', stroke=RED, w=2, fill='#FCA5A5')
    for x in (150, 420):
        f.add(f'<rect x="{x}" y="{base - 56}" width="70" height="56" fill="none" stroke="{MUTED}" stroke-width="3"/>')
    f.rect(270, base - 130, 100, 130, fill='#93C5FD', stroke=BLUE, sw=3, rx=0)
    f.line(50, base, 600, base, stroke=INK, w=3, arrow=True)
    f.text(320, base + 28, 'tu señal', size=19, weight='bold', fill=BLUE)
    f.text(185, base + 28, 'vecina', size=19, fill=MUTED)
    f.text(455, base + 28, 'vecina', size=19, fill=MUTED)
    if k == 0:
        darrow(f, 270, base - 146, 370, color=BLUE)
        f.text(320, base - 156, '2,7 kHz', size=19, weight='bold', fill=BLUE)
    else:
        f.text(150, base - 96, 'splatter', size=19, weight='bold', fill=RED)
        f.text(492, base - 96, 'splatter', size=19, weight='bold', fill=RED)
f.line(60, 284, 580, 284, stroke=PAPER_EDGE, w=2)
f.save()

# 10 ── intermodulation ────────────────────────────────────────────────────
f = Fig('s07-intermodulacion', 400, 'Productos de intermodulación')
f.text(320, 42, 'Intermodulación: señales que no existen', size=22, weight='bold')
base = 300
f.line(40, base, 606, base, stroke=INK, w=3, arrow=True)
for x, name in [(270, '7.200'), (370, '7.210')]:
    f.line(x, base, x, base - 170, stroke=RED, w=14, cap='butt')
    f.text(x, base + 30, name, size=19, weight='bold', fill=RED)
for x, name in [(170, '7.190'), (470, '7.220')]:
    f.add(f'<rect x="{x - 7}" y="{base - 70}" width="14" height="70" fill="{LIGHT_AMBER}" stroke="{AMBER}" '
          f'stroke-width="3" stroke-dasharray="6 4"/>')
    f.text(x, base + 30, name, size=19, weight='bold', fill=AMBER)
    f.text(x, base - 84, 'fantasma', size=19, weight='bold', fill=AMBER)
f.text(320, base - 186, 'dos señales muy fuertes', size=19, weight='bold', fill=RED)
f.text(580, base + 30, 'kHz', size=18, fill=MUTED)
f.text(320, 372, 'Los fantasmas se fabrican dentro del receptor', size=19, fill=MUTED)
f.save()
