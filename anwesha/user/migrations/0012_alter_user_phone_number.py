# Generated by Django 4.1 on 2022-10-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0011_alter_user_accomadation_selected_alter_user_email_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default="", max_length=13),
        ),
    ]
