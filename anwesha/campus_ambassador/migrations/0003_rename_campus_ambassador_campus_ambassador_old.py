# Generated by Django 4.1.3 on 2022-12-10 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_user_profile_photo_alter_user_qr_code'),
        ('campus_ambassador', '0002_alter_campus_ambassador_age_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='campus_ambassador',
            new_name='campus_ambassador_old',
        ),
    ]
