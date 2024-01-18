# Generated by Django 5.0 on 2024-01-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reservation', '0006_alter_course_reservation_course_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_reservation',
            name='Date',
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Category',
            field=models.CharField(default='課程類別', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Class_status',
            field=models.CharField(default='班級狀態，尚未達開班人數、已達開班人數、停開、僅現場報名', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Classroom',
            field=models.CharField(default='教室', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Coach_name',
            field=models.CharField(default='教練名子', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Course_code',
            field=models.CharField(default='課程代碼', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Course_name',
            field=models.CharField(default='課程名稱', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Full_number_applicants',
            field=models.IntegerField(default=26, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Period',
            field=models.CharField(default='期別', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Time_end',
            field=models.DateField(default='結束日期', null=True),
        ),
        migrations.AlterField(
            model_name='course_reservation',
            name='Time_start',
            field=models.DateField(default='開始日期', null=True),
        ),
    ]