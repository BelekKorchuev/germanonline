# Generated by Django 4.2.7 on 2023-12-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_view', '0004_alter_listoflevels_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listoflevels',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]