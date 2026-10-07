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
    W, H = 1400, 566
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']

    def fits(txt, size, width, bold=False):
        assert len(txt) * size * (0.56 if bold else 0.52) <= width, (txt, size, width)

    # --- evidence path (top row) ---
    s.append(text(0, 26, "EVIDENCE PATH (WP1)", 21, ACCENT, weight="bold"))
    ev = [(0, "Open literature", ["searched live"]),
          (250, "Extraction", ["provenance + quality"]),
          (500, "Evidence priors", ["values, variables,", "models, thresholds"])]
    for x, title, subs in ev:
        s.append(box(x, 38, 215, 92, ACCENT_BG, ACCENT))
        fits(title, 22, 205, bold=True)
        s.append(text(x + 107, 68, title, 22, INK, "middle", "bold"))
        ys = [100] if len(subs) == 1 else [92, 112]
        for sub, sy in zip(subs, ys):
            fits(sub, 16, 205)
            s.append(text(x + 107, sy, sub, 16, MUTE, "middle"))
    s.append(arrow(217, 84, 247, 84, ACCENT))
    s.append(arrow(467, 84, 497, 84, ACCENT))

    # --- local data path (left) ---
    s.append(text(0, 190, "LOCAL DATA (short at onset)", 21, MUTE, weight="bold"))
    s.append(box(0, 204, 320, 128))
    for i, l in enumerate(["CASU-144 demand (primary)", "ED presentations", "ICU occupancy",
                           "weather + surveillance"]):
        fits(l, 18.5, 300, bold=(i == 0))
        s.append(text(16, 234 + i * 27, l, 18.5, INK if i == 0 else MUTE,
                      weight="bold" if i == 0 else "normal"))

    # --- state model (centre) with threshold anchors ---
    mx0, my0, mw = 390, 176, 380
    s.append(box(mx0, my0, mw, 240, "white", INK, 6, 1.8))
    s.append(text(mx0 + mw / 2, my0 + 30, "LATENT STATE MODEL (WP2)", 21, ACCENT, "middle", "bold"))
    states = [("routine", "below P75", 0), ("elevated", "P75 to P90", 1),
              ("strained", "above P90 or ICU > 85%", 2), ("critical", "above P97.5 / saturation", 3)]
    for nm, anchor, i in states:
        y = my0 + 46 + i * 47
        f = ACCENT_BG if i == 3 else FILL
        st = ACCENT if i == 3 else LINE
        s.append(box(mx0 + 16, y, 132, 36, f, st, 4))
        s.append(text(mx0 + 82, y + 25, nm, 18.5, INK, "middle", "bold" if i == 3 else "normal"))
        fits(anchor, 16.5, 214)
        s.append(text(mx0 + 158, y + 25, anchor, 16.5, MUTE))
    s.append(arrow(607, 134, 607, 172, ACCENT))      # priors into model
    s.append(arrow(324, 268, 386, 268, MUTE))        # local data into model

    # --- model library + automated selection (top right) ---
    lx, lw = 1040, 300
    s.append(box(lx, 38, lw, 152, "white", INK, 6, 1.8))
    lib = [("MODEL LIBRARY (WP3)", 19, ACCENT, "bold", 64),
           ("baselines, surveillance, ML,", 17, MUTE, "normal", 89),
           ("regime; mechanistic models", 17, MUTE, "normal", 110),
           ("for epidemic crises only", 17, MUTE, "normal", 131),
           ("assumption + validity checks;", 17, INK, "normal", 152),
           ("automated champion per arm", 17, INK, "bold", 173)]
    s.append(box(lx, 38, lw, 152, "white", INK, 6, 1.8))
    for txt, size, col, w8, yy in lib:
        fits(txt, size, lw - 14, bold=(w8 == "bold"))
        s.append(text(lx + lw/2, yy, txt, size, col, "middle", w8))
    s.append(arrow(719, 84, lx - 4, 84, ACCENT))      # priors into library
    s.append(arrow(774, 230, lx - 4, 160, MUTE))      # state model into library
    s.append(arrow(lx + lw/2, 194, lx + lw/2, 222, MUTE))  # champion into decisions

    # --- decision layer (right) ---
    s.append(box(lx, 226, lw, 132, ACCENT_BG, ACCENT))
    dec = [("DECISIONS (WP4)", 19, ACCENT, "bold", 252),
           ("elicited thresholds;", 17, MUTE, "normal", 277),
           ("net benefit, not accuracy alone", 17, MUTE, "normal", 298),
           ("daily dashboard,", 17.5, INK, "bold", 322),
           ("observation mode", 17.5, INK, "bold", 343)]
    for txt, size, col, w8, yy in dec:
        fits(txt, size, lw - 10, bold=(w8 == "bold"))
        s.append(text(lx + lw/2, yy, txt, size, col, "middle", w8))
    s.append(arrow(774, 300, lx - 4, 300, MUTE))

    # --- living evidence monitor (bottom right) ---
    s.append(box(lx, 386, lw, 130, FILL, LINE, 6))
    mon = [("LIVING EVIDENCE MONITOR", 18, INK, "bold", 412),
           ("reviews re-run daily;", 17, MUTE, "normal", 436),
           ("new evidence revises priors,", 17, MUTE, "normal", 457),
           ("variables, thresholds, models:", 17, MUTE, "normal", 478),
           ("registered update rules only", 17, INK, "normal", 499)]
    for txt, size, col, w8, yy in mon:
        fits(txt, size, lw - 14, bold=(w8 == "bold"))
        s.append(text(lx + lw/2, yy, txt, size, col, "middle", w8))
    s.append(arrow(lx + lw/2, 362, lx + lw/2, 382, MUTE, "6,5"))  # dashboard feeds monitor
    s.append(f'<path d="M 1344 451 L 1372 451 L 1372 16 L 715 16 L 715 32" fill="none" '
             f'stroke="{MUTE}" stroke-width="2.2" stroke-dasharray="6,5" marker-end="url(#a)"/>')

    # --- H3a sketch (bottom left, below the state model) ---
    iy = 452
    s.append(text(0, iy, "H3a, THE TEST (WP3):  skill advantage of evidence use, by elapsed local data",
                  19, INK, weight="bold"))
    px, py, pw, ph = 64, iy + 14, 560, 74
    s.append(f'<line x1="{px}" y1="{py+ph}" x2="{px+pw}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<path d="M {px} {py+16} C {px+150} {py+20} {px+300} {py+38} {px+pw} {py+48}" '
             f'fill="none" stroke="{ACCENT}" stroke-width="3.4"/>')
    s.append(f'<path d="M {px} {py+64} C {px+130} {py+59} {px+300} {py+51} {px+pw} {py+48}" '
             f'fill="none" stroke="{MUTE}" stroke-width="3" stroke-dasharray="7,5"/>')
    s.append(text(px + pw + 12, py + 46, "evidence-informed", 17, ACCENT))
    s.append(text(px + pw + 12, py + 72, "local-only", 17, MUTE))
    s.append(text(px - 10, py + 10, "skill", 17, MUTE, "end"))
    s.append(text(px, py + ph + 23, "crisis onset", 17, MUTE))
    s.append(text(px + pw, py + ph + 23, "local data accumulate", 17, MUTE, "end"))
    s.append("</svg>")
    (OUT / "fig1-framework.svg").write_text("\n".join(s))


