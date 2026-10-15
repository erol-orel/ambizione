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
        fits(title, 19, CW - 40, True); label(x + CW/2, CY + 36, title, 19, col, "middle", True)
        for i, ln in enumerate(lines):
            fits(ln, 16, CW - 40); label(x + CW/2, CY + 70 + i * 27, ln, 16, INK if i < 2 else MUTE, "middle")
    s.append(box(0, 228, W, 64, GREY_BG, GREY, 8, 1.2))
    g1 = "The gap is rarely the context data. It is too little local outcome history to learn how context relates to this episode"
    g2 = "The target is chosen before any model comparison, using registered criteria for relevance, access and data quality"
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
        head = f"{wp}  {l1}"
        fits(head, 17, BW - 24, True); label(x + BW/2, BY + 40, head, 17, col, "middle", True)
        fits(l2, 15, BW - 36); label(x + BW/2, BY + 72, l2, 15, INK, "middle")
        fits(l3, 15, BW - 36); label(x + BW/2, BY + 96, l3, 15, INK, "middle")
        if k < 3:
            s.append(arrow(x + BW + 4, BY + BH/2, x + 356, BY + BH/2, MUTE))

    # ---------- row 3: the test and the Geneva sequence ----------
    header(540, "THE TEST (schematic hypothesis, not observed results)")
    px, py, pw, ph = 100, 574, 440, 186
    s.append(f'<line x1="{px}" y1="{py+ph}" x2="{px+pw}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{py+ph}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<path d="M {px+10} {py+24} C {px+170} {py+38} {px+370} {py+150} {px+pw-10} {py+ph-2}" fill="none" stroke="{BLUE}" stroke-width="4"/>')
    label(px - 10, py + 8, "skill score", 15, MUTE, "end")
    label(px - 10, py + ph + 4, "0", 15, MUTE, "end")
    label(px, py + ph + 24, "episode onset", 15, MUTE)
    label(px + pw, py + ph + 24, "more outcomes observed", 15, MUTE, "end")
    for i, ln in enumerate(["gain of the evidence-informed", "strategy over the reference"]):
        fits(ln, 15, 280); label(px + pw + 34, py + 62 + i * 22, ln, 15, BLUE)
    for i, ln in enumerate(["largest at onset, fading as", "local outcomes accumulate", "(0 = no gain)"]):
        fits(ln, 15, 280); label(px + pw + 34, py + 128 + i * 22, ln, 15, MUTE)

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
    label(1140, 762, "Outcome, levels and thresholds registered before any test", 15, MUTE, "middle")
    label(1140, 786, "Dashboard in observation mode where authorised, never directs care", 15, MUTE, "middle")
    s.append("</g></svg>")
    (OUT / "fig1-framework.svg").write_text("\n".join(s), encoding="utf-8")


WPS = [
    ("WP1", "Published evidence into model inputs", 1, 20, [
        ("T1.1 Fix what to look for, register", 1, 4),
        ("T1.2 Build the manual benchmark", 3, 9),
        ("T1.3 Measure extraction errors", 7, 14),
        ("T1.4 Turn numbers into distributions", 12, 18),
        ("T1.5 Check transfer to the local setting", 15, 20)]),
    ("WP2", "Model the levels of pressure", 1, 28, [
        ("T2.1 Build and test the pressure model", 1, 9),
        ("T2.2 Model rare peaks of demand", 6, 14),
        ("T2.3 Bring the evidence into the model", 10, 20),
        ("T2.4 Test two early-warning signals", 12, 20),
        ("T2.5 Calibrate, automate, check validity", 20, 28)]),
    ("WP3", "Replay past crises and test", 1, 42, [
        ("T3.0 Choose outcome, check data, register", 1, 14),
        ("T3.1 Assemble the data", 12, 20),
        ("T3.2 Replay with past information only", 18, 30),
        ("T3.3 Model library and the main tests", 20, 34),
        ("T3.4 Map when evidence helps or harms", 28, 38),
        ("T3.5 Heat and legionellosis tests", 34, 42)]),
    ("WP4", "From forecast skill to decision value", 24, 48, [
        ("T4.1 Elicit costs and thresholds", 24, 32),
        ("T4.2 Judge forecasts by the decisions", 30, 40),
        ("T4.3 Dashboard and living updates", 34, 48)]),
]
MILESTONES = [(4, "MS1", "protocol and outcome candidates registered"),
              (9, "MS2", "manual benchmark released"),
              (12, "MS3", "data gate passed, pressure model checked"),
              (20, "MS4", "second registration, open-data benchmark done"),
              (34, "MS5", "main respiratory test done"),
              (42, "MS6", "heat and legionellosis tests done"),
              (48, "MS7", "decision value measured, dashboard running")]


def fig2():
    L, R, TOP, ROW, GAP = 440, 30, 56, 25, 18
    W = 1200
    nrows = sum(len(w[4]) + 1 for w in WPS)
    H = TOP + nrows * ROW + GAP * len(WPS) + 184
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
        s.append(text(x, body_bottom + 84, lab, 14.5, ACCENT, "middle", "bold"))
    s.append(text(0, body_bottom + 110, "Milestones", 14, MUTE, weight="bold"))
    cols = [MILESTONES[:4], MILESTONES[4:]]
    for c, col in enumerate(cols):
        for r, (_, lab, desc) in enumerate(col):
            x, yy = 110 + c * 560, body_bottom + 110 + r * 22
            s.append(text(x, yy, lab, 14, ACCENT, weight="bold"))
            s.append(text(x + 40, yy, desc, 14, MUTE))
    s.append("</g></svg>")
    (OUT / "fig2-gantt.svg").write_text("\n".join(s))


fig1()
fig2()
print("wrote fig1-framework.svg and fig2-gantt.svg")
