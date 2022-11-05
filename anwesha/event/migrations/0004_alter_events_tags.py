# Generated by Django 4.1 on 2022-10-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0003_alter_events_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="tags",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A", "Tech"),
                    ("B", "Cultural"),
                    ("C", "Sports"),
                    ("D", "Gaming"),
                    ("E", "Workshop"),
                    ("F", "Other"),
                ],
                max_length=40,
            ),
        ),
    ]
