""" Imports """
from django.shortcuts import render
from django.views.generic import ListView
from .models import Feedback


# def home_view(request):
#     """ Home Page """
#     return render(request, "index.html", {})
class HomeView(ListView):
    model = Feedback
    queryset = Feedback.objects.filter().order_by('-created_date')[:3]
    template_name = 'index.html'
