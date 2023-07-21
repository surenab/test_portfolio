from django.contrib import admin
from .models import Education, Skill, Experience, Message, PortfolioProject


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date", "end_date", "grade", "created_on"]
    list_filter = ["start_date"]


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "user"]
    list_filter = ["value"]
    search_fields = ["name"]


# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience)
admin.site.register(Message)
admin.site.register(PortfolioProject)
