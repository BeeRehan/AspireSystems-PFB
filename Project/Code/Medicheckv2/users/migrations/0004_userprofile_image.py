# Generated by Django 3.2.7 on 2021-09-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_userprofile_secret_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics"),
        ),
    ]