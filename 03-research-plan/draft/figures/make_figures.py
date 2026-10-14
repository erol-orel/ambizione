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
    W, H = 1400, 600
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']
    NAVY, GREEN, ORANGE, BLUE, GREY = "#1f3a5f", "#2e8b57", "#c8701a", "#1f5f8b", "#8a97a6"
    GREEN_BG, ORANGE_BG, BLUE_BG, GREY_BG = "#eaf5ef", "#fdf3e6", "#e8f0f7", "#f3f5f7"

    def fits(txt, size, width, bold=False):
        assert len(txt) * size * (0.56 if bold else 0.52) <= width, (txt, size, width)

    def label(x, y, t, size, col=INK, anchor="start", bold=False):
        s.append(text(x, y, t, size, col, anchor, "bold" if bold else "normal"))

    # ---------- row 1: what exists at the start of a crisis ----------
    label(0, 30, "AT THE START OF A CRISIS", 20, NAVY, bold=True)
    cards = [(0, "Published studies", BLUE, BLUE_BG), (330, "Context data", GREEN, GREEN_BG),
             (660, "Outcomes of this episode", ORANGE, ORANGE_BG)]
    for x, title, col, bg in cards:
        s.append(box(x, 48, 300, 118, bg, col, 10, 2.2))
        fits(title, 20, 280, True); label(x + 150, 82, title, 20, col, "middle", True)
    # glyphs: stack of pages, tall bars, one short bar
    for k in range(3):
        s.append(f'<rect x="{112 + k*6}" y="{96 + k*6}" width="54" height="34" rx="3" fill="white" stroke="{BLUE}" stroke-width="2"/>')
    for k, hgt in enumerate([34, 46, 40, 50, 44]):
        s.append(f'<rect x="{420 + k*22}" y="{154 - hgt}" width="16" height="{hgt}" fill="{GREEN}" opacity="{0.55 + 0.09*k}"/>')
    s.append(f'<rect x="770" y="140" width="16" height="14" fill="{ORANGE}"/>')
    s.append(f'<rect x="794" y="146" width="16" height="8" fill="{ORANGE}"/>')
    for k in range(3):
        s.append(f'<rect x="{818 + k*24}" y="100" width="16" height="54" fill="none" stroke="{ORANGE}" stroke-dasharray="4,3" stroke-width="1.5"/>')
    label(150, 160, "numbers, variables, lags, thresholds", 15, MUTE, "middle")
    s.append(box(980, 48, 280, 118, GREY_BG, GREY, 10, 1.4))
    label(1120, 82, "What is known", 22, NAVY, "middle", True)
    label(1120, 112, "a lot elsewhere and in the past", 16, MUTE, "middle")
    label(1120, 134, "a lot about today's conditions", 16, MUTE, "middle")
    label(1120, 156, "very little about this episode's outcomes", 16, MUTE, "middle")
    # ---------- row 2: what HEADSTART does ----------
    label(0, 218, "WHAT HEADSTART DOES", 20, NAVY, bold=True)
    steps = [("WP1", "Extract and grade", "the published evidence", BLUE),
             ("WP2", "Model levels of", "pressure on the system", NAVY),
             ("WP3", "Replay past crises", "with and without the evidence", NAVY),
             ("WP4", "Measure the value", "for emergency decisions", NAVY)]
    for k, (wp, l1, l2, col) in enumerate(steps):
        x = k * 350
        s.append(box(x, 236, 320, 96, BLUE_BG if k == 0 else GREY_BG, col, 10, 2.2 if k == 0 else 1.4))
        label(x + 18, 268, wp, 22, col, bold=True)
        fits(l1, 19, 230, True); label(x + 80, 268, l1, 19, INK, bold=True)
        fits(l2, 16.5, 290); label(x + 80, 294, l2, 16.5, MUTE)
        if k < 3:
            s.append(arrow(x + 322, 284, x + 346, 284, MUTE))
    # inputs feed the steps
    s.append(arrow(150, 166, 150, 232, BLUE))
    s.append(arrow(480, 166, 760, 232, GREEN))
    s.append(arrow(810, 166, 800, 232, ORANGE))
    # ---------- row 3: the test and where it runs ----------
    label(0, 384, "THE TEST", 20, NAVY, bold=True)
    px, py, pw, ph = 110, 404, 520, 128
    s.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="white" stroke="none"/>')
    s.append(f'<line x1="{px}" y1="{py+ph}" x2="{px+pw}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<path d="M {px+10} {py+30} C {px+180} {py+40} {px+380} {py+95} {px+pw-10} {py+112}" fill="none" stroke="{BLUE}" stroke-width="4"/>')
    s.append(f'<path d="M {px+10} {py+118} C {px+150} {py+116} {px+380} {py+114} {px+pw-10} {py+112}" fill="none" stroke="{MUTE}" stroke-width="3" stroke-dasharray="7,6"/>')
    label(px + pw + 12, py + 40, "with published evidence", 16, BLUE)
    label(px + pw + 12, py + 118, "local data only", 16, MUTE)
    label(px - 8, py + 8, "forecast skill", 15, MUTE, "end")
    label(px, py + ph + 22, "crisis onset", 15, MUTE)
    label(px + pw, py + ph + 22, "outcomes accumulate", 15, MUTE, "end")
    label(px + 300, py + ph + 44, "each past episode replayed using only what was known at the time", 15, MUTE, "middle")
    label(880, 384, "WHERE", 20, NAVY, bold=True)
    chips = [("Respiratory epidemics", "main test", BLUE), ("Heatwaves", "second, if the first passes", NAVY),
             ("Legionellosis", "year-4 extension", GREY)]
    for k, (nm, sub, col) in enumerate(chips):
        y = 400 + k * 50
        s.append(box(880, y, 500, 42, GREY_BG, col, 21, 1.8))
        fits(nm, 18, 220, True); label(900, y + 27, nm, 18, col, bold=True)
        fits(sub, 15, 230); label(1360, y + 27, sub, 15, MUTE, "end")
    label(880, 572, "Geneva, with the emergency services", 15, MUTE)
    label(880, 592, "dashboard in observation mode, where authorised", 15, MUTE)
    s.append("</svg>")
    (OUT / "fig1-framework.svg").write_text("\n".join(s), encoding="utf-8")


