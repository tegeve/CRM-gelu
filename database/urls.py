from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.home, name="home"),
    path('tichete', views.all_tichets, name="list-tichets"),
    path('list_clients', views.list_clients, name="list-clients"),
    path('add_ticket', views.add_ticket, name="add-tichets"),
    path('add_client', views.add_client, name="add-clients"),
    path('show_client/<client_id>', views.show_client, name='show-client'),
    path('show_ticket/<ticket_id>', views.show_ticket, name='show-ticket'),
    path('search_client', views.search_client, name='search-client'),
    path('search_ticket', views.search_ticket, name='search-ticket'),
    path('update_ticket/<ticket_id>', views.update_ticket, name='update-ticket'),
    path('update_client<client_id>', views.update_client, name='update-client'),
    path('delete_client<client_id>', views.delete_client, name='delete-client'),
    path('delete_ticket<ticket_id>', views.delete_ticket, name='delete-ticket'),
    path('ticket_csv', views.ticket_csv, name='ticket-csv'),
    path('client_csv', views.client_csv, name='client-csv'),
    path('generate_to_pdf', views.generate_to_pdf, name='generate_to_pdf')

]
