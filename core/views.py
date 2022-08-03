from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import AddWorkedHours
from .models import WorkedHours

menu_superuser = {'home': '', 'cadastro': 'users/register', 'serviço': '',
                  'planilha': 'planilha', 'Notas': 'notas', 'Vagas': 'vagas', 'logout': 'users/logout/'}

menu_user = {'home': '', 'planilha': 'planilha/',
             'notas': 'notas/', 'logout': 'users/logout/'}

menu_nouser = {'login': 'login_user', }

url_users = reverse_lazy('core:vacancies_view')
url_superusers = reverse_lazy('core:sheet_view')

# @method_decorator(login_required, name='dispatch')


class HomeView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "index_menu"
        context["title"] = "Home"
        if self.request.user.is_superuser:
            print("uau, superuser")
            context['menu'] = menu_superuser
        elif self.request.user.is_authenticated:
            print("É... dá pra pssar, usuário comum")
            context['menu'] = menu_user
        return context


class SheetView(ListView):
    model = WorkedHours
    template_name = "core/planilha.html"
    context_object_name = "hours"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "sheet_menu"
        context["title"] = "Planilha"
        if self.request.user.is_superuser:
            print("uau, superuser")
            context['menu'] = menu_superuser
        elif self.request.user.is_authenticated:
            print("É... dá pra pssar, usuário comum")
            context['menu'] = menu_user
        context["form"] = AddWorkedHours
        return context


class ReceiptView(TemplateView):
    template_name = "core/receipt.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "receipt_menu"
        context["title"] = "Recibos"
        if self.request.user.is_superuser:
            print("uau, superuser")
            context['menu'] = menu_superuser
        elif self.request.user.is_authenticated:
            print("É... dá pra pssar, usuário comum")
            context['menu'] = menu_user
        return context


class VacanciesView(TemplateView):
    template_name = "core/vagas.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "vacancies_menu"
        context["title"] = "Vagas"
        if self.request.user.is_superuser:
            print("uau, superuser")
            context['menu'] = menu_superuser
        elif self.request.user.is_authenticated:
            print("É... dá pra pssar, usuário comum")
            context['menu'] = menu_user
        return context


class AddHoursView(CreateView):
    model = WorkedHours
    template_name = "core/planilha.html"
    form_class = AddWorkedHours
    success_url = reverse_lazy("core:sheet_view")

    def get_initial(self, *args, **kwargs):
        initial = super(AddHoursView, self).get_initial(**kwargs)
        initial["worker"] = self.request.user
        print(initial)
        return initial
