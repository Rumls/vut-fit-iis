# Generated by Django 3.1.2 on 2020-11-30 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0002_auto_20201130_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalact',
            old_name='compensatable',
            new_name='covered',
        ),
        migrations.RemoveField(
            model_name='healthrecord',
            name='covered',
        ),
    ]
