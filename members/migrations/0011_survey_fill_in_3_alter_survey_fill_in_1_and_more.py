# Generated by Django 5.0.1 on 2024-05-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='fill_in_3',
            field=models.TextField(null=True, verbose_name='給予系統的任何建議'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='fill_in_1',
            field=models.TextField(null=True, verbose_name='你認為此系統的 UX 有哪裡好的地方嗎？'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='fill_in_2',
            field=models.TextField(null=True, verbose_name='你認為此系統的 UX 有哪裡不好的地方嗎？'),
        ),
    ]