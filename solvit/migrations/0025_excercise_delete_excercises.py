# Generated by Django 4.1.2 on 2022-11-12 00:26

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('solvit', '0024_excercises'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excercise_name', models.CharField(max_length=200, null=True)),
                ('belonging_topic', models.SlugField(help_text='Ingresar nombre de la materia', max_length=200, null=True)),
                ('excersise', models.ImageField(upload_to='uploads')),
                ('excersise_video', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.DeleteModel(
            name='Excercises',
        ),
    ]