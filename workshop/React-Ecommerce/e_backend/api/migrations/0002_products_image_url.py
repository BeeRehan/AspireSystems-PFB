# Generated by Django 4.0.4 on 2022-05-10 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_url',
            field=models.URLField(default=None),
        ),
    ]
