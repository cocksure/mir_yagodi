from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')
    list_display = ('username', 'email', 'phone_number')
