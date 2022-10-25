from django.db import models
from django.urls import reverse

class Semester(models.Model):   # Modelo que representa un semestre
    semester_num = models.IntegerField(help_text='Ingresar n° del semestre', null=True)
    def __str__(self):
        return 'Semestre '+str(self.semester_num)

class Course(models.Model):     # Modelo que representa un ramo
    course_name = models.CharField(max_length=200, help_text='Ingresar nombre del ramo', null=True)
    course_code = models.CharField(max_length=6, help_text='Ingresar código del ramo', null=True)
    semester_given = models.ForeignKey('Semester', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.course_name

class Topic(models.Model):
    # Campos por Rellenar
    topic_name = models.CharField(max_length=200, help_text='Ingresar nombre de la materia', null=True)
    belonging_course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    semester_given = models.ForeignKey('Semester', on_delete=models.SET_NULL, null=True)

    # Metadata
    class Meta:
        ordering = ['semester_given']
    
    # Métodos
    def get_abs_url(self):
        return reverse('model-detailed-view', args=[str(self.id)])

    def __str__(self):
        return self.topic_name