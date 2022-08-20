""" Imports """
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.db.models import Q
from car_park.models import Booking
from car_park.models import Parking
from car_park.models import SearchParking
from car_park.models import Car
from .forms import BookingForm
from .forms import SearchParkingForm


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
    form_class = BookingForm

    def get(self, request, id):
        """ Function to retrive data for Booking """
        search = SearchParking.objects.get(id=id)
        start_date = search.start_date
        end_date = search.end_date
        recharger_ecar = search.recharge_ecar

        # Return all booking of parking in the range of selected dates
        bookings = Booking.objects.exclude(
            (Q(end_date__lt=start_date) & Q(start_date__lt=start_date)) | (
                Q(start_date__gt=end_date) & Q(end_date__gt=end_date))
        )

        # Return all available Parking (Remove previous "bookings") - All parking and parking occupied. 
        parkings_avail = Parking.objects.all().values_list(
            "id", flat=True).difference(bookings.values_list("parking", flat=True))

        # Since used value_list in parking_avail mapping all opbject instead of having 
        parking_list = Parking.objects.filter(id__in=parkings_avail).order_by("name")
      
        if recharger_ecar:
            car = Car.objects.filter(user=request.user).filter(is_electric=True)
            parking_list = parking_list.filter(is_electric=True)
            print("MACCHINA ELETTRICA SI")
        else:
            car = Car.objects.filter(user=request.user)
            print("MACCHINA ELETTRICA NO")

        price = (abs((end_date - start_date).days) + 1) * PARKING_DAILY_COST
        
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
            messages.info(
                request,
                'Error: Form not filled in correctly! Please try again!'
                )
            return redirect('searchparking')


class RecapBookingView(DetailView):
    """ Show Recap Booking """
    model = Booking
    queryset = Booking.objects.all()
    template_name = 'booking/recap-booking.html'
    
    def get_initial(self):
        return {'created_by': self.request.user}