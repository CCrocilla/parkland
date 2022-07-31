from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField(label="Enter First Name", max_length=50)
    lastname = forms.CharField(label="Enter Last Name", max_length=100)
    email = forms.EmailField(label="Enter Email Address")
