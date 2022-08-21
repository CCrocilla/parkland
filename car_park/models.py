from django.db import models
# https://docs.djangoproject.com/en/4.0/ref/contrib/auth/
from django.contrib.auth.models import User
from django.urls import reverse
# from django.urls import reverse_lazy
# from cloudinary.models import CloudinaryField


class Car(models.Model):
    """ Model for the Cars """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cars"
        )
    is_electric = models.BooleanField(default=False)
    registration_number = models.CharField(max_length=12)

    def __str__(self):
        return str(self.registration_number)

    def get_absolute_url(self):
        """ Redirect to List of Feedback """
        return reverse('profile-car-list')


class Area(models.Model):
    """ Model for the Parking Area """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Parking(models.Model):
    """ Model for the Parking Slot """
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="parkings"
        )
    is_electric = models.BooleanField(default=False)
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name="parkings"
        )
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class SearchParking(models.Model):
    """ Model for Booking of Parking Slots """
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="searchParking"
        )
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    recharge_ecar = models.BooleanField(default=False)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """ Redirect to List of Search Parking """
        return reverse('booking', kwargs={'id': self.id})


class Booking(models.Model):
    """ Model for Booking of Parking Slots """
    code = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="bookings"
        )
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="bookings"
        )
    recharge_car = models.BooleanField(default=False)
    parking = models.ForeignKey(
        Parking,
        on_delete=models.CASCADE,
        related_name="bookings"
        )
    final_price = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        """ Order by Create Date """
        ordering = ['created_date']

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """ Redirect to List of Feedback """
        return reverse('booking')


class Feedback(models.Model):
    """ Model for Users' Feedback """
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="feedbacks",
        default=User
        )
    created_date = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(
        Booking,
        null=True,
        on_delete=models.CASCADE,
        related_name="feedbacks"
        )
    title = models.CharField(max_length=100)
    rating_stars = models.IntegerField(null=True, blank=False)
    comment = models.TextField(max_length=100, blank=False, null=False)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']

    def __str__(self):
        """ Return Title and Comment """
        return str(self.title)

    def get_absolute_url(self):
        """ Redirect to List of Feedback """
        return reverse('list-feedback')


class Contact(models.Model):
    """ Model for Users' Feedback """
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    newsletter = models.BooleanField(default=False, blank=True, null=True)
    terms = models.BooleanField(default=False)
    body = models.TextField(blank=False, null=False)

    class Meta:
        """ Sorting by Create Date """
        ordering = ['created_date']

    def __str__(self):
        """ Return First and Last Name """
        return str(self.first_name) + ' ' + str(self.last_name)


class ProfileAvatar(models.Model):
    """ Model for Profile's Avatar """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user"
        )
    avatar = models.ImageField(
        upload_to='images/avatar/',
        blank=True,
        null=True
        )
