""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from car_park.models import Parking, Booking, Car 


class ParkingForm(ModelForm):
    """ Form for Users' Feedback """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
    
    class Meta:
        model = Parking
        fields = ('created_by', 'is_electric', 'recharge_car', 'area', 'location_x', 'location_y', 'price')
        labels = {
            'created_by': '',
            'is_electric': 'Electric?',
            'recharge_car': 'Recharge?',
            'area': 'Parking Area',
            'location_x': '',
            'location_y': '',
            'price': 'Price',
        }

        widgets = {
            'created_by': forms.HiddenInput(),
            'is_electric': forms.CheckboxInput(attrs={'class': 'required checkbox'}),
            'recharge_car': forms.CheckboxInput(attrs={'class': 'required checkbox'}),
            'area': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'location_x': forms.TextInput(attrs={'class': 'form-control'}),
            'location_y': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.DecimalField(attrs={'class': 'form-control'}),
        }
