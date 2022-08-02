""" Imports """
from django.views.generic import DetailView, CreateView
from car_park.models import Parking, Booking


class BookingAddView(CreateView):
    """ Rendering Booking Page """
    model = Parking
    template_name = 'booking/booking.html'
    fields = '__all__'


class BookingRecapView(DetailView):
    """ Rendering Booking Page """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'booking/booking-recap.html'

    def get_initial(self):
        return {'created_by': self.request.user}

