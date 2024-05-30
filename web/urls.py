from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_v1_2/', views.login_v1_2, name='login_v1_2'),
    path('logout/', views.logout, name='logout'),
    # path('signin/', views.signin, name='signin'),
]