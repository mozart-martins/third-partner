from django.urls import path

from . import views
from .views import LogoutView, login_user

app_name = "users"

urlpatterns = [
    path("login_user", login_user, name="login_view"),
    path("logout/", LogoutView.as_view(), name="logout_view"),
    path("register/", views.RegisterUserView.as_view(), name="register_view"),
]
