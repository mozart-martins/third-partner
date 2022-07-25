from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import LoginForm, NewUserForm

from .models.coworkermodel import CoworkerModel


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("Estou no if de cima")
        if user is not None:
            login(request, user)
            print("Login ok, is not None")
            return redirect('core:index_view')
        else:
            print("Estou no else decima")
            messages.success(
                request, ("There was an error logging in, try again..."))
            return redirect('users:login_view')
    else:
        print("Estou no else debaixo")
    context = {
        'form': LoginForm,
        'info': 'login_menu',
    }
    print("Estou aqui antes do return")
    return render(request, "users/login.html", context)


def logout_user(request):
    logout(request)


class RegisterUserView(CreateView):
    model = CoworkerModel
    form_class = NewUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy('core:index_view')
