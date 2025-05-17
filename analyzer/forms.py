from django import forms

class ResumeForm(forms.Form):
    resume = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        required=False
    )
