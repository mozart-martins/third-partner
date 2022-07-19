from django.views.generic import TemplateView
from django.views.generic.list import ListView

from .models import WorkedHours


class SheetView(ListView):
    model = WorkedHours
    template_name = 'core/planilha.html'
    context_object_name = 'hours'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = 'sheet_menu'
        return context


class ReceiptView(TemplateView):
    template_name = 'core/receipt.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = 'receipt_menu'
        return context


class VacanciesView(TemplateView):
    template_name = 'core/vagas.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = 'vacancies_menu'
        return context
