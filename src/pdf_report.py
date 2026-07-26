from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(name, age, stress, prediction, performance):

    filename = "student_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>STUDENT PERFORMANCE REPORT</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Student Name:</b> {name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Age:</b> {age}", styles["Normal"]))
    story.append(Paragraph(f"<b>Stress Level:</b> {stress}", styles["Normal"]))
    story.append(Paragraph(f"<b>Predicted GPA:</b> {prediction:.2f}", styles["Normal"]))
    story.append(Paragraph(f"<b>Performance:</b> {performance}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Recommendations</b>", styles["Heading2"]))

    if prediction < 3.0:
        story.append(Paragraph("• Increase study hours.", styles["Normal"]))

    if stress == "High":
        story.append(Paragraph("• Reduce stress through exercise or meditation.", styles["Normal"]))

    if prediction >= 3.7:
        story.append(Paragraph("• Keep maintaining your excellent routine.", styles["Normal"]))

    doc.build(story)

    return filename