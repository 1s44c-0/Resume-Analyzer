from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_resume, name='analyze_resume'),
]
