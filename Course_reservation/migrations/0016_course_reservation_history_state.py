# Generated by Django 4.2.10 on 2024-02-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reservation', '0015_course_reservation_history_coach_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_reservation_history',
            name='State',
            field=models.CharField(help_text='預約狀態，完成預約、已取消', max_length=255, null=True),
        ),
    ]
