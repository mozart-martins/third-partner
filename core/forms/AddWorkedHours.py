from core.models import WorkedHours
from django import forms
from django.forms import ModelForm


class AddWorkedHours(ModelForm):
    class Meta:
        model = WorkedHours

        fields = ("worker", "date", "worked_hours", "description")
        labels = {
            "worker": "Trabalhador",
            "date": "Data",
            "worked_hours": "Horas Trabalhadas",
            "description": "Descrição",
        }
        widgets = {
            "worker": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "1",
                    "value": "1",
                    "type": "hidden",
                }
            ),
            "date": forms.DateInput(attrs={"class": "form-control ml-2", "type": "date"}),
            "worked_hours": forms.TimeInput(
                format="%H:%M",
                attrs={"class": "form-control ml-2", "type": "time"},
            ),
            "description": forms.TextInput(attrs={"class": "form-control ml-2"}),
        }
