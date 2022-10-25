from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Semester, Course, Topic

def index(request):
    num_semesters = Semester.objects.all().count()
    num_courses = Course.objects.all().count()
    num_topics = Topic.objects.all().count()

    context = {
        'num_semesters': num_semesters,
        'num_courses': num_courses,
        'num_topics': num_topics,
    }
    return render(request, 'index.html', context=context)

class SemestersView(generic.ListView):
    template_name = 'semesters.html'
    context_object_name = 'semester_list'

    def get_queryset(self):
        return Semester.objects.all().order_by('semester_num')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_list'] = list(Course.objects.all())
        return context
