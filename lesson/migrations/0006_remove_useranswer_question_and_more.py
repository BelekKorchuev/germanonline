# Generated by Django 4.2.7 on 2023-12-16 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_rename_user_id_useranswer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='selected_choice',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
