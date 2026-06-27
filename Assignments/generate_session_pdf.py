from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.lib import colors

OUTPUT = "/Users/jane/projects/ Venture Code/Assignments/Week4_Session_Analysis.pdf"

# Colors
NAVY = HexColor("#1B2A4A")
ACCENT = HexColor("#4A7FA5")
LIGHT_GRAY = HexColor("#F4F5F7")
MID_GRAY = HexColor("#9AA5B1")
DARK_GRAY = HexColor("#3D4B5C")
CONFIRM_GREEN = HexColor("#E8F5E9")
CHALLENGE_RED = HexColor("#FDE8E8")
FLAG_YELLOW = HexColor("#FFF8E1")
TABLE_HEADER = HexColor("#1B2A4A")
ROW_ALT = HexColor("#F4F5F7")

styles = getSampleStyleSheet()

def make_styles():
    return {
        "cover_title": ParagraphStyle("cover_title",
            fontSize=28, fontName="Helvetica-Bold", textColor=white,
            alignment=TA_CENTER, leading=34, spaceAfter=12),
        "cover_sub": ParagraphStyle("cover_sub",
            fontSize=14, fontName="Helvetica", textColor=HexColor("#CBD5E0"),
            alignment=TA_CENTER, leading=20, spaceAfter=6),
        "cover_meta": ParagraphStyle("cover_meta",
            fontSize=11, fontName="Helvetica", textColor=HexColor("#A0AEC0"),
            alignment=TA_CENTER, leading=16),
        "section_label": ParagraphStyle("section_label",
            fontSize=9, fontName="Helvetica-Bold", textColor=ACCENT,
            spaceAfter=4, spaceBefore=24, leading=12,
            textTransform="uppercase", letterSpacing=1.5),
        "section_title": ParagraphStyle("section_title",
            fontSize=18, fontName="Helvetica-Bold", textColor=NAVY,
            spaceAfter=10, leading=22),
        "subsection": ParagraphStyle("subsection",
            fontSize=13, fontName="Helvetica-Bold", textColor=DARK_GRAY,
            spaceAfter=6, spaceBefore=14, leading=17),
        "body": ParagraphStyle("body",
            fontSize=10, fontName="Helvetica", textColor=DARK_GRAY,
            spaceAfter=7, leading=16, alignment=TA_JUSTIFY),
        "body_left": ParagraphStyle("body_left",
            fontSize=10, fontName="Helvetica", textColor=DARK_GRAY,
            spaceAfter=7, leading=16),
        "bullet": ParagraphStyle("bullet",
            fontSize=10, fontName="Helvetica", textColor=DARK_GRAY,
            spaceAfter=5, leading=15, leftIndent=16, bulletIndent=4),
        "quote": ParagraphStyle("quote",
            fontSize=10, fontName="Helvetica-Oblique", textColor=DARK_GRAY,
            spaceAfter=6, leading=15, leftIndent=20, rightIndent=20),
        "quote_attr": ParagraphStyle("quote_attr",
            fontSize=9, fontName="Helvetica-Bold", textColor=ACCENT,
            spaceAfter=8, leftIndent=20),
        "flag": ParagraphStyle("flag",
            fontSize=9.5, fontName="Helvetica-Oblique", textColor=HexColor("#7B6000"),
            spaceAfter=6, leading=14, leftIndent=12, rightIndent=12),
        "table_header": ParagraphStyle("table_header",
            fontSize=9, fontName="Helvetica-Bold", textColor=white,
            alignment=TA_CENTER, leading=12),
        "table_cell": ParagraphStyle("table_cell",
            fontSize=9, fontName="Helvetica", textColor=DARK_GRAY,
            leading=13, spaceAfter=3),
        "table_cell_bold": ParagraphStyle("table_cell_bold",
            fontSize=9, fontName="Helvetica-Bold", textColor=DARK_GRAY,
            leading=13),
        "verdict_strong": ParagraphStyle("verdict_strong",
            fontSize=10, fontName="Helvetica-Bold", textColor=NAVY,
            spaceAfter=4, leading=14),
        "page_num": ParagraphStyle("page_num",
            fontSize=8, fontName="Helvetica", textColor=MID_GRAY,
            alignment=TA_CENTER),
    }

S = make_styles()

def header_footer(canvas, doc):
    canvas.saveState()
    w, h = letter
    # Header bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 0.45*inch, w, 0.45*inch, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(0.5*inch, h - 0.27*inch, "BUS 395: Venture Creation with AI  |  Week 4 Analysis")
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawRightString(w - 0.5*inch, h - 0.27*inch, "Jane Dias  |  June 2026")
    # Footer
    canvas.setFillColor(LIGHT_GRAY)
    canvas.rect(0, 0, w, 0.4*inch, fill=1, stroke=0)
    canvas.setFillColor(MID_GRAY)
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(w/2, 0.15*inch, f"Page {doc.page}")
    canvas.restoreState()

def cover_page(canvas, doc):
    canvas.saveState()
    w, h = letter
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, h * 0.55, w, 4, fill=1, stroke=0)
    canvas.restoreState()

def divider(story, color=ACCENT):
    story.append(HRFlowable(width="100%", thickness=1.5, color=color, spaceAfter=10, spaceBefore=4))

def flag_box(story, text):
    data = [[Paragraph(f"⚑  {text}", S["flag"])]]
    t = Table(data, colWidths=[6.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), FLAG_YELLOW),
        ("BOX", (0,0), (-1,-1), 0.5, HexColor("#F6C90E")),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))

def quote_block(story, quote_text, attribution, bg=LIGHT_GRAY):
    data = [[
        Paragraph(f'"{quote_text}"', S["quote"]),
    ]]
    t = Table(data, colWidths=[6.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 16),
        ("RIGHTPADDING", (0,0), (-1,-1), 16),
        ("TOPPADDING", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LINEAFTER", (0,0), (0,-1), 3, ACCENT),
    ]))
    story.append(t)
    story.append(Paragraph(f"— {attribution}", S["quote_attr"]))
    story.append(Spacer(1, 4))

def section_heading(story, number, title):
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"SECTION {number}", S["section_label"]))
    story.append(Paragraph(title, S["section_title"]))
    divider(story)

