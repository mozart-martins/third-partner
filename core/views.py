from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView  # , DeleteView, UpdateView
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


class AddHoursView(CreateView):
    model = WorkedHours
    template_name = "core/planilha.html"
    form_class = AddWorkedHours
    success_url = reverse_lazy('core:sheet_view')

    def get_initial(self, *args, **kwargs):
        initial = super(AddHoursView, self).get_initial(**kwargs)
        initial['worker'] = self.request.user
        print(initial)
        return initial
