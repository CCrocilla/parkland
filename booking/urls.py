from django.urls import path
from .views import BookingAddView

urlpatterns = [
    path('', BookingAddView.as_view(), name='booking'),
]
