from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CoworkerModel


class NewUserForm(UserCreationForm):
    user_name = forms.CharField(
        label="Nome do Usuário",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "focus:outline-none", "placeholder": "user123"}
        ),
    )
    name_pj = forms.CharField(
        label="Nome da Pessoa Jurídica",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "focus:outline-none", "placeholder": "Jhonny Inc."}
        ),
    )
    name_coworker = forms.CharField(
        label="Nome Completo",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "focus:outline-none", "placeholder": "Jhonny Cash"}
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "focus:outline-none",
                   "placeholder": "demo@gmail.com"}
        ),
    )
    phone_number = forms.CharField(
        label="Telefone",
        required=True,
        widget=forms.TextInput(attrs={"class": "focus:outline-none"})
    )
    password1 = forms.CharField(
        label="Senha",
        required=True, widget=forms.PasswordInput(attrs={"class": "focus:outline-none"})
    )
    password2 = forms.CharField(
        label="Confirme Senha",
        required=True, widget=forms.PasswordInput(attrs={"class": "focus:outline-none"})
    )

    class Meta:
        model = CoworkerModel
        labels = {"user_name": "Nome do Usuário", "name_pj": "Nome da Pessoa Jurídica", "name_coworker": "Nome Completo",
                  "email": "E-mail", "phone_number": "Número de Telefone", "password1": "Senha", "password2": "Confirme sua Senha"}
        fields = ("user_name", "name_pj", "name_coworker", "email", "phone_number",
                  "password1", "password2")
