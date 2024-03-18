from django.urls import path
from . import views

urlpatterns = [
    path('test_2/', views.test_2, name='test_2'),
    path('Course_content', views.Course_content, name='Course_content'),
    path('first_stage/', views.Course_content, name='first_stage'),
    path('second_stage/', views.Course_content, name='second_stage'),
    path('third_stage/', views.Course_content, name='third_stage'),
    path('', views.index, name='index'),
    path('Coursereservation/', views.CourseReservation, name='CourseReservation'),
    path('Course_search/', views.Course_search, name='Course_search')
]