# ---------------------------------------------------------------- Figure 2
# This list mirrors the 19 tasks in draft/04-workplan.md exactly.
WPS = [
    ("WP1", 1, 20, [
        ("T1.1 evidence target + protocol", 1, 4),
        ("T1.2 extraction benchmark", 3, 9),
        ("T1.3 automated extraction error", 7, 14),
        ("T1.4 evidence distributions", 12, 18),
        ("T1.5 transportability screen", 15, 20)]),
    ("WP2", 1, 28, [
        ("T2.1 state model + identifiability", 1, 9),
        ("T2.2 critical tail", 6, 14),
        ("T2.3 evidence-derived priors", 10, 20),
        ("T2.4 resilience indicators", 12, 20),
        ("T2.5 calibration, automation, validity", 20, 28)]),
    ("WP3", 1, 42, [
        ("T3.0 outcome hierarchy + registration", 1, 14),
        ("T3.1 retrospective information set", 12, 20),
        ("T3.2 information-set reconstruction", 18, 30),
        ("T3.3 model library + automated selection", 20, 34),
        ("T3.4 benefit + failure map", 28, 38),
        ("T3.5 cross-archetype generalisation", 34, 42)]),
    ("WP4", 24, 48, [
        ("T4.1 losses + thresholds (SHELF)", 24, 32),
        ("T4.2 decision analysis + equity audit", 30, 40),
        ("T4.3 counterfactuals, observation dashboard", 34, 48)]),
]
MILESTONES = [(9, "M1"), (12, "M2"), (20, "M3"), (34, "M4"), (40, "M5"), (48, "M6")]


def fig2():
    L, R, TOP, ROW, GAP = 392, 24, 44, 21, 8
    W = 1150
    nrows = sum(len(w[3]) for w in WPS)
    H = TOP + nrows * ROW + GAP * len(WPS) + 50
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
