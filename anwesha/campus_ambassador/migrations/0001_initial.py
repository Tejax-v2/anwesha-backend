# Generated by Django 3.2.12 on 2022-10-28 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0012_merge_20221026_1740"),
    ]

    operations = [
        migrations.CreateModel(
            name="campus_ambassador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=13)),
                ("email_id", models.EmailField(max_length=254, unique=True)),
                ("full_name", models.CharField(max_length=100)),
                (
                    "college_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "college_city",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "college_state",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("degree", models.CharField(blank=True, max_length=150, null=True)),
                ("years_of_study", models.DateField()),
                (
                    "refferal_code",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "profile_photo",
                    models.ImageField(
                        blank=True,
                        default="static/images.jpeg",
                        null=True,
                        upload_to="static/profile_photo",
                    ),
                ),
                ("age", models.SmallIntegerField(blank=True, null=True)),
                (
                    "intrests",
                    models.CharField(
                        blank=True,
                        choices=[("intrest1", "Intrest 1")],
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("others", "Others"),
                            ("rather_not_say", "Rather not say"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("score", models.IntegerField(default=0)),
                ("active", models.BooleanField(default=False)),
                ("validation", models.BooleanField(default=False)),
                (
                    "instagram_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "facebook_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("linkdin_id", models.CharField(blank=True, max_length=255, null=True)),
                ("twitter_id", models.CharField(blank=True, max_length=255, null=True)),
                ("date_of_birth", models.DateTimeField()),
                ("time_of_registration", models.DateTimeField(auto_now_add=True)),
                (
                    "anwesha_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.user",
                    ),
                ),
            ],
        ),
    ]
