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
    W, H = 1400, 470
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}">', DEFS, f'<rect width="{W}" height="{H}" fill="white"/>']

    def fits(txt, size, width, bold=False):
        assert len(txt) * size * (0.56 if bold else 0.52) <= width, (txt, size, width)

    def panel(x, y, w, h, title, lines, accent=False, title_size=19, body=16.5):
        s.append(box(x, y, w, h, ACCENT_BG if accent else FILL, ACCENT if accent else LINE, 6, 1.8 if accent else 1.4))
        fits(title, title_size, w - 20, True)
        s.append(text(x + w / 2, y + 27, title, title_size, ACCENT if accent else INK, "middle", "bold"))
        yy = y + 50
        for ln in lines:
            bold = ln.startswith("*")
            ln = ln.lstrip("*")
            fits(ln, body, w - 20, bold)
            s.append(text(x + w / 2, yy, ln, body, INK if bold else MUTE, "middle", "bold" if bold else "normal"))
            yy += 21

    # --- column 1: inputs available at onset ---
    cx, cw = 0, 372
    panel(cx, 20, cw, 118, "CONTEXT DATA, shared by both",
          ["weather, air quality, calendar effects,", "wastewater and surveillance feeds,",
           "*from public sources or partners"])
    panel(cx, 158, cw, 118, "LOCAL OUTCOMES, shared by both",
          ["long historical records of the service", "only a few outcomes from the new episode",
           "*emergency demand by cause (CASU-144)"])
    panel(cx, 296, cw, 154, "PUBLISHED STUDIES (WP1)",
          ["extracted automatically, with provenance", "and certainty grades, benchmarked (H1)",
           "parameter values, variables and lags,", "model forms, outcome thresholds",
           "*relevance to Geneva assessed (T1.5)"], accent=True)

    # --- column 2: the two strategies and the pressure levels ---
    sx, sw = 452, 400
    panel(sx, 40, sw, 112, "REFERENCE STRATEGY",
          ["candidate models fitted to context data", "and local outcomes only",
           "*best chosen by registered rules"])
    panel(sx, 190, sw, 134, "EVIDENCE-INFORMED STRATEGY",
          ["the same candidates and inputs, plus the", "published-evidence distributions, variables",
           "and model forms, with fixed or adaptive", "*weighting under evidence conflict"], accent=True)
    panel(sx, 352, sw, 98, "PRESSURE LEVELS (WP2)",
          ["routine, elevated, strained, critical", "*defaults, seeded from the evidence"])

    # --- column 3: evaluation, decisions, updating ---
    ex, ew = 932, 468
    panel(ex, 20, ew, 150, "EVALUATION AGAINST LATER OUTCOMES (WP3)",
          ["each past episode replayed from its onset,", "every forecast date uses only what was known then",
           "*H3a, evidence-informed vs reference, CRPS skill", "respiratory first, heat only if respiratory passes"])
    panel(ex, 190, ew, 112, "DECISION VALUE (WP4)",
          ["losses and escalation thresholds elicited", "from emergency services, net benefit",
           "*dashboard in observation mode, where authorised"])
    panel(ex, 322, ew, 112, "LIVING UPDATE",
          ["daily literature check, syntheses refreshed", "on a registered schedule",
           "*changes only through pre-registered rules"])

    # --- arrows ---
    s.append(arrow(cx + cw, 79, sx - 4, 96, MUTE))            # context -> reference
    s.append(arrow(cx + cw, 95, sx - 4, 257, MUTE))           # context -> evidence-informed
    s.append(arrow(cx + cw, 210, sx - 4, 110, MUTE))          # outcomes -> reference
    s.append(arrow(cx + cw, 226, sx - 4, 270, MUTE))          # outcomes -> evidence-informed
    s.append(arrow(cx + cw, 373, sx - 4, 300, ACCENT))        # studies -> evidence-informed only
    s.append(arrow(sx + sw / 2, 324, sx + sw / 2, 348, MUTE)) # strategies -> pressure levels
    s.append(arrow(sx + sw, 96, ex - 4, 80, MUTE))            # reference -> evaluation
    s.append(arrow(sx + sw, 257, ex - 4, 110, MUTE))          # evidence-informed -> evaluation
    s.append(arrow(ex + ew / 2, 170, ex + ew / 2, 186, MUTE)) # evaluation -> decision
    s.append(arrow(ex + ew / 2, 302, ex + ew / 2, 318, MUTE, "6,5"))  # decision -> living update
    s.append(f'<path d="M {ex + ew / 2} 434 L {ex + ew / 2} 458 L {cx + cw / 2} 458 L {cx + cw / 2} 454" '
             f'fill="none" stroke="{MUTE}" stroke-width="2.2" stroke-dasharray="6,5" marker-end="url(#a)"/>')
    s.append("</svg>")
    (OUT / "fig1-framework.svg").write_text("\n".join(s), encoding="utf-8")


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
