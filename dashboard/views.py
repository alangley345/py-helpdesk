from django.shortcuts import render
from django.views import generic
from .models import Ticket

#defining the index.html page
def index(request):
    ticket_instances = Ticket.objects.all()

    context = {
        'ticket_instances': ticket_instances,
    }

    return render(request, 'index.html', context=context)