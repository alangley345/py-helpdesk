from django.shortcuts import render
from django.views.generic import ListView
from .models import Ticket

#listview for index
class ListTickets(ListView):
    paginate_by = 20
    
    def show_tickets():
        return Ticket.objects.values_list
        


    


#defining the index.html page
def index(request):
    ticket_instances = ListTickets.show_tickets()

    context = {
        'ticket_instances': ticket_instances ,
    }

    return render(request, 'index.html', context=context)