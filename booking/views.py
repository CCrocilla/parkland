""" Imports """
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from django.views.generic import CreateView, DetailView
from car_park.models import Booking, Parking, SearchParking
from .forms import BookingForm, SearchParkingForm
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
import logging
import json


class SearchParkingView(CreateView):
    """ Create Search Parking """
    model = SearchParking
    form_class = SearchParkingForm
    template_name = 'booking/search-parking.html'

    def get_initial(self):
        return {'created_by': self.request.user}


class AddBookingView(View):
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
            (Q(
                end_date__lt=start_date
                ) & Q(
                    start_date__lt=start_date
                    )) | (Q(
                        start_date__gt=end_date
                        ) & Q(
                            end_date__gt=end_date
                            ))
        )

        parkings_all = Parking.objects.all()
        parkings_avail = parkings_all.values_list(
            "id").difference(bookings.values_list("parking"))

        parking_ids = parkings_avail.values_list("id",  flat=True)
        parking_list = Parking.objects.filter(id__in=parking_ids)

        form_booking = self.form_class

        request.session['start_date'] = json.dumps(start_date, cls=DjangoJSONEncoder)
        request.session['end_date'] = json.dumps(end_date, cls=DjangoJSONEncoder)

        context = {
            'form': form_booking,
            'created_by': self.request.user,
            'parking_list': parking_list,
            'start_date': start_date,
            'end_date': end_date,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                booking = form.save()
                booking.created_by = self.request.user
                booking.code = booking.id
                logging.error('BOOKING ID', booking.code)
                print('BOOKING ID', booking.code)
                # booking.start_date = start_date
                # logging.error('START DATE BOOKING')
                # logging.error(booking.start_date)
                # booking.end_date = end_date
                booking.start_date = request.session.get(json.dumps('start_date', cls=DjangoJSONEncoder))
                logging.error('DATE START', booking.start_date)
                print('DATE START', booking.start_date)
                
                booking.end_date = request.session.get(json.dumps('end_date', cls=DjangoJSONEncoder))
                logging.error('DATE END', booking.end_date)
                print('DATE END', booking.end_date)
                
                booking.save()
                
                url = reverse('recap-booking')
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