from django.urls import path
from . import views

urlpatterns = [
    path('', views.remind, name='remind'),
    path('survey_view/', views.survey_view, name='survey_view'),
    path('main/', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]

