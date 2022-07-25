from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")
        labels = {"username": "Usuário", "password": "Senha"}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(
                attrs={"type": "password mr-1", "class": "form-control"}
            ),
        }
