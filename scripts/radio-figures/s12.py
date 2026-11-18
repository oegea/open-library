"""Figures of section 12 (regulations).

Every number drawn here comes from the consolidated Orden IET/1311/2013
(arts. 5-7, 10, 18-20, 27 and annex I, 3.1-3.2) and from the national column
of the CNAF approved by Orden TDF/732/2026 (primary / secondary status).
"""
from figlib import *

# 1 ── who rules the spectrum: three floors ────────────────────────────────
f = Fig('s12-tres-pisos', 560, 'Los tres pisos de normas del espectro: UIT, CEPT y España')
f.text(320, 42, 'Quién decide qué en el espectro', size=22, weight='bold')
rows = [
    ('EL MUNDO: la UIT', 'Reglamento de Radiocomunicaciones',
     'Reparte el espectro entre servicios y Regiones', BLUE),
    ('EUROPA: la CEPT', 'Recomendaciones T/R 61-01 y T/R 61-02',
     'Licencias y exámenes que valen entre países', AMBER),
    ('ESPAÑA: el Estado', 'Ley 11/2022, Orden IET/1311/2013 y CNAF',
     'Quién emite, en qué bandas y con cuánta potencia', GREEN),
]
for k, (who, what, role, col) in enumerate(rows):
    y = 70 + k * 162
    f.rect(40, y, 560, 124, fill='#FFFFFF', stroke=col, sw=4, rx=14)
    f.rect(40, y, 560, 40, fill=col, rx=14)
    f.rect(40, y + 22, 560, 18, fill=col, rx=0)
    f.text(320, y + 28, who, size=20, weight='bold', fill='#FFFFFF')
    f.text(320, y + 74, what, size=20, weight='bold')
    f.text(320, y + 104, role, size=19, fill=MUTED)
    if k < 2:
        f.line(320, y + 128, 320, y + 156, stroke=INK, w=4, arrow=True)
f.save()

# 2 ── the path to the air in Spain ────────────────────────────────────────
f = Fig('s12-camino', 900, 'El camino administrativo en España, del examen a la primera emisión')
f.text(320, 42, 'Del examen a la primera emisión', size=22, weight='bold')
steps = [
    ('1', 'Solicitud de examen y tasa', 'En la sede electrónica del Ministerio', SOFT),
    ('2', 'Examen: dos partes de 30 preguntas', '15 aciertos en cada una · 90 minutos', SOFT),
    ('3', 'Certificado HAREC', 'Acredita que has superado la prueba', '#FDE68A'),
    ('4', 'Solicitud de autorización y tasa', 'La Administración tiene seis semanas', SOFT),
    ('5', 'Autorización y distintivo de llamada', 'Personal, intransferible, sin caducidad', '#FDE68A'),
]
y = 66
for n, title, sub, fill in steps:
    f.rect(70, y, 500, 84, fill=fill, stroke=INK, sw=3, rx=14)
    f.circle(110, y + 42, 20, fill=INK, stroke=INK)
    f.text(110, y + 50, n, size=22, weight='bold', fill='#FFFFFF')
    f.text(146, y + 36, title, size=20, weight='bold', anchor='start')
    f.text(146, y + 64, sub, size=18, anchor='start', fill=MUTED)
    y += 84
    if n != '5':
        f.line(320, y + 2, 320, y + 22, stroke=INK, w=4, arrow=True)
        y += 26
# branch
f.path(f'M320 {y + 2} V{y + 22} H170 V{y + 44}', stroke=INK, w=4, arrow=True)
f.path(f'M320 {y + 22} H470 V{y + 44}', stroke=INK, w=4, arrow=True)
yb = y + 50
f.rect(30, yb, 280, 150, fill='#D1FAE5', stroke=GREEN, sw=3, rx=14)
f.text(170, yb + 34, 'Equipo móvil', size=20, weight='bold')
f.text(170, yb + 60, 'o portátil', size=20, weight='bold')
f.text(170, yb + 98, 'Ya puedes emitir', size=20, weight='bold', fill=GREEN)
f.text(170, yb + 126, 'con la autorización', size=18, fill=MUTED)
f.rect(330, yb, 280, 150, fill='#FFFFFF', stroke=AMBER, sw=3, rx=14)
f.text(470, yb + 34, 'Estación fija', size=20, weight='bold')
f.text(470, yb + 62, 'Hace falta además', size=18, fill=MUTED)
f.text(470, yb + 88, 'la licencia de estación', size=19, weight='bold', fill=AMBER)
f.text(470, yb + 122, 'solicitud, montaje,', size=18, fill=MUTED)
f.text(470, yb + 144, 'seguro e inspección', size=18, fill=MUTED)
f.line(470, yb + 154, 470, yb + 178, stroke=INK, w=4, arrow=True)
f.rect(330, yb + 184, 280, 62, fill='#D1FAE5', stroke=GREEN, sw=3, rx=14)
f.text(470, yb + 224, 'Ya puedes emitir desde casa', size=19, weight='bold', fill=GREEN)
f.h = yb + 270
f.save()

