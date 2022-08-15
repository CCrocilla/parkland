from django.urls import path
from .views import SearchParkingView, BookingView, RecapBookingView

urlpatterns = [
    path('search', SearchParkingView.as_view(), name='searchparking'),
    # re_path(r"^search/(?P<id>\d+)?/$", BookingView.as_view(), name='booking'),
    path('search/<int:id>', BookingView.as_view(), name='booking'),
    path('booking/<int:pk>', RecapBookingView.as_view(), name='recap-booking'),
    
    
]