# Generated by Django 4.1 on 2024-10-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news_app", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="slug",
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
