# Generated by Django 4.2.2 on 2023-12-22 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0007_court_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date(2023, 12, 22)),
        ),
    ]
