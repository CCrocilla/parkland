""" Imports """
from django.views.generic import CreateView, DetailView
from car_park.models import Booking
from .forms import BookingForm


class BookingAddView(CreateView):
    """ Rendering Booking Page """
    model = Booking
    template_name = 'booking/booking.html'
    form_class = BookingForm

    def get_initial(self):
        return {'created_by': self.request.user}


class BookingRecapView(DetailView):
    """ Rendering Booking Page """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'booking/booking-recap.html'
