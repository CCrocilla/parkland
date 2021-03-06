from django.db import models
# https://docs.djangoproject.com/en/4.0/ref/contrib/auth/
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Car(models.Model):
    """ Model for the Cars """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner")
    is_electric = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Car: {self.registration_number}"


class Area(models.Model):
    """ Model for the Parking Area """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        """ Sorting by Create Date """
        ordering = ['name']

    def __str__(self):
        return f"Area: {self.name}"


class Parking(models.Model):
    """ Model for the Parking Slot """
    name = models.CharField(max_length=100)
    is_electric = models.BooleanField(default=False)
    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name="area")
    location_x = models.CharField(max_length=5)
    location_y = models.IntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return f"Parking: {self.name}"


class Booking(models.Model):
    """ Model for Booking of Parking Slots """
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE,
        related_name="user")
    created_date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name="vehicle")
    parking = models.ForeignKey(
        Parking, on_delete=models.CASCADE, related_name="slot")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']
        
    def __str__(self):
        return str(self.id)


class Feedback(models.Model):
    """ Model for Users' Feedback """
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE,
        related_name="feedback")
    created_date = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="book")
    rating_stars = models.IntegerField()
    comment = models.TextField(
        blank=False, null=False, default="Leave your Feedback here!")

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']

    def __str__(self):
        return f"Feedback: {self.comment}."
