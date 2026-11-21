"""Tiny helpers to draw UML-ish class boxes and connectors as SVG (used while authoring)."""
def box(x, y, w, name, attrs=(), italic=False, fill="#fffbe8"):
    h = 26 + (len(attrs) * 18 + 8 if attrs else 6)
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#333" stroke-width="1.4"/>',
         f'<text x="{x+w/2}" y="{y+18}" text-anchor="middle" font-weight="bold"{" font-style=\"italic\"" if italic else ""}>{name}</text>',
         f'<line x1="{x}" y1="{y+26}" x2="{x+w}" y2="{y+26}" stroke="#333"/>']
    for i, a in enumerate(attrs):
        s.append(f'<text x="{x+8}" y="{y+44+i*18}" font-size="12">{a}</text>')
    return '\n'.join(s), h

def line(pts, dashed=False, start=None, end=None):
    d = ' '.join(f'{x},{y}' for x, y in pts)
    extra = (' stroke-dasharray="6,4"' if dashed else '') + (f' marker-start="url(#{start})"' if start else '') + (f' marker-end="url(#{end})"' if end else '')
    return f'<polyline points="{d}" fill="none" stroke="#333" stroke-width="1.4"{extra}/>'

def text(x, y, t, anchor="middle", size=12, style=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}"{style}>{t}</text>'

MARKERS = '''<defs>
 <marker id="dOpen" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L10,6 L0,12" fill="none" stroke="#333" stroke-width="1.4"/></marker>
 <marker id="dFill" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,1 L10,6 L0,11 z" fill="#222"/></marker>
 <marker id="dTri" markerWidth="16" markerHeight="16" refX="14" refY="8" orient="auto"><path d="M0,0 L14,8 L0,16 z" fill="#fff" stroke="#333" stroke-width="1.4"/></marker>
 <marker id="dDiaF" markerWidth="22" markerHeight="12" refX="1" refY="6" orient="auto"><path d="M1,6 L10,1 L19,6 L10,11 z" fill="#333"/></marker>
 <marker id="dDiaH" markerWidth="22" markerHeight="12" refX="1" refY="6" orient="auto"><path d="M1,6 L10,1 L19,6 L10,11 z" fill="#fff" stroke="#333" stroke-width="1.4"/></marker>
</defs>'''

def svg(w, h, parts):
    return (f':::raw\n<div class="svgwrap"><svg viewBox="0 0 {w} {h}" width="100%" style="max-width:{w}px" '
            f'xmlns="http://www.w3.org/2000/svg" font-size="13">\n{MARKERS}\n' + '\n'.join(parts) + '\n</svg></div>\n:::\n')
