# Generated by Django 4.1.4 on 2022-12-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0002_auto_20221212_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
