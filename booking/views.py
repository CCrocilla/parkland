""" Imports """
from django.views.generic import ListView
from car_park.models import Booking


# Create your views here.
class BookingView(ListView):
    """ Rendering Booking Page """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'booking/booking.html'
