# Generated by Django 2.1.5 on 2019-04-04 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishes',
            old_name='w_test',
            new_name='w_text',
        ),
    ]
