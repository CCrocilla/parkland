""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from car_park.models import Parking, Booking, Car, Area
from django.core.exceptions import ValidationError
import logging


class BookingForm(ModelForm):
    """ Form for Users' Booking """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

        # if self.instance and self.instance.start_date is not None and self.instance.end_date is not None:
        #         if self.instance.start_date == self.instance.end_date:
        #             self.fields["start_date"].disabled = True

    def clean(self):
        if self.cleaned_data['start_date'] > self.cleaned_data['end_date']:
            logging.error("ERROR: Start Date > End Date")
            raise ValidationError('Error: Start Date should be greater than the End Date!')

    class Meta:
        model = Booking
        fields = "__all__"
        # fields = ('code', 'created_by', 'start_date', 'end_date', 'car', 'recharge_car', 'parking')

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            # 'created_by': forms.HiddenInput(),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'recharge_car': forms.CheckboxInput(attrs={'class': 'required checkbox'}),
        }
