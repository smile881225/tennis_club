from django.urls import path
from . import views

urlpatterns = [
    # path('', views.remind, name='remind'),
    path('', views.Questionnaire, name='remind'),
    path('main/', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    # path('Questionnaire.html/', views.Questionnaire, name='Questionnaire'),
]