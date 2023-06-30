from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email', 'subject')
    list_display = ('name', 'email', 'phone', )
    list_filter = ('subject',)


admin.site.register(Contact, ContactAdmin)