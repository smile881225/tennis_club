from django.urls import path
from . import views

urlpatterns = [
    path('test_2/', views.test_2, name='test_2'),
    path('Course_content/', views.Course_content, name='Course_content'),
    path('', views.index, name='index'),
]
