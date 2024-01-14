from django.urls import path
from . import views

urlpatterns = [
    path('', views.Course_reservation, name='Course_reservation'),
]
