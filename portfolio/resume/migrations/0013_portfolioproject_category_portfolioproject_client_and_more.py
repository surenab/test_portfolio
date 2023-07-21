# Generated by Django 4.1.2 on 2023-07-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0012_portfolioproject"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolioproject",
            name="category",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="client",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="portfolioproject",
            name="url",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="portfolioproject",
            name="image",
            field=models.ImageField(upload_to="media"),
        ),
    ]
