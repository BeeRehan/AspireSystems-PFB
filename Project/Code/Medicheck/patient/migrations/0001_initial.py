# Generated by Django 3.2.6 on 2021-08-19 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('appoinment_date', models.DateField()),
                ('reason', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=8)),
                ('doctor_name', models.CharField(max_length=20)),
                ('vaccinated', models.CharField(max_length=7)),
                ('file', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
