# Generated by Django 4.1.2 on 2022-10-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solvit', '0007_alter_semester_semester_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]