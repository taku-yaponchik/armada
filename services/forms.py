from django.forms import ModelForm
from django import forms
from .models import ContactClient


class ContactClientForm(forms.ModelForm):

    class Meta:
        model = ContactClient
        fields = [
            'name',
            'phone'
        ]

        widgets = {
            'name': forms.TextInput(attrs = {'class': "control",
                                             'id': "name",
                                             'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': "control",
                                           'id': "phone",
                                           'placeholder': '+996 700 123 456'}),
            }
