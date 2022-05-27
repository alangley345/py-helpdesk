from django.db import models
from django.forms import CharField
from django.urls import reverse
from django.contrib.auth.models import User

#ticket category
class Category(models.Model):
    name = models.CharField(max_length=100, help_text='What category does this ticket belong to?')

    def __str__(self):
        return self.name

#ticket agent
class Agent(models.Model):
    agent = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return User.get_username(self.agent)

#ticket status
class Status(models.Model):

    TICKET_STATUS = (
         ('Open','Open'),
         ('Resolved','Resolved'),
         ('On-hold','On-hold'),
    )

    status = models.CharField(
        max_length=10,
        choices=TICKET_STATUS,
        default='Open',
        blank=False,
        help_text='Current Status',

    )

    def __str__(self):
        return self.status

#instance of a ticket that can be viewed
class Ticket(models.Model):
    id = models.BigAutoField(
        primary_key=True, editable=False, unique=True,auto_created=True,
    )
    summary = models.CharField(
        max_length=100, default= 'No Summary', blank=False, 
        help_text = 'Summarize Issue'
    )
    description = models.TextField(
        max_length=500, blank=False, default= 'Needs Description',
        help_text = 'Describe your issue here:'
    )
    category = models.ManyToManyField(Category, help_text='Ticket Category')
    agent = models.ManyToManyField(Agent, help_text='Ticket Assignee')
    status = models.ManyToManyField(Status, help_text='Enter ticket status')

    #functions for ticket model
    def __str__(self):
        return str(self.id)
        
    def get_absolute_url(self):
        return reverse('ticket-detail', args=[str(self.id)])

    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])

    display_category.short_description = 'Category'

    def display_status(self):
        return ', '.join(status.status for status in self.status.all()[:3])

    display_status.short_description = 'Status'

    def display_agent(self):
       return ', '.join(agent.agent for agent in self.agent.all()[:3])

    display_status.short_description = 'Agent'

    

