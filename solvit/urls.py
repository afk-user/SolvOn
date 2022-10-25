from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('semesters/',views.SemestersView.as_view(), name='semesters')
]