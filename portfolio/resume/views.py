from django.shortcuts import render
from .models import Skill
from blog.models import PersonalInfo
from .forms import MessageForm


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
    personal_info = PersonalInfo.objects.get(user__username="surenabrahamyan")
    messageForm = MessageForm()
    data = {"skills": skills, "personal_info": personal_info, "messageForm": messageForm}
    return render(request, "index.html", context=data, status=status)
