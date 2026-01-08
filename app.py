from flask import Flask, render_template, request, send_file, make_response
import conversions
import pdf_generator

app = Flask(__name__)

def get_theme():
    return request.cookies.get('theme', 'light')

@app.context_processor
def inject_theme():
    return dict(theme=get_theme())

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/set-theme/<t>")
def set_theme(t):
    resp = make_response("ok")
    resp.set_cookie('theme', t, max_age=60*60*24*30)
    return resp

@app.route("/sgpa-cgpa", methods=["GET","POST"])
def sgpa_cgpa():
    result = None
    if request.method == "POST":
        try:
            semesters = int(request.form.get("semesters", 1))
            sgpas = [request.form.get(f"sgpa{i}") for i in range(semesters)]
            result = conversions.sgpa_list_to_cgpa(sgpas)
        except Exception:
            result = "Error in calculation"
    return render_template("sgpa_cgpa.html", result=result)

@app.route("/cgpa-sgpa", methods=["GET","POST"])
def cgpa_sgpa():
    result = None
    if request.method == "POST":
        result = conversions.cgpa_to_sgpa(request.form.get("cgpa"))
    return render_template("cgpa_sgpa.html", result=result)

@app.route("/sgpa-percentage", methods=["GET","POST"])
def sgpa_percentage():
    result = None
    if request.method == "POST":
        try:
            semesters = int(request.form.get("semesters", 1))
            sgpas = [request.form.get(f"sgpa{i}") for i in range(semesters)]
            result = conversions.sgpa_to_percentage(sgpas)
        except:
            result = None
    return render_template("sgpa_percentage.html", result=result)

@app.route("/cgpa-percentage", methods=["GET","POST"])
def cgpa_percentage():
    result = None
    if request.method == "POST":
        result = conversions.cgpa_to_percentage(request.form.get("cgpa"))
    return render_template("cgpa_percentage.html", result=result)

@app.route("/mu-cgpa-percentage", methods=["GET","POST"])
def mu_cgpa_percentage():
    result = None
    if request.method == "POST":
        result = conversions.mu_cgpa_to_percentage(request.form.get("cgpa"))
    return render_template("mu_cgpa_percentage.html", result=result)

@app.route("/mu-sgpa-percentage", methods=["GET","POST"])
def mu_sgpa_percentage():
    result = None
    if request.method == "POST":
        try:
            semesters = int(request.form.get("semesters", 1))
            sgpas = [request.form.get(f"sgpa{i}") for i in range(semesters)]
            result = conversions.mu_sgpa_to_percentage(sgpas)
        except:
            result = None
    return render_template("mu_sgpa_percentage.html", result=result)

@app.route("/generate-pdf", methods=["GET","POST"])
def generate_pdf():
    if request.method == "POST":
        try:
            student_name = request.form.get("student_name", "Student")
            semesters = int(request.form.get("semesters", 1))
            sgpas = [request.form.get(f"sgpa{i}") for i in range(semesters)]

            cgpa = conversions.sgpa_list_to_cgpa(sgpas)
            std_percent = conversions.cgpa_to_percentage(cgpa)
            mu_percent = conversions.mu_cgpa_to_percentage(cgpa)

            pdf_file = pdf_generator.create_marksheet_pdf(
                student_name,
                sgpas,
                cgpa,
                std_percent,
                mu_percent
            )

            return send_file(
                pdf_file,
                as_attachment=True,
                download_name=f"{student_name.replace(' ', '_')}_Marksheet.pdf",
                mimetype='application/pdf'
            )
        except Exception as e:
            return f"Error generating PDF: {str(e)}"

    return render_template("generate_pdf.html")

if __name__ == "__main__":
    app.run(debug=True)