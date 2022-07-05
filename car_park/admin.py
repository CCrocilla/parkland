from django.contrib import admin
from .models import Car, Parking


# admin.site.register(Car)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'is_electric', 'registration_number')


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_electric', 'location_x', 'location_y', 'price', 'area_parking_id')
