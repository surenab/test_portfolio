# Generated by Django 4.1.2 on 2023-07-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0008_education_created_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="created_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
