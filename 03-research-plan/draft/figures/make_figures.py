#!/usr/bin/env python3
"""Generate the two research-plan figures as SVG. No dependencies.

    python3 make_figures.py

Writes fig1-framework.svg and fig2-gantt.svg alongside this script.
Designed to stay legible in greyscale print: one accent colour, everything
else distinguished by weight and position rather than by hue.
"""
import pathlib

OUT = pathlib.Path(__file__).parent
INK, MUTE, LINE = "#1a1a1a", "#5c5c5c", "#9a9a9a"
ACCENT, ACCENT_BG = "#1f5f8b", "#e3edf4"
FILL = "#f4f4f4"
FONT = "Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=13, fill=INK, anchor="start", weight="normal", style="normal"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
            f'font-style="{style}">{esc(s)}</text>')


def box(x, y, w, h, fill=FILL, stroke=LINE, rx=4, sw=1):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def arrow(x1, y1, x2, y2, stroke=MUTE, dash=None, sw=1.6):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" marker-end="url(#a)"{d}/>')


def wrap(x, y, lines, size=11.5, fill=MUTE, lh=14, anchor="start"):
    return "".join(text(x, y + i * lh, l, size, fill, anchor) for i, l in enumerate(lines))


DEFS = ('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{MUTE}"/></marker></defs>')


# ---------------------------------------------------------------- Figure 1
def fig1():
    W, H = 1000, 470
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']

    s.append(text(0, 18, "Figure 1. The cold-start problem and the proposed framework.",
                  13.5, INK, weight="bold"))

    # --- evidence path (top) ---
    s.append(text(0, 52, "EVIDENCE PATH", 10.5, ACCENT, weight="bold"))
    ev = [(0, "Published\nliterature", "80k+ documents,\ncontinuously indexed"),
          (200, "Structured\nextraction", "effect sizes with\nprovenance + quality"),
          (400, "Pooling and\nprior construction", "robust MAP mixture,\nadaptive discounting")]
    for x, title, sub in ev:
        s.append(box(x, 62, 165, 62, ACCENT_BG, ACCENT))
        for i, l in enumerate(title.split("\n")):
            s.append(text(x + 12, 82 + i * 15, l, 12.5, INK, weight="bold"))
        s.append(wrap(x + 12, 112, sub.split("\n"), 9.5, MUTE, 11))
    for x in (165, 365):
        s.append(arrow(x + 2, 93, x + 33, 93, ACCENT))
    s.append(text(178, 88, "WP1", 9, ACCENT, "middle", "bold"))
    s.append(text(378, 88, "WP1", 9, ACCENT, "middle", "bold"))

    # --- local data path (bottom) ---
    s.append(text(0, 196, "LOCAL DATA PATH", 10.5, MUTE, weight="bold"))
    s.append(box(0, 206, 365, 62))
    s.append(text(12, 226, "Operational series", 12.5, INK, weight="bold"))
    s.append(wrap(12, 242, ["144 / CASU dispatch  ·  HUG emergency presentations",
                            "ICU occupancy  ·  weather, surveillance covariates"], 9.5, MUTE, 11))
    s.append(text(12, 284, "short and unstable at crisis onset", 10, MUTE, style="italic"))
    s.append(arrow(367, 237, 596, 200, MUTE))

    # --- model ---
    s.append(box(600, 62, 190, 206, "white", INK, 5, 1.6))
    s.append(text(695, 84, "REGIME-SWITCHING", 10.5, ACCENT, "middle", "bold"))
    s.append(text(695, 98, "STATE MODEL", 10.5, ACCENT, "middle", "bold"))
    s.append(text(695, 112, "WP2", 9, MUTE, "middle"))
    states = [("routine", 128), ("elevated", 156), ("strained", 184), ("critical", 212)]
    for i, (nm, y) in enumerate(states):
        f = ACCENT_BG if i == 3 else FILL
        st = ACCENT if i == 3 else LINE
        s.append(box(620, y, 150, 22, f, st, 3))
        s.append(text(695, y + 15, nm, 11, INK, "middle",
                      "bold" if i == 3 else "normal"))
        if i < 3:
            s.append(f'<line x1="695" y1="{y+22}" x2="695" y2="{y+28}" '
                     f'stroke="{LINE}" stroke-width="1.2" marker-end="url(#a)"/>')
    s.append(text(695, 252, "tail: generalised Pareto", 9.5, MUTE, "middle", style="italic"))
    s.append(arrow(568, 93, 596, 110, ACCENT))

    # --- decision ---
    s.append(box(820, 128, 180, 90, ACCENT_BG, ACCENT))
    s.append(text(910, 150, "DECISION LAYER", 10.5, ACCENT, "middle", "bold"))
    s.append(text(910, 164, "WP4", 9, MUTE, "middle"))
    s.append(wrap(910, 182, ["thresholds elicited from",
                             "responders; evaluated on",
                             "net benefit, not accuracy"], 9.5, MUTE, 12, "middle"))
    s.append(arrow(792, 165, 816, 165))

    # --- inset: the hypothesis ---
    ix, iy, iw, ih = 0, 320, 520, 130
    s.append(box(ix, iy, iw, ih, "white", LINE))
    s.append(text(ix + 12, iy + 20, "H3a — the claim being tested (WP3)", 11, INK, weight="bold"))
    px, py, pw, ph = ix + 48, iy + 36, 300, 74
    s.append(f'<line x1="{px}" y1="{py+ph}" x2="{px+pw}" y2="{py+ph}" stroke="{INK}" stroke-width="1.2"/>')
    s.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+ph}" stroke="{INK}" stroke-width="1.2"/>')
    # with priors: high early, flattening
    s.append(f'<path d="M {px} {py+16} C {px+80} {py+18} {px+160} {py+30} {px+pw} {py+34}" '
             f'fill="none" stroke="{ACCENT}" stroke-width="2.2"/>')
    # without priors: poor early, converging
    s.append(f'<path d="M {px} {py+68} C {px+70} {py+62} {px+150} {py+38} {px+pw} {py+34}" '
             f'fill="none" stroke="{MUTE}" stroke-width="2.2" stroke-dasharray="5,4"/>')
    s.append(text(px + pw + 8, py + 30, "with evidence priors", 9.5, ACCENT))
    s.append(text(px + pw + 8, py + 62, "without", 9.5, MUTE))
    s.append(text(px - 6, py + 8, "forecast", 9.5, MUTE, "end"))
    s.append(text(px - 6, py + 20, "skill", 9.5, MUTE, "end"))
    s.append(text(px, py + ph + 16, "crisis onset", 9.5, MUTE))
    s.append(text(px + pw, py + ph + 16, "local data accumulate", 9.5, MUTE, "end"))

    s.append(wrap(560, iy + 34,
                  ["The advantage is hypothesised to exist early and to",
                   "decay to nothing. WP3 measures the shape of that curve",
                   "by rolling-origin refitting that uses only data — and only",
                   "literature — available at each historical origin.",
                   "",
                   "H3b asks the harder question: when the prior is wrong,",
                   "is the harm bounded and detectable early enough to act?"],
                  10.5, MUTE, 15))
    s.append("</svg>")
    (OUT / "fig1-framework.svg").write_text("\n".join(s))


