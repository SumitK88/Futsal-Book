# Generated by Django 4.1.7 on 2023-03-19 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_booking_bokked_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pimg',
            field=models.FileField(default='defaultpic.png', max_length=250, null=True, upload_to='displaypic/'),
        ),
    ]