from django import forms
from django.forms import ModelForm
from users.models.coworkermodel import CoworkerModel


class LoginForm(ModelForm):
    class Meta:
        model = CoworkerModel
        fields = ("user_name", "password")
        labels = {"user_name": "Nome do Usuário", "password": "Senha"}
        widgets = {
            "user_name": forms.TextInput(attrs={"class": "form-control", "id": "floatingInput", "placeholder": "Seu login"}),
            "password": forms.PasswordInput(
                attrs={"type": "password", "class": "form-control"}
            ),
        }
