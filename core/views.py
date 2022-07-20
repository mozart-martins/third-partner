from django.views.generic import TemplateView
from django.views.generic.list import ListView

from .forms import AddWorkedHours
from .models import WorkedHours


class SheetView(ListView):
    model = WorkedHours
    template_name = "core/planilha.html"
    queryset = WorkedHours.objects.all()
    context_object_name = "hours"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "sheet_menu"
        context["title"] = "Planilha"
        context["form"] = AddWorkedHours
        return context


class ReceiptView(TemplateView):
    template_name = "core/receipt.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "receipt_menu"
        context["title"] = "Recibos"
        return context


class VacanciesView(TemplateView):
    template_name = "core/vagas.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "vacancies_menu"
        context["title"] = "Vagas"
        return context
