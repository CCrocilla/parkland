""" Imports """
from django.shortcuts import render


def home_view(request):
    """ Home Page """
    return render(request, "index.html", {})
