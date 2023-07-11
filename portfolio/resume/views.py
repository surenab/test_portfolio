from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill


def home(request):
    skills = Skill.objects.all()
    data = {
        "first_name": "Suren",
        "last_name": "Abrahamyan",
        "skills": skills,
    }
    return render(request, "index.html", context=data)
