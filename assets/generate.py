#!/usr/bin/env python3
"""Regenerate the profile banner and rule, in light and dark variants.

Run with `python3 assets/generate.py` from anywhere; it writes beside itself.

Motif: a circos-style genome ring (the visual language of GenomeDrawer /
DNMB output) cropped to the right of a typographic block.
"""
import math
import os

W, H = 1200, 260
CX, CY = 1044.0, 126.0

THEMES = {
    "light": dict(
        ink="#0A1B26",
        muted="#5C6B78",
        faint="#8B98A4",
        accent="#0E7C86",
        track=["#0E7C86", "#B96C34", "#3C6C9C", "#7A6BA8", "#5C8A5F"],
    ),
    "dark": dict(
        ink="#E9EFF4",
        muted="#93A1AE",
        faint="#5E6E7C",
        accent="#35B6C2",
        track=["#35B6C2", "#DE9558", "#6EA4D8", "#A996DA", "#84BC88"],
    ),
}


def polar(r, deg):
    a = math.radians(deg - 90.0)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def arc(r, a0, a1):
    """Stroked arc path from a0 to a1 degrees (clockwise, 0 = top)."""
    x0, y0 = polar(r, a0)
    x1, y1 = polar(r, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M {x0:.2f} {y0:.2f} A {r} {r} 0 {large} 1 {x1:.2f} {y1:.2f}"


def ring(r, width, segments, colors, opacity=1.0):
    out = []
    for i, (a0, a1) in enumerate(segments):
        c = colors[i % len(colors)]
        out.append(
            f'<path d="{arc(r, a0, a1)}" fill="none" stroke="{c}" '
            f'stroke-width="{width}" stroke-linecap="butt" opacity="{opacity}"/>'
        )
    return out


def ticks(r, length, count, color, opacity, every_major=5, major=2.0):
    out = []
    for i in range(count):
        deg = 360.0 * i / count
        ln = length * (major if i % every_major == 0 else 1.0)
        x0, y0 = polar(r - ln / 2, deg)
        x1, y1 = polar(r + ln / 2, deg)
        out.append(
            f'<line x1="{x0:.2f}" y1="{y0:.2f}" x2="{x1:.2f}" y2="{y1:.2f}" '
            f'stroke="{color}" stroke-width="1" opacity="{opacity:.2f}"/>'
        )
    return out


def skew_plot(base_r, amp, color, opacity):
    """A deterministic GC-skew-like radial trace."""
    pts = []
    n = 180
    for i in range(n + 1):
        deg = 360.0 * i / n
        t = math.radians(deg)
        v = (
            math.sin(t * 3.0) * 0.55
            + math.sin(t * 7.0 + 1.1) * 0.28
            + math.sin(t * 13.0 + 2.3) * 0.17
        )
        x, y = polar(base_r + v * amp, deg)
        pts.append(f"{x:.2f},{y:.2f}")
    return (
        f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" '
        f'stroke-width="1.4" opacity="{opacity}" stroke-linejoin="round"/>'
    )


def chords(r, pairs, color, opacity):
    out = []
    for a0, a1 in pairs:
        x0, y0 = polar(r, a0)
        x1, y1 = polar(r, a1)
        out.append(
            f'<path d="M {x0:.2f} {y0:.2f} Q {CX:.2f} {CY:.2f} {x1:.2f} {y1:.2f}" '
            f'fill="none" stroke="{color}" stroke-width="1.2" opacity="{opacity}"/>'
        )
    return out


# Feature blocks, in degrees. Uneven on purpose: real genome tracks are.
TRACK_A = [(4, 46), (52, 74), (81, 128), (136, 158), (167, 214),
           (222, 262), (270, 291), (298, 344), (350, 360)]
TRACK_B = [(18, 58), (66, 96), (110, 141), (152, 196), (206, 233),
           (244, 288), (300, 331), (338, 358)]
TRACK_C = [(30, 72), (88, 119), (130, 172), (196, 224), (262, 305), (318, 350)]

CHORDS = [(18, 162), (96, 284), (142, 332), (208, 58), (250, 24), (312, 118)]


def build(theme_name):
    t = THEMES[theme_name]
    g = []

    # A larger, very faint ring bleeding off the top-right edge, for depth.
    g.append(
        f'<circle cx="{CX + 96}" cy="{CY - 84}" r="196" fill="none" '
        f'stroke="{t["accent"]}" stroke-width="1" opacity="0.10"/>'
    )
    g.append(
        f'<circle cx="{CX + 96}" cy="{CY - 84}" r="164" fill="none" '
        f'stroke="{t["accent"]}" stroke-width="1" opacity="0.07"/>'
    )

    # Outer guide + coordinate ticks.
    g.append(
        f'<circle cx="{CX}" cy="{CY}" r="122" fill="none" '
        f'stroke="{t["faint"]}" stroke-width="1" opacity="0.30"/>'
    )
    g += ticks(122, 4.0, 60, t["faint"], 0.45)

    # Feature tracks.
    g += ring(112, 9, TRACK_A, t["track"], 0.92)
    g.append(
        f'<circle cx="{CX}" cy="{CY}" r="99" fill="none" '
        f'stroke="{t["faint"]}" stroke-width="1" opacity="0.22"/>'
    )
    g += ring(88, 8, TRACK_B, t["track"][1:] + t["track"][:1], 0.72)
    g += ring(64, 6, TRACK_C, t["track"][3:] + t["track"][:3], 0.55)

    # Inner origin marker — kept quiet so the feature tracks carry the eye.
    g.append(
        f'<circle cx="{CX}" cy="{CY}" r="44" fill="none" '
        f'stroke="{t["faint"]}" stroke-width="1" opacity="0.18"/>'
    )
    g.append(
        f'<line x1="{CX}" y1="{CY - 8}" x2="{CX}" y2="{CY + 8}" '
        f'stroke="{t["accent"]}" stroke-width="1.2" opacity="0.45"/>'
    )
    g.append(
        f'<line x1="{CX - 8}" y1="{CY}" x2="{CX + 8}" y2="{CY}" '
        f'stroke="{t["accent"]}" stroke-width="1.2" opacity="0.45"/>'
    )

    font = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

    text = f'''
  <g font-family="{font}">
    <text x="10" y="98" font-size="46" font-weight="700" letter-spacing="-1.2"
          fill="{t["ink"]}">Jae-Yoon Sung</text>
    <text x="12" y="132" font-size="16.5" font-weight="500" letter-spacing="0.1"
          fill="{t["muted"]}">Ph.D. · Research Professor, Dept. of Biotechnology, Yonsei University</text>
    <rect x="12" y="158" width="40" height="3" rx="1.5" fill="{t["accent"]}"/>
    <text x="12" y="196" font-size="18.5" font-weight="500" letter-spacing="-0.2"
          fill="{t["ink"]}">Computational tools for domesticating non-model bacteria</text>
    <text x="12" y="222" font-size="15" font-weight="400" letter-spacing="0.1"
          fill="{t["faint"]}">genome analysis · editor discovery · thermophile engineering</text>
  </g>'''

    body = "\n    ".join(g)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     width="{W}" height="{H}" role="img"
     aria-label="Jae-Yoon Sung — Research Professor, Yonsei University. Computational tools for domesticating non-model bacteria.">
  <g>
    {body}
  </g>{text}
</svg>
'''


FW, FH = 1200, 44


def build_footer(theme_name):
    """A genome-coordinate ruler: the header's motif, unrolled."""
    t = THEMES[theme_name]
    g = [
        f'<line x1="0" y1="26" x2="{FW}" y2="26" stroke="{t["faint"]}" '
        f'stroke-width="1" opacity="0.30"/>'
    ]
    for i in range(0, FW + 1, 20):
        major = i % 100 == 0
        h = 6 if major else 3
        g.append(
            f'<line x1="{i}" y1="{26 - h}" x2="{i}" y2="26" stroke="{t["faint"]}" '
            f'stroke-width="1" opacity="{0.40 if major else 0.22}"/>'
        )
    blocks = [(58, 96), (212, 74), (352, 142), (546, 88), (702, 116),
              (884, 70), (1006, 130)]
    for i, (x, w) in enumerate(blocks):
        g.append(
            f'<rect x="{x}" y="20" width="{w}" height="6" rx="3" '
            f'fill="{t["track"][i % len(t["track"])]}" opacity="0.75"/>'
        )
    body = "\n    ".join(g)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {FW} {FH}" '
        f'width="{FW}" height="{FH}" role="presentation">\n    {body}\n</svg>\n'
    )


out_dir = os.path.dirname(os.path.abspath(__file__))
for name in THEMES:
    for label, svg in (("header", build(name)), ("rule", build_footer(name))):
        path = os.path.join(out_dir, f"{label}-{name}.svg")
        with open(path, "w") as fh:
            fh.write(svg)
        print("wrote", path, os.path.getsize(path), "bytes")
