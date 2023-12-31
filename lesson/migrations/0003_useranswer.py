# Generated by Django 4.2.7 on 2023-12-13 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_question_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.question')),
                ('selected_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.choice')),
            ],
        ),
    ]
