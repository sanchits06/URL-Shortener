# Generated by Django 4.1 on 2022-08-09 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='uid',
            new_name='uuid',
        ),
    ]
