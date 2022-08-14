from django.urls import path
from .views import SearchParkingView, AddBookingView, RecapBookingView

urlpatterns = [
    # path('', AddBookingView.as_view(), name='bookingre'),
    path('search', SearchParkingView.as_view(), name='searchparking'),
    path('search/<int:id>', AddBookingView.as_view(), name='booking'),
    path('booking/<int:pk>/details', RecapBookingView.as_view(), name='recap-booking'),
]
