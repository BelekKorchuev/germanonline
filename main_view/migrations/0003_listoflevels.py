# Generated by Django 4.2.7 on 2023-12-05 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_view', '0002_rename_aboutus_ourinformations'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfLevels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