WPS = [
    ("WP1", 1, 20, [
        ("T1.1 Evidence target and protocol", 1, 4),
        ("T1.2 Extraction benchmark", 3, 9),
        ("T1.3 Extraction error analysis", 7, 14),
        ("T1.4 Evidence distributions", 12, 18),
        ("T1.5 Transportability screen", 15, 20)]),
    ("WP2", 1, 28, [
        ("T2.1 State model and identifiability", 1, 9),
        ("T2.2 Critical tail", 6, 14),
        ("T2.3 Evidence-derived priors", 10, 20),
        ("T2.4 Resilience indicators", 12, 20),
        ("T2.5 Calibration and automation", 20, 28)]),
    ("WP3", 1, 42, [
        ("T3.0 Outcome hierarchy and registration", 1, 14),
        ("T3.1 Retrospective information set", 12, 20),
        ("T3.2 Historical information set", 18, 30),
        ("T3.3 Candidate models and selection", 20, 34),
        ("T3.4 Benefit and failure analysis", 28, 38),
        ("T3.5 Heat and legionellosis extension", 34, 42)]),
    ("WP4", 24, 48, [
        ("T4.1 Operational losses and thresholds", 24, 32),
        ("T4.2 Decision analysis and equity", 30, 40),
        ("T4.3 Counterfactuals and dashboard", 34, 48)]),
]
MILESTONES = [(9, "M1"), (12, "M2"), (20, "M3"), (34, "M4"), (40, "M5"), (48, "M6")]


def fig2():
    L, R, TOP, ROW, GAP = 392, 24, 40, 18.5, 5
    W = 1150
    nrows = sum(len(w[3]) for w in WPS)
    H = TOP + nrows * ROW + GAP * len(WPS) + 44
    span = W - L - R

    def mx(m):
        return L + (m / 48) * span

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']

    body_bottom = TOP + nrows * ROW + GAP * len(WPS)
    for yr in range(5):
        x = mx(yr * 12)
        s.append(f'<line x1="{x}" y1="{TOP-6}" x2="{x}" y2="{body_bottom}" '
                 f'stroke="{LINE}" stroke-width="0.9" stroke-dasharray="3,4"/>')
        if yr < 4:
            s.append(text(mx(yr * 12 + 6), TOP - 14, f"Year {yr+1}", 17, MUTE, "middle"))

    y = TOP
    for code, a, b, tasks in WPS:
        s.append(text(0, y + 17, code, 17.5, ACCENT, weight="bold"))
        s.append(box(mx(a), y + 16, mx(b) - mx(a), 5, ACCENT, ACCENT, 2, 0))
        for tname, ta, tb in tasks:
            s.append(text(44, y + 17, tname, 16, INK))
            s.append(box(mx(ta), y + 5, max(mx(tb) - mx(ta), 4), 15, FILL, LINE, 3))
            y += ROW
        y += GAP

    for m, lab in MILESTONES:
        x = mx(m)
        s.append(f'<line x1="{x}" y1="{TOP-6}" x2="{x}" y2="{body_bottom}" stroke="{ACCENT}" '
                 f'stroke-width="1.4" stroke-dasharray="4,4" opacity="0.6"/>')
        s.append(f'<polygon points="{x},{body_bottom+4} {x+7},{body_bottom+13} '
                 f'{x},{body_bottom+22} {x-7},{body_bottom+13}" fill="{ACCENT}"/>')
        s.append(text(x, body_bottom + 40, lab, 16.5, ACCENT, "middle", "bold"))
    s.append("</svg>")
    (OUT / "fig2-gantt.svg").write_text("\n".join(s))


fig1()
fig2()
print("wrote fig1-framework.svg and fig2-gantt.svg")
