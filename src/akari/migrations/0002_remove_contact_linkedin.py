# Generated by Django 5.1.4 on 2024-12-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akari', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='linkedin',
        ),
    ]