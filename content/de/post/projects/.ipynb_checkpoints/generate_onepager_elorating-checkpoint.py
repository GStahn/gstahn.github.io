# -*- coding: utf-8 -*-
# pip install reportlab
# pip install svglib
import os
from svglib.svglib import svg2rlg
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, Image
)
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfgen import canvas as canvas_mod

# --- Farbschema ---
GREEN = colors.HexColor("#84BF67")
GREEN_DARK = colors.HexColor("#3E5A31")
VIOLET = colors.HexColor("#A267BF")
VIOLET_DARK = colors.HexColor("#5A3157")
GREY = colors.HexColor("#555555")
LIGHTBG = colors.HexColor("#F4F8F1")

PAGE_W, PAGE_H = A4

# --- Custom Canvas für die Fußzeile ---
class FooterCanvas(canvas_mod.Canvas):
    def showPage(self):
        self.setFillColor(GREY)
        self.setFont("Helvetica", 7.5)
        self.drawString(20*mm, 10*mm, "EvenlyGreat – Faire Teams. Jetzt!  ·  gerrit.stahn93.gs4@gmail.com")
        self.drawRightString(PAGE_W-20*mm, 10*mm, "DSGVO-konform · Selbstgehostet")
        canvas_mod.Canvas.showPage(self)

# --- Dokumenten-Einrichtung ---
doc = SimpleDocTemplate(
    "faire-teams-onepager.pdf",
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=14*mm, bottomMargin=16*mm,
    title="Faire Teams. Jetzt! – Onepager",
    author="Gerrit Stahn",
    subject="Elo-Rating basierte Team-Einteilung fuer Sportvereine",
)

styles = getSampleStyleSheet()

# --- Textstile ---
eyebrow_style = ParagraphStyle(
    "Eyebrow", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10.5, leading=12, textColor=VIOLET, spaceAfter=2, alignment=TA_LEFT
)
title_style = ParagraphStyle(
    "TitleBrand", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=25, leading=28, textColor=GREEN_DARK, spaceAfter=2, alignment=TA_LEFT
)
subtitle_style = ParagraphStyle(
    "Subtitle", parent=styles["Normal"], fontName="Helvetica-Oblique",
    fontSize=11, leading=14, textColor=VIOLET_DARK, spaceAfter=10
)
h2_style = ParagraphStyle(
    "H2", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=12.5, leading=15, textColor=GREEN_DARK, spaceBefore=8, spaceAfter=4
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10.3, leading=14.2, textColor=colors.HexColor("#222222"), spaceAfter=5
)
bullet_style = ParagraphStyle(
    "Bullet", parent=body_style, leftIndent=10, bulletIndent=0, spaceAfter=3.5, fontSize=10, leading=13.6
)
small_style = ParagraphStyle(
    "Small", parent=styles["Normal"], fontName="Helvetica", fontSize=7,
    leading=12, textColor=GREY
)
cell_head = ParagraphStyle(
    "CellHead", parent=body_style, fontName="Helvetica-Bold", fontSize=10,
    textColor=colors.white, leading=12.5
)
cell_body = ParagraphStyle(
    "CellBody", parent=body_style, fontSize=9.6, leading=12.5
)
cta_style = ParagraphStyle(
    "CTA", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=12.5,
    leading=16, textColor=colors.white, alignment=TA_CENTER
)
cta_sub_style = ParagraphStyle(
    "CTASub", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5,
    leading=13, textColor=colors.white, alignment=TA_CENTER
)

story = []

# --- Header-Bereich (Titel + Logo) ---
# 1. Nutzbare Breite explizit berechnen (z. B. A4 210mm - 2x 20mm Rand = 170mm)
# Ersetze PAGE_W durch deine tatsächliche Gesamtbreite oder definiere die Nutzbreite direkt:
PRINTABLE_WIDTH = PAGE_W - 40 * mm if 'PAGE_W' in locals() else 170 * mm

# 2. Titel-Block
title_block = [
    Paragraph("Faire Teams. Jetzt!", eyebrow_style),
    Paragraph("EvenlyGreat", title_style),
    Paragraph("Automatische & faire Teameinteilung. Für alle.", subtitle_style),
]

# 3. Logo laden & skalieren
svg_path = "/Users/apxww/Desktop/GitHub/myside/public/img/elorating_app/logo_landing.svg"
target_size = 20 * mm
logo_img = None

if os.path.exists(svg_path):
    try:
        drawing = svg2rlg(svg_path)
        if drawing is not None:
            orig_w = drawing.width or 1
            orig_h = drawing.height or 1
            
            scale = min(target_size / orig_w, target_size / orig_h)
            drawing.scale(scale, scale)
            
            # Bounding Box explizit überschreiben
            drawing.width = orig_w * scale
            drawing.height = orig_h * scale
            logo_img = drawing
    except Exception:
        logo_img = None

