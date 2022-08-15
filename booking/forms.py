""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from car_park.models import Booking, SearchParking
import datetime
import logging


class SearchParkingForm(ModelForm):
    """ Form for SearchParking """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

    def clean(self):
        if self.cleaned_data['start_date'] > self.cleaned_data['end_date']:
            logging.error("ERROR: Start Date > End Date")
            logging.error(datetime.datetime.today())
            raise ValidationError('Error: Start Date is greater than the End Date!')

    class Meta:
        model = SearchParking
        fields = "__all__"
        
        widgets = {
            'created_by': forms.HiddenInput(),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }


class BookingForm(ModelForm):
    """ Form for Users' Booking """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
        self.fields['code'].disabled = True

    class Meta:
        model = Booking
        fields = "__all__"
        # fields = (
            # 'code', 'created_by', 'start_date', 'end_date', 'car', 'recharge_car', 'parking')

        widgets = {
            'code': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
            'start_date': forms.HiddenInput(),
            'end_date': forms.HiddenInput(),
            # 'start_date': forms.DateInput(
            #     format=('%m/%d/%Y'), attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Select a date',
            #         'type': 'date'
            #         }),
            # 'end_date': forms.DateInput(
            #     format=('%m/%d/%Y'), attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Select a date',
            #         'type': 'date'
            #         }),
            'recharge_car': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'parking': forms.HiddenInput(),
        }
