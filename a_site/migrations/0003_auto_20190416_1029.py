# Generated by Django 2.2 on 2019-04-16 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_site', '0002_auto_20190404_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='w_text',
            field=models.CharField(max_length=1000),
        ),
    ]