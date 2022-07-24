""" Imports """
from django import forms
from car_park.models import Feedback


class FeedbackForm(forms.ModelForm):
    """ Form for Users' Feedback """
    class Meta:
        model = Feedback
        fields = ('title', 'comment')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }
