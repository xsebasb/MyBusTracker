# Generated by Django 3.2.3 on 2021-05-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]