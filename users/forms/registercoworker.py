from django import forms
from django.forms import ModelForm
from users.models import CoworkerModel


class AddWorkedHours(ModelForm):
    class Meta:
        model = CoworkerModel

        fields = (
            "user",
            "name_pj",
            "name_coworker",
            "cnpj",
            "specialty",
            "email",
            "whatsapp",
            "phone_numer",
            "address",
            "working_place",
            "image",
        )
        labels = {
            "user": "Usuário",
            "name_pj": "Nome da Pessoa Jurídica",
            "name_coworker": "Nome do Colaborador",
            "cnpj": "CNPJ",
            "specialty": "Especialidade",
            "email": "E-mail",
            "whatsapp": "É whatsapp?",
            "phone_numer": "Telefone",
            "address": "Endereço",
            "working_place": "Alocado em",
            "image": "Foto",
        }
        widgets = {
            "user": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "name_pj": forms.TextInput(attrs={"class": "form-control ml-2"}),
            "name_coworker": forms.TextInput(attrs={"class": "form-control ml-2"}),
            "cnpj": forms.TextInput(attrs={"class": "form-control ml-2"}),
            "specialty": forms.TextInput(attrs={"class": "form-control ml-2"}),
            "email": forms.EmailInput(attrs={"class": "form-control ml-2"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control ml-2"}),
            "whatsapp": forms.CheckboxInput(),
            "address": forms.TextInput(attrs={"class": "form-control ml-2"}),
            "working_place": forms.TextInput(attrs={"class": "form-control ml-2"}),
            "image": forms.
        }
