# Generated by Django 4.1.2 on 2022-10-25 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solvit', '0005_rename_semester_semester_semester_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester_given',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='solvit.semester'),
        ),
    ]
