from django.shortcuts import render
from django.views.generic import CreateView
from car_park.models import Contact
from contact.forms import ContactForm
from django.urls import reverse_lazy


class ContactView(CreateView):
    """ Contact Page """
    model = Contact
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('homepage')
    # def post(self, request, *args, **kwargs):
    #     contact = ContactForm()
    #     return render(request, self.template_name, {'form': contact})
