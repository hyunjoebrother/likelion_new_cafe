# Generated by Django 3.2.5 on 2021-07-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalreservation',
            name='wating_time',
        ),
        migrations.AddField(
            model_name='personalreservation',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
