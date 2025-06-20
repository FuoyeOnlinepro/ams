# Generated by Django 5.1 on 2025-06-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendancemanagementsystem', '0003_classsession_department_classsession_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classsession',
            name='max_students',
            field=models.PositiveIntegerField(default=30, help_text='Maximum number of students allowed to mark attendance for this session.'),
        ),
    ]
