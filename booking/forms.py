""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from car_park.models import Parking, Booking, Car, Area
from django.core.exceptions import ValidationError
import datetime
import logging


class BookingForm(ModelForm):
    """ Form for Users' Booking """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

    # if self.instance and self.instance.start_date is not None and self.instance.end_date is not None:
    #         if self.instance.start_date == self.instance.end_date:
    #             self.fields["start_date"].disabled = True
    # def clean_start_date For Specific Field
    
    def clean(self):
        if self.cleaned_data['start_date'] > self.cleaned_data['end_date']:
            logging.error("ERROR: Start Date > End Date")
            logging.error(datetime.datetime.today())
            raise ValidationError('Error: Start Date is greater than the End Date!')
    
    # def clean_start_date(self):
    #     start_date = self.cleaned_data['start_date']
        
    #     if start_date < datetime.datetime.today():
    #         raise ValidationError('Error: Start Date cannot be in the past')
        

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
