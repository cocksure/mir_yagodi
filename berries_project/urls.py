from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django_email_verification import urls as email_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('berries.urls')),
    path('', include('contact.urls')),
    path('', include('users.urls')),
    path('email/', include(email_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

