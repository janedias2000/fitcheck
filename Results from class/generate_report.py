#!/usr/bin/env python3
"""Generate Customer Discovery PDF Report — Customer Discovery, June 2026"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT

W, H = letter

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY      = HexColor('#1C2B4B')
NAVY_MID  = HexColor('#2A3F6B')
TEAL      = HexColor('#2A7B78')
TEAL_LT   = HexColor('#EAF4F3')
TEAL_MED  = HexColor('#A8D4D2')
ORANGE    = HexColor('#B84E0B')
ORANGE_LT = HexColor('#FDF2EB')
GRAY_LT   = HexColor('#F5F7FA')
GRAY_MID  = HexColor('#8A9BAE')
GRAY_DK   = HexColor('#2D3748')
BORDER    = HexColor('#DDE4ED')

CW = 6.5 * inch  # content width

# ── Page callbacks ─────────────────────────────────────────────────────────────
def on_first_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(TEAL)
    canvas.rect(0, 0, W, 0.15 * inch, fill=1, stroke=0)
    canvas.restoreState()


def on_later_pages(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, H - 0.55 * inch, W - doc.rightMargin, H - 0.55 * inch)
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(GRAY_MID)
    canvas.drawString(doc.leftMargin, H - 0.40 * inch,
                      'Customer Discovery Report  ·  Women\'s Clothing & Style Confidence')
    canvas.drawRightString(W - doc.rightMargin, H - 0.40 * inch,
                           'BUS 395  ·  Jane Dias  ·  June 2026')
    canvas.line(doc.leftMargin, 0.60 * inch, W - doc.rightMargin, 0.60 * inch)
    canvas.setFont('Helvetica', 8)
    canvas.drawCentredString(W / 2, 0.38 * inch, str(doc.page - 1))
    canvas.restoreState()


# ── Styles ────────────────────────────────────────────────────────────────────
def S():
    return {
        # Cover
        'cover_eyebrow': ParagraphStyle('cover_eyebrow',
            fontName='Helvetica', fontSize=9, textColor=TEAL_MED,
            alignment=TA_CENTER, leading=13, spaceAfter=10),
        'cover_title': ParagraphStyle('cover_title',
            fontName='Helvetica-Bold', fontSize=32, textColor=white,
            alignment=TA_CENTER, leading=38, spaceAfter=10),
        'cover_subtitle': ParagraphStyle('cover_subtitle',
            fontName='Helvetica', fontSize=14, textColor=TEAL_MED,
            alignment=TA_CENTER, leading=20, spaceAfter=0),
        'cover_meta': ParagraphStyle('cover_meta',
            fontName='Helvetica', fontSize=9, textColor=HexColor('#7A9AB5'),
            alignment=TA_CENTER, leading=14, spaceAfter=0),
        'cover_finding_label': ParagraphStyle('cover_finding_label',
            fontName='Helvetica-Bold', fontSize=9, textColor=TEAL,
            alignment=TA_CENTER, leading=13, spaceAfter=8),
        'cover_finding': ParagraphStyle('cover_finding',
            fontName='Helvetica', fontSize=12, textColor=GRAY_DK,
            alignment=TA_CENTER, leading=19, spaceAfter=0),

        # Section structure
        'section_title': ParagraphStyle('section_title',
            fontName='Helvetica-Bold', fontSize=20, textColor=NAVY,
            alignment=TA_LEFT, leading=24, spaceAfter=4, spaceBefore=4),
        'subsection_title': ParagraphStyle('subsection_title',
            fontName='Helvetica-Bold', fontSize=13, textColor=NAVY,
            alignment=TA_LEFT, leading=17, spaceAfter=4, spaceBefore=2),

        # Interview header
        'int_name': ParagraphStyle('int_name',
            fontName='Helvetica-Bold', fontSize=15, textColor=white,
            alignment=TA_LEFT, leading=19, spaceAfter=0),
        'int_meta': ParagraphStyle('int_meta',
            fontName='Helvetica', fontSize=8.5, textColor=TEAL_MED,
            alignment=TA_LEFT, leading=13, spaceAfter=0),

        # Body text
        'body': ParagraphStyle('body',
            fontName='Helvetica', fontSize=10, textColor=GRAY_DK,
            alignment=TA_JUSTIFY, leading=15.5, spaceAfter=8),
        'body_sm': ParagraphStyle('body_sm',
            fontName='Helvetica', fontSize=9.5, textColor=GRAY_DK,
            alignment=TA_LEFT, leading=14.5, spaceAfter=6),
        'bold_label': ParagraphStyle('bold_label',
            fontName='Helvetica-Bold', fontSize=10, textColor=NAVY,
            alignment=TA_LEFT, leading=14, spaceAfter=3),
        'bullet': ParagraphStyle('bullet',
            fontName='Helvetica', fontSize=10, textColor=GRAY_DK,
            alignment=TA_LEFT, leading=15, spaceAfter=4,
            leftIndent=12),

        # Quotes
        'quote': ParagraphStyle('quote',
            fontName='Helvetica-Oblique', fontSize=10.5,
            textColor=HexColor('#1E4A48'),
            alignment=TA_LEFT, leading=17, spaceAfter=0),
        'attribution': ParagraphStyle('attribution',
            fontName='Helvetica', fontSize=8.5, textColor=GRAY_MID,
            alignment=TA_LEFT, leading=12, spaceAfter=0),

        # Tables
        'th': ParagraphStyle('th',
            fontName='Helvetica-Bold', fontSize=9, textColor=white,
            alignment=TA_LEFT, leading=12, spaceAfter=0),
        'td': ParagraphStyle('td',
            fontName='Helvetica', fontSize=9, textColor=GRAY_DK,
            alignment=TA_LEFT, leading=13, spaceAfter=0),

        # Tags / labels
        'challenge_label': ParagraphStyle('challenge_label',
            fontName='Helvetica-Bold', fontSize=7.5, textColor=ORANGE,
            alignment=TA_LEFT, leading=10, spaceAfter=4),
        'pattern_label': ParagraphStyle('pattern_label',
            fontName='Helvetica-Bold', fontSize=7.5, textColor=TEAL,
            alignment=TA_LEFT, leading=10, spaceAfter=4),
    }


# ── Component builders ────────────────────────────────────────────────────────

def gap(h=8):
    return Spacer(1, h)


def rule(color=BORDER, thickness=0.5):
    return HRFlowable(width='100%', thickness=thickness, color=color, spaceAfter=0, spaceBefore=0)


def quote_block(text, styles, attribution=None):
    """Teal left-border pull quote block."""
    rows = [[Paragraph(f'“{text}”', styles['quote'])]]
    if attribution:
        rows.append([Paragraph(f'— {attribution}', styles['attribution'])])
    inner = Table(rows, colWidths=[CW - 0.6 * inch - 28])
    inner.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    outer = Table([[inner]], colWidths=[CW - 0.6 * inch])
    outer.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TEAL_LT),
        ('LINEBEFORE', (0, 0), (-1, -1), 3, TEAL),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 11),
    ]))
    return outer


def challenge_block(text, styles):
    """Orange left-border challenge/surprise block."""
    rows = [
        [Paragraph('CHALLENGED ASSUMPTION', styles['challenge_label'])],
        [Paragraph(text, styles['body_sm'])],
    ]
    inner = Table(rows, colWidths=[CW - 0.6 * inch - 28])
    inner.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    outer = Table([[inner]], colWidths=[CW - 0.6 * inch])
    outer.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), ORANGE_LT),
        ('LINEBEFORE', (0, 0), (-1, -1), 3, ORANGE),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 14),
        ('TOPPADDING', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 11),
    ]))
    return outer


def section_rule(title, styles):
    """Navy-accented section title with rule."""
    title_bar = Table(
        [[Paragraph(title, styles['section_title'])]],
        colWidths=[CW]
    )
    title_bar.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 2, NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return title_bar


def interview_header_block(name, segment, meta, styles):
    top = Table(
        [[Paragraph(name, styles['int_name'])],
         [Paragraph(segment, styles['int_meta'])],
         [Paragraph(meta, styles['int_meta'])]],
        colWidths=[CW]
    )
    top.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 16),
        ('TOPPADDING', (0, 0), (0, 0), 14),
        ('TOPPADDING', (0, 1), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -2), 2),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 14),
    ]))
    return top


def pattern_item(number, title, body, challenge, styles):
    num_para = Paragraph(f'<b><font color="#2A7B78">{number}</font></b>', styles['subsection_title'])
    title_para = Paragraph(title, styles['subsection_title'])
    header_row = Table([[num_para, title_para]], colWidths=[0.45 * inch, CW - 0.45 * inch])
    header_row.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    items = [header_row, Paragraph(body, styles['body'])]
    if challenge:
        items.append(gap(4))
        items.append(challenge_block(challenge, styles))
    items.append(gap(16))
    return KeepTogether(items)


# ── Content builders ──────────────────────────────────────────────────────────

def build_cover(s):
    elements = []

    # Large navy block for title area
    cover_data = [
        [Paragraph('CUSTOMER DISCOVERY REPORT', s['cover_title'])],
        [Paragraph("Women’s Clothing &amp; Style Confidence", s['cover_subtitle'])],
        [gap(12)],
        [rule(color=TEAL, thickness=1.2)],
        [gap(10)],
        [Paragraph('5 Interviews · BUS 395: Venture Creation with AI · Jane Dias · June 2026',
                   s['cover_meta'])],
    ]
    cover_top = Table(cover_data, colWidths=[CW])
    cover_top.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('TOPPADDING', (0, 0), (0, 0), 52),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 48),
        ('BOTTOMPADDING', (0, 0), (-1, -2), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 36),
        ('RIGHTPADDING', (0, 0), (-1, -1), 36),
    ]))
    elements.append(cover_top)
    elements.append(gap(36))

    # Key finding box
    finding_data = [
        [Paragraph('KEY FINDING', s['cover_finding_label'])],
        [Paragraph(
            'Every woman interviewed described the same unmet need: trusted, honest, '
            'personalized feedback on whether a specific piece of clothing looks good '
            'on her specific body. None had a reliable way to get it alone.',
            s['cover_finding'])],
    ]
    finding_table = Table(finding_data, colWidths=[CW])
    finding_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), GRAY_LT),
        ('LINEABOVE', (0, 0), (-1, 0), 2, TEAL),
        ('LINEBELOW', (0, -1), (-1, -1), 2, TEAL),
        ('LEFTPADDING', (0, 0), (-1, -1), 28),
        ('RIGHTPADDING', (0, 0), (-1, -1), 28),
        ('TOPPADDING', (0, 0), (0, 0), 20),
        ('TOPPADDING', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 22),
        ('BOTTOMPADDING', (0, 0), (-1, -2), 6),
    ]))
    elements.append(finding_table)
    elements.append(gap(36))

    # What this report contains
    elements.append(Paragraph('<b>This report contains:</b>', s['bold_label']))
    elements.append(gap(6))
    for item in [
        'Individual profiles for all 5 interviewees with verbatim quotes',
        'What surprised me or challenged my assumptions in each conversation',
        'Confirmed patterns — things 3 or more interviewees said independently',
        'Contradictions — where what they said didn’t match what they did',
        'Surprises — things that should not have been assumed going in',
    ]:
        elements.append(Paragraph(f'•  {item}', s['bullet']))

    elements.append(PageBreak())
    return elements


def build_overview(s):
    elements = []
    elements.append(section_rule('Research Overview', s))
    elements.append(gap(14))

    elements.append(Paragraph('<b>Research Question</b>', s['bold_label']))
    elements.append(Paragraph(
        'How do women make decisions when shopping for clothing, and how do they feel '
        'about the clothes they buy and wear? Specifically: what happens when they are '
        'unsure whether something looks good on them, and what would help?', s['body']))
    elements.append(gap(10))

    elements.append(Paragraph('<b>Method</b>', s['bold_label']))
    elements.append(Paragraph(
        '5 one-on-one phone interviews, 8–13 minutes each, conducted June 7, 2026. '
        'All recorded via Granola (audio + transcript). Interviewees were recruited from '
        'personal network and selected to represent different budget levels, life stages, '
        'and relationships with clothing.', s['body']))
    elements.append(gap(16))

    elements.append(Paragraph('<b>Who Was Interviewed</b>', s['bold_label']))
    elements.append(gap(6))

    headers = ['#', 'Name', 'Profile', 'Budget', 'Body / Complexion Note']
    rows = [
        ['1', 'Allison G.', 'Woman in her 40s, primary in-store shopper', 'Larger, mindful', 'Tall'],
        ['2', 'Aly S.', 'Woman in her 20s, mixed online/in-store', 'Limited', 'Pale complexion'],
        ['3', 'Danai', 'Preschool teacher & business owner, primary online shopper', 'Very budget-conscious', 'Small waist, larger hips/thighs'],
        ['4', 'Mya', 'Woman in her 20s, highly social shopper', 'Limited', '—'],
        ['5', 'Meg', 'Mom in her 30s, former fashion industry; shops online out of necessity', 'Moderate', 'Narrow hips, thicker waist; body changes from pregnancy'],
    ]

    col_widths = [0.3 * inch, 0.85 * inch, 2.1 * inch, 1.05 * inch, 2.2 * inch]
    table_data = [[Paragraph(h, s['th']) for h in headers]]
    for row in rows:
        table_data.append([Paragraph(cell, s['td']) for cell in row])

    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('BACKGROUND', (0, 1), (-1, 1), GRAY_LT),
        ('BACKGROUND', (0, 2), (-1, 2), white),
        ('BACKGROUND', (0, 3), (-1, 3), GRAY_LT),
        ('BACKGROUND', (0, 4), (-1, 4), white),
        ('BACKGROUND', (0, 5), (-1, 5), GRAY_LT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [GRAY_LT, white]),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(t)
    elements.append(PageBreak())
    return elements


def build_interview_1(s):
    elements = []
    elements.append(interview_header_block(
        'Interview 1 — Allison G.',
        'Woman in her 40s · Tall · Larger budget, mindful with spending · Primary in-store shopper',
        'June 7, 2026 · 12 minutes · Phone', s))
    elements.append(gap(14))

    elements.append(Paragraph('<b>Who she is</b>', s['bold_label']))
    elements.append(Paragraph(
        'Allison has spent decades developing a reliable "formula" for dressing well through trial '
        'and error. She shops almost exclusively in-store to avoid returns, uses three-sided mirrors, '
        'and evaluates every item against the same criteria: fit, quality, price, and ability to '
        'integrate into her existing wardrobe. She feels confident getting dressed about 90% of mornings.', s['body']))
    elements.append(gap(10))

    elements.append(Paragraph('<b>Key Quotes</b>', s['bold_label']))
    elements.append(gap(6))
    for q in [
        ('I want to be really certain when I leave the store that I actually want to take that '
         'item home, that I feel good about it, that I’m confident wearing it.',),
        ('I especially think when it’s like a family member or a friend more than the sales '
         'associate, because I understand the sales associate is just trying to make a sale.',),
        ('I didn’t have a personal stylist. I didn’t have somebody like, helping me figure '
         'out outfits, which would have been great. But it was really a lot of trial and error, '
         'and I’ve made a lot of mistakes.',),
        ('Having somebody who is trusted give me some feedback on the outfit — knowing that '
         'that would be the case. If somebody who I trusted really would give me that kind of '
         'feedback, that would be helpful.',),
    ]:
        elements.append(quote_block(q[0], s))
        elements.append(gap(8))

    elements.append(gap(4))
    elements.append(challenge_block(
        'Allison has largely solved her own problem through decades of experience — she reports '
        '90% morning confidence. Her pain is real but mostly in the past. She may represent a '
        'future state rather than the current target customer. The product needs to serve who she '
        'was in her 20s and 30s, not necessarily who she is now.', s))
    elements.append(PageBreak())
    return elements


def build_interview_2(s):
    elements = []
    elements.append(interview_header_block(
        'Interview 2 — Aly S.',
        'Woman in her 20s · Limited budget · Mixed online/in-store · Pale complexion',
        'June 7, 2026 · 8 minutes · Phone', s))
    elements.append(gap(14))

    elements.append(Paragraph('<b>Who she is</b>', s['bold_label']))
    elements.append(Paragraph(
        'Aly is in the early stages of figuring out her style. She shops on a limited budget, '
        'avoids buying things she already has, and relies on friends’ opinions when shopping '
        'together. She knows certain colors wash her out due to her complexion — but keeps picking '
        'them anyway. She feels confident in her outfit about 50% of mornings, and compensates '
        'for a weak outfit by doing her hair and makeup.', s['body']))
    elements.append(gap(10))

    elements.append(Paragraph('<b>Key Quotes</b>', s['bold_label']))
    elements.append(gap(6))
    for q in [
        ('Knowing what kind of styles and silhouettes look good on your body is important, '
         'and sometimes it’s hard to figure that out in the store.',),
        ('I feel like, because I’m kind of pale, a lot of colors wash me out, and sometimes '
         'I’ll still pick up a color that doesn’t look good on me — and if I knew, '
         'like, okay, stay away from this color, I would stop doing that.',),
        ('It just makes you feel good about yourself and you feel confident and like, oh, I would '
         'feel fine if I would, like, took a picture in this outfit. Like, you know, I want to go '
         'out and be seen.',),
        ('Sometimes I will sacrifice. If I’m lacking in the outfit, then I do my hair and '
         'makeup to make up for what’s lacking in the outfit.',),
    ]:
        elements.append(quote_block(q[0], s))
        elements.append(gap(8))

    elements.append(gap(4))
    elements.append(challenge_block(
        'Aly already knows about her color problem but keeps doing it anyway. This means the '
        'problem is not a lack of information — it\'s something about the moment of decision '
        'that bypasses what she already knows. A solution that only delivers style rules or '
        'education may not be enough to change behavior at the point of purchase.', s))
    elements.append(PageBreak())
    return elements


def build_interview_3(s):
    elements = []
    elements.append(interview_header_block(
        'Interview 3 — Danai',
        'Preschool teacher & business owner · Very budget-conscious · Primary online shopper',
        'June 7, 2026 · 9 minutes · Phone', s))
    elements.append(gap(14))

    elements.append(Paragraph('<b>Who she is</b>', s['bold_label']))
    elements.append(Paragraph(
        'Danai is financially disciplined and has built an efficient system around the problem: '
        'she shops primarily online because returns via UPS are easy, sends photos to trusted '
        'family members for feedback, and follows body-type influencers on social media for '
        'styling guidance. Her body type (small waist, larger hips and thighs) makes pants and '
        'shorts particularly hard to fit. When she finds something that works, she buys it in '
        'every color.', s['body']))
    elements.append(gap(10))

    elements.append(Paragraph('<b>Key Quotes</b>', s['bold_label']))
    elements.append(gap(6))
    for q in [
        ('A lot of pants and shorts fit me kind of weird. And it’s like usually when I find '
         'a short that fits me great, I’ll just buy in every color.',),
        ('I sat there and I do remember feeling a little sad at the end of our day because I '
         'really didn’t find anything that really worked for me.',),
        ('I don’t know if maybe the store mirror and the lights just made it look like it '
         'looked amazing. And then when I got home and actually saw it in real light in my '
         'bathroom, I was like, what the hell was I thinking?',),
        ('One of the things that has been so helpful with clothes — I try to find an '
         'influencer that has my body type, and then I follow them, and I’m like, okay, '
         'yeah, she’s figured out what looks good on our body type. And then I kind of '
         'just go from there.',),
    ]:
        elements.append(quote_block(q[0], s))
        elements.append(gap(8))

    elements.append(gap(4))
    elements.append(challenge_block(
        'Danai already has a working solution: she follows influencers with her body type and '
        'uses easy online returns as her fallback. She volunteered the influencer strategy '
        'unprompted as genuinely helpful. Any new product needs to be meaningfully better than '
        '"find someone who looks like you on Instagram" — which is already free and working for her.', s))
    elements.append(PageBreak())
    return elements


def build_interview_4(s):
    elements = []
    elements.append(interview_header_block(
        'Interview 4 — Mya',
        'Woman in her 20s · Limited budget · Highly social shopper · Wears gym clothes frequently',
        'June 7, 2026 · 8 minutes · Phone', s))
    elements.append(gap(14))

    elements.append(Paragraph('<b>Who she is</b>', s['bold_label']))
    elements.append(Paragraph(
        'For Mya, shopping is fundamentally social — she brings friends and family to get a '
        '360-degree view of herself and a confidence boost. She takes spin videos in dressing '
        'rooms, FaceTimes her mom before going out, and has clearly identified which people '
        'give her honest feedback (her mom is "brutal") versus polite feedback (some friends). '
        'She feels confident in a going-out outfit about 50% of the time, and avoids being '
        '"seen in public" when her outfit isn\'t working. Confidence is around 40% for everyday outfits.', s['body']))
    elements.append(gap(10))

    elements.append(Paragraph('<b>Key Quotes</b>', s['bold_label']))
    elements.append(gap(6))
    for q in [
        ('I think that’s a big part of shopping, and for me, it’s kind of, like, '
         'social. I do think half of the time, if somebody is like, that looks good, then '
         'I’m like, that will push me to buy it. I can’t get a 360 of myself sometimes.',),
        ('I do think my mom is kind of brutal, and she’ll be like, that doesn’t look '
         'good. But then sometimes when you do ask a friend, they’re just trying to be nice, '
         'and they won’t give you real input on the outfit.',),
        ('When I’m not wearing a good outfit, I don’t want to be so seen in public.',),
        ('Sometimes I’ll, like, FaceTime my mom and be like, do you like this outfit? '
         'Or I’ll ask my twin sister before I go out. So that type of thing definitely helps.',),
    ]:
        elements.append(quote_block(q[0], s))
        elements.append(gap(8))

    elements.append(gap(4))
    elements.append(challenge_block(
        'Mya explicitly named the 360-degree visibility gap — "I can\'t get a 360 of myself" — '
        'as a core reason she relies on others. This is a physical/spatial problem, not a style '
        'knowledge gap. She also already knows which sources give honest feedback and which don\'t. '
        'She isn\'t searching for an honest advisor — she has her mom. The problem is availability, '
        'not existence.', s))
    elements.append(PageBreak())
    return elements


def build_interview_5(s):
    elements = []
    elements.append(interview_header_block(
        'Interview 5 — Meg',
        'Mom in her 30s · Former fashion industry · Online shopper by necessity · Narrow hips, thicker waist',
        'June 7, 2026 · 13 minutes · Phone', s))
    elements.append(gap(14))

    elements.append(Paragraph('<b>Who she is</b>', s['bold_label']))
    elements.append(Paragraph(
        'Meg worked in fashion and still rarely feels confident in what she wears — she '
        'attributes it to body image, not style knowledge. She shops online because bringing '
        'her 4-year-old to stores is unworkable. She has navigated significant body changes '
        'through pregnancy and aging, and deals with sizing systems that don\'t reflect her '
        'actual proportions (narrow hips, thicker waist). She could not articulate what or '
        'who could help her — but she described exactly what she would want.', s['body']))
    elements.append(gap(10))

    elements.append(Paragraph('<b>Key Quotes</b>', s['bold_label']))
    elements.append(gap(6))
    for q in [
        ('As someone who’s been through a lot of changes in her body between getting older, '
         'having babies, different things like that, it definitely presents challenges in finding '
         'something that you think looks good.',),
        ('I accidentally bought a pair of jeans — they were “curvy” — but I '
         'didn’t realize that curvy means that the waist is small and the hips are bigger in '
         'proportion. But I have the opposite. I got more narrow hips and a thicker waist. And '
         'these are my size, and they did not fit at all.',),
        ('Until you actually start wearing the item out, you almost don’t know if you like '
         'it. You think you do, but something about it can bug you when you actually put it on '
         'and wear it out.',),
        ('I very rarely feel confident in what I’m wearing, but it’s mostly a body '
         'image issue.',),
        ('Maybe if somebody who was skilled in knowing what looks good on certain body types '
         '— but everyone’s got a different body type. Maybe just having some information '
         'about my dimensions and like, hey, that type of waist doesn’t look great. I’m '
         'not sure who or what could give me that kind of information.',),
    ]:
        elements.append(quote_block(q[0], s))
        elements.append(gap(8))

    elements.append(gap(4))
    elements.append(challenge_block(
        'Meg worked in fashion and still can\'t crack this. Industry knowledge doesn\'t solve it. '
        'She was the most open to help of all five interviewees, and still couldn\'t imagine what '
        'a solution would look like. If your most receptive potential customer can\'t picture your '
        'product, trust and credibility are the hardest problems you\'re facing — not the feature set.', s))
    elements.append(PageBreak())
    return elements


def build_patterns(s):
    elements = []
    elements.append(section_rule('Confirmed Patterns', s))
    elements.append(Paragraph(
        'Things 3 or more interviewees said independently, without prompting.', s['body_sm']))
    elements.append(gap(16))

    elements.append(pattern_item('01', 'Everyone uses trusted people as their feedback system — and knows it\'s flawed.',
        'All 5 described the same workaround: send a photo or ask someone in person. '
        'Allison: "It\'s more reassuring when you ask a friend or family member." '
        'Danai: "If they are hesitant in any way, I just won\'t get it." '
        'Mya: "My mom is kind of brutal, and she\'ll be like, that doesn\'t look good. '
        'But sometimes when you do ask a friend, they\'re just trying to be nice." '
        'Meg: wanted "somebody who was skilled in knowing what looks good on certain body types" but couldn\'t imagine where that would come from.',
        'The demand for trusted feedback is confirmed and real. But these women already have a system. '
        'You are competing with mom, the twin sister, the husband — not filling a vacuum. '
        'Your solution needs to be more honest, more available, or more capable than those people.', s))

    elements.append(pattern_item('02', 'Online shopping reliably produces unworn items — and the culprit is proportions, not size.',
        'All 5 had a story about something bought online that didn\'t work. In every case, '
        'the item was the right size on paper. Allison: items sitting in her closet with tags, '
        'missed return windows. Aly: Old Navy athletic wear — "some of them fit, some of them '
        'didn\'t, even though they were the same size." Danai: "It wasn\'t so much that it was '
        'the wrong size. It just didn\'t fit my body well." Mya: tube top bought on sale without '
        'trying on — never worn. Meg: "curvy" jeans that were her size but completely wrong '
        'for her actual proportions.',
        'This is the most consistent, concrete pain point. It\'s measurable (unworn items), '
        'it happens to everyone, and it\'s rooted in a real structural problem: sizing systems '
        'don\'t capture proportion. This is your strongest confirmed signal.', s))

    elements.append(pattern_item('03', 'Body proportions are where the system breaks down — not size labels.',
        'Three interviewees described specific body proportions as the source of chronic fit '
        'problems. Danai (small waist, large hips/thighs): "usually when I find a short that '
        'fits me great, I\'ll just buy in every color." Meg (narrow hips, thicker waist): '
        'bought jeans in her size that didn\'t fit at all due to the "curvy" label mismatch. '
        'Aly: a different axis — pale complexion means many colors wash her out regardless of fit. '
        'Allison developed her "formula" over decades specifically to navigate this.',
        'A solution that doesn\'t account for individual body proportions — not just size — '
        'is solving the wrong problem. Standard sizing is not the pain point. '
        'The interaction between clothing cut and individual body shape is.', s))

    elements.append(pattern_item('04', 'Low outfit confidence has real behavioral consequences.',
        'All 5 described concrete behaviors that result from not feeling confident. Allison: '
        '"I do not want to leave the house not feeling confident or comfortable" — she changes '
        'entirely. Aly: does hair and makeup to compensate for a weak outfit. '
        'Mya: "when I\'m not wearing a good outfit, I don\'t want to be so seen in public." '
        'Danai: has separate work and going-out wardrobes with entirely different confidence levels. '
        'Meg: "I very rarely feel confident in what I\'m wearing."',
        None, s))

    elements.append(PageBreak())

    # Contradictions
    elements.append(section_rule('Contradictions', s))
    elements.append(Paragraph(
        'Where what they said doesn\'t match what they did, or where interviewees\' experiences contradict each other.', s['body_sm']))
    elements.append(gap(16))

    elements.append(pattern_item('01', 'They say in-store try-on is the solution — but in-store also fails them.',
        'Allison, Aly, and Mya all said in-store shopping produces better outcomes. But the '
        'actual stories tell a more complicated picture. Danai: bought something in-store that '
        'looked great, was horrified at home — "I don\'t know if maybe the store mirror and the '
        'lights just made it look like it looked amazing. And then when I got home and actually '
        'saw it in real light in my bathroom, I was like, what the hell was I thinking?" '
        'Meg: "Until you actually start wearing the item out, you almost don\'t know if you like '
        'it." Danai also left an in-store trip feeling "a little sad" because nothing worked '
        'despite trying everything on.',
        'They believe try-before-you-buy is the fix, but their own stories show it\'s not reliable '
        'either. Store lighting is deceptive, and how something actually wears (rides up, breathes, '
        'moves) only reveals itself in real life. The problem is not fully solved by in-store try-on.', s))

    elements.append(pattern_item('02', 'They know what doesn\'t work on them — and keep doing it anyway.',
        'Aly explicitly: "I feel like, because I\'m kind of pale, a lot of colors wash me out, '
        'and sometimes I\'ll still pick up a color that doesn\'t look good on me, even though — '
        'and if I knew, like, okay, stay away from this color, I would stop doing that." '
        'She already knows. She keeps doing it. Mya bought a tube top without trying it on '
        'despite knowing that\'s what causes unworn purchases. Danai shops primarily online '
        'even though proportion-fit is her main problem — because returns are easier.',
        'The problem is not a lack of information for Aly — she has the information. '
        'Something about the moment of decision bypasses what she already knows. A solution '
        'that only provides style rules or education may not change behavior if the behavior '
        'is already informed and still failing.', s))

    elements.append(pattern_item('03', 'They say they want honest feedback — but they also want validation.',
        'Mya: "if somebody is like, that looks good, then I\'m like, that will push me to buy it" '
        '— in the same interview where she values her mom\'s brutal honesty. Allison frames '
        'asking friends as seeking confirmation that something "is a good fit." Danai: "If I\'m '
        'feeling really confident in it, I\'ll just buy it right then" — she bypasses feedback '
        'entirely when she wants to. The desire for validation and the desire for honest feedback '
        'are two different things, and they coexist in the same person.',
        'What they say they want (honest feedback) and what actually moves them (positive validation) '
        'may be different things. A product that delivers hard truths may be less used than one '
        'that confirms what someone already wants to hear. This is a design and trust problem '
        'you\'ll need to solve explicitly.', s))

    elements.append(pattern_item('04', 'Confidence levels vary so widely across interviewees that they may not have the same problem.',
        'Allison: 90% confident most mornings. Problem largely solved through decades of iteration. '
        'Aly: 50% confident. Mya: 40% in regular outfits, 50% in going-out outfits. '
        'Danai: confident in work context, separate concern for going out. '
        'Meg: "I very rarely feel confident in what I\'m wearing" — explicitly attributes it to body image.',
        'Allison is not the same customer as Meg. Allison\'s problem is at purchase time. '
        'Meg\'s problem is her relationship with her own body, which no styling tool solves. '
        'If your venture targets "women who don\'t feel confident in their clothes," that ranges from '
        '"occasionally unsure at checkout" to "chronic body image struggle." These need different responses.', s))

    elements.append(PageBreak())

    # Surprises
    elements.append(section_rule('Surprises', s))
    elements.append(Paragraph(
        'Things that should not have been assumed going in — findings that reframe the problem.', s['body_sm']))
    elements.append(gap(16))

    elements.append(pattern_item('01', 'Fashion industry experience doesn\'t solve the problem.',
        'Meg worked in fashion and still rarely feels confident in what she wears. She couldn\'t '
        'articulate what would help, said "I\'m not sure who or what could give me that kind of '
        'information," and explicitly named body image — not style literacy — as the root issue. '
        'Professional training doesn\'t close the gap. The problem is structural (proportions, '
        'body changes over time) and psychological (body image), not educational.',
        'If you\'re building something that teaches women how to dress better, you need to explain '
        'why Meg — who had professional training — still couldn\'t crack it. "More style information" '
        'is probably not the answer.', s))

    elements.append(pattern_item('02', 'The influencer-with-same-body-type strategy is a real, working solution — already in market.',
        'Danai volunteered this without being asked: "One of the things that has been so helpful '
        'with clothes — I try to find an influencer that has my body type, and then I follow them, '
        'and I\'m like, okay, yeah, she\'s figured out what looks good on our body type. And then '
        'I kind of just go from there." This is free, personalized to body type, and it\'s already '
        'working for her. She didn\'t describe it as a workaround — she described it as a solution.',
        'Your venture needs to be meaningfully better than "follow someone who looks like you on '
        'Instagram." That is not a trivial bar. It\'s free, already adopted, and — from Danai\'s '
        'perspective — effective.', s))

    elements.append(pattern_item('03', 'The 360-degree visibility gap is a physical problem, not a knowledge gap.',
        'Mya named this explicitly and unprompted: "I can\'t get a 360 of myself sometimes." '
        'This is why she takes spin videos in dressing rooms and brings people shopping. It\'s not '
        'that she doesn\'t know what looks good — she literally cannot see herself from behind '
        'and from the sides. She has compensated with videos, but it\'s imperfect.',
        'This is a more tractable problem than "teach someone their style." It\'s a visibility and '
        'perspective problem. Tools that address this directly — a mirror system, a photo tool, '
        'augmented reality — speak to a specific physical limitation, not a vague confidence gap.', s))

    elements.append(pattern_item('04', 'Easy returns are a competing solution, not just a symptom.',
        'Danai explicitly prefers online shopping because returns are easy: "That\'s why the online '
        'shopping is so much easier, because then I can just go return it at UPS." She has built '
        'her entire shopping system around the problem. She buys, tries at home in real lighting, '
        'and returns what doesn\'t work. This isn\'t suffering — it\'s adaptation.',
        'For Danai, a new product would need to replace a system that already works. You\'re not '
        'filling a gap — you\'re asking her to change a routine that functions. That\'s a harder '
        'sell than it looks.', s))

    elements.append(pattern_item('05', 'The people who give honest feedback are rare, known by name, and the problem is their availability — not their existence.',
        'Every interviewee who uses human feedback has already identified their honest person: '
        'Mya\'s mom. Danai\'s husband and sisters. Allison\'s trusted friends. They aren\'t '
        'searching for honest feedback — they\'ve found their specific person. The gap is not '
        '"honest feedback doesn\'t exist." It\'s "my honest person isn\'t available at the '
        'moment I need them." That reframes the problem entirely.',
        'If the real gap is availability, not existence, the product question becomes: how do '
        'you replicate what their most trusted person would say, at the moment they need it, '
        'in a way that feels as credible? That is a narrower and more tractable problem than '
        '"provide honest feedback."', s))

    return elements


# ── Main ──────────────────────────────────────────────────────────────────────
def build():
    out = '/Users/jane/projects/venture/Interviews/Customer_Discovery_Report.pdf'
    doc = SimpleDocTemplate(
        out,
        pagesize=letter,
        leftMargin=1 * inch,
        rightMargin=1 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.85 * inch,
        title='Customer Discovery Report — Women\'s Clothing & Style Confidence',
        author='Jane Dias',
        subject='BUS 395: Venture Creation with AI',
    )

    s = S()
    story = []
    story += build_cover(s)
    story += build_overview(s)
    story += build_interview_1(s)
    story += build_interview_2(s)
    story += build_interview_3(s)
    story += build_interview_4(s)
    story += build_interview_5(s)
    story += build_patterns(s)

    doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
    print(f'Done → {out}')


build()
