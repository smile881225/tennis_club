# Generated by Django 4.2.10 on 2024-05-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reservation', '0018_alter_course_reservation_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_reservation_history',
            name='class_time_end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='course_reservation_history',
            name='class_time_start',
            field=models.TimeField(null=True),
        ),
    ]
