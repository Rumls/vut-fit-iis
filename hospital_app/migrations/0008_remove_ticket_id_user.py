# Generated by Django 3.1.2 on 2020-11-26 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0007_remove_healthrecord_id_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id_user',
        ),
    ]
