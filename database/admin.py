from django.contrib import admin
from .models import Ticket, Client, CrmUser

# admin.site.register(Ticket)
admin.site.register(Client)


# admin.site.register(CrmUser)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('cod_produs', 'client', 'data_ticket', 'agent', 'approved')
    ordering = ('-data_ticket',)
    search_fields = ('cod_produs',)


@admin.register(CrmUser)
class CrmUserAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'email')
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'email')
    ordering = ('-first_name',)
    search_fields = ('first_name', 'last_name', 'email')
