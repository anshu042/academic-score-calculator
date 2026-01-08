import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

def create_marksheet_pdf(name, sgpas, cgpa, std_percentage, mu_percentage):
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        name="title",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=18,
        spaceAfter=20
    )

    normal_style = ParagraphStyle(
        name="normal",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        spaceAfter=10
    )

    elements = []

    elements.append(Paragraph("Scorify", title_style))
    elements.append(Spacer(1, 0.1 * inch))
    elements.append(Paragraph("Instant conversions for SGPA, CGPA, and Percentage", title_style))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("Academic Conversion Marksheet", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"<b>Student Name:</b> {name}", normal_style))
    elements.append(Spacer(1, 0.2 * inch))

    data = [["Semester", "SGPA Obtained"]]
    for i, s in enumerate(sgpas):
        score = s if s else "-"
        data.append([f"Semester {i+1}", str(score)])

    table = Table(data, colWidths=[2.5*inch, 2.5*inch])
    table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,0), "Helvetica-Bold"),
        ('FONTNAME', (0,1), (-1,-1), "Helvetica"),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('bottomPadding', (0,0), (-1,0), 12),
        ('topPadding', (0,0), (-1,0), 12),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.3 * inch))

    cgpa_str = str(cgpa) if cgpa is not None else "N/A"
    std_str = f"{std_percentage}%" if std_percentage is not None else "N/A"
    mu_str = f"{mu_percentage}%" if mu_percentage is not None else "N/A"

    summary = [
        ["Final CGPA", cgpa_str],
        ["Standard Percentage (CGPA x 9.5)", std_str],
        ["Mumbai University Percentage", mu_str]
    ]

    summary_table = Table(summary, colWidths=[3.5*inch, 1.5*inch])
    summary_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), "Helvetica-Bold"),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (0,-1), colors.whitesmoke)
    ]))

    elements.append(summary_table)
    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph("🇸‌🇨‌🇴‌🇷‌🇮‌🇫‌🇾‌", ParagraphStyle('centered', parent=normal_style, alignment=TA_CENTER)))
    elements.append(Paragraph("SCORIFY 2026", ParagraphStyle('centered', parent=normal_style, alignment=TA_CENTER)))
    elements.append(Paragraph("Designed and Developed by Anshu Kushwaha", ParagraphStyle('centered', parent=normal_style, alignment=TA_CENTER)))
    elements.append(Paragraph("---- End of Marksheet ----", ParagraphStyle('centered', parent=normal_style, alignment=TA_CENTER)))

    doc.build(elements)
    
    buffer.seek(0)
    return buffer