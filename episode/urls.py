from django.urls import path
from . import views

urlpatterns = [
    path('', views.seasons, name='seasons'),
    path('seasons', views.seasons, name='seasons'),
    path('episodes', views.episodes, name='episodes'),
    path('episode/<int:id>', views.episode, name = 'episode'),
    path('casts', views.casts, name='casts'),
]

