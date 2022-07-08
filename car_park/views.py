""" Imports """
from django.shortcuts import render


def home_view(request):
    """ Home Page """
    return render(request, "index.html", {})


def signin_view(request):
    """ Home Page """
    return render(request, "sign-in.html", {})


def signup_view(request):
    """ Home Page """
    return render(request, "sign-up.html", {})


def reset_password_view(request):
    """ Home Page """
    return render(request, "reset-password.html", {})
