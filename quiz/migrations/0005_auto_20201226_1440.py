# Generated by Django 3.1.4 on 2020-12-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20201225_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(max_length=200, verbose_name='Ответ'),
        ),
    ]
