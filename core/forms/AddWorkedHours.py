from django import forms
from models import WorkedHours


class AddWorkedHours(forms.ModelForm):
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
                attrs={"class": "form-control", "type": "hidden"}
            ),
            "date": forms.DateInput(attrs={"class": "form-control"}),
            "worked_hours": forms.TimeInput(
                format="%H:%M", attrs={"class": "form-control", "type": "time"}
            ),
            "description": forms.TextInput(attrs={"class": "form-control"}),
        }
