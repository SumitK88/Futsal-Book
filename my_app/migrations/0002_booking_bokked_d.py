# Generated by Django 4.1.7 on 2023-03-19 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bokked_d',
            field=models.DateField(null=True, verbose_name='booked_d'),
        ),
    ]
