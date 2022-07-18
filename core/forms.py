from django import forms

from .models import HoraTrabalhada

class AddWorkedHours(forms.ModelForm):
    class Meta:
        model = HoraTrabalhada
        fields = ('worker', 'date', 'worked_hours', 'description')
        labels = {'worker': 'Trabalhador', 'date':'Data', 'worked_hours':'Horas Trabalhadas', 'description':'Descrição'}
        widgets {
            'worker': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            
        }