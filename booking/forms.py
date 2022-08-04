""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from car_park.models import Parking, Booking, Car, Area


class BookingForm(ModelForm):
    """ Form for Users' Booking """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
    
    class Meta:
        model = Booking
        fields = ('name', 'created_by', 'start_date', 'end_date', 'area', 'car', 'recharge_car', 'parking', 'price')


        widgets = {
            'name': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'recharge_car': forms.CheckboxInput(attrs={'class': 'required checkbox'}),
        }
