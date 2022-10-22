from datetime import datetime
from django.shortcuts import render, redirect
from .models import Ticket, Client
from .forms import TicketFormAdmin, ClientForm
from django.http import HttpResponseRedirect, HttpResponse
import csv
from .utils import render_to_pdf
from django.core.paginator import Paginator


def generate_to_pdf(request):
    tickets = Ticket.objects.all()
    clients = Client.objects.all()
    for ticket in tickets:
        for client in clients:
            data = {
                'numar_deviz': ticket.id,
                'cod_produs': ticket.cod_produs,
                'nume_produs': ticket.nume_produs,
                'brand_produs': ticket.brand_produs,
                'data_ticket': ticket.data_ticket,
                'client': ticket.client,
                'agent': ticket.agent,
                'descriere': ticket.descriere,
                'tehnician': ticket.tehnician,
                'approved': ticket.approved,
                'name': client.name,
                'adresa': client.adresa,
                'cod_postal': client.zip_code,
                'telefon': client.phone,
                'email_address': client.email_address,
                'contact': client.contact,
            }

            pdf = render_to_pdf('pdf/deviz.html', data)
            response = HttpResponse(pdf, content_type='application/pdf')
            return response


def client_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= client.csv'
    writer = csv.writer(response)
    clients = Client.objects.all()
    writer.writerow([
        'Nume Client',
        'Adresa',
        'Cod Postal',
        'Telefon',
        'Adresa email',
        'Persoana de contact',
    ])
    for client in clients:
        writer.writerow([
            client.name,
            client.adresa,
            client.zip_code,
            client.phone,
            client.email_address,
            client.contact,

        ])
    return response


def ticket_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= ticket.csv'
    writer = csv.writer(response)
    tickets = Ticket.objects.all()
    writer.writerow([
        'Cod Produs',
        'Nume Produs',
        'Brand',
        'Data ticket',
        'Nume Client',
        'Agent',
        'Descriere',
        'Tehnician',
        'Aprobat',
    ])
    for ticket in tickets:
        writer.writerow([
            ticket.cod_produs,
            ticket.nume_produs,
            ticket.brand_produs,
            ticket.data_ticket,
            ticket.client,
            ticket.agent,
            ticket.descriere,
            ticket.tehnician.get(),
            ticket.approved,
        ])
    return response


def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.delete()
    return redirect('list-tichets')


def delete_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    client.delete()
    return redirect('list-clients')


def update_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('list-clients')
    return render(request, 'database/update_client.html', {
        'client': client,
        'form': form,
    })


def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    form = TicketFormAdmin(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('list-tichets')
    return render(request, 'database/update_ticket.html', {
        'ticket': ticket,
        'form': form,
    })


def search_ticket(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        tickets = Ticket.objects.filter(nume_produs__contains=searched)
        return render(request, 'database/search_ticket.html',
                      {'searched': searched, 'tickets': tickets})
    else:
        return render(request, 'database/search_ticket.html',
                      {})


def search_client(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        clients = Client.objects.filter(name__contains=searched)
        return render(request, 'database/search_client.html',
                      {'searched': searched, 'clients': clients})
    else:
        return render(request, 'database/search_client.html',
                      {})


def show_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'database/show_client.html', {
        'client': client})


def show_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'database/show_ticket.html', {
        'ticket': ticket})


def list_clients(request):
    client_list = Client.objects.all()
    p = Paginator(Client.objects.all(), 3)
    page = request.GET.get('page')
    clients = p.get_page(page)
    return render(request, 'database/client.html', {
        'client_list': client_list,
        'clients': clients
    })


def add_client(request):
    submitted = False
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_client?submitted=True')
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'database/add_client.html', {'form': form, 'submitted': submitted})


def add_ticket(request):
    submitted = False
    if request.method == 'POST':
        form = TicketFormAdmin(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_ticket?submitted=True')
    else:
        form = TicketFormAdmin
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'database/add_ticket.html', {'form': form, 'submitted': submitted})


def all_tichets(request):
    ticket_list = Ticket.objects.all()
    p = Paginator(Ticket.objects.all(), 3)
    page = request.GET.get('page')
    tickets = p.get_page(page)
    return render(request, 'database/ticket_list.html', {
        'ticket_list': ticket_list,
        'tickets': tickets,
    })


def index(request):
    return render(request, 'database/index.html', {})


def home(request):
    return render(request, 'database/home.html', {})
