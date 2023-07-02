from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView

from contact.forms import ContactForm


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return render(request, 'contact.html')
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)
