""" Imports """
from django.views import generic
from car_park.models import Booking


# Create your views here.
class DashboardView(generic.ListView):
    """ Rendering Booking Page """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'dashboard/dashboard.html'
