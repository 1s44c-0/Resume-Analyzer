# 🧠 AI-Powered Resume Analyzer (Django)

This is a simple Django web application that allows users to upload their resumes and compare them against a job description. It highlights **matched** and **missing** keywords and calculates a **match score**, helping candidates optimize their resumes for job roles.

---

## 🔍 Features

- 📄 Upload PDF resumes
- 🧾 Paste or type job descriptions
- 🔍 Extracts text using `pdfminer.six`
- 📊 Calculates keyword match percentage
- ✅ Shows matched and missing keywords
- 💻 Fully responsive Bootstrap interface

---

## 🛠️ Tech Stack

- Python 3
- Django
- pdfminer.six
- Bootstrap 5
- Gunicorn (for deployment)

---

## 🚀 Live Demo

> 🔗 [https://your-deployed-url.onrender.com](https://your-deployed-url.onrender.com)

---

## 📷 Screenshots

<img src="/resume_analyzer/image1.png/800x400?text=Upload+Resume+Page" alt="Upload Page Screenshot" />
<br/>
<img src="/resume_analyzer/image2.png/800x400?text=Analysis+Result" alt="Results Page Screenshot" />

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py runserver
