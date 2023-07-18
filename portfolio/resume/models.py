from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} skill value is {self.value}"


class Education(models.Model):
    university_name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    grade = models.TextField(max_length=30, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.university_name} university, grade is {self.grade}"


class Experience(models.Model):
    job_possition = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField()
    address = models.TextField()
    job_description = models.TextField()
    company_name = models.TextField()
    company_logo = models.ImageField()

    def __str__(self) -> str:
        return f"{self.company_name} company, job_possition is {self.job_possition}"
