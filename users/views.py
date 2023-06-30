from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "create_form": create_form
        }
        return render(request, "register.html", context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
        else:
            context = {
                "create_form": create_form
            }
            return render(request, "register.html", context)

        return redirect('users:login')


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()

        return render(request, 'login.html', {"login_form": login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            messages.success(request, "Вы успешно вошли в наш сайт.")

            return redirect("berries:home-page")
        else:
            return render(request, 'login.html', {"login_form": login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "Вы успешно вышли из системы.")
        return redirect("berries:home-page")