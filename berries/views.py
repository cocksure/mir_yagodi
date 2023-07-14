from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from berries.models import Orders, Berries, BerryImage, Categories
from berries.forms import OrderBerryForm, OrderBerryForm2
import requests


class BerriesHomeView(View):
    def get(self, request):
        berries = Berries.objects.all()
        context = {
            'berries': berries
        }
        return render(request, 'index.html', context)


class SingleProductView(DetailView):
    model = Berries
    template_name = 'single-product.html'
    pk_url_kwarg = 'id'
    context_object_name = 'berries'


class ShopView(ListView):
    model = Berries
    template_name = 'shop.html'
    context_object_name = 'berries'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        berries = context['berries']
        berry_images = BerryImage.objects.filter(berry__in=berries)
        context['berry_images'] = berry_images

        # Add category data
        categories = Categories.objects.all()
        context['categories'] = categories

        # Add pagination data


        return context


class AddToFavoritesView(LoginRequiredMixin, View):
    def post(self, request, id):
        favorites = request.session.get('favorites', [])
        if id not in favorites:
            favorites.append(id)
            request.session['favorites'] = favorites
            messages.success(request, 'Товар успешно добавлен в избранное.')
        else:
            messages.warning(request, 'Товар уже добавлен в избранное.', extra_tags='warning')

        return redirect('berries:shop-page')


class RemoveFromBasketView(View):
    def get(self, request, berry_id):
        favorites = request.session.get('favorites', [])
        if berry_id in favorites:
            favorites.remove(berry_id)
            request.session['favorites'] = favorites
            messages.success(request, 'Товар успешно удален из корзины.')
        return redirect('berries:basket-page')


class BasketView(View):
    def get(self, request):
        favorites = request.session.get('favorites', [])
        berries = Berries.objects.filter(id__in=favorites)
        context = {
            'favorites': favorites,
            'berries': berries
        }
        return render(request, 'basket.html', context)


class BerryOrderView2(TemplateView):
    template_name = 'berry_order.html'

    def get(self, request, *args, **kwargs):
        category = Categories.objects.all()
        default_phone_number = request.user.phone_number if request.user.is_authenticated else None
        form = OrderBerryForm2(initial={'phone_number': default_phone_number})
        context = {
            'form': form,
            'category': category
        }
        return render(request, 'berry_order.html', context)

    def post(self, request, *args, **kwargs):
        form = OrderBerryForm2(request.POST)

        if request.method == 'POST' and form.is_valid():
            form.save()

            # Отправка сообщения в Telegram-бот
            bot_token = '6228144935:AAHvUWyWApFwqZasUbbhgH_oRWeHNG3Q2Cs'
            chat_id = '-913715733'
            message = "Новый заказ зарегистрирован!"
            send_telegram_message(bot_token, chat_id, message)

            messages.success(request, 'Заказ успешно регистрирован, мы скоро с вами свяжемся!')
            return redirect(reverse('berries:berry-order'))

        context = {
            'form': form
        }
        return render(request, 'berry_order.html', context)


class OrderCheckView(View):
    def get(self, request):
        favorites = request.session.get('favorites', [])
        berries = Berries.objects.filter(id__in=favorites)
        default_phone_number = request.user.phone_number if request.user.is_authenticated else None
        default_email = request.user.email if request.user.is_authenticated else None
        form = OrderBerryForm(initial={'phone_number': default_phone_number, 'email': default_email})
        context = {
            'favorites': favorites,
            'berries': berries,
            'form': form
        }
        return render(request, 'checkout.html', context)

    def post(self, request, *args, **kwargs):
        form = OrderBerryForm(request.POST)

        if request.method == 'POST' and form.is_valid():
            form.save()

            # Отправка сообщения в Telegram-бот
            bot_token = '6228144935:AAHvUWyWApFwqZasUbbhgH_oRWeHNG3Q2Cs'
            chat_id = '-913715733'
            message = "Новый заказ зарегистрирован!"
            send_telegram_message(bot_token, chat_id, message)

            messages.success(request, 'Заказ успешно регистрирован, мы скоро с вами свяжемся!')
            return redirect(reverse('berries:berry-order'))

        context = {
            'form': form
        }
        return render(request, 'berry_order.html', context)


def send_telegram_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=params)
    if response.status_code != 200:
        print('Не удалось отправить сообщение в Telegram')
        print(response.text)


class OrderListView(ListView):
    template_name = "order_list.html"
    queryset = Orders.objects.all()
    context_object_name = "orders"





