from django.shortcuts import render


# Create your views here.
def contactview(request):
    """ Contact Page """
    return render(request, 'contact/contact.html')
