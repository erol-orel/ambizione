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
    # Reproduces the applicant's 14 Oct design (3300 x 1305) as vector art, without semicolons.
    W, H = 3300, 1305
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="white"/>']
    NAVY, GREEN, ORANGE, BLUE, GREY = "#1f3a5f", "#2e8b57", "#c8701a", "#1f5f8b", "#8a97a6"
    GREEN_BG, ORANGE_BG, BLUE_BG, GREY_BG = "#eaf5ef", "#fdf3e6", "#e8f0f7", "#eef2f6"
    SMALL = "#5b6675"

    def fits(txt, size, width, bold=False):
        assert len(txt) * size * (0.56 if bold else 0.52) <= width, (txt, size, width)

    def card(x, y, w, h, title, lines, small, border, title_col, bg, sw=5, rx=28, dark=False):
        s.append(box(x, y, w, h, bg, border, rx, sw))
        fits(title, 42, w - 60, True)
        s.append(text(x + 38, y + 68, title, 42, title_col, weight="bold"))
        yy = y + 128
        for ln in lines:
            fits(ln, 36, w - 60)
            s.append(text(x + 38, yy, ln, 36, "white" if dark else INK)); yy += 48
        for ln in small:
            fits(ln, 30, w - 60)
            s.append(text(x + 38, yy, ln, 30, "#dbe3ec" if dark else SMALL)); yy += 42

    def varrow(x, y1, y2, col):
        s.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 26}" stroke="{col}" stroke-width="7"/>')
        s.append(f'<path d="M {x - 18} {y2 - 30} L {x + 18} {y2 - 30} L {x} {y2} z" fill="{col}"/>')

    s.append(text(55, 68, "Context data may be plentiful, while outcomes from the current episode are initially few.", 52, NAVY, weight="bold"))
    # row 1
    card(55, 115, 1005, 255, "CONTEXT DATA, OFTEN AVAILABLE",
         ["Weather, air quality and calendar", "Wastewater and public surveillance"],
         ["Public feeds or links through partners"], GREEN, GREEN, GREEN_BG)
    card(1148, 115, 1005, 255, "OUTCOMES FROM THIS EPISODE",
         ["Cause-specific calls and ED demand", "Occupancy and service pressure"],
         ["Only a few observations at the start"], ORANGE, ORANGE, ORANGE_BG)
    card(2240, 115, 1005, 255, "PUBLISHED STUDIES",
         ["Effect estimates and uncertainty", "Variables, lags, model forms, thresholds"],
         ["Evidence from other events and settings"], BLUE, BLUE, BLUE_BG)
    # row 2
    card(55, 425, 2098, 170, "SAME RAW INPUTS TO BOTH STRATEGIES",
         ["Context feeds + historical local outcomes + outcomes observed so far"], [], GREY, NAVY, GREY_BG)
    s.append(box(2240, 425, 1005, 170, BLUE_BG, BLUE, 28, 5))
    s.append(text(2278, 493, "PREPARE THE EVIDENCE", 42, BLUE, weight="bold"))
    s.append(text(2278, 540, "Extract, then check uncertainty and relevance", 30, INK))
    s.append(text(2278, 580, "to Geneva before using it in a model", 30, INK))
    # row 3
    card(55, 650, 1495, 265, "REFERENCE STRATEGY",
         ["Fits registered models to the shared data."],
         ["No model inputs derived from HEADSTART extraction.", "Same selection and validity rules."], NAVY, NAVY, "white")
    card(1620, 650, 1625, 265, "STRATEGY USING PUBLISHED EVIDENCE",
         ["Uses the same data, plus findings from published studies."],
         ["Parameter distributions retain extraction uncertainty.", "Evidence also informs variables, lags and model forms."], BLUE, BLUE, BLUE_BG)
    # bottom
    card(55, 980, 3190, 255, "REPLAY PAST EPISODES USING ONLY WHAT WAS AVAILABLE AT EACH DATE",
         ["Compare probability forecasts with later outcomes, and assess calibration and operational value."],
         ["A dashboard is considered only for validated demand-based applications and with service authorisation."],
         NAVY, "white", NAVY, dark=True)
    # arrows
    varrow(557, 370, 425, GREEN); varrow(1650, 370, 425, ORANGE); varrow(2742, 370, 425, BLUE)
    varrow(750, 595, 650, GREY); varrow(1860, 595, 650, GREY); varrow(2742, 595, 650, BLUE)
    varrow(800, 915, 980, NAVY); varrow(2432, 915, 980, BLUE)
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
