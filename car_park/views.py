""" Imports """
from django.shortcuts import render
from django.views import generic
from .models import Feedback


# def home_view(request):
#     """ Home Page """
#     return render(request, "index.html", {})
class HomeView(generic.ListView):
    model = Feedback
    queryset = Feedback.objects.filter().order_by('-create_date')
    template_name = 'index.html'
    paginated_by = 6



def signin_view(request):
    """ Home Page """
    return render(request, "sign-in.html", {})


def signup_view(request):
    """ Home Page """
    return render(request, "sign-up.html", {})


def reset_password_view(request):
    """ Home Page """
    return render(request, "reset-password.html", {})

