from django.shortcuts import render
from .models import Ticket

def index(request):
    ticket_instances = Ticket.objects.all()

    context = {
        'ticket_instances': ticket_instances,
    }

    return render(request, 'index.html', context=context)