# Fallback
if logo_img is None:
    fallback = Drawing(target_size, target_size)
    fallback.add(Rect(0, 0, target_size, target_size, fillColor=LIGHTBG, strokeColor=GREEN, strokeWidth=1, rx=4, ry=4))
    fallback.add(String(target_size/2, target_size/2 - 3, "LOGO", textAnchor="middle", fontName="Helvetica-Bold", fontSize=8, fillColor=GREEN_DARK))
    logo_img = fallback

# 4. Spaltenbreiten dynamisch an die verfügbare Nutzbreite anpassen
logo_col_width = target_size
text_col_width = PRINTABLE_WIDTH - logo_col_width

header_table = Table(
    [[title_block, logo_img]],
    colWidths=[text_col_width, logo_col_width],
    hAlign="LEFT"
)

header_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
]))

story.append(header_table)
story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", thickness=1.4, color=GREEN, spaceAfter=4))

# --- Problem & Lösung (2 Spalten) ---
problem_text = (
    "<b>Das Problem:</b> Klassisches Teams-Auslosen dauert lange, ist meist unfair "
    "verteilt und hängt von der subjektiven Einschätzung einer einzelnen Person ab. "
    "Das Ergebnis: unausgeglichene Spiele und frustrierte Mitglieder."
)
solution_text = (
    "<b>Die Lösung:</b> Unsere App nutzt ein <b>Elo-Rating-System</b> "
    "(wie beim Schach): Jede:r Spieler:in erhält eine "
    "objektive, laufend aktualisierte Spielstärke-Bewertung. Daraus entstehen in Sekunden "
    "<b>ausgeglichene Teams</b> und alles ohne Vorwissen bedienbar."
)

two_col = Table(
    [[Paragraph(problem_text, body_style), Paragraph(solution_text, body_style)]],
    colWidths=[(PAGE_W-30*mm)/2 - 3*mm, (PAGE_W-30*mm)/2 - 3*mm],
    hAlign="LEFT"
)
two_col.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (0,0), 0),
    ("RIGHTPADDING", (0,0), (0,0), 8),
    ("LEFTPADDING", (1,0), (1,0), 8),
    ("RIGHTPADDING", (1,0), (1,0), 0),
]))
story.append(two_col)
story.append(Spacer(1, 2.5))

# --- Mehrwert-Tabelle ---
story.append(Paragraph("Der Mehrwert für Sie", h2_style))

data = [
    [Paragraph("Nutzen", cell_head), Paragraph("Was das konkret bedeutet", cell_head)],
    [Paragraph("<b>Zeitersparnis</b>", cell_body), Paragraph("Keine Diskussion mehr vor dem Training – Einteilung in Sekunden.", cell_body)],
    [Paragraph("<b>Faire, motivierende Spiele</b>", cell_body), Paragraph("Ausgeglichene Teams sorgen für spannendere Matches.", cell_body)],
    [Paragraph("<b>Besseres Training</b>", cell_body), Paragraph("Ausgeglichenere Matches erhöhen Trainingseffekt und Spielstärke.", cell_body)],
    [Paragraph("<b>Objektivität</b>", cell_body), Paragraph("Nachvollziehbare Ratings statt Bauchgefühl einer einzelnen Person.", cell_body)],
    [Paragraph("<b>Einfache Bedienung</b>", cell_body), Paragraph("Interaktive, webbasierte Oberfläche – keine Schulung nötig.", cell_body)],
    [Paragraph("<b>Datenhoheit &amp; Sicherheit</b>", cell_body), Paragraph("Volle Kontrolle über die eigenen Vereins- und Spielerdaten.", cell_body)],
]

table = Table(data, colWidths=[55*mm, PAGE_W - 40*mm - 55*mm], hAlign="LEFT")
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GREEN),
    ("BACKGROUND", (0,1), (-1,-1), LIGHTBG),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHTBG]),
    ("BOX", (0,0), (-1,-1), 0.6, colors.HexColor("#D8D8D8")),
    ("INNERGRID", (0,0), (-1,-1), 0.4, colors.HexColor("#E2E2E2")),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
]))
story.append(table)
story.append(Spacer(1, 8))

# --- DSGVO ---
story.append(Paragraph("DSGVO-konform: Ihre Daten bleiben bei Ihnen", h2_style))
dsgvo_items = [
    "Spieler- und Ergebnisdaten verlassen zu keinem Zeitpunkt Ihre eigene Infrastruktur.",
    "Zugriffsschutz sitzt vor der Anwendung – ohne gültige Anmeldung keine Verbindung.",
    "Passwörter werden ausschließlich als Hash gespeichert, niemals im Klartext.",
    "Automatische, regelmäßige Datensicherung für zusätzliche Ausfallsicherheit.",
]
for item in dsgvo_items:
    story.append(Paragraph("&#8226;&nbsp;&nbsp;" + item, bullet_style))

story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", thickness=0.8, color=VIOLET, spaceAfter=6))

# --- 3-Schritte-Prozess ---
story.append(Paragraph("So einfach geht's", h2_style))

