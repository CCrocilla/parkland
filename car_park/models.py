from django.db import models
# https://docs.djangoproject.com/en/4.0/ref/contrib/auth/
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


class Car(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner")
    is_electric = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=10)


class Parking(models.Model):
    name = models.CharField(max_length=100)
    is_electric = models.BooleanField(default=False)
    area_parking_id = models.IntegerField()
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
