from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from users.forms import LoginForm, NewUserForm


def login_user(request):
    """if request.method == "POST":
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
        pass
    context = {
        'form': LoginForm,
        'info': 'login_menu',
    }
    print("Estou aqui antes do return")"""
    return render(request, "users/login.html", {})


def logout_user(request):
    logout(request)


def register_user(request):
    # Se for post, ele pega os dados do formulário
    if request.method == "POST":
        print("Post METHOD")
        form = NewUserForm(request.POST)
        print("Form: ", form.is_valid())
        if form.is_valid():
            user = form.save()
            print("User: ", form, user)
            return redirect("/")
    form = NewUserForm()
    context = {"form": form, "info": "register_menu"}
    return render(request, "registration/register.html", context)
