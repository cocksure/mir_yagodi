from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from users.forms import UserCreateForm, CustomAuthenticationForm
from users.models import CustomUser

from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'create_form': create_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            messages.success(request, "Вы успешно прошли регистрацию.")
            create_form.save()
        else:
            context = {
                'create_form': create_form
            }
            return render(request, 'users/register.html', context)
        return redirect('users:login')


class LoginView(View):
    def get(self, request):
        login_form = CustomAuthenticationForm()

        return render(request, 'users/login.html', {"login_form": login_form})

    def post(self, request):
        login_form = CustomAuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            messages.success(request, "Вы успешно вошли в сайт.")

            return redirect("berries:home-page")
        else:
            return render(request, 'users/login.html', {"login_form": login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "Вы успешно вышли из системы.")
        return redirect('users:login')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users/profile.html", {"user": request.user})
