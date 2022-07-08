from django.db import models
# https://docs.djangoproject.com/en/4.0/ref/contrib/auth/
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


class Car(models.Model):
    """ Model for the Cars """
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner")
    is_electric = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=10)


class Area(models.Model):
    """ Model for the Parking Area """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Parking(models.Model):
    """ Model for the Parking Slot """
    name = models.CharField(max_length=100)
    is_electric = models.BooleanField(default=False)
    area_id = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name="area")
    location_x = models.CharField(max_length=5)
    location_y = models.IntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=2)


class Booking(models.Model):
    """ Model for Booking of Parking Slots """
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    car_id = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name="vehicle")
    parking_id = models.ForeignKey(
        Parking, on_delete=models.CASCADE, related_name="slot")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    
    class Meta:
        """ Sorting by Create Date """
        ordering = ['create_date']


class Feedback(models.Model):
    """ Model for Users' Feedback """
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="feedback")
    rating_stars = models.IntegerField()
    comment = models.TextField(
        blank=False, null=False, default="Leave your Feedback here!")
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['create_date']

    def __str__(self):
        return f"Feedback: {self.comment}."
