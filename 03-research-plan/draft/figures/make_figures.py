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
    # General overview: what exists at onset, the gap, what HEADSTART does (WP1 to WP4), the test, the test sequence.
    W, H = 1400, 820
    PAD = 28
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W+2*PAD}" height="{H+2*PAD}" '
         f'viewBox="0 0 {W+2*PAD} {H+2*PAD}">', DEFS, f'<rect width="{W+2*PAD}" height="{H+2*PAD}" fill="white"/>',
         f'<g transform="translate({PAD},{PAD})">']
    NAVY, GREEN, ORANGE, BLUE, GREY = "#1f3a5f", "#2e8b57", "#c8701a", "#1f5f8b", "#8a97a6"
    GREEN_BG, ORANGE_BG, BLUE_BG, GREY_BG = "#eaf5ef", "#fdf3e6", "#e8f0f7", "#f3f5f7"

    def fits(txt, size, width, bold=False):
        assert len(txt) * size * (0.56 if bold else 0.52) <= width, (txt, size, width)

    def label(x, y, t, size, col=INK, anchor="start", bold=False):
        s.append(text(x, y, t, size, col, anchor, "bold" if bold else "normal"))

    def header(y, t):
        label(0, y, t, 19, NAVY, bold=True)
        s.append(f'<line x1="0" y1="{y+10}" x2="{W}" y2="{y+10}" stroke="{LINE}" stroke-width="0.8" opacity="0.6"/>')

    # ---------- row 1: what is available when a crisis starts ----------
    header(30, "WHAT IS AVAILABLE WHEN A CRISIS STARTS")
    CW, CH, CY = 440, 150, 58
    cards = [(0, "Published evidence", BLUE, BLUE_BG,
              ["Parameter estimates and their uncertainty", "Predictors, lags, model types, thresholds", "From other settings and past events"]),
             (480, "Context data", GREEN, GREEN_BG,
              ["Weather, air quality and calendar effects", "Wastewater and surveillance indicators", "Often public or available through partners"]),
             (960, "Local outcome candidates", ORANGE, ORANGE_BG,
              ["Calls, ED visits, admissions, occupancy", "Chosen from what the data and the evidence allow", "Few, delayed or incomplete early in an episode"])]
    for x, title, col, bg, lines in cards:
        s.append(box(x, CY, CW, CH, bg, col, 10, 2.2))
        fits(title, 19, CW - 40, True); label(x + 20, CY + 36, title, 19, col, bold=True)
        for i, ln in enumerate(lines):
            fits(ln, 16, CW - 40); label(x + 20, CY + 70 + i * 27, ln, 16, INK if i < 2 else MUTE)
    s.append(box(0, 228, W, 64, GREY_BG, GREY, 8, 1.2))
    g1 = "The gap is rarely the context data. It is too little local outcome history to learn how context relates to this episode."
    g2 = "The target is chosen before any model comparison, using registered criteria for relevance, access and data quality."
    fits(g1, 17, W - 40, True); label(W/2, 255, g1, 17, NAVY, "middle", True)
    fits(g2, 15, W - 40); label(W/2, 279, g2, 15, MUTE, "middle")

    # ---------- row 2: what HEADSTART does ----------
    header(340, "WHAT HEADSTART DOES")
    BY, BH, BW = 372, 118, 320
    steps = [("WP1", "Build evidence inputs", "Extract studies, assess uncertainty", "and relevance to the local setting", BLUE, BLUE_BG),
             ("WP2", "Model levels of pressure", "Combine context and outcomes,", "estimate levels of system pressure", GREEN, GREEN_BG),
             ("WP3", "Replay past episodes", "Compare two strategies with the", "same feeds and the same target", NAVY, GREY_BG),
             ("WP4", "Test decision value", "Would a better forecast change", "a defensible operational decision?", ORANGE, ORANGE_BG)]
    for k, (wp, l1, l2, l3, col, bg) in enumerate(steps):
        x = k * 360
        s.append(box(x, BY, BW, BH, bg, col, 10, 1.8))
        label(x + 18, BY + 40, wp, 20, col, bold=True)
        fits(l1, 17, 250, True); label(x + 68, BY + 40, l1, 17, col, bold=True)
        fits(l2, 15, BW - 36); label(x + 18, BY + 72, l2, 15, INK)
        fits(l3, 15, BW - 36); label(x + 18, BY + 96, l3, 15, INK)
        if k < 3:
            s.append(arrow(x + BW + 4, BY + BH/2, x + 356, BY + BH/2, MUTE))

    # ---------- row 3: the test and the Geneva sequence ----------
    header(540, "THE TEST (schematic hypothesis, not observed results)")
    px, py, pw, ph = 135, 574, 490, 140
    s.append(f'<line x1="{px}" y1="{py+ph}" x2="{px+pw}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<path d="M {px+10} {py+30} C {px+170} {py+40} {px+360} {py+92} {px+pw-10} {py+106}" fill="none" stroke="{BLUE}" stroke-width="4"/>')
    s.append(f'<path d="M {px+10} {py+132} C {px+150} {py+131} {px+360} {py+120} {px+pw-10} {py+106}" fill="none" stroke="{MUTE}" stroke-width="3" stroke-dasharray="7,6"/>')
    label(px + pw + 14, py + 42, "evidence-informed strategy", 16, BLUE)
    label(px + pw + 14, py + 132, "reference strategy, local data only", 16, MUTE)
    label(px - 10, py + 8, "forecast quality", 15, MUTE, "end")
    label(px, py + ph + 24, "episode onset", 15, MUTE)
    label(px + pw, py + ph + 24, "more outcomes observed", 15, MUTE, "end")

    label(880, 540, "THE GENEVA TEST SEQUENCE", 19, NAVY, bold=True)
    chips = [("1", "Respiratory epidemics", "primary confirmatory test", BLUE),
             ("2", "Heat events", "second test", GREEN),
             ("3", "Legionellosis", "third test", ORANGE)]
    for k, (n, nm, sub, col) in enumerate(chips):
        y = 566 + k * 56
        s.append(box(880, y, 520, 44, GREY_BG, col, 22, 1.8))
        s.append(f'<circle cx="{906}" cy="{y+22}" r="13" fill="white" stroke="{col}" stroke-width="2"/>')
        label(906, y + 27, n, 14, col, "middle", True)
        fits(nm, 18, 220, True); label(930, y + 29, nm, 18, col, bold=True)
        fits(sub, 14.5, 230); label(1378, y + 29, sub, 14.5, MUTE, "end")
    label(880, 762, "Outcome, levels and thresholds registered before any test", 15, MUTE)
    label(880, 786, "Dashboard in observation mode where authorised, never directs care", 15, MUTE)
    s.append("</g></svg>")
    (OUT / "fig1-framework.svg").write_text("\n".join(s), encoding="utf-8")


