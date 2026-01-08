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
<img width="1918" height="1035" alt="Scorify-Preview01" src="https://github.com/user-attachments/assets/f624f2c0-4fdc-4b37-9c2b-53ba6b56a457" />
<img width="1919" height="1036" alt="Scorify-Preview02" src="https://github.com/user-attachments/assets/ebd9001b-bb37-4d26-902e-00cdd18c7a1c" />
<img width="1919" height="1034" alt="Scorify-Preview03" src="https://github.com/user-attachments/assets/f2c9ec41-76c1-4d66-b0cc-f7bc0bca1bdf" />
<img width="1916" height="1035" alt="Scorify-Preview04" src="https://github.com/user-attachments/assets/9f705a68-014c-4564-b4d7-bc0c7be29128" />
<img width="1919" height="1038" alt="Scorify-Preview05" src="https://github.com/user-attachments/assets/8fd51f7a-ec7e-4b26-9d92-97244d26262c" />

<div align="center">
  
## 📫 Connect With Me

[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:anshu04232@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/anshu042)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/anshhu04)

**Anshu Kushwaha**

</div>
