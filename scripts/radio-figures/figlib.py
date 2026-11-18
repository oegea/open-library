"""Tiny helpers shared by the figure generators of the radioafición course.

Every figure is a self-contained SVG, 640 units wide, drawn on a light "paper"
card so it reads the same on the light and dark themes of the site. Text is
never smaller than 18 units: figures are shown ~360 px wide on phones.

Usage: python3 scripts/radio-figures/s02.py   (writes into media/radioaficion/)
"""
import os, html, random, math

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'media', 'radioaficion')

INK = '#1F2933'      # text and outlines
MUTED = '#5B6673'    # secondary text
WIRE = '#374151'     # cables
BLUE = '#2563EB'     # electrons / current
RED = '#DC2626'      # positive pole, warnings
AMBER = '#D97706'    # highlights (the amber of Vicente's dial)
GREEN = '#059669'    # "ok" / results
WATER = '#38BDF8'    # water analogy
PAPER = '#FAF6EC'
PAPER_EDGE = '#E7DFCC'
SOFT = '#EFE7D6'     # panels inside the card
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"


class Fig:
    def __init__(self, name, height, title_text=None):
        self.name, self.h, self.parts = name, height, []
        self.title_text = title_text or name

    def add(self, s):
        self.parts.append(s)
        return self

    def text(self, x, y, s, size=20, anchor='middle', weight='normal', fill=INK, italic=False, rotate=None):
        assert size >= 18, f'text too small in {self.name}: {s}'
        extra = ' font-style="italic"' if italic else ''
        if rotate is not None:
            extra += f' transform="rotate({rotate} {x} {y})"'
        return self.add(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" '
                        f'font-weight="{weight}" fill="{fill}"{extra}>{html.escape(s)}</text>')

    def line(self, x1, y1, x2, y2, stroke=WIRE, w=4, arrow=False, dash=None, cap='round'):
        a = ' marker-end="url(#arr-%s)"' % stroke.strip('#') if arrow else ''
        d = f' stroke-dasharray="{dash}"' if dash else ''
        if arrow:
            self._need_arrow(stroke)
        return self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
                        f'stroke-width="{w}" stroke-linecap="{cap}"{a}{d}/>')

    def path(self, d, stroke=WIRE, w=4, fill='none', arrow=False, dash=None, join='round'):
        a = ' marker-end="url(#arr-%s)"' % stroke.strip('#') if arrow else ''
        ds = f' stroke-dasharray="{dash}"' if dash else ''
        if arrow:
            self._need_arrow(stroke)
        return self.add(f'<path d="{d}" stroke="{stroke}" stroke-width="{w}" fill="{fill}" '
                        f'stroke-linecap="round" stroke-linejoin="{join}"{a}{ds}/>')

    def rect(self, x, y, w, h, fill=SOFT, stroke='none', sw=2, rx=10):
        return self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
                        f'stroke="{stroke}" stroke-width="{sw}"/>')

    def circle(self, x, y, r, fill='none', stroke=INK, sw=3):
        return self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    _arrows = None

    def _need_arrow(self, color):
        if self._arrows is None:
            self._arrows = set()
        self._arrows.add(color)

    # ---- reusable electrical symbols -------------------------------------
    def battery(self, x, y, h=90, label=None, plus_top=True):
        """Vertical battery body centred on x, top at y. Returns (top, bottom) terminals."""
        self.rect(x - 26, y + 8, 52, h - 16, fill='#FFFFFF', stroke=INK, sw=3, rx=8)
        self.rect(x - 10, y, 20, 10, fill=INK, rx=3)
        top, bot = ('+', '−') if plus_top else ('−', '+')
        self.text(x, y + 36, top, size=26, weight='bold', fill=RED if top == '+' else BLUE)
        self.text(x, y + h - 18, bot, size=26, weight='bold', fill=RED if bot == '+' else BLUE)
        if label:
            self.text(x - 38, y + h / 2 + 7, label, size=20, anchor='end', weight='bold')
        return (x, y), (x, y + h - 8)

    def bulb(self, x, y, r=24, lit=True, label=None):
        self.circle(x, y, r, fill='#FDE68A' if lit else '#FFFFFF', stroke=INK, sw=3)
        k = r * 0.6
        self.line(x - k, y - k, x + k, y + k, stroke=INK, w=3)
        self.line(x - k, y + k, x + k, y - k, stroke=INK, w=3)
        if label:
            self.text(x + r + 10, y + 7, label, size=20, anchor='start', weight='bold')

    def meter(self, x, y, letter, reading, color=GREEN, r=26):
        """Round instrument (V or A) with its reading written next to it."""
        self.circle(x, y, r, fill='#FFFFFF', stroke=color, sw=4)
        self.text(x, y + 9, letter, size=26, weight='bold', fill=color)
        return self

    def save(self):
        defs = ''
        if self._arrows:
            defs = '<defs>' + ''.join(
                f'<marker id="arr-{c.strip("#")}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
                f'markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{c}"/></marker>'
                for c in sorted(self._arrows)) + '</defs>'
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 {self.h}" width="640" height="{self.h}" '
               f'font-family="{FONT}" role="img"><title>{html.escape(self.title_text)}</title>{defs}'
               f'<rect x="1" y="1" width="638" height="{self.h - 2}" rx="18" fill="{PAPER}" stroke="{PAPER_EDGE}" stroke-width="2"/>'
               + '\n'.join(self.parts) + '</svg>\n')
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, self.name + '.svg'), 'w') as f:
            f.write(svg)
        print('wrote', self.name)
