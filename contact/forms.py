from django import forms
from django.forms import ModelForm
from car_park.models import Contact


################################
#         Contact Form         #
################################
class ContactForm(ModelForm):
    """ Form for Users' Contact Us Page """
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'newsletter', 'body', 'terms')

        labels = {
                    'first_name': 'First Name',
                    'last_name': 'Last Name',
                    'email': 'Email',
                    'newsletter': 'Newsletter',
                    'body': 'Message',
                    'terms': 'Terms & Conditions*',
                }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'newsletter': forms.CheckboxInput(attrs={'class': 'required checkbox'}),
            'body': forms.Textarea(attrs={'rows': 3, 'cols': 5}),
            'terms': forms.CheckboxInput(attrs={'class': 'checkbox', 'required': 'true'}),
        }