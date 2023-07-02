from django.contrib import admin

from berries.models import Berries, Categories, Units, Orders, Currency


@admin.register(Berries)
class BerriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('category', )
    search_fields = ('name', )


@admin.register(Categories)
class BerriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', )


@admin.register(Units)
class BerriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Currency)
class BerriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Orders)
class BerriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'berry', 'category', 'amount', 'address')
    list_filter = ('category', )
    search_fields = ('name', )
