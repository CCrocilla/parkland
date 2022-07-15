from django.contrib import admin
from .models import Car, Parking, Area, Booking, Feedback


# admin.site.register(Car)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """ Cars """
    list_display = (
        'user', 'is_electric', 'registration_number')


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    """ Parking Slots """
    list_display = (
        'name', 'is_electric', 'location_x', 'location_y', 'price', 'area')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    """ Parking Area """
    list_display = (
        'name', 'description')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Booking """
    list_display = (
        'created_by', 'car', 'parking', 'created_date', 'price')
    list_filter = (
        'created_date', 'start_date', 'end_date')
    search_fields = (
        'created_by', 'car', 'created_date', 'start_date', 'end_date')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """ Users' Feedback """
    list_display = (
        'created_by', 'created_date', 'booking', 'rating_stars', 'comment')
