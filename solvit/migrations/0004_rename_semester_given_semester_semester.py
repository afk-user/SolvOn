# Generated by Django 4.1.2 on 2022-10-24 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solvit', '0003_course_semester_alter_topic_belonging_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='semester_given',
            new_name='semester',
        ),
    ]
