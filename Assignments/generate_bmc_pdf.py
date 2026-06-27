from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT

OUTPUT = "/Users/jane/projects/ Venture Code/Assignments/BusinessModelCanvas.pdf"

NAVY      = HexColor("#1B2A4A")
ACCENT    = HexColor("#4A7FA5")
LIGHT_GRAY = HexColor("#F4F5F7")
DARK_GRAY = HexColor("#3D4B5C")

WEAK_BG   = HexColor("#FFEBEE")
MOD_BG    = HexColor("#FFF8F2")
STRONG_BG = HexColor("#F0FFF4")

EV_STRONG = "#2E7D32"
EV_MOD    = "#BF5000"
EV_WEAK   = "#C62828"

PAGE_W, PAGE_H = landscape(letter)
MARGIN = 0.42 * inch

CELL_STYLE = ParagraphStyle(
    "cell", fontName="Helvetica", fontSize=7.5, leading=11, textColor=DARK_GRAY
)


def cell(title, ev, bullets, note):
    ev_color = EV_STRONG if ev == "Strong" else (EV_MOD if ev == "Moderate" else EV_WEAK)
    ev_label = (
        "Strong Evidence" if ev == "Strong"
        else ("Moderate Evidence" if ev == "Moderate" else "Weak Evidence  ⚑")
    )
    parts = [
        f'<font name="Helvetica-Bold" size="8" color="#1B2A4A">{title}</font>',
        f'<font name="Helvetica-Bold" size="6.5" color="{ev_color}">{ev_label}</font>',
        "",
    ]
    for b in bullets:
        parts.append(f'<font size="7.5">• {b}</font>')
    parts += ["", f'<font name="Helvetica-Oblique" size="6.5" color="#8896A4">{note}</font>']
    return Paragraph("<br/>".join(parts), CELL_STYLE)


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=landscape(letter),
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.58 * inch, bottomMargin=0.38 * inch,
    )

    COL = (PAGE_W - 2 * MARGIN) / 5   # ~2.03 in per column
    R0  = 2.44 * inch                  # upper two rows
    R1  = 2.44 * inch
    R2  = 2.04 * inch                  # bottom row

    kp = cell(
        "KEY PARTNERSHIPS", "Weak",
        [
            "AI/LLM provider (hard dependency — core infrastructure)",
            "Fashion/styling expertise to calibrate advice quality",
            "Platform APIs: iMessage, WhatsApp, Instagram",
            "Body-type influencers for distribution",
            "No retail/brand partnerships — conflicts with honest positioning",
        ],
        "Not explored in interviews. Structural inference only.",
    )

    ka = cell(
        "KEY ACTIVITIES", "Moderate",
        [
            "Generate honest, proportions-aware styling feedback per session",
            "Build user profile progressively through use",
            "Close the feedback loop: kept item vs. returned",
            "Organic content creation for discovery (Instagram/TikTok)",
        ],
        "Feedback loop closure depends on a user behavior not yet validated.",
    )

    vp = cell(
        "VALUE PROPOSITIONS", "Strong",
        [
            "Honest, specific feedback at the exact moment of decision",
            "Not polite like a friend — not biased like a sales associate",
            "Applies her body knowledge to specific items (translation layer)",
            "Gets smarter and more personal with every session",
            "“Trusted feedback — tell me, yeah, that’s not a good look” — Allison",
            "“Sometimes just trying to be nice” — Mya (names the exact gap)",
        ],
        "Grounded in 5/5 interviews. Strongest block on the canvas.",
    )

    cr = cell(
        "CUSTOMER RELATIONSHIPS", "Moderate",
        [
            "2–3 onboarding questions; value delivered on session 1",
            "Profile deepens progressively through use (not front-loaded)",
            "Freemium: 8 free sessions → $6/month",
            "Switching cost grows as product learns her — retention built in",
        ],
        "8-session freemium threshold is a hypothesis, not customer data.",
    )

    cs = cell(
        "CUSTOMER SEGMENTS", "Moderate",
        [
            "Women 22–35 whose wardrobe formula is missing or broken",
            "Trigger: never built one, or life transition disrupted it",
            "Sends photos, seeks opinions, still returns items",
            "Mya (20s): 40% outfit confidence — target archetype",
            "Aly (20s): 50% outfit confidence — target archetype",
        ],
        "Based on 5 interviews. Age range inferred, not statistically confirmed.",
    )

    kr = cell(
        "KEY RESOURCES", "Moderate",
        [
            "AI model calibrated for proportional fit — not generic styling",
            "User profile data: builds with use (the product moat)",
            "Founder domain knowledge: lived, personal connection to problem",
            "Trust: earned through accuracy session by session",
        ],
        "Photo-based proportional fit assessment is technically unproven.",
    )

    ch = cell(
        "CHANNELS", "Weak",
        [
            "Discovery: Instagram/TikTok organic content (problem she recognizes)",
            "Discovery: body-type influencers who already have her trust",
            "Access: app download or web sign-up (entry point)",
            "Growth: referral — she already sends photos socially; product travels the same path",
        ],
        "No interviewee asked how they discover new tools. All channel logic is inference.",
    )

    cost = cell(
        "COST STRUCTURE", "Weak",
        [
            "AI inference cost per photo per session (scales with usage)",
            "Product development: onboarding flow, profile algorithm, feedback loop",
            "Customer acquisition: organic-first (content, referral) — low CAC at launch",
            "Organic CAC estimate: $10–20 (vs. $100+ for paid acquisition)",
            "Fashion app churn is typically high — unit economics not yet modeled",
        ],
        "No unit economics modeled. Must be run before anything is built.",
    )

    rev = cell(
        "REVENUE STREAMS", "Weak",
        [
            "Free model at launch — lower barrier, faster trust-building",
            "Post-decision ads in non-competing categories (skincare, lifestyle, travel)",
            "Ads architecturally separated from advice engine — integrity preserved",
            "Subscription ($6/mo hypothetical) as optional premium tier once habit is formed",
        ],
        "Ad revenue negligible at early scale. Validate user base before monetizing.",
    )

    E = Paragraph("", CELL_STYLE)   # placeholder for spanned cells

    data = [
        [kp,  ka,  vp,  cr,  cs],
        [E,   kr,  E,   ch,  E ],
        [cost, E,  rev,  E,  E ],
    ]

    t = Table(data, colWidths=[COL] * 5, rowHeights=[R0, R1, R2])

    t.setStyle(TableStyle([
        # spans
        ("SPAN", (0, 0), (0, 1)),   # Key Partnerships
        ("SPAN", (2, 0), (2, 1)),   # Value Propositions
        ("SPAN", (4, 0), (4, 1)),   # Customer Segments
        ("SPAN", (0, 2), (1, 2)),   # Cost Structure
        ("SPAN", (2, 2), (4, 2)),   # Revenue Streams

        # backgrounds
        ("BACKGROUND", (0, 0), (0, 1), WEAK_BG),    # Key Partnerships   — Weak
        ("BACKGROUND", (1, 0), (1, 0), MOD_BG),     # Key Activities     — Moderate
        ("BACKGROUND", (2, 0), (2, 1), STRONG_BG),  # Value Propositions — Strong
        ("BACKGROUND", (3, 0), (3, 0), MOD_BG),     # Customer Rel.      — Moderate
        ("BACKGROUND", (4, 0), (4, 1), MOD_BG),     # Customer Segments  — Moderate
        ("BACKGROUND", (1, 1), (1, 1), MOD_BG),     # Key Resources      — Moderate
        ("BACKGROUND", (3, 1), (3, 1), WEAK_BG),    # Channels           — Weak
        ("BACKGROUND", (0, 2), (1, 2), WEAK_BG),    # Cost Structure     — Weak
        ("BACKGROUND", (2, 2), (4, 2), WEAK_BG),    # Revenue Streams    — Weak

        # grid
        ("GRID", (0, 0), (-1, -1), 1.2, NAVY),

        # padding & alignment
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("TOPPADDING",    (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))

    story = [Spacer(1, 0.05 * inch), t]

    def on_page(canvas, doc):
        canvas.saveState()
        w, h = landscape(letter)

        # Header bar
        canvas.setFillColor(NAVY)
        canvas.rect(0, h - 0.55 * inch, w, 0.55 * inch, fill=1, stroke=0)
        canvas.setFillColor(white)
        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawCentredString(w / 2, h - 0.35 * inch, "BUSINESS MODEL CANVAS")
        canvas.setFont("Helvetica", 8)
        canvas.drawString(MARGIN, h - 0.35 * inch,
                          "BUS 395: Venture Creation with AI  │  Week 4")
        canvas.drawRightString(w - MARGIN, h - 0.35 * inch,
                               "Jane Dias  │  June 2026")

        # Footer legend
        canvas.setFillColor(LIGHT_GRAY)
        canvas.rect(0, 0, w, 0.34 * inch, fill=1, stroke=0)
        y = 0.11 * inch
        x = MARGIN

        canvas.setFillColor(HexColor(EV_STRONG))
        canvas.rect(x, y, 0.08 * inch, 0.09 * inch, fill=1, stroke=0)
        canvas.setFillColor(DARK_GRAY)
        canvas.setFont("Helvetica-Bold", 7)
        canvas.drawString(x + 0.12 * inch, y + 0.01 * inch, "Strong Evidence")

        x2 = x + 1.55 * inch
        canvas.setFillColor(HexColor(EV_MOD))
        canvas.rect(x2, y, 0.08 * inch, 0.09 * inch, fill=1, stroke=0)
        canvas.setFillColor(DARK_GRAY)
        canvas.drawString(x2 + 0.12 * inch, y + 0.01 * inch, "Moderate Evidence")

        x3 = x + 3.3 * inch
        canvas.setFillColor(HexColor(EV_WEAK))
        canvas.rect(x3, y, 0.08 * inch, 0.09 * inch, fill=1, stroke=0)
        canvas.setFillColor(DARK_GRAY)
        canvas.drawString(x3 + 0.12 * inch, y + 0.01 * inch,
                          "Weak Evidence ⚑  (red blocks)  —  Priority to-dos for next interview round")

        canvas.restoreState()

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF saved: {OUTPUT}")


build_pdf()
