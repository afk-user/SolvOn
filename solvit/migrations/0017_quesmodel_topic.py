# Generated by Django 4.1.2 on 2022-11-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solvit', '0016_quesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='topic',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
