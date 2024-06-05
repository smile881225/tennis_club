from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_v1_2/', views.login_v1_2, name='login_v1_2'),
    path('logout/', views.logout, name='logout'),
    path('practice/', include('episode.urls')),
    # path('signin/', views.signin, name='signin'),
]