# Generated by Django 3.2.6 on 2021-08-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="account_status",
            field=models.CharField(default="Open", max_length=20),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="attempt",
            field=models.IntegerField(default=0),
        ),
    ]
