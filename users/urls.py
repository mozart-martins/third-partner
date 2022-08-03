from django.urls import include, path

from users.forms.loginform import CLoginForm

from . import views
from .views import LogoutView, StdIndexView

app_name = "users"

urlpatterns = [

    path("users/", include("django.contrib.auth.urls")),
    path("", StdIndexView.as_view(), name="nouser_view"),
    path("login_user", StdIndexView.as_view(), name="nouser_view"),
    path("logout/", LogoutView.as_view(), name="logout_view"),
    path("register", views.RegisterUserView.as_view(), name="register_view"),
]
