from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from berries.models import Orders, Berries, Categories

from berries.forms import OrderBerryForm


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


class BerryOrderView(TemplateView):
    template_name = 'berry_order.html'

    def get(self, request, *args, **kwargs):
        form = OrderBerryForm()
        context = {
            'form': form
        }
        return render(request, 'berry_order.html', context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = OrderBerryForm(request.POST)
        context = {
            'form': form
        }
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, 'Заказ успешно регистрирован, мы скоро с вами свяжемся!')
            return render(request, 'berry_order.html', context)

        return render(request, 'berry_order.html', context)


class OrderListView(ListView):
    template_name = "order_list.html"
    queryset = Orders.objects.all()
    context_object_name = "orders"