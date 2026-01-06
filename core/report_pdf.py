from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(target, results, risk):
    pdf = SimpleDocTemplate(f"reports/{target}_report.pdf")
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>CyberScope Scan Report</b>", styles["Title"]))
    content.append(Paragraph(f"Target: {target}", styles["Normal"]))
    content.append(Paragraph(f"Risk Level: {risk}", styles["Normal"]))

    for p, s, st in results:
        content.append(Paragraph(f"Port {p} | {s} | {st}", styles["Normal"]))

    pdf.build(content)
