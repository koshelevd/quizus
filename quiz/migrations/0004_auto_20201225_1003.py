# Generated by Django 3.1.4 on 2020-12-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20201223_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='right_answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(default=False, verbose_name='Правильный ответ'),
        ),
    ]