# 3 ── anatomy of a call sign ──────────────────────────────────────────────
f = Fig('s12-distintivo', 500, 'Las tres piezas de un distintivo de llamada español')
f.text(320, 42, 'Las tres piezas de un distintivo', size=22, weight='bold')
parts = [('EA', 150, BLUE), ('5', 300, AMBER), ('JMS', 455, GREEN)]
for s, x, col in parts:
    w = {'EA': 150, '5': 80, 'JMS': 200}[s]
    f.rect(x - w / 2, 70, w, 110, fill='#FFFFFF', stroke=col, sw=5, rx=14)
    f.text(x, 152, s, size=76, weight='bold', fill=col)
    f.line(x, 184, x, 216, stroke=col, w=4)
f.text(150, 244, 'PREFIJO', size=20, weight='bold', fill=BLUE)
f.text(150, 272, 'el país y el', size=18, fill=MUTED)
f.text(150, 294, 'tipo de estación', size=18, fill=MUTED)
f.text(300, 244, 'DISTRITO', size=20, weight='bold', fill=AMBER)
f.text(300, 272, 'dónde vivías', size=18, fill=MUTED)
f.text(300, 294, 'al obtenerlo', size=18, fill=MUTED)
f.text(465, 244, 'SUFIJO', size=20, weight='bold', fill=GREEN)
f.text(465, 272, 'hasta tres letras,', size=18, fill=MUTED)
f.text(465, 294, 'por orden de llegada', size=18, fill=MUTED)
f.line(60, 326, 580, 326, stroke=PAPER_EDGE, w=2)
f.text(320, 362, 'Y lo que se le puede añadir', size=20, weight='bold')
f.text(190, 404, 'F/EA5JMS', size=26, weight='bold')
f.text(190, 436, 'de visita en Francia', size=18, fill=MUTED)
f.text(460, 404, 'EA5JMS/P', size=26, weight='bold')
f.text(460, 436, 'en portable (opcional)', size=18, fill=MUTED)
f.text(320, 476, 'La barra separa siempre el añadido del distintivo', size=18, fill=MUTED, italic=True)
f.save()

# 4 ── schematic map of the nine districts ─────────────────────────────────
f = Fig('s12-distritos', 660, 'Mapa esquemático de los nueve distritos de los distintivos españoles')
f.text(320, 42, 'Los nueve distritos (mapa esquemático)', size=22, weight='bold')
COL = {1: '#BFDBFE', 2: '#FDE68A', 3: '#FBCFE8', 4: '#DDD6FE', 5: '#FCA5A5',
       6: '#A7F3D0', 7: '#FED7AA', 8: '#BAE6FD', 9: '#E5E7EB'}


def tile(x, y, w, h, d, l1, l2=None):
    f.rect(x, y, w, h, fill=COL[d], stroke=INK, sw=2, rx=10)
    f.text(x + 12, y + 30, str(d), size=28, weight='bold', anchor='start')
    if l2:
        f.text(x + w / 2, y + 54, l1, size=18)
        f.text(x + w / 2, y + 75, l2, size=18)
    else:
        f.text(x + w / 2, y + 64, l1, size=18)


