from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView

from users.forms import LoginForm, NewUserForm

from .models.coworkermodel import CoworkerModel

app_name = 'users'
""" class LoginView(View):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        print("No get")

    def post(self, request):
        print("No post")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Contexto")
        context['form'] = LoginForm
        return context """


def login_user(request):

    if request.method == "POST":
        username = request.POST['user_name']
        password = request.POST['password']
        print("Dados:", username, password)
        user = authenticate(request, username=username, password=password)
        print("Estou no if de cima")
        if user is not None:
            login(request, user)
            return redirect('core:index_view')
        else:
            print("Deu erro")
            return redirect('users:login_view')
    else:
        context = {
            'form': LoginForm,
            'info': 'login_menu',
        }
        return render(request, "registration/login.html", context)


class LogoutView(View):
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
        return context


"""     def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs) """
