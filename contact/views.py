""" Imports """
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from car_park.models import Contact
from contact.forms import ContactForm


class ContactView(SuccessMessageMixin, CreateView):
    """ Contact Page """
    model = Contact
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = "Thanks! Your request have been sent successfully!"


class TermsView(View):
    template_name = 'contact/terms.html'

    def get(self, request):
        return render(request, self.template_name, {})
