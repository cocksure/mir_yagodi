from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from berries.models import Orders, Berries, Categories

from berries.forms import OrderBerryForm


class BerriesHomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class OrderCheckView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class SingleProductView(DetailView):
    model = Berries
    template_name = 'single-product.html'
    pk_url_kwarg = 'id'
    context_object_name = 'berries'


class BasketView(View):
    def get(self, request):
        return render(request, 'basket.html')


class ShopView(ListView):
    model = Berries
    template_name = 'shop.html'
    context_object_name = 'berries'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context


import requests


class BerryOrderView(TemplateView):
    template_name = 'berry_order.html'

    def get(self, request, *args, **kwargs):
        form = OrderBerryForm()
        context = {
            'form': form
        }
        return render(request, 'berry_order.html', context)

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