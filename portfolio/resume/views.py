from django.shortcuts import render
from .models import Skill, PortfolioProject
from blog.models import PersonalInfo
from .forms import MessageForm
from django.shortcuts import get_object_or_404


def home(request):

    status = 200

    if request.method == "POST":
        print("POSTED DATA")
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            status = 201
        else:
            print("TELL them that sent data is not valid")

    skills = Skill.objects.filter(user__username="admin")
    portfolio_projects = PortfolioProject.objects.all()

    personal_info = PersonalInfo.objects.get(user__username="surenabrahamyan")
    messageForm = MessageForm()
    data = {
        "portfolio_projects": portfolio_projects,
        "skills": skills,
        "personal_info": personal_info,
        "messageForm": messageForm,
    }
    return render(request, "index.html", context=data, status=status)


def portfolio_project(request, id):
    project = get_object_or_404(PortfolioProject, id=id)
    return render(request, "portfolio-details.html", context={"project": project})
