# Generated by Django 5.1 on 2025-06-06 05:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendancemanagementsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('session_code', models.CharField(max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='apartment_application',
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('class_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendancemanagementsystem.classsession')),
            ],
            options={
                'unique_together': {('student', 'class_session')},
            },
        ),
        migrations.DeleteModel(
            name='ApartmentApplication',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
