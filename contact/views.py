from django.shortcuts import render


# Create your views here.
def ContactView(request):
    """ Contact Page """
    return render(request, 'contact/contact.html')