step_num_style = ParagraphStyle(
    "StepNum", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=15,
    leading=18, textColor=colors.white, alignment=TA_CENTER
)
step_title_style = ParagraphStyle(
    "StepTitle", parent=body_style, fontName="Helvetica-Bold", fontSize=10.3, spaceAfter=2
)
step_text_style = ParagraphStyle(
    "StepText", parent=body_style, fontSize=9.3, leading=12.5, textColor=GREY
)

def circle(num, bg):
    t = Table([[Paragraph(str(num), step_num_style)]], colWidths=[9*mm], rowHeights=[9*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROUNDEDCORNERS", [12, 12, 12, 12]),
    ]))
    return t

steps = [
    (circle(1, GREEN), "Spieler:innen erfassen", "Namen einmalig anlegen, anwesende Personen markieren."),
    (circle(2, VIOLET), "Ergebnisse eintragen", "Nach jedem Spiel Ergebnis erfassen – das Rating aktualisiert sich automatisch."),
    (circle(3, GREEN_DARK), "Teams generieren", "Ein Klick genügt: faire, ausgeglichene Teams stehen sofort bereit."),
]

step_row = []
for icon, title, text in steps:
    cell = Table([[icon, Spacer(1,4)],[Paragraph(title, step_title_style)],[Paragraph(text, step_text_style)]],
                 colWidths=[(PAGE_W - 40*mm - 2*8*mm)/3])
    cell.setStyle(TableStyle([
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 1),
        ("BOTTOMPADDING", (0,0), (-1,-1), 1),
    ]))
    step_row.append(cell)

steps_table = Table([step_row], colWidths=[(PAGE_W-40*mm-16*mm)/3]*3, hAlign="LEFT", spaceBefore=2)
steps_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(steps_table)

story.append(Spacer(1, 8))

# --- Live-Testversion ---
qr_placeholder_style = ParagraphStyle(
    "QRPlaceholder", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=7.5, leading=9, textColor=GREY, alignment=TA_CENTER
)
qr_size = 24*mm
qr_box = Table([[Paragraph("QR-Code<br/>Platzhalter", qr_placeholder_style)]],
               colWidths=[qr_size], rowHeights=[qr_size])
qr_box.setStyle(TableStyle([
    ("BOX", (0,0), (-1,-1), 1, VIOLET),
    ("LINEABOVE", (0,0), (-1,-1), 1, VIOLET, None, (2,2)),
    ("LINEBELOW", (0,0), (-1,-1), 1, VIOLET, None, (2,2)),
    ("LINEBEFORE", (0,0), (-1,-1), 1, VIOLET, None, (2,2)),
    ("LINEAFTER", (0,0), (-1,-1), 1, VIOLET, None, (2,2)),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#A267BF10")),
]))

test_text = [
    Paragraph("Jetzt live testen", h2_style),
    Paragraph(
        "Neugierig geworden? Probieren Sie EvenlyGreat direkt in unserer Testversion aus – "
        "einfach den QR-Code scannen oder im Browser aufrufen:",
        body_style
    ),
    Paragraph("<b>www.evenlygreat.de</b>", ParagraphStyle(
        "TestUrl", parent=body_style, fontSize=12, textColor=VIOLET_DARK, spaceBefore=2
    )),
]

test_table = Table([[test_text, qr_box]],
                    colWidths=[PAGE_W - 40*mm - qr_size - 8*mm, qr_size],
                    hAlign="LEFT")
test_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 0),
    ("RIGHTPADDING", (1,0), (1,0), 0),
    ("RIGHTPADDING", (0,0), (0,0), 8),
]))
story.append(test_table)

story.append(Spacer(1, 7))

# --- Call to Action (CTA Box) ---
cta_content = [
    Paragraph("Interesse an fairen Teams für Ihren Verein, Sportunterricht oder Ähnlichem?", cta_style),
    Spacer(1, 4),
    Paragraph(
        "Schreiben Sie uns – wir freuen uns auf Sie.<br/>"
        "<b>gerrit.stahn93.gs4@gmail.com</b>",
        cta_sub_style
    ),
]
cta_table = Table([[cta_content]], colWidths=[PAGE_W - 40*mm], hAlign="LEFT")
cta_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), VIOLET_DARK),
    ("TOPPADDING", (0,0), (-1,-1), 12),
    ("BOTTOMPADDING", (0,0), (-1,-1), 12),
    ("LEFTPADDING", (0,0), (-1,-1), 14),
    ("RIGHTPADDING", (0,0), (-1,-1), 14),
    ("ROUNDEDCORNERS", [8, 8, 8, 8]),
]))
story.append(cta_table)

story.append(Spacer(1, 2))

# --- Entwickler-Credits ---
story.append(Paragraph(
    "<b>Entwickelt von:</b> Felix Heinrich, MSc (Statistik-Guru) · "
    "André Willig (Technik-Hase) · Dr. Gerrit Stahn (Mädchen für alles)<br/> "
    "EvenlyGreat entstanden aus der Praxis für unseren geliebten Volleyballverein SC261 Halle e.V.",
    small_style
))

# --- PDF erstellen ---
doc.build(story, canvasmaker=FooterCanvas)
print("PDF erfolgreich erstellt: faire-teams-onepager.pdf")