from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from users.models.coworkermodel import CoworkerModel


class CLoginForm(AuthenticationForm):
    model = CoworkerModel

    username = UsernameField(label="Nome do usuário",
                             widget=forms.TextInput(
                                 attrs={"class": "form-control", "id": "floatingInput", "placeholder": "Seu login"}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(
        attrs={"type": "password", "class": "form-control", "placeholder": "Sua senha"}))
