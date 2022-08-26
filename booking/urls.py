from django.urls import path
from .views import SearchParkingView
from .views import BookingView
from .views import RecapBookingView

urlpatterns = [
    path('search', SearchParkingView.as_view(), name='searchparking'),
    path('search/<int:id>', BookingView.as_view(), name='booking'),
    path('booking/<int:pk>', RecapBookingView.as_view(), name='recap-booking'),
]
