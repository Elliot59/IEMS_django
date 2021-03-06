# Generated by Django 3.2.9 on 2021-12-21 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iems_app', '0005_attendence_routine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iems_app.batch'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iems_app.semester'),
        ),
        migrations.AlterField(
            model_name='routine',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iems_app.teacher'),
        ),
    ]
