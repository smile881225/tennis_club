# Generated by Django 5.0 on 2024-01-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reservation', '0010_course_reservation_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_reservation',
            name='class_time_end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='course_reservation',
            name='class_time_start',
            field=models.TimeField(null=True),
        ),
    ]