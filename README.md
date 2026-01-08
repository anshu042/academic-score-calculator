# 🎓 Academic Score Calculator

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?style=for-the-badge&logo=flask&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-Deploy-black?style=for-the-badge&logo=vercel&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A comprehensive web application designed to simplify academic conversions between CGPA, SGPA, and Percentage, featuring specific support for **Mumbai University** standards and instant PDF report generation.

## ✨ Features

This application acts as a central hub for students to calculate and document their academic performance.

### 🧮 Core Calculators
| Calculator Type | Description |
|-----------------|-------------|
| **CGPA ↔ Percentage** | Convert cumulative grades to percentage and vice-versa. |
| **CGPA ↔ SGPA** | Calculate Semester GPA from Cumulative GPA. |
| **SGPA ↔ Percentage** | Direct conversion for individual semester performance. |

### 🎓 University Specials
* **Mumbai University (MU) Mode:** Specialized algorithms tailored for Mumbai University grading standards (CGPA & SGPA to Percentage).

### 📄 Utilities
* **PDF Report Generator:** Instantly generate a downloadable PDF report of your calculated scores for official use or record-keeping.

---

## 🚀 Live Demo

You can access the deployed application here:
<br />
👉 **[https://scorifyy.vercel.app/]**
<br />

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Jinja2 Templates
* **PDF Generation:** ReportLab, Pillow (PIL)
* **Deployment:** Vercel (Serverless Python)

---

## 📂 Project Structure

```text
academic-score-calculator/
├── app.py                  # Main Flask application entry point
├── conversions.py          # Logic for score calculation and conversion formulas
├── pdf_generator.py        # Logic for generating PDF reports using ReportLab
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment configuration
├── static/
│   └── style.css           # Global application styling
└── templates/              # Jinja2 HTML Templates
    ├── base.html           # Base layout
    ├── index.html          # Homepage
    ├── generate_pdf.html   # PDF download page
    ├── cgpa_percentage.html
    ├── cgpa_sgpa.html
    ├── sgpa_cgpa.html
    ├── sgpa_percentage.html
    ├── mu_cgpa_percentage.html  # Mumbai University specific
    └── mu_sgpa_percentage.html  # Mumbai University specific
```
## 🖥️ Preview

<div align="center">
  
## 📫 Connect With Me

[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:anshu04232@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/anshu042)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/anshhu04)

**Anshu Kushwaha**

</div>