# ---------------------------------------------------------------- Figure 2
WPS = [
    ("WP1", "Evidence to quantitative priors", 1, 24, [
        ("T1.1 parameter classes, protocol", 1, 4),
        ("T1.2 gold-standard benchmark", 3, 10),
        ("T1.3 extraction error characterised", 8, 16),
        ("T1.4 error model, corrected priors", 14, 22),
        ("T1.5 transportability assessment", 18, 24)]),
    ("WP2", "Regime switching with extreme-value tail", 1, 30, [
        ("T2.1 state process + identifiability sim.", 1, 8),
        ("T2.2 tail model", 6, 14),
        ("T2.3 prior structure, adaptive discounting", 10, 20),
        ("T2.4 baselines pre-specified", 12, 22),
        ("T2.5 resilience indicators as covariates", 8, 18),
        ("T2.6 conformal calibration layer", 20, 28),
        ("T2.7 reference implementation", 18, 30)]),
    ("WP3", "Retrospective cold-start evaluation", 12, 42, [
        ("T3.1 operational record assembled", 12, 20),
        ("T3.2 rolling-origin evaluation", 18, 32),
        ("T3.3 skill and calibration", 24, 36),
        ("T3.4 failure and stress analysis", 28, 38),
        ("T3.5 waterborne archetype (extension)", 34, 42)]),
    ("WP4", "Decision relevance and prospective test", 24, 48, [
        ("T4.1 threshold elicitation", 24, 32),
        ("T4.2 consequence-weighted evaluation", 30, 40),
        ("T4.3 value of information", 34, 42),
        ("T4.4 prospective shadow mode", 36, 48),
        ("T4.5 equity audit", 32, 40),
        ("T4.6 retrospective counterfactuals", 36, 44)]),
]
MILESTONES = [(10, "M1"), (12, "M2"), (20, "M3"), (32, "M4"), (40, "M5"), (48, "M6")]
MS_TEXT = ["M1 extraction benchmark released", "M2 regime model identifiable in simulation",
           "M3 operational data in place", "M4 cold-start result",
           "M5 decision-analytic evaluation", "M6 prospective validation"]


