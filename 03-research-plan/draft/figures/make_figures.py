#!/usr/bin/env python3
"""Generate the two research-plan figures as SVG. No dependencies.

    python3 make_figures.py

Writes fig1-framework.svg and fig2-gantt.svg alongside this script.
Print targets: fig1 placed at ~12.8 cm width, fig2 at ~16.5 cm width.
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
    W, H = 1064, 540
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']

    # --- evidence path (top row) ---
    s.append(text(0, 24, "EVIDENCE PATH (WP1)", 19, ACCENT, weight="bold"))
    ev = [(0, "Open literature", "searched live"),
          (235, "Extraction", "provenance + quality"),
          (470, "Evidence priors", "values, variables, forms, thresholds")]
    for x, title, sub in ev:
        s.append(box(x, 36, 200, 72, ACCENT_BG, ACCENT))
        s.append(text(x + 100, 65, title, 21, INK, "middle", "bold"))
        s.append(text(x + 100, 92, sub, 17 if len(sub) < 24 else 12.5, MUTE, "middle"))
    s.append(arrow(202, 72, 232, 72, ACCENT))
    s.append(arrow(437, 72, 467, 72, ACCENT))

    # --- local data path (bottom left) ---
    s.append(text(0, 168, "LOCAL DATA (short at onset)", 19, MUTE, weight="bold"))
    s.append(box(0, 180, 300, 120))
    for i, l in enumerate(["CASU-144 demand (primary)", "ED presentations", "ICU occupancy",
                           "weather + surveillance"]):
        s.append(text(16, 208 + i * 25, l, 17, INK if i == 0 else MUTE,
                      weight="bold" if i == 0 else "normal"))

    # --- state model (centre) with threshold anchors ---
    mx0, my0, mw = 360, 150, 340
    s.append(box(mx0, my0, mw, 230, "white", INK, 6, 1.8))
    s.append(text(mx0 + mw / 2, my0 + 26, "LATENT STATE MODEL (WP2)", 19, ACCENT, "middle", "bold"))
    states = [("routine", "below P75", 0), ("elevated", "P75 to P90", 1),
              ("strained", "above P90 or ICU > 85%", 2), ("critical", "above P97.5 / saturation", 3)]
    for nm, anchor, i in states:
        y = my0 + 42 + i * 45
        f = ACCENT_BG if i == 3 else FILL
        st = ACCENT if i == 3 else LINE
        s.append(box(mx0 + 16, y, 120, 34, f, st, 4))
        s.append(text(mx0 + 76, y + 23, nm, 17, INK, "middle", "bold" if i == 3 else "normal"))
        s.append(text(mx0 + 150, y + 23, anchor, 15, MUTE))
    s.append(arrow(540, 112, 540, 146, ACCENT))      # priors into model
    s.append(arrow(304, 240, 356, 240, MUTE))        # local data into model

    # --- model library + automated selection (top right) ---
    s.append(box(760, 36, 240, 118, "white", INK, 6, 1.8))
    s.append(text(880, 58, "MODEL LIBRARY (WP3)", 17, ACCENT, "middle", "bold"))
    s.append(text(880, 80, "baselines, surveillance, ML,", 15, MUTE, "middle"))
    s.append(text(880, 98, "regime; mechanistic: epidemic only", 15, MUTE, "middle"))
    s.append(text(880, 122, "assumption + validity checks", 15, INK, "middle"))
    s.append(text(880, 140, "automated champion per arm", 15, INK, "middle", "bold"))
    s.append(arrow(674, 72, 756, 72, ACCENT))         # priors into library
    s.append(arrow(880, 158, 880, 186, MUTE))         # library champion into decisions
    s.append(arrow(704, 200, 756, 128, MUTE))         # state model into library

    # --- decision layer (right) ---
    s.append(box(760, 190, 240, 150, ACCENT_BG, ACCENT))
    s.append(text(880, 216, "DECISIONS (WP4)", 19, ACCENT, "middle", "bold"))
    s.append(text(880, 242, "elicited thresholds;", 15, MUTE, "middle"))
    s.append(text(880, 262, "net benefit, not accuracy alone", 15, MUTE, "middle"))
    s.append(text(880, 290, "daily dashboard,", 15.5, INK, "middle", "bold"))
    s.append(text(880, 310, "observation mode", 15.5, INK, "middle", "bold"))
    s.append(arrow(704, 260, 756, 260, MUTE))

    # --- living update loop (bottom right) ---
    s.append(box(760, 380, 240, 120, FILL, LINE, 6))
    s.append(text(880, 404, "LIVING EVIDENCE MONITOR", 16, INK, "middle", "bold"))
    s.append(text(880, 426, "reviews re-run daily; new evidence", 15, MUTE, "middle"))
    s.append(text(880, 444, "revises priors, variables,", 15, MUTE, "middle"))
    s.append(text(880, 462, "thresholds, models:", 15, MUTE, "middle"))
    s.append(text(880, 482, "registered update rules only", 15, INK, "middle"))
    s.append(arrow(880, 344, 880, 376, MUTE, "6,5"))  # dashboard feeds monitor
    s.append(f'<path d="M 1004 440 L 1038 440 L 1038 16 L 672 16 L 672 30" fill="none" '
             f'stroke="{MUTE}" stroke-width="2.2" stroke-dasharray="6,5" marker-end="url(#a)"/>')

    # --- H3a sketch (bottom) ---
    iy = 410
    s.append(text(0, iy, "H3a, THE TEST (WP3):  skill advantage of evidence priors, by elapsed local data",
                  18, INK, weight="bold"))
    px, py, pw, ph = 70, iy + 18, 460, 86
    s.append(f'<line x1="{px}" y1="{py+ph}" x2="{px+pw}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<path d="M {px} {py+18} C {px+140} {py+22} {px+280} {py+42} {px+pw} {py+52}" '
             f'fill="none" stroke="{ACCENT}" stroke-width="3.4"/>')
    s.append(f'<path d="M {px} {py+74} C {px+120} {py+68} {px+260} {py+56} {px+pw} {py+52}" '
             f'fill="none" stroke="{MUTE}" stroke-width="3" stroke-dasharray="7,5"/>')
    s.append(text(px + pw + 12, py + 50, "with evidence priors", 16, ACCENT))
    s.append(text(px + pw + 12, py + 78, "without", 16, MUTE))
    s.append(text(px - 10, py + 10, "skill", 15, MUTE, "end"))
    s.append(text(px, py + ph + 24, "crisis onset", 15, MUTE))
    s.append(text(px + pw, py + ph + 24, "local data accumulate", 15, MUTE, "end"))
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
    L, R, TOP, ROW, GAP = 348, 24, 44, 22, 8
    W = 1000
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
            s.append(text(mx(yr * 12 + 6), TOP - 14, f"Year {yr+1}", 15, MUTE, "middle"))

    y = TOP
    for code, a, b, tasks in WPS:
        s.append(text(0, y + 17, code, 16, ACCENT, weight="bold"))
        s.append(box(mx(a), y + 16, mx(b) - mx(a), 5, ACCENT, ACCENT, 2, 0))
        for tname, ta, tb in tasks:
            s.append(text(44, y + 17, tname, 14, INK))
            s.append(box(mx(ta), y + 5, max(mx(tb) - mx(ta), 4), 15, FILL, LINE, 3))
            y += ROW
        y += GAP

    for m, lab in MILESTONES:
        x = mx(m)
        s.append(f'<line x1="{x}" y1="{TOP-6}" x2="{x}" y2="{body_bottom}" stroke="{ACCENT}" '
                 f'stroke-width="1.4" stroke-dasharray="4,4" opacity="0.6"/>')
        s.append(f'<polygon points="{x},{body_bottom+4} {x+7},{body_bottom+13} '
                 f'{x},{body_bottom+22} {x-7},{body_bottom+13}" fill="{ACCENT}"/>')
        s.append(text(x, body_bottom + 40, lab, 14.5, ACCENT, "middle", "bold"))
    s.append("</svg>")
    (OUT / "fig2-gantt.svg").write_text("\n".join(s))


fig1()
fig2()
print("wrote fig1-framework.svg and fig2-gantt.svg")
