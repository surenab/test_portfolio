from django.shortcuts import render
from .models import Skill
from blog.models import PersonalInfo


def home(request):
    skills = Skill.objects.filter(user__username="admin")
    personal_info = PersonalInfo.objects.get(user__username="surenabrahamyan")
    data = {
        "skills": skills,
        "personal_info": personal_info,
    }
    return render(request, "index.html", context=data)
