import tempfile
from pdfminer.high_level import extract_text
from django.shortcuts import render
from .forms import ResumeForm

def extract_text_from_pdf(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(pdf_file.read())
        temp.flush()
        text = extract_text(temp.name)
    return text

def analyze_resume(request):
    result = {}
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = form.cleaned_data['resume']
            job_desc = form.cleaned_data['job_description']
            resume_text = extract_text_from_pdf(resume_file)

            resume_words = set(resume_text.lower().split())
            job_words = set(job_desc.lower().split()) if job_desc else set()

            matched = resume_words & job_words
            missing = job_words - resume_words

            result = {
                'matched_keywords': list(matched),
                'missing_keywords': list(missing),
                'match_score': round(len(matched) / len(job_words) * 100, 2) if job_words else "N/A"
            }
    else:
        form = ResumeForm()

    return render(request, 'analyzer.html', {'form': form, 'result': result})