def build_pdf():
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=letter,
        rightMargin=0.65*inch,
        leftMargin=0.65*inch,
        topMargin=0.75*inch,
        bottomMargin=0.65*inch,
    )

    cover_frame = Frame(0, 0, letter[0], letter[1], leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    content_frame = Frame(doc.leftMargin, doc.bottomMargin,
                          doc.width, doc.height - 0.45*inch,
                          leftPadding=0, rightPadding=0)

    doc.addPageTemplates([
        PageTemplate(id="Cover", frames=[cover_frame], onPage=cover_page),
        PageTemplate(id="Content", frames=[content_frame], onPage=header_footer),
    ])

    story = []

    # ── COVER PAGE ──────────────────────────────────────────────────────────
    story.append(Spacer(1, 2.4*inch))
    story.append(Paragraph("Week 4 Analysis", S["cover_sub"]))
    story.append(Spacer(1, 0.15*inch))
    story.append(Paragraph("Customer Discovery\nSession Report", S["cover_title"]))
    story.append(Spacer(1, 0.2*inch))
    story.append(HRFlowable(width="40%", thickness=1.5, color=ACCENT,
                             hAlign="CENTER", spaceAfter=20, spaceBefore=10))
    story.append(Paragraph("BUS 395: Venture Creation with AI", S["cover_sub"]))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Jane Dias  ·  June 15, 2026", S["cover_meta"]))
    story.append(Spacer(1, 0.3*inch))

    toc_items = [
        "1  Cross-Interview Pattern Synthesis",
        "2  Key Quotes — Confirming & Challenging",
        "3  Focus Group Fit Assessment",
        "4  Assumption Scorecard",
        "5  Refined Problem Statement & Target Customer",
        "6  Business Model Canvas",
    ]
    toc_data = [[Paragraph(item, ParagraphStyle("toc", fontSize=10,
                fontName="Helvetica", textColor=HexColor("#CBD5E0"), leading=18))]
                for item in toc_items]
    toc = Table(toc_data, colWidths=[5*inch], hAlign="CENTER")
    toc.setStyle(TableStyle([
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    story.append(toc)
    story.append(PageBreak())

    # Switch to content template
    from reportlab.platypus import NextPageTemplate
    story.append(NextPageTemplate("Content"))
    story.append(PageBreak())

    # ── SECTION 1: PATTERNS ─────────────────────────────────────────────────
    section_heading(story, "1", "Cross-Interview Pattern Synthesis")
    story.append(Paragraph(
        "Analysis across all 5 customer discovery interviews conducted June 7, 2026. "
        "Interviewees: Allison G. (40s), Aly S. (20s), Danai (early 50s), Mya (20s), Meg (30s).",
        S["body"]))
    story.append(Spacer(1, 8))

    patterns = [
        ("Pattern 1", "The Core Question — 5/5 Interviewees",
         "Every interviewee — across different ages, budgets, and even Meg who worked in fashion — "
         "struggled with the same thing. Not \"does it fit?\" but \"does it look right on my specific body?\" "
         "These are different problems, and only the second remains unsolved.",
         []),
        ("Pattern 2", "External Validation is the Universal Workaround — 5/5 Interviewees",
         "All 5 women cope the same way: ask someone they trust. But the system has a reliability "
         "problem. Sales associates are out (biased). Friends are unreliable. Family varies. "
         "There is a gap between needing honest feedback and actually getting it.",
         [
             ("Mya", "Sometimes when you do ask a friend, they're just trying to be nice, and they won't give you real input on the outfit."),
             ("Allison", "It's more reassuring when you ask a friend or family member and they give you the thumbs up — the sales associate is just trying to make a sale."),
         ]),
        ("Pattern 3", "Online Shopping is Where the Problem Compounds — 5/5 Interviewees",
         "Every interviewee had unworn items from online purchases. The cause is almost never wrong "
         "size — it's that things fit but don't look right on their proportions. Returns are the "
         "workaround, not the fix.",
         [
             ("Danai", "It wasn't so much that it was the wrong size. It just didn't fit my body well."),
             ("Meg", "I only found out later that curvy means that the waist is small and the hips are bigger in proportion. But I have the opposite."),
         ]),
        ("Pattern 4", "Proportions Are the Real Pain Point — 4/5 Interviewees",
         "Standard sizing is one-dimensional. Proportions are multidimensional. "
         "Danai (small waist, bigger hips/thighs), Meg (narrow hips, thicker waist), "
         "Aly (pale complexion — colors wash her out), Allison (tall). Nobody taught these "
         "women the rules — they figured it out through years of mistakes, or haven't yet.",
         [
             ("Danai", "I have a smaller waist, but bigger hips and thighs. A lot of pants and shorts fit me kind of weird. Usually when I find a short that fits me great, I'll just buy it in every color."),
         ]),
        ("Pattern 5", "Style Knowledge Takes Decades to Develop — All Interviews",
         "Allison's arc is the clearest. Younger women (Aly, Mya) are clearly still mid-journey. "
         "The pattern: this is a skill that takes decades to develop, and women are building it "
         "alone through costly trial and error.",
         [
             ("Allison", "It really took years for me to develop my ability to pick out clothes... I didn't have a personal stylist... it was really a lot of trial and error, and I've made a lot of mistakes."),
             ("Danai", "I try to find an influencer that has my body type, and then I follow them — she's figured out what looks good on our body type. Because I'm not good at it."),
         ]),
        ("Pattern 6", "Low Confidence Has Real Behavioral Stakes — 5/5 Interviewees",
         "This isn't aesthetic inconvenience — it affects what women do and where they go.",
         [
             ("Mya", "If I'm not wearing a good outfit, I don't want to be so seen in public."),
             ("Aly", "I would feel fine if I took a picture in this outfit. I want to go out and be seen."),
             ("Allison", "I do not want to leave the house not feeling confident or comfortable."),
         ]),
        ("Pattern 7", "The Photo/Video Workaround Signals Product Readiness",
         "Multiple women already take photos or spin-videos of themselves in clothes to self-assess. "
         "Mya takes videos and does a spin. Danai takes photos and sends them. Allison sends photos "
         "to friends. This behavior is already normalized — a photo-based feedback tool would feel "
         "natural, not foreign.",
         []),
    ]

    for tag, title, body_text, quotes in patterns:
        block = []
        block.append(Paragraph(tag, S["section_label"]))
        block.append(Paragraph(title, S["subsection"]))
        block.append(Paragraph(body_text, S["body"]))
        for attr, q in quotes:
            quote_block(block, q, attr)
        story.append(KeepTogether(block))
        story.append(Spacer(1, 6))

    story.append(Spacer(1, 10))
    # Through-line callout
    through_data = [[Paragraph(
        "Through-line: Women fundamentally cannot answer \"does this actually look good on me — "
        "on my specific proportions, coloring, and style?\" reliably or independently. Every coping "
        "mechanism they've developed is a partial substitute for personalized, honest, knowledgeable "
        "feedback they don't have access to.",
        ParagraphStyle("through", fontSize=10.5, fontName="Helvetica-BoldOblique",
                       textColor=NAVY, leading=17, alignment=TA_JUSTIFY))]]
    t = Table(through_data, colWidths=[6.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#EBF2FA")),
        ("BOX", (0,0), (-1,-1), 1.5, ACCENT),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 12), ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ]))
    story.append(t)

    story.append(PageBreak())

    # ── SECTION 2: KEY QUOTES ────────────────────────────────────────────────
    section_heading(story, "2", "Key Quotes — Confirming & Challenging")
    story.append(Paragraph(
        "8 quotes selected from verbatim transcripts. Labeled by whether they confirm or challenge "
        "the core venture idea: an AI tool providing honest, personalized, proportions-aware styling "
        "feedback at the moment of decision.", S["body"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("CONFIRMING — Support the problem and solution direction", S["section_label"]))
    story.append(Spacer(1, 4))

    confirming = [
        ("Allison — p.4",
         "It really took years for me to develop my ability to pick out clothes and know if I was going "
         "to wear them... I didn't have a personal stylist, I didn't have somebody like, helping me "
         "figure out outfits, which would have been great. But it was really a lot of trial and error, "
         "and I've made a lot of mistakes.",
         "Confirms problem: style knowledge has no accessible shortcut. The solution she wished she had "
         "is exactly the product being considered."),
        ("Mya — p.16",
         "I kind of do need people to tell me what it looks like, because I can't see. I can't get a "
         "360 of myself sometimes.",
         "Confirms the self-assessment gap. Already pre-adapted to using external input at the mirror."),
        ("Mya — p.18",
         "Sometimes when you do ask a friend, they're just trying to be nice, and they won't give you "
         "real input on the outfit. Sometimes I do feel like people are just trying to be nice.",
         "Names the honesty gap directly — the exact problem an AI without social incentives could solve."),
        ("Allison — p.4",
         "Having somebody who is trusted give me some feedback on the outfit... tell me, like, yeah, "
         "that is not a good look for you. If somebody who I trusted really would give me that kind "
         "of feedback, that would be helpful.",
         "Direct articulation of the product's core value proposition: trusted, honest, in-the-moment feedback."),
    ]

    for attr, q, note in confirming:
        block = []
        data = [[Paragraph(f'"{q}"', S["quote"])]]
        t = Table(data, colWidths=[6.5*inch])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), CONFIRM_GREEN),
            ("LEFTPADDING", (0,0), (-1,-1), 16), ("RIGHTPADDING", (0,0), (-1,-1), 16),
            ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("LINEAFTER", (0,0), (0,-1), 3, HexColor("#43A047")),
        ]))
        block.append(t)
        block.append(Paragraph(f"— {attr}", S["quote_attr"]))
        block.append(Paragraph(f"→ {note}", ParagraphStyle("note_green",
            fontSize=9, fontName="Helvetica", textColor=HexColor("#2E7D32"),
            leftIndent=20, spaceAfter=12, leading=13)))
        story.append(KeepTogether(block))

    story.append(Spacer(1, 8))
    story.append(Paragraph("CHALLENGING — Complicate or challenge the venture idea", S["section_label"]))
    story.append(Spacer(1, 4))

    challenging = [
        ("Meg — p.23",
         "I very rarely feel confident in what I'm wearing, but it's mostly a body image issue.",
         "The sharpest challenge. Meg's problem is not lack of style information — it's deeper. "
         "Better outfit feedback won't fix body image. This represents a customer segment that "
         "could try the product and remain unsatisfied."),
        ("Meg — p.22",
         "Until you actually start wearing the item out of it, you almost don't know if you like it. "
         "You think you do, but something about it can bug you when you actually put it on and wear it out.",
         "Challenges any point-of-purchase solution. The real verdict comes after wearing — "
         "not in the dressing room. Even perfect in-the-moment feedback has limits."),
        ("Danai — p.13",
         "I think I just go off my own gut feeling... That's more about how I feel about stuff, "
         "more than the fit. Because I pretty much have figured out the fit, right?",
         "Danai's problem is age-appropriateness and identity expression — not fit or appearance. "
         "At least one interviewee's core need is outside the product's current scope."),
        ("Allison — p.2",
         "I understand the sales associate is just trying to make a sale... it's more reassuring "
         "when you ask a friend or family member and they give you the thumbs up.",
         "Trust comes from relationship, not expertise. An AI giving style feedback could be "
         "dismissed the same way she dismisses sales associates — as having an agenda. "
         "Trust must be earned structurally."),
    ]

    for attr, q, note in challenging:
        block = []
        data = [[Paragraph(f'"{q}"', S["quote"])]]
        t = Table(data, colWidths=[6.5*inch])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), CHALLENGE_RED),
            ("LEFTPADDING", (0,0), (-1,-1), 16), ("RIGHTPADDING", (0,0), (-1,-1), 16),
            ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("LINEAFTER", (0,0), (0,-1), 3, HexColor("#E53935")),
        ]))
        block.append(t)
        block.append(Paragraph(f"— {attr}", S["quote_attr"]))
        block.append(Paragraph(f"→ {note}", ParagraphStyle("note_red",
            fontSize=9, fontName="Helvetica", textColor=HexColor("#B71C1C"),
            leftIndent=20, spaceAfter=12, leading=13)))
        story.append(KeepTogether(block))

    story.append(PageBreak())

    # ── SECTION 3: FOCUS GROUP FIT ───────────────────────────────────────────
    section_heading(story, "3", "Focus Group Fit Assessment")
    story.append(Paragraph(
        "Evaluation of which interviewees should be invited to the next-stage focus group, "
        "based on acuity of pain, motivation to try a new solution, and alignment with "
        "the target customer profile.", S["body"]))
    story.append(Spacer(1, 10))

    focus_data = [
        [Paragraph("Interviewee", S["table_header"]),
         Paragraph("Recommendation", S["table_header"]),
         Paragraph("Rationale", S["table_header"])],
        [Paragraph("Mya (20s)", S["table_cell_bold"]),
         Paragraph("✓ Invite", ParagraphStyle("green_bold", fontSize=9,
             fontName="Helvetica-Bold", textColor=HexColor("#2E7D32"))),
         Paragraph("Highest acute pain (40% confidence). Already uses photo/video workarounds. "
                   "Named the honesty gap explicitly. Ended the interview: \"I'm excited.\"", S["table_cell"])],
        [Paragraph("Aly (20s)", S["table_cell_bold"]),
         Paragraph("✓ Invite", ParagraphStyle("green_bold", fontSize=9,
             fontName="Helvetica-Bold", textColor=HexColor("#2E7D32"))),
         Paragraph("50% confidence, still mid-journey, no satisfying workaround. "
                   "Clear style knowledge gaps (silhouettes, colors). Strong early adopter profile.", S["table_cell"])],
        [Paragraph("Meg (30s)", S["table_cell_bold"]),
         Paragraph("⚑ Conditional", ParagraphStyle("yellow_bold", fontSize=9,
             fontName="Helvetica-Bold", textColor=HexColor("#7B6000"))),
         Paragraph("Body image is the stated root cause — a styling tool may not satisfy her. "
                   "Valuable for \"hard case\" testing but could dampen group energy. "
                   "Useful in a separate session.", S["table_cell"])],
        [Paragraph("Allison (40s)", S["table_cell_bold"]),
         Paragraph("✗ Deprioritize", ParagraphStyle("red_bold", fontSize=9,
             fontName="Helvetica-Bold", textColor=HexColor("#B71C1C"))),
         Paragraph("90% confident — has largely solved the problem through decades of experience. "
                   "Low urgency. Risk of anchoring the group with \"what I learned over 20 years\" "
                   "rather than \"what I need now.\"", S["table_cell"])],
        [Paragraph("Danai (50s)", S["table_cell_bold"]),
         Paragraph("✗ Deprioritize", ParagraphStyle("red_bold", fontSize=9,
             fontName="Helvetica-Bold", textColor=HexColor("#B71C1C"))),
         Paragraph("Already has a free, satisfying workaround (body-type influencers). "
                   "Very budget-conscious. Her core remaining challenge is identity/age-appropriateness, "
                   "outside the product's current scope.", S["table_cell"])],
    ]

    t = Table(focus_data, colWidths=[1.3*inch, 1.1*inch, 4.1*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER),
        ("BACKGROUND", (0,2), (-1,2), ROW_ALT),
        ("BACKGROUND", (0,4), (-1,4), ROW_ALT),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#D1D5DB")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, ROW_ALT]),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Secondary signal: Meg's experience shopping with her daughter Ren (a whole mall trip yielding "
        "nothing due to proportion issues) suggests a gifting or co-shopping entry point that was not "
        "probed in interviews. Worth exploring in Week 5.", S["body_left"]))

    story.append(PageBreak())

    # ── SECTION 4: ASSUMPTION SCORECARD ──────────────────────────────────────
    section_heading(story, "4", "Assumption Scorecard")
    story.append(Paragraph(
        "Five pre-interview assumptions tested against transcript evidence. Includes "
        "confirmation bias flags where the data is being read generously.", S["body"]))
    story.append(Spacer(1, 10))

    assumptions = [
        {
            "num": "1",
            "title": "Women across ages 20–60 experience this issue",
            "verdict": "PARTIALLY CONFIRMED",
            "verdict_color": HexColor("#E65100"),
            "for_points": [
                "All 5 women across 20s, 30s, 40s, and 50s named the core problem",
                "Age range confirmed: the problem exists across the full spectrum",
            ],
            "against_points": [
                "Intensity drops sharply with age — Allison (40s) is 90% confident; Mya (20s) is 40%",
                "Allison's confidence was built over decades — suggests the problem naturally resolves",
                "Danai (50s): \"I pretty much have figured out the fit, right?\" — low acute pain",
            ],
            "flag": "You have 5 data points and all 5 confirmed the problem — easy to read as universal. "
                    "But older women are aging OUT of the problem, not into it. Real urgency skews 20s–30s, "
                    "with a secondary trigger at body-change moments (pregnancy, aging) regardless of age.",
        },
        {
            "num": "2",
            "title": "Women with limited budgets have less room for trial and error",
            "verdict": "WEAKLY SUPPORTED",
            "verdict_color": HexColor("#B71C1C"),
            "for_points": [
                "Aly: stuck with non-returnable Old Navy sale items that didn't fit",
                "Mya: bought a Target tube top without trying it on, couldn't return it, never wore it",
            ],
            "against_points": [
                "Allison (larger budget) also has items with tags in her closet — missed return windows online",
                "Danai (very budget-conscious) built a MORE disciplined return system: \"I'd rather get my money back\"",
                "The mechanism is non-returnable sale purchases, not budget level per se",
            ],
            "flag": "The stuck-purchase stories from Aly and Mya are compelling but the common thread is "
                    "non-returnable online sale items — which trap any income level. The assumption implies "
                    "budget worsens the problem; the evidence shows it changes the problem, not necessarily worsens it.",
        },
        {
            "num": "3",
            "title": "Women don't know their body type or measurements",
            "verdict": "LARGELY CONTRADICTED",
            "verdict_color": HexColor("#B71C1C"),
            "for_points": [
                "Meg bought \"curvy\" jeans without understanding the proportional meaning",
                "Aly struggles to identify which silhouettes work for her body",
            ],
            "against_points": [
                "Danai: \"I have a smaller waist, but bigger hips and thighs\" — precise body knowledge",
                "Meg (same interview): \"I got more narrow hips and a thicker waist\" — knows her body well",
                "Allison built her formula around knowing she's tall",
                "Danai: \"I pretty much have figured out the fit, right?\"",
            ],
            "flag": "This is the assumption most clearly at odds with the transcripts. Women know their bodies. "
                    "The gap is between their body knowledge and the clothing industry's labeling system. "
                    "Meg's jeans failure was an industry vocabulary problem, not a self-knowledge problem. "
                    "Building a product that teaches women their body type solves a problem they don't have.",
        },
        {
            "num": "4",
            "title": "A personal stylist or large budget solves the problem",
            "verdict": "WEAKLY SUPPORTED",
            "verdict_color": HexColor("#E65100"),
            "for_points": [
                "Allison (larger budget) is the most confident at 90%",
                "Allison explicitly said she wished she'd had a personal stylist",
            ],
            "against_points": [
                "Allison's confidence came from decades of trial and error — not from a stylist or budget",
                "Meg worked in fashion (equivalent expertise) and \"very rarely\" feels confident",
                "Allison still has unworn items from online purchases despite larger budget",
                "No interviewee had actually used a personal stylist — assumption entirely untested",
            ],
            "flag": "You may want this confirmed because it validates the AI-as-stylist concept. "
                    "But the evidence shows fashion expertise (Meg) and larger budget (Allison still "
                    "has waste) don't fully solve it. What solved it for Allison was time — 20 years. "
                    "Whether a stylist would have accelerated that remains unknown from this data.",
        },
        {
            "num": "5",
            "title": "Seeking a second opinion signals self-doubt",
            "verdict": "CONTRADICTED",
            "verdict_color": HexColor("#B71C1C"),
            "for_points": [
                "Mya and Aly (least confident) do rely most heavily on external validation",
                "Some correlation between lower confidence and more validation-seeking",
            ],
            "against_points": [
                "Allison — 90% confident — still texts photos to friends/family when uncertain",
                "Mya described shopping as \"social\" — asking opinions is part of the enjoyment, not distress",
                "Danai treats it as a decision rule: \"if they are hesitant in any way, I just won't get it\" — a system, not insecurity",
            ],
            "flag": "This assumption matters for positioning. If you believe it, you'd frame the product "
                    "as targeting \"insecure women who need reassurance.\" The data shows a different frame: "
                    "seeking a second opinion is rational information-gathering that confident AND unconfident "
                    "women both do. The problem is that feedback is unreliable — not that women are insecure.",
        },
    ]

    verdict_colors = {
        "PARTIALLY CONFIRMED": HexColor("#E65100"),
        "WEAKLY SUPPORTED": HexColor("#B71C1C"),
        "LARGELY CONTRADICTED": HexColor("#B71C1C"),
        "CONTRADICTED": HexColor("#B71C1C"),
        "CONFIRMED": HexColor("#2E7D32"),
    }

    for a in assumptions:
        block = []
        # Header row
        header_data = [[
            Paragraph(f"Assumption {a['num']}", ParagraphStyle("a_num",
                fontSize=9, fontName="Helvetica-Bold", textColor=white)),
            Paragraph(a["verdict"], ParagraphStyle("a_verdict",
                fontSize=9, fontName="Helvetica-Bold", textColor=white, alignment=TA_LEFT)),
        ]]
        h = Table(header_data, colWidths=[1.2*inch, 5.3*inch])
        h.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,0), NAVY),
            ("BACKGROUND", (1,0), (1,0), a["verdict_color"]),
            ("LEFTPADDING", (0,0), (-1,-1), 8),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ]))
        block.append(h)
        block.append(Paragraph(a["title"], ParagraphStyle("a_title",
            fontSize=11, fontName="Helvetica-Bold", textColor=NAVY,
            spaceBefore=8, spaceAfter=8, leading=15)))

        # For / Against table
        for_paras = [Paragraph(f"• {p}", S["bullet"]) for p in a["for_points"]]
        against_paras = [Paragraph(f"• {p}", S["bullet"]) for p in a["against_points"]]

        fa_header = [
            [Paragraph("Evidence For", ParagraphStyle("fa_h", fontSize=9,
                fontName="Helvetica-Bold", textColor=HexColor("#2E7D32"))),
             Paragraph("Evidence Against", ParagraphStyle("fa_h", fontSize=9,
                fontName="Helvetica-Bold", textColor=HexColor("#B71C1C")))],
        ]
        max_rows = max(len(for_paras), len(against_paras))
        for i in range(max_rows):
            row = [
                for_paras[i] if i < len(for_paras) else Paragraph("", S["bullet"]),
                against_paras[i] if i < len(against_paras) else Paragraph("", S["bullet"]),
            ]
            fa_header.append(row)

        fa_t = Table(fa_header, colWidths=[3.25*inch, 3.25*inch])
        fa_t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,0), CONFIRM_GREEN),
            ("BACKGROUND", (1,0), (1,0), CHALLENGE_RED),
            ("BOX", (0,0), (-1,-1), 0.5, HexColor("#D1D5DB")),
            ("LINEAFTER", (0,0), (0,-1), 0.5, HexColor("#D1D5DB")),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ]))
        block.append(fa_t)
        block.append(Spacer(1, 6))
        flag_box(block, a["flag"])
        block.append(Spacer(1, 10))
        story.append(KeepTogether(block))

    # Summary table
    story.append(Spacer(1, 6))
    story.append(Paragraph("SUMMARY", S["section_label"]))
    sum_data = [
        [Paragraph("Assumption", S["table_header"]), Paragraph("Verdict", S["table_header"])],
        [Paragraph("1. Age-universal problem", S["table_cell"]),
         Paragraph("Partially confirmed — intensity varies; urgency skews younger", S["table_cell"])],
        [Paragraph("2. Budget = higher cost of mistakes", S["table_cell"]),
         Paragraph("Weakly supported — mechanism is sale/return policy, not budget", S["table_cell"])],
        [Paragraph("3. Women don't know their body type", S["table_cell"]),
         Paragraph("Largely contradicted — they know their bodies; not clothing systems", S["table_cell"])],
        [Paragraph("4. Personal stylist / large budget solves it", S["table_cell"]),
         Paragraph("Weakly supported — Meg (fashion background) still rarely confident", S["table_cell"])],
        [Paragraph("5. Second opinions signal self-doubt", S["table_cell"]),
         Paragraph("Contradicted — rational behavior across ALL confidence levels", S["table_cell"])],
    ]
    sum_t = Table(sum_data, colWidths=[2.8*inch, 3.7*inch])
    sum_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, ROW_ALT]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#D1D5DB")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    story.append(sum_t)

    story.append(PageBreak())

    # ── SECTION 5: PROBLEM STATEMENT & TARGET CUSTOMER ───────────────────────
    section_heading(story, "5", "Refined Problem Statement & Target Customer")
    story.append(Spacer(1, 4))

    story.append(Paragraph("Refined Problem Statement", S["subsection"]))
    ps_data = [[Paragraph(
        "Women have detailed knowledge of their own bodies, but the clothing industry speaks a "
        "different language — one built around generic sizes and opaque cut labels that don't "
        "account for individual proportions. Without a way to translate their body knowledge into "
        "clothing decisions, women rely on trial and error, unreliable feedback from people who are "
        "\"just trying to be nice,\" and years of expensive mistakes before developing a formula that works.",
        ParagraphStyle("ps", fontSize=11, fontName="Helvetica-BoldOblique",
                       textColor=NAVY, leading=18, alignment=TA_JUSTIFY))]]
    ps_t = Table(ps_data, colWidths=[6.5*inch])
    ps_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#EBF2FA")),
        ("BOX", (0,0), (-1,-1), 2, ACCENT),
        ("LEFTPADDING", (0,0), (-1,-1), 16), ("RIGHTPADDING", (0,0), (-1,-1), 16),
        ("TOPPADDING", (0,0), (-1,-1), 14), ("BOTTOMPADDING", (0,0), (-1,-1), 14),
    ]))
    story.append(ps_t)
    story.append(Spacer(1, 10))

    story.append(Paragraph(
        "This framing locates the problem in the system, not in the woman. It implies the solution "
        "is a translation layer — not a confidence tool, not a shopping platform, not a closet organizer.", S["body"]))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Target Customer", S["subsection"]))
    story.append(Paragraph(
        "Primary: Women in their 20s–30s who are actively mid-journey in developing their style formula.", S["body_left"]))

    tc_items = [
        ("Defining characteristic", "They know their body has proportional quirks — but can't translate that knowledge into reliable purchase decisions"),
        ("Shopping behavior", "Shop both online and in-store; already take photos or videos in dressing rooms as a workaround"),
        ("Pain acuity", "Feel genuinely confident in outfits 40–50% of the time (Mya: 40%, Aly: 50%)"),
        ("Motivation", "Not yet satisfied — no stable formula, no free workaround that fully works"),
        ("Body change trigger", "Post-pregnancy, significant weight change, or aging can re-activate the problem regardless of age"),
        ("Secondary segment", "Mothers shopping with daughters facing proportion-fit challenges (Meg + Ren at American Eagle)"),
    ]

    tc_data = [[Paragraph(k, S["table_cell_bold"]), Paragraph(v, S["table_cell"])] for k, v in tc_items]
    tc_t = Table(tc_data, colWidths=[1.8*inch, 4.7*inch])
    tc_t.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [white, ROW_ALT]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#D1D5DB")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    story.append(tc_t)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Who to Deprioritize", S["subsection"]))
    deprio = [
        ("Allison (40s+, formula developed)", "Low urgency — has built her own system over decades. Valuable for aspirational positioning, not core product design."),
        ("Danai (50s, influencer workaround)", "Already has a free, working solution. Budget-conscious. Her remaining challenge (age-appropriateness/identity) is outside current scope."),
        ("Meg (body image as root cause)", "If the root problem is body image, the product may not satisfy her. Risk of early churn that damages product reputation."),
    ]
    for who, why in deprio:
        story.append(Paragraph(f"• {who}: {why}", S["bullet"]))

    story.append(Spacer(1, 10))
    flag_box(story, "Critical open question: The customers with the sharpest pain (Aly, Mya) have limited budgets. "
             "The most willing-to-pay customer is probably Allison — who doesn't feel the problem acutely anymore. "
             "The target customer and the paying customer may not be the same person. This is the venture's most "
             "important unresolved tension.")

    story.append(PageBreak())

    # ── SECTION 6: BUSINESS MODEL CANVAS ────────────────────────────────────
    section_heading(story, "6", "Business Model Canvas")
    story.append(Paragraph(
        "All 9 blocks. Evidence grounded in interview transcripts and Week 3 competitive analysis. "
        "Evidence strength rated per block. Flags indicate where assumptions are untested.", S["body"]))
    story.append(Spacer(1, 8))

    STRONG = HexColor("#2E7D32")
    MODERATE = HexColor("#E65100")
    WEAK_C = HexColor("#B71C1C")

    def strength_badge(level):
        color = STRONG if level == "Strong" else (MODERATE if level == "Moderate" else WEAK_C)
        return Paragraph(f"Evidence: {level}", ParagraphStyle("badge",
            fontSize=8, fontName="Helvetica-Bold", textColor=color))

    bmc_blocks = [
        {
            "num": "1",
            "title": "Customer Segments",
            "strength": "Moderate",
            "best_answer": "Women in their 20s–30s, mid-journey in developing a style formula. "
                           "Shop online and in-store. Have at least one proportional body challenge. "
                           "Already using photo/video workarounds. Feel the problem acutely (40–50% outfit confidence).",
            "evidence": [
                "Mya (20s): 40% confident, FaceTimes mom before going out, takes spin videos in dressing rooms",
                "Aly (20s): 50% confident, still picking unflattering colors despite knowing better",
                "Meg (30s): body changed through pregnancy/aging — the trigger, not just the age",
                "Secondary: mothers + daughters (Meg + Ren, a whole mall trip finding nothing)",
            ],
            "flag": "5 interviews is not enough to define a segment statistically. The 20–60 age range "
                    "from the competitive analysis is likely too broad — urgency skews 20s–30s.",
        },
        {
            "num": "2",
            "title": "Value Propositions",
            "strength": "Strong",
            "best_answer": "Honest, proportions-aware styling feedback at the moment of decision. "
                           "Not post-purchase. Not generic. Not filtered through politeness. Gets more "
                           "personal with every session. Teaches the translation layer between body "
                           "knowledge and clothing systems. Low effort — photo is the only input.",
            "evidence": [
                "Allison: \"having somebody who is trusted give me some feedback... tell me, yeah, that is not a good look for you\"",
                "Danai: follows influencers with her body type because \"I'm not good at it\" — wants the output of that knowledge applied to herself",
                "Meg: \"maybe if somebody who was skilled in knowing what looks good on certain body types\"",
                "Competitive gap: StyleDNA is \"stronger on color than on nuanced body-type fit diagnostics\"",
                "All 5 already take photos — the input behavior requires no new habit",
            ],
            "flag": "The VP assumes the AI can deliver non-generic advice. Generic advice is the #1 "
                    "complaint against every existing AI styling product. This is both the core claim "
                    "and the hardest product problem. Must be validated before anything else matters.",
        },
        {
            "num": "3",
            "title": "Channels",
            "strength": "Weak",
            "best_answer": "Mobile app, photo-based interaction. Discovery likely through body-type "
                           "influencers and social media (Instagram, TikTok).",
            "evidence": [
                "All 5 interviewees naturally take or send photos — photo input requires no behavior change",
                "Danai's most effective workaround is following body-type influencers — these are natural distribution partners",
            ],
            "flag": "No interviewee was asked how they discover apps, what platforms they use, or how "
                    "they'd want to be introduced to this tool. Channels are entirely logical inference. "
                    "This block needs a dedicated discovery round.",
        },
        {
            "num": "4",
            "title": "Customer Relationships",
            "strength": "Moderate",
            "best_answer": "Freemium trust-builder: free for the first 8 sessions so the user "
                           "experiences value before paying. The relationship must feel like a trusted "
                           "friend who knows your body — not a service trying to sell you more clothes.",
            "evidence": [
                "Trust is the consistent driver across all 5 interviews: dismissed sales associates (Allison), dismissed polite friends (Mya)",
                "Alle App failure: chatbot oriented toward shopping (not learning) failed due to wrong relationship model",
                "Freemium rationale: user experiences the loop working before being asked to pay",
            ],
            "flag": "The 8-session threshold is a hypothesis from Remix 1, not from customer data. "
                    "\"Validate first: at which session does advice start feeling personal?\" — "
                    "this is the most important thing to test before building.",
        },
        {
            "num": "5",
            "title": "Revenue Streams",
            "strength": "Weak",
            "best_answer": "$6/month subscription after free onboarding period. Potential secondary "
                           "stream: anonymized aggregate body-proportion data sold to clothing brands (B2B).",
            "evidence": [
                "Competitive benchmarks: Whering $7.99/mo, Indyx $9–$12.99/mo — $6 positions below both",
                "Stitch Fix charges $20 per styling session — $6/mo is less than one session fee",
                "Personal stylists: $150+/hour — establishes the ceiling on perceived value",
            ],
            "flag": "BIGGEST GAP IN THE CANVAS. Not a single interviewee was asked about willingness "
                    "to pay, current spending on clothing tools, or acceptable price points. Every number "
                    "here is competitive inference, not customer data. Run a willingness-to-pay test "
                    "before Week 5. Also: AI inference costs at $6/mo with unlimited sessions may be "
                    "margin-negative until significant scale.",
        },
        {
            "num": "6",
            "title": "Key Resources",
            "strength": "Moderate",
            "best_answer": "A proportions-aware AI model (not just color/style typing); a low-friction "
                           "photo intake system; proprietary body-to-clothing translation knowledge base "
                           "that compounds in value with every user.",
            "evidence": [
                "StyleDNA's competitive gap: \"stronger on color than nuanced body-type fit diagnostics\" — proportional fit logic is the scarce resource",
                "Closet-logging apps (Indyx, Acloset, Whering) fail because they require too much user input — AI must do the heavy lifting from a photo",
                "Meg's jeans failure: the translation layer (what \"curvy\" means in proportional terms) is exactly what's missing",
            ],
            "flag": "Computer vision good enough to assess proportional fit from a mirror photo is "
                    "technically non-trivial. User trust in AI's read of a photo (vs. a human's) is also "
                    "unproven. Both capability and trust are unvalidated resources.",
        },
        {
            "num": "7",
            "title": "Key Activities",
            "strength": "Moderate",
            "best_answer": "Build the feedback loop (photo in → proportions-aware assessment → gets more "
                           "personal over time). Keep onboarding friction below the threshold that killed "
                           "competitors. Validate the session-8 conversion trigger.",
            "evidence": [
                "Competitive failure pattern: \"asked users to do too much work — uploading closets, waiting on stylists, mailed rentals\"",
                "All 5 interviewees already take photos in dressing rooms — the core activity maps to existing behavior",
                "Alle App: chatbot without body-type intelligence failed — activity must include proportion diagnosis, not just style chat",
            ],
            "flag": "The session-8 conversion trigger is the most important product design question and "
                    "is completely unvalidated. This should be a Week 5 experiment.",
        },
        {
            "num": "8",
            "title": "Key Partnerships",
            "strength": "Weak",
            "best_answer": "Body-type influencers (distribution). Potentially clothing brands for "
                           "proportional cut data to power the translation layer.",
            "evidence": [
                "Danai's most effective workaround is following body-type influencers — built-in trust with target customer",
                "Meg's \"curvy\" jeans failure: clothing brands hold the cut/proportion data that could prevent this mistake",
            ],
            "flag": "Retail/brand partnerships create a direct conflict with the honest-and-unbiased "
                    "positioning that is the core differentiation. If brands are partners, users may rightly "
                    "wonder if advice steers toward partner inventory. Influencer partnerships are cleaner — "
                    "extend reach without compromising the feedback engine.",
        },
        {
            "num": "9",
            "title": "Cost Structure",
            "strength": "Weak",
            "best_answer": "AI infrastructure (inference costs per photo), initial style knowledge curation "
                           "(human experts needed to seed the model before data accumulates), customer acquisition.",
            "evidence": [
                "Competitive context: fashion/beauty app space has high CAC due to crowded field",
                "Cold-start problem: early cohort gets weaker AI advice (before scale) — may need human styling to bridge gap",
                "Alle App: $3M seed funding was insufficient — AI fashion apps have historically struggled with unit economics",
            ],
            "flag": "No unit economics modeled. At $6/month, need ~17 months to recover a $100 CAC at "
                    "zero churn. Fashion app churn is typically high. This math must be run before Week 5. "
                    "The B2B data play (selling anonymized proportion data to brands) may be more sustainable "
                    "than consumer subscription at this price point.",
        },
    ]

    for block_data in bmc_blocks:
        block = []
        # Block header
        hdr = [[
            Paragraph(f"Block {block_data['num']}  ·  {block_data['title']}", ParagraphStyle("bh",
                fontSize=12, fontName="Helvetica-Bold", textColor=white)),
            strength_badge(block_data["strength"]),
        ]]
        h = Table(hdr, colWidths=[5*inch, 1.5*inch])
        h.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), NAVY),
            ("LEFTPADDING", (0,0), (-1,-1), 10), ("RIGHTPADDING", (0,0), (-1,-1), 10),
            ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ]))
        block.append(h)

        # Best answer
        block.append(Spacer(1, 6))
        block.append(Paragraph("Current Best Answer", ParagraphStyle("ca_label",
            fontSize=8.5, fontName="Helvetica-Bold", textColor=ACCENT, spaceAfter=3)))
        block.append(Paragraph(block_data["best_answer"], S["body"]))

        # Evidence
        block.append(Paragraph("Evidence", ParagraphStyle("ev_label",
            fontSize=8.5, fontName="Helvetica-Bold", textColor=DARK_GRAY, spaceAfter=3)))
        for e in block_data["evidence"]:
            block.append(Paragraph(f"• {e}", S["bullet"]))

        block.append(Spacer(1, 4))
        flag_box(block, block_data["flag"])
        block.append(Spacer(1, 12))
        story.append(KeepTogether(block))

    # BMC Summary
    story.append(Spacer(1, 6))
    story.append(Paragraph("EVIDENCE STRENGTH SUMMARY", S["section_label"]))
    bmc_sum = [
        [Paragraph("Block", S["table_header"]),
         Paragraph("Evidence", S["table_header"]),
         Paragraph("Biggest Open Question", S["table_header"])],
        [Paragraph("1. Customer Segments", S["table_cell"]),
         Paragraph("Moderate", ParagraphStyle("m", fontSize=9, fontName="Helvetica-Bold", textColor=MODERATE)),
         Paragraph("Is 20s–30s the right cut, or is it body-change life stage?", S["table_cell"])],
        [Paragraph("2. Value Propositions", S["table_cell"]),
         Paragraph("Strong", ParagraphStyle("s", fontSize=9, fontName="Helvetica-Bold", textColor=STRONG)),
         Paragraph("Can the AI actually deliver non-generic advice?", S["table_cell"])],
        [Paragraph("3. Channels", S["table_cell"]),
         Paragraph("Weak", ParagraphStyle("w", fontSize=9, fontName="Helvetica-Bold", textColor=WEAK_C)),
         Paragraph("How do they find you? Not asked in interviews.", S["table_cell"])],
        [Paragraph("4. Customer Relationships", S["table_cell"]),
         Paragraph("Moderate", ParagraphStyle("m2", fontSize=9, fontName="Helvetica-Bold", textColor=MODERATE)),
         Paragraph("When does advice feel personal enough to pay?", S["table_cell"])],
        [Paragraph("5. Revenue Streams", S["table_cell"]),
         Paragraph("Weak ⚑", ParagraphStyle("w2", fontSize=9, fontName="Helvetica-Bold", textColor=WEAK_C)),
         Paragraph("Willingness to pay was NEVER tested — biggest gap.", S["table_cell"])],
        [Paragraph("6. Key Resources", S["table_cell"]),
         Paragraph("Moderate", ParagraphStyle("m3", fontSize=9, fontName="Helvetica-Bold", textColor=MODERATE)),
         Paragraph("Can photo-based AI assess proportional fit reliably?", S["table_cell"])],
        [Paragraph("7. Key Activities", S["table_cell"]),
         Paragraph("Moderate", ParagraphStyle("m4", fontSize=9, fontName="Helvetica-Bold", textColor=MODERATE)),
         Paragraph("Session-8 threshold is a hypothesis — validate this first.", S["table_cell"])],
        [Paragraph("8. Key Partnerships", S["table_cell"]),
         Paragraph("Weak", ParagraphStyle("w3", fontSize=9, fontName="Helvetica-Bold", textColor=WEAK_C)),
         Paragraph("Brand partnerships conflict with honest positioning.", S["table_cell"])],
        [Paragraph("9. Cost Structure", S["table_cell"]),
         Paragraph("Weak", ParagraphStyle("w4", fontSize=9, fontName="Helvetica-Bold", textColor=WEAK_C)),
         Paragraph("Unit economics not modeled at $6/month.", S["table_cell"])],
    ]
    bmc_t = Table(bmc_sum, colWidths=[1.9*inch, 0.9*inch, 3.7*inch])
    bmc_t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TABLE_HEADER),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, ROW_ALT]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#D1D5DB")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    story.append(bmc_t)
    story.append(Spacer(1, 16))

    closing_data = [[Paragraph(
        "Two things to do before this canvas is credible: (1) Test willingness to pay with "
        "existing interviewees — even informally. (2) Run one experiment on when advice starts "
        "feeling personal enough to convert. Everything else can wait.",
        ParagraphStyle("closing", fontSize=10.5, fontName="Helvetica-Bold",
                       textColor=NAVY, leading=17, alignment=TA_JUSTIFY))]]
    ct = Table(closing_data, colWidths=[6.5*inch])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), HexColor("#EBF2FA")),
        ("BOX", (0,0), (-1,-1), 1.5, ACCENT),
        ("LEFTPADDING", (0,0), (-1,-1), 14), ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (-1,-1), 12), ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ]))
    story.append(ct)

    doc.build(story)
    print(f"PDF generated: {OUTPUT}")

build_pdf()
