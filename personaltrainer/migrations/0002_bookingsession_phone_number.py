# Generated by Django 3.2.20 on 2023-08-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaltrainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingsession',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
