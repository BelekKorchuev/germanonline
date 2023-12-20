# Generated by Django 4.2.7 on 2023-12-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_view', '0008_listoftheme_theme_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
