# Generated by Django 4.1 on 2022-08-09 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='downloaded_date',
            field=models.DateField(default=datetime.date(2022, 8, 9)),
        ),
    ]
