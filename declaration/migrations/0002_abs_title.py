# Generated by Django 4.1.4 on 2022-12-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declaration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abs',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
