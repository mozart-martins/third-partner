from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import NewUserForm
from users.forms.loginform import CLoginForm

from .models.coworkermodel import CoworkerModel

app_name = 'users'
superuser = False
user = False
menu_superuser = {'home': '', 'cadastro': 'users/register', 'serviço': '',
                  'planilha': 'planilha', 'Notas': 'notas', 'Vagas': 'vagas', 'logout': 'users/logout/'}

menu_user = {'home': '', 'planilha': 'planilha/',
             'notas': 'notas/', 'logout': 'users/logout/'}
menu_nouser = {'login': 'login_user', }
url_users = reverse_lazy('core:vacancies_view')
url_superusers = reverse_lazy('core:sheet_view')


class StdIndexView(LoginView):
    template_name = 'users/index.html'
    sucess_url = reverse_lazy('core:vacancies_view')
    global menu_superuser, menu_user

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            print("Ta autenticado, superuser.")

            return HttpResponseRedirect(url_superusers)
        elif request.user.is_authenticated:
            print("Ta autenticado, user comum.")

            return HttpResponseRedirect(url_superusers)
        else:
            return render(request, self.template_name, {'form': CLoginForm})

    def form_valid(self, form):
        login(self.request, form.get_user())

        if (form.get_user().is_superuser):
            return HttpResponseRedirect(url_superusers)
        else:
            return HttpResponseRedirect(url_users)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'site': current_site,
            'site_name': current_site.name,
            **(self.extra_context or {})
        })
        return context


class LogoutView(LogoutView):
    def get(self, request):
        print("No get")

    def post(self, request):
        print("No post")


class RegisterUserView(CreateView):
    model = CoworkerModel
    form_class = NewUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy('core:index_view')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "register_menu"
        if self.request.user.is_superuser:
            print("uau, superuser")
            context['menu'] = menu_superuser
        elif self.request.user.is_authenticated:
            print("É... dá pra pssar, usuário comum")
            context['menu'] = menu_user
        return context
