""" Imports """
from django.views.generic import ListView, CreateView
from car_park.models import Booking, Feedback


class DashboardView(ListView):
    """ Rendering Booking Page """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'dashboard/dashboard.html'
    

class AddFeedbackView(CreateView):
    """ Class to create Users' Feedback """
    model = Feedback
    template_name = 'dashboard/add-feedback.html'
    fields = '__all__'
