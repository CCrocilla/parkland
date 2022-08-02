""" Imports """
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from car_park.models import Feedback, Car, ProfileAvatar


CHOICES = [
    (1, 'Bad'), (2, 'Poor'), (3, 'OK'), (4, 'Good'), (5, 'Excellent'), ]

################################
#         Feedback Forms       #
################################

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


################################
#         Profile Forms        #
################################

class EditProfileForm(UserChangeForm):
    """ Form for User's Profile Edit Page """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')
        labels = {
            'username': 'Username*',
            'first_name': 'First Name*',
            'last_name': 'Last Name*',
            'email': 'Email*',
            'date_joined': 'Date Account Creation',
            'last_login': 'Last Login',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_joined': forms.DateTimeInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'form-control',
                    'required': 'false'
                    }),
            'last_login': forms.DateTimeInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'form-control',
                    'required': 'false'
                    }),
        }


class ProfileAvatarForm(ModelForm):
    """ Form for Users' Avatar """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        model = ProfileAvatar
        fields = ('user', 'avatar')
        labels = {
            'user': '',
            'avatar': 'Upload your Avatar!',
        }


class ProfileCarForm(ModelForm):
    """ Form for Users' Feedback """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True
    
    class Meta:
        model = Car
        fields = ('user', 'is_electric', 'registration_number')
        labels = {
            'user': '',
            'is_electric': 'Electric Car',
            'registration_number': 'Car Registration Number',
        }

        widgets = {
            'user': forms.HiddenInput(),
            'is_electric': forms.CheckboxInput(attrs={'class': 'required checkbox'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
        }