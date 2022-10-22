from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    name = models.CharField('Nume Client', max_length=120)
    adresa = models.CharField(max_length=300, blank=True)
    zip_code = models.CharField('Cod Postal', max_length=15, blank=True)
    phone = models.CharField('Telefon contact', max_length=25, blank=True)
    email_address = models.EmailField('Email ', blank=True)
    contact = models.CharField("Persoana de contact", max_length=15, blank=True)

    def __str__(self):
        return self.name


class CrmUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Ticket(models.Model):
    cod_produs = models.CharField('Cod Produs', max_length=120)
    nume_produs = models.CharField('Nume Produs', max_length=120)
    brand_produs = models.CharField('Brand', max_length=120)
    data_ticket = models.DateTimeField('Data ticket')
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    agent = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    descriere = models.TextField(blank=True)
    tehnician = models.ManyToManyField(CrmUser, blank=True)
    approved = models.BooleanField('Aprobat', default=False)

    def __str__(self):
        return self.cod_produs
