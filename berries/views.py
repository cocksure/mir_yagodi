from django.shortcuts import render
from django.views import View


class BerriesHomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class OrderCheckView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class SingleProductView(View):
    def get(self, request):
        return render(request, 'single-product.html')


class BasketView(View):
    def get(self, request):
        return render(request, 'basket.html')


class ShopView(View):
    def get(self, request):
        return render(request, 'shop.html')
