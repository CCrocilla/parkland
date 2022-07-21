from django.shortcuts import render
from contact.forms import ContactForm
# from django.views.generic import ListView, DeleteView


# Create your views here.
def ContactView(request):
    """ Contact Page """
    contact = ContactForm()
    return render(request, 'contact/contact.html', {'form': contact})
