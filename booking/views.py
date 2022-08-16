""" Imports """
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from django.views.generic import CreateView, DetailView
from car_park.models import Booking, Parking, SearchParking, Car
from .forms import BookingForm, SearchParkingForm
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
import logging
import json

PARKING_DAILY_COST = 8


class SearchParkingView(CreateView):
    """ Create Search Parking """
    model = SearchParking
    form_class = SearchParkingForm
    template_name = 'booking/search-parking.html'

    def get_initial(self):
        return {'created_by': self.request.user}

class BookingView(View):
    """ Create Booking """
    model = Booking
    template_name = 'booking/booking.html'
    queryset = Booking.objects.all()
    form_class = BookingForm

    def get(self, request, id):
        """ Function to retrive data for Booking """
        id_search = id
        search = SearchParking.objects.get(id=id_search)
        start_date = search.start_date
        end_date = search.end_date

        bookings = Booking.objects.exclude(
            (Q(end_date__lt=start_date) & Q(start_date__lt=start_date)) | (
                Q(start_date__gt=end_date) & Q(end_date__gt=end_date))
        )

        parkings_all = Parking.objects.all()
        parkings_avail = parkings_all.values_list(
            "id").difference(bookings.values_list("parking"))

        parking_ids = parkings_avail.values_list("id",  flat=True)
        parking_list = Parking.objects.filter(id__in=parking_ids)

        car = Car.objects.filter(user=request.user)

        price = (abs((end_date - start_date).days) + 1) * PARKING_DAILY_COST
        print(price)
        
        context = {
            'form': BookingForm({
                'start_date': start_date,
                'end_date': end_date,
                'final_price': price,
                'car': car,
                }),
            'created_by': self.request.user,
            'parking_list': parking_list,
            'start_date': start_date,
            'end_date': end_date,
            'final_price': price,
            'car_list': car,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """ Post Function Booking """
        form = self.form_class(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.created_by = self.request.user
            booking.code = booking.id
            booking.start_date = request.POST.get('start_date', None)
            booking.end_date = request.POST.get('end_date', None)
            booking.final_price = request.POST.get('final_price', None)
            booking.save()

            url = reverse('recap-booking', args=(booking.pk, ))
            return HttpResponseRedirect(url)
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})


class RecapBookingView(DetailView):
    """ Show Recap Booking """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'booking/recap-booking.html'
    
    def get_initial(self):
        return {'created_by': self.request.user}