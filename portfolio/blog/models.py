from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Blog(models.Model):
    header = models.TextField(max_length=60)
    posted = models.DateTimeField()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.header} user name is {self.user.username}"


class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.TextField()
