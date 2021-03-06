# Generated by Django 4.0 on 2021-12-24 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iems_app', '0006_auto_20211221_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('registeredCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iems_app.courseregistration')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iems_app.routine')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iems_app.student')),
                ('takenBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iems_app.teacher')),
            ],
        ),
        migrations.DeleteModel(
            name='Attendence',
        ),
    ]
