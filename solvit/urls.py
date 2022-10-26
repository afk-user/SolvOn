from django.urls import path
from . import views

app_name = 'solvit'
urlpatterns = [
    path('',views.index, name='index'),
    path('semesters/',views.SemestersView.as_view(), name='semesters'),
    path('course/<slug:course_code>',views.CourseView.as_view(), name='course_detail'),
]