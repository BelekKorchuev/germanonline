# Generated by Django 4.2.7 on 2023-12-05 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_view', '0003_listoflevels'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listoflevels',
            options={'verbose_name': 'level', 'verbose_name_plural': 'levels'},
        ),
        migrations.AlterModelOptions(
            name='ourinformations',
            options={'verbose_name': 'information', 'verbose_name_plural': 'informations'},
        ),
    ]