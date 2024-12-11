# /src/pages/forms.py
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100, required=True)
    last_name = forms.CharField(label="Last Name", max_length=100, required=True)
    email = forms.EmailField(label="Your email", max_length=255, required=True)
    phone_number = forms.CharField(label="Phone Number", max_length=15, required=True)
    subject = forms.CharField(label="Subject", max_length=255, required=True)
    message = forms.CharField(label="Your message", widget=forms.Textarea, required=True)
