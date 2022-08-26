""" Imports """
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from car_park.models import Booking
from car_park.models import SearchParking


class SearchParkingForm(ModelForm):
    """ Form for SearchParking """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True

    def clean(self):
        today = timezone.now()
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        if start_date > end_date:
            raise ValidationError(
                'Error: Start Date cannot be greater than the End Date!')
        elif start_date < today:
            raise ValidationError(
               'Error: Start Date cannot be in the past and must be \
                   greater than today!')

    class Meta:
        model = SearchParking
        fields = "__all__"

        recharge_ecar = forms.BooleanField(
            widget=forms.CheckboxInput(
                attrs={'class': 'checkbox'}), required=False)

        labels = {
            'recharge_ecar': 'Recharger Electric Car',
        }

        widgets = {
            'created_by': forms.HiddenInput(),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={
                'class': 'form-control',
                'type': 'date'
                }),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={
                'class': 'form-control',
                'type': 'date'
                }),
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

        widgets = {
            'code': forms.HiddenInput(),
            'created_by': forms.HiddenInput(),
            'start_date': forms.HiddenInput(),
            'end_date': forms.HiddenInput(),
            'car': forms.HiddenInput(),
            'recharge_car': forms.HiddenInput(),
            'parking': forms.HiddenInput(),
            'final_price': forms.HiddenInput(),
        }