G, W, H = 8, 112, 84
X = [20 + k * (W + G) for k in range(5)]
Y = [70 + k * (H + G) for k in range(6)]
tile(X[0], Y[0], W, H, 1, 'Galicia')
tile(X[1], Y[0], W, H, 1, 'Asturias')
tile(X[2], Y[0], W, H, 1, 'Cantabria')
tile(X[3], Y[0], W, H, 2, 'País', 'Vasco')
tile(X[4], Y[0], W, H, 2, 'Navarra')
tile(X[0], Y[1], 2 * W + G, H, 1, 'Castilla y León')
tile(X[2], Y[1], W, H, 1, 'La Rioja')
tile(X[3], Y[1], W, H, 2, 'Aragón')
tile(X[4], Y[1], W, H, 3, 'Cataluña')
tile(X[0], Y[2], W, H, 4, 'Extre-', 'madura')
tile(X[1], Y[2], W, H, 4, 'Madrid')
tile(X[2], Y[2], W, H, 4, 'Castilla-', 'La Mancha')
tile(X[3], Y[2], W, H, 5, 'Comunidad', 'Valenciana')
tile(X[4], Y[2], W, H, 6, 'Baleares')
tile(X[0], Y[3], 2 * W + G, H, 7, 'Andalucía')
tile(X[2], Y[3], W, H, 5, 'Albacete')
tile(X[3], Y[3], W, H, 5, 'Murcia')
tile(X[0], Y[4], W, H, 8, 'Canarias')
tile(X[1], Y[4], W, H, 9, 'Ceuta')
tile(X[2], Y[4], W, H, 9, 'Melilla')
f.text(X[3] + 8, Y[4] + 36, 'La cifra 0 queda', size=18, anchor='start', fill=MUTED)
f.text(X[3] + 8, Y[4] + 60, 'para casos especiales', size=18, anchor='start', fill=MUTED)
f.text(320, Y[5] + 22, 'Albacete es de Castilla-La Mancha, pero va con el 5.', size=18, fill=MUTED)
f.text(320, Y[5] + 48, 'La Rioja va con el 1. Ceuta y Melilla son el 9.', size=18, fill=MUTED)
f.h = Y[5] + 72
f.save()

# 5 ── bands, status and maximum power ─────────────────────────────────────
f = Fig('s12-bandas-potencias', 800, 'Bandas de aficionado en España: categoría y potencia máxima')
f.text(320, 40, 'Bandas, categoría y potencia máxima', size=22, weight='bold')
f.text(30, 78, 'Banda', size=18, anchor='start', weight='bold', fill=MUTED)
f.text(120, 78, 'Frecuencias', size=18, anchor='start', weight='bold', fill=MUTED)
f.text(398, 78, 'Categoría', size=18, weight='bold', fill=MUTED)
f.text(610, 78, 'Máximo', size=18, anchor='end', weight='bold', fill=MUTED)
P, S = 'primaria', 'secundaria'
bands = [
    ('2.200 m', '135,7–137,8 kHz', S, '1 W PIRE'),
    ('630 m', '472–479 kHz', S, '1 W PIRE*'),
    ('160 m', '1.810–1.830 kHz', S, '500 W PEP'),
    ('160 m', '1.830–1.850 kHz', P, '1.000 W PEP'),
    ('80 m', '3.500–3.800 kHz', P, '1.000 W PEP'),
    ('60 m', '5.351,5–5.366,5 kHz', S, '15 W PIRE'),
    ('40 m', '7.000–7.200 kHz', P, '1.000 W PEP'),
    ('30 m', '10.100–10.150 kHz', S, '500 W PEP'),
    ('20 m', '14.000–14.350 kHz', P, '1.000 W PEP'),
    ('17 m', '18.068–18.168 kHz', P, '1.000 W PEP'),
    ('15 m', '21.000–21.450 kHz', P, '1.000 W PEP'),
    ('12 m', '24.890–24.990 kHz', P, '1.000 W PEP'),
    ('10 m', '28.000–29.700 kHz', P, '1.000 W PEP'),
    ('6 m', '50–52 MHz', S, '300 W PEP*'),
    ('4 m', '70,150–70,250 MHz', S, '300 W PEP'),
    ('2 m', '144–146 MHz', P, '600 W PEP'),
    ('70 cm', '430–440 MHz', P, '300 W PEP'),
    ('23 cm', '1.240–1.300 MHz', S, 'ver el texto'),
]
y = 92
for name, freq, cat, pw in bands:
    col = GREEN if cat == P else AMBER
    f.rect(20, y, 600, 32, fill='#FFFFFF' if cat == P else '#FEF3C7', rx=6)
    f.text(30, y + 23, name, size=18, anchor='start', weight='bold')
    f.text(120, y + 23, freq, size=18, anchor='start')
    f.rect(340, y + 4, 116, 24, fill=col, rx=12)
    f.text(398, y + 22, cat, size=18, fill='#FFFFFF', weight='bold')
    f.text(610, y + 23, pw, size=18, anchor='end', weight='bold')
    y += 36
f.text(320, y + 22, 'En las bandas secundarias el máximo es la mitad', size=18, fill=MUTED)
f.text(320, y + 46, 'del valor de la tabla del reglamento.', size=18, fill=MUTED)
f.text(320, y + 74, '* Con matices: ver el texto.', size=18, fill=MUTED)
f.h = y + 94
f.save()
