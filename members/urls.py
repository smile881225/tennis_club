from django.urls import path
from . import views

urlpatterns = [
    path('', views.remind, name='remind'),
    path('remind_v1_2/', views.remind_v1_2, name='remind_v1_2'),
    path('survey_view/', views.survey_view, name='survey_view'),
    path('main/', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),

]

# urlpatterns = [
#     path('main_base/', views.main_base, name='main_base'),
#     path('main/', views.main, name='main'),
#     path('survey_view/', views.survey_view, name='survey_view'),
#     path('members/', views.members, name='members'),
#     path('members/details/<int:id>', views.details, name='details'),
# ]
