from django import forms
from django.forms import ModelForm
from .models import Ticket, Client


class TicketFormAdmin(ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'cod_produs',
            'nume_produs',
            'brand_produs',
            'data_ticket',
            'client',
            'agent',
            'descriere',
            'tehnician',
        )
        labels = {
            'cod_produs': '',
            'nume_produs': '',
            'brand_produs': '',
            'data_ticket': 'YYYY-MM-DD HH:MM:SS',
            'client': 'Client',
            'agent': 'Agent',
            'descriere': '',
            'tehnician': 'Tehnician',

        }
        widgets = {
            'cod_produs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cod Produs'}),
            'nume_produs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume Produs'}),
            'brand_produs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'}),
            'data_ticket': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data ticket'}),
            'client': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Client'}),
            'agent': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Agent'}),
            'descriere': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriere'}),
            'tehnician': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Tehnician'}),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = (
            'name',
            'adresa',
            'zip_code',
            'phone',
            'email_address',
            'contact',
        )
        labels = {
            'name': '',
            'adresa': '',
            'zip_code': '',
            'phone': '',
            'email_address': '',
            'contact': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume Client'}),
            'adresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa Client'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cod Postal'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Persoana de contact'}),
        }