from django import forms
from .models import ContactClient


class ContactClientForm(forms.ModelForm):
    class Meta:
        model = ContactClient
        fields = [
            'name',
            'phone'
        ]
