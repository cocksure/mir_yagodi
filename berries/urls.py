from django.urls import path

from berries.views import BerriesHomeView, SingleProductView, BasketView, ShopView, \
    OrderCheckView, BerryOrderView, OrderListView

app_name = 'berries'

urlpatterns = [
    path('', BerriesHomeView.as_view(), name='home-page'),
    path('single-product/<int:id>/', SingleProductView.as_view(), name='single-page'),

    path('basket/', BasketView.as_view(), name='basket-page'),
    path('shop/', ShopView.as_view(), name='shop-page'),
    path('order-check/', OrderCheckView.as_view(), name='order-check'),
    path('berry-order/', BerryOrderView.as_view(), name='berry-order'),
    path('orders/', OrderListView.as_view(), name='orders'),

]
