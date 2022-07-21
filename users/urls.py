from django.contrib.auth import views as authentication_views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_user, name='login_view'),
    path('logout/', views.logout_user, name='logout_view'),
    path('register/', views.register_user, name='register_view'),
]