def fig2():
    L, R, TOP, ROW = 320, 60, 76, 19
    W = 1000
    n = sum(1 + len(w[4]) for w in WPS)
    H = TOP + n * ROW + 130
    span = W - L - R
    def mx(m):
        return L + (m / 48) * span

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']
    s.append(text(0, 18, "Figure 2. Work plan, 48 months.", 13.5, INK, weight="bold"))
    s.append(text(0, 36, "No work package is contingent on another succeeding; fallbacks are "
                         "triggered at the milestones marked below.", 10.5, MUTE, style="italic"))

    # year grid
    for yr in range(5):
        x = mx(yr * 12)
        s.append(f'<line x1="{x}" y1="{TOP-14}" x2="{x}" y2="{TOP + n*ROW + 6}" '
                 f'stroke="{LINE}" stroke-width="0.8" stroke-dasharray="2,3"/>')
        if yr < 4:
            s.append(text(mx(yr * 12 + 6), TOP - 20, f"Year {yr+1}", 10, MUTE, "middle"))
    s.append(text(L, TOP - 34, "month 0", 9, MUTE))
    s.append(text(W - R, TOP - 34, "month 48", 9, MUTE, "end"))

    y = TOP
    for code, title, a, b, tasks in WPS:
        s.append(text(0, y + 13, f"{code}", 11.5, ACCENT, weight="bold"))
        s.append(text(38, y + 13, title, 11.5, INK, weight="bold"))
        s.append(box(mx(a), y + 3, mx(b) - mx(a), 13, ACCENT_BG, ACCENT, 3))
        y += ROW
        for tname, ta, tb in tasks:
            s.append(text(20, y + 12, tname, 10, MUTE))
            s.append(box(mx(ta), y + 4, max(mx(tb) - mx(ta), 3), 10, FILL, LINE, 2))
            y += ROW
    base = y + 6

    # milestones
    for m, lab in MILESTONES:
        x = mx(m)
        s.append(f'<line x1="{x}" y1="{TOP-14}" x2="{x}" y2="{base}" stroke="{ACCENT}" '
                 f'stroke-width="1" stroke-dasharray="3,3" opacity="0.55"/>')
        s.append(f'<polygon points="{x},{base+4} {x+6},{base+12} {x},{base+20} {x-6},{base+12}" '
                 f'fill="{ACCENT}"/>')
        s.append(text(x, base + 34, lab, 9.5, ACCENT, "middle", "bold"))

    for i, t in enumerate(MS_TEXT):
        col, row = i % 2, i // 2
        s.append(text(col * 500, base + 62 + row * 15, t, 10, MUTE))
    s.append("</svg>")
    (OUT / "fig2-gantt.svg").write_text("\n".join(s))


fig1()
fig2()
print("wrote fig1-framework.svg and fig2-gantt.svg")
