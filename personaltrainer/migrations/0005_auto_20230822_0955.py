# Generated by Django 3.2.20 on 2023-08-22 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personaltrainer', '0004_alter_bookingsession_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingsession',
            name='slug',
        ),
        migrations.AlterField(
            model_name='bookingsession',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Select date'),
        ),
    ]