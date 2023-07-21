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


class Message(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)


class PortfolioProject(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    short_description = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    url = models.URLField()