WPS = [
    ("WP1", "Evidence and model inputs", 1, 20, [
        ("T1.1 Evidence target and protocol", 1, 4),
        ("T1.2 Manual extraction benchmark", 3, 9),
        ("T1.3 Automated extraction error", 7, 14),
        ("T1.4 Evidence distributions", 12, 18),
        ("T1.5 Transportability screen", 15, 20)]),
    ("WP2", "Model demand and pressure", 1, 28, [
        ("T2.1 Pressure model and identifiability", 1, 9),
        ("T2.2 Critical tail", 6, 14),
        ("T2.3 Evidence in the parameters", 10, 20),
        ("T2.4 Resilience indicators", 12, 20),
        ("T2.5 Calibration and automation", 20, 28)]),
    ("WP3", "Historical forecast test", 1, 42, [
        ("T3.0 Outcomes, data gate, registration", 1, 14),
        ("T3.1 Assemble the data", 12, 20),
        ("T3.2 Replay with past information only", 18, 30),
        ("T3.3 Model library and confirmatory tests", 20, 34),
        ("T3.4 Map benefit and failure", 28, 38),
        ("T3.5 Heat and legionellosis tests", 34, 42)]),
    ("WP4", "Decision value and deployment", 24, 48, [
        ("T4.1 Elicit costs and thresholds", 24, 32),
        ("T4.2 Decision analysis and fairness", 30, 40),
        ("T4.3 Dashboard and living updates", 34, 48)]),
]
MILESTONES = [(9, "M1", "benchmark released"), (12, "M2", "model passes, data gate"),
              (20, "M3", "open-data benchmark, target chosen"), (34, "M4", "main test done"),
              (40, "M5", "decision value"), (48, "M6", "three tests, dashboard")]


def fig2():
    L, R, TOP, ROW, GAP = 440, 30, 56, 25, 18
    W = 1200
    nrows = sum(len(w[4]) + 1 for w in WPS)
    H = TOP + nrows * ROW + GAP * len(WPS) + 118
    span = W - L - R

    def mx(m):
        return L + (m / 48) * span

    PAD = 28
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W+2*PAD}" height="{H+2*PAD}" '
         f'viewBox="0 0 {W+2*PAD} {H+2*PAD}">', DEFS, f'<rect width="{W+2*PAD}" height="{H+2*PAD}" fill="white"/>',
         f'<g transform="translate({PAD},{PAD})">']

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
        s.append(text(x, body_bottom + 20, str(yr * 12), 14, MUTE, "middle"))
    s.append(text(mx(24), body_bottom + 38, "project month", 14, MUTE, "middle"))

    y = TOP
    for code, title, a, b, tasks in WPS:
        assert len(f"{code}  {title}") * 17 * 0.56 <= L - 20, title
        s.append(text(0, y + 18, code, 17, ACCENT, weight="bold"))
        s.append(text(52, y + 18, title, 17, ACCENT, weight="bold"))
        s.append(box(mx(a), y + 8, mx(b) - mx(a), 7, ACCENT, ACCENT, 2, 0))
        y += ROW
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
        s.append(f'<polygon points="{x},{body_bottom+46} {x+7},{body_bottom+55} '
                 f'{x},{body_bottom+64} {x-7},{body_bottom+55}" fill="{ACCENT}"/>')
        s.append(text(x, body_bottom + 84, lab, 16.5, ACCENT, "middle", "bold"))
    legend = " · ".join(f"{lab} {desc}" for _, lab, desc in MILESTONES)
    assert len("Milestones.  " + legend) * 13.5 * 0.5 <= W, legend
    s.append(text(0, body_bottom + 110, "Milestones.  " + legend, 13.5, MUTE))
    s.append("</g></svg>")
    (OUT / "fig2-gantt.svg").write_text("\n".join(s))


fig1()
fig2()
print("wrote fig1-framework.svg and fig2-gantt.svg")
