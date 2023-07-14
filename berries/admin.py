from django.contrib import admin

from berries.models import Berries, Categories, Units, Orders, Currency, BerryImage
from users.models import Basket


class BerriesImageInline(admin.TabularInline):
    model = BerryImage


@admin.register(Berries)
class BerriesAdmin(admin.ModelAdmin):
    inlines = [BerriesImageInline]
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('category', )
    search_fields = ('name', )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', )


@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address')
    search_fields = ('name', )


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'berry', )