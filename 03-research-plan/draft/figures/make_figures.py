#!/usr/bin/env python3
"""Generate the two research-plan figures as SVG. No dependencies.

    python3 make_figures.py

Writes fig1-framework.svg and fig2-gantt.svg alongside this script.
Print targets: both figures placed at the full 18.44 cm text width.
Font sizes are chosen so body text renders at >= 7 pt at those sizes.
Greyscale-safe: one accent hue; identity carried by weight and position.
"""
import pathlib

OUT = pathlib.Path(__file__).parent
INK, MUTE, LINE = "#1a1a1a", "#4e4e4e", "#9a9a9a"
ACCENT, ACCENT_BG = "#1f5f8b", "#e3edf4"
FILL = "#f3f3f3"
FONT = "Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size, fill=INK, anchor="start", weight="normal", style="normal"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
            f'font-style="{style}">{esc(s)}</text>')


def box(x, y, w, h, fill=FILL, stroke=LINE, rx=5, sw=1.4):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def arrow(x1, y1, x2, y2, stroke=MUTE, dash=None, sw=2.2):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" marker-end="url(#a)"{d}/>')


DEFS = ('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{MUTE}"/></marker></defs>')


# ---------------------------------------------------------------- Figure 1
def fig1():
    # General overview: what exists at onset, what HEADSTART does (WP1 to WP4), what it tests, where.
    W, H = 1400, 760
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']
    NAVY, GREEN, ORANGE, BLUE, GREY = "#1f3a5f", "#2e8b57", "#c8701a", "#1f5f8b", "#8a97a6"
    GREEN_BG, ORANGE_BG, BLUE_BG, GREY_BG = "#eaf5ef", "#fdf3e6", "#e8f0f7", "#f3f5f7"

    def fits(txt, size, width, bold=False):
        assert len(txt) * size * (0.56 if bold else 0.52) <= width, (txt, size, width)

    def label(x, y, t, size, col=INK, anchor="start", bold=False):
        s.append(text(x, y, t, size, col, anchor, "bold" if bold else "normal"))

    def header(y, t):
        label(0, y, t, 19, NAVY, bold=True)
        s.append(f'<line x1="0" y1="{y+10}" x2="{W}" y2="{y+10}" stroke="{LINE}" stroke-width="0.8" opacity="0.6"/>')

    # ---------- row 1: what exists at the start of a crisis ----------
    header(30, "AT THE START OF A CRISIS")
    CW, CH, CY = 300, 130, 62
    cards = [(0, "Published studies", BLUE, BLUE_BG, "numbers, variables, lags, thresholds"),
             (340, "Context data", GREEN, GREEN_BG, "weather, air quality, wastewater"),
             (680, "Outcomes of this episode", ORANGE, ORANGE_BG, "a few days, more each day")]
    for x, title, col, bg, sub in cards:
        s.append(box(x, CY, CW, CH, bg, col, 10, 2.2))
        fits(title, 19, 280, True); label(x + CW/2, CY + 30, title, 19, col, "middle", True)
        fits(sub, 14, 290); label(x + CW/2, CY + CH - 14, sub, 14, MUTE, "middle")
    # glyphs: stack of pages, tall bars, one short bar then dashed placeholders
    for k in range(3):
        s.append(f'<rect x="{118 + k*6}" y="{CY + 48 + k*6}" width="54" height="32" rx="3" fill="white" stroke="{BLUE}" stroke-width="2"/>')
    for k, hgt in enumerate([30, 42, 36, 46, 40]):
        s.append(f'<rect x="{436 + k*22}" y="{CY + 100 - hgt}" width="16" height="{hgt}" fill="{GREEN}" opacity="{0.55 + 0.09*k}"/>')
    s.append(f'<rect x="{778}" y="{CY + 86}" width="16" height="14" fill="{ORANGE}"/>')
    s.append(f'<rect x="{802}" y="{CY + 92}" width="16" height="8" fill="{ORANGE}"/>')
    for k in range(3):
        s.append(f'<rect x="{826 + k*24}" y="{CY + 46}" width="16" height="54" fill="none" stroke="{ORANGE}" stroke-dasharray="4,3" stroke-width="1.5"/>')
    s.append(box(1030, CY, 370, CH, GREY_BG, GREY, 10, 1.4))
    label(1215, CY + 30, "What is known", 19, NAVY, "middle", True)
    label(1215, CY + 60, "much from elsewhere and from the past", 15, MUTE, "middle")
    label(1215, CY + 84, "much about today's conditions", 15, MUTE, "middle")
    label(1215, CY + 108, "little about this episode's outcomes", 15, MUTE, "middle")

    # ---------- row 2: what HEADSTART does ----------
    header(262, "WHAT HEADSTART DOES")
    BY, BH, BW = 294, 110, 320
    steps = [("WP1", "Extract and grade", "the published evidence", BLUE),
             ("WP2", "Model the levels of", "pressure on the system", NAVY),
             ("WP3", "Replay past crises", "with and without the evidence", NAVY),
             ("WP4", "Measure the value", "for emergency decisions", NAVY)]
    for k, (wp, l1, l2, col) in enumerate(steps):
        x = k * 360
        s.append(box(x, BY, BW, BH, BLUE_BG if k == 0 else GREY_BG, col, 10, 2.2 if k == 0 else 1.4))
        label(x + 20, BY + 42, wp, 22, col, bold=True)
        fits(l1, 18.5, 220, True); label(x + 86, BY + 42, l1, 18.5, INK, bold=True)
        fits(l2, 16, 250); label(x + 86, BY + 70, l2, 16, MUTE)
        if k < 3:
            s.append(arrow(x + BW + 4, BY + BH/2, x + 356, BY + BH/2, MUTE))
    # inputs feed the steps
    s.append(arrow(150, CY + CH, 150, BY - 6, BLUE))
    s.append(arrow(490, CY + CH, 760, BY - 6, GREEN))
    s.append(arrow(830, CY + CH, 820, BY - 6, ORANGE))

    # ---------- row 3: the test and where it runs ----------
    header(474, "THE TEST")
    px, py, pw, ph = 110, 506, 500, 150
    s.append(f'<line x1="{px}" y1="{py+ph}" x2="{px+pw}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<path d="M {px+10} {py+32} C {px+170} {py+44} {px+360} {py+112} {px+pw-10} {py+132}" fill="none" stroke="{BLUE}" stroke-width="4"/>')
    s.append(f'<path d="M {px+10} {py+138} C {px+150} {py+136} {px+360} {py+134} {px+pw-10} {py+132}" fill="none" stroke="{MUTE}" stroke-width="3" stroke-dasharray="7,6"/>')
    label(px + pw + 14, py + 44, "with published evidence", 16, BLUE)
    label(px + pw + 14, py + 138, "local data only", 16, MUTE)
    label(px - 10, py + 8, "forecast skill", 15, MUTE, "end")
    label(px, py + ph + 24, "crisis onset", 15, MUTE)
    label(px + pw, py + ph + 24, "outcomes accumulate", 15, MUTE, "end")
    label(px + pw/2, py + ph + 48, "each past episode replayed with only what was known at the time", 15, MUTE, "middle")
    label(px + pw/2, py + ph + 70, "same data for both strategies, outcome and thresholds registered before any test", 15, MUTE, "middle")

    label(880, 474, "WHERE", 19, NAVY, bold=True)
    chips = [("Respiratory epidemics", "main test", BLUE), ("Heat events", "second test", NAVY),
             ("Legionellosis", "third test, year 4", GREY)]
    for k, (nm, sub, col) in enumerate(chips):
        y = 496 + k * 58
        s.append(box(880, y, 520, 44, GREY_BG, col, 22, 1.8))
        fits(nm, 18, 240, True); label(902, y + 29, nm, 18, col, bold=True)
        fits(sub, 15, 230); label(1378, y + 29, sub, 15, MUTE, "end")
    label(880, 696, "Geneva, with the emergency services", 15, MUTE)
    label(880, 720, "dashboard in observation mode where authorised", 15, MUTE)
    s.append("</svg>")
    (OUT / "fig1-framework.svg").write_text("\n".join(s), encoding="utf-8")


WPS = [
    ("WP1", 1, 20, [
        ("T1.1 Evidence target and protocol", 1, 4),
        ("T1.2 Manual extraction benchmark", 3, 9),
        ("T1.3 Automated extraction error", 7, 14),
        ("T1.4 Evidence distributions", 12, 18),
        ("T1.5 Transportability screen", 15, 20)]),
    ("WP2", 1, 28, [
        ("T2.1 Pressure model and identifiability", 1, 9),
        ("T2.2 Critical tail", 6, 14),
        ("T2.3 Evidence in the parameters", 10, 20),
        ("T2.4 Resilience indicators", 12, 20),
        ("T2.5 Calibration and automation", 20, 28)]),
    ("WP3", 1, 42, [
        ("T3.0 Outcomes, data gate, registration", 1, 14),
        ("T3.1 Assemble the data", 12, 20),
        ("T3.2 Replay with past information only", 18, 30),
        ("T3.3 Model library and confirmatory tests", 20, 34),
        ("T3.4 Map benefit and failure", 28, 38),
        ("T3.5 Heat and legionellosis tests", 34, 42)]),
    ("WP4", 24, 48, [
        ("T4.1 Elicit costs and thresholds", 24, 32),
        ("T4.2 Decision analysis and fairness", 30, 40),
        ("T4.3 Dashboard and living updates", 34, 48)]),
]
MILESTONES = [(9, "M1", "benchmark released"), (12, "M2", "model passes, data gate"),
              (20, "M3", "open-data benchmark"), (34, "M4", "main test done"),
              (40, "M5", "decision value"), (48, "M6", "three tests, dashboard")]


def fig2():
    L, R, TOP, ROW, GAP = 420, 30, 56, 25, 16
    W = 1200
    nrows = sum(len(w[3]) for w in WPS)
    H = TOP + nrows * ROW + GAP * len(WPS) + 92
    span = W - L - R

    def mx(m):
        return L + (m / 48) * span

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']

    body_bottom = TOP + nrows * ROW + GAP * len(WPS)
    for yr in range(4):
        x0, x1 = mx(yr * 12), mx(yr * 12 + 12)
        if yr % 2 == 1:
            s.append(f'<rect x="{x0}" y="{TOP-8}" width="{x1-x0}" height="{body_bottom-TOP+8}" fill="#f7f8fa"/>')
        s.append(text((x0 + x1) / 2, TOP - 18, f"Year {yr+1}", 17, MUTE, "middle"))
    for yr in range(5):
        x = mx(yr * 12)
        s.append(f'<line x1="{x}" y1="{TOP-8}" x2="{x}" y2="{body_bottom}" '
                 f'stroke="{LINE}" stroke-width="0.9" stroke-dasharray="3,4"/>')

    y = TOP
    for code, a, b, tasks in WPS:
        s.append(text(0, y + 18, code, 18, ACCENT, weight="bold"))
        s.append(box(mx(a), y + 20, mx(b) - mx(a), 5, ACCENT, ACCENT, 2, 0))
        for tname, ta, tb in tasks:
            assert len(tname) * 16 * 0.52 <= L - 60, tname
            s.append(text(52, y + 18, tname, 16, INK))
            s.append(box(mx(ta), y + 5, max(mx(tb) - mx(ta), 4), 17, FILL, LINE, 3))
            y += ROW
        y += GAP

    for m, lab, desc in MILESTONES:
        x = mx(m)
        s.append(f'<line x1="{x}" y1="{TOP-8}" x2="{x}" y2="{body_bottom}" stroke="{ACCENT}" '
                 f'stroke-width="1.4" stroke-dasharray="4,4" opacity="0.6"/>')
        s.append(f'<polygon points="{x},{body_bottom+6} {x+7},{body_bottom+15} '
                 f'{x},{body_bottom+24} {x-7},{body_bottom+15}" fill="{ACCENT}"/>')
        s.append(text(x, body_bottom + 44, lab, 16.5, ACCENT, "middle", "bold"))
    legend = "  ·  ".join(f"{lab} {desc}" for _, lab, desc in MILESTONES)
    s.append(text(0, body_bottom + 78, "Milestones.  " + legend, 14.5, MUTE))
    s.append("</svg>")
    (OUT / "fig2-gantt.svg").write_text("\n".join(s))


fig1()
fig2()
print("wrote fig1-framework.svg and fig2-gantt.svg")
