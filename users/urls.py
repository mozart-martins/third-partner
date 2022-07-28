from django.urls import path

from . import views
from .views import LogoutView, StdIndexView, login_user

app_name = "users"

urlpatterns = [
    path("", StdIndexView.as_view(), name="nouser_view"),
    path("login_user", login_user, name="login_view"),
    path("logout/", LogoutView.as_view(), name="logout_view"),
    path("register/", views.RegisterUserView.as_view(), name="register_view"),
]
