""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from car_park.models import Feedback


CHOICES = [
    (1, 'Bad'), (2, 'Poor'), (3, 'OK'), (4, 'Good'), (5, 'Excellent'), ]


class FeedbackForm(ModelForm):
    """ Form for Users' Feedback """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_by'].disabled = True
    
    class Meta:
        model = Feedback
        fields = ('created_by', 'title', 'comment', 'rating_stars')
        labels = {
            'created_by': '',
            'title': 'Title',
            'comment': 'Comment',
            'rating_stars': '',
        }

        widgets = {
            'created_by': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'rating_stars': forms.HiddenInput(),
        }


class EditProfileForm(UserChangeForm):
    """ Form for User's Profile Edit Page """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')
        labels = {
            'username': 'Username',
            'first_name': 'Title',
            'last_name': 'Comment',
            'email': 'Email',
            'date_joined': 'Date Joined',
            'last_login': 'Last Login',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_joined': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'last_login': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
        }
