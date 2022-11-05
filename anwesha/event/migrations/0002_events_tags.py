# Generated by Django 4.1 on 2022-10-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="tags",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1", "Tech"),
                    ("2", "Cultural"),
                    ("3", "Sports"),
                    ("4", "Gaming"),
                    ("5", "Workshop"),
                    ("6", "Other"),
                ],
                max_length=40,
            ),
        ),
    ]
