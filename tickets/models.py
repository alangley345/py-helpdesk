import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#ticket category
class Category(models.Model):
    name = models.CharField(max_length=100, help_text='What category does this ticket belong to?')

    def __str__(self):
        return self.name

#ticket agent
class Agent(models.Model):
    agent = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.agent

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
        blank=False,
        help_text='Current Status',

    )

    def __str__(self):
        return self.status

#instance of a ticket that can be viewed
class TicketInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable =False)
    category = models.ManyToManyField(Category, help_text='Ticket Category')
    assignee = models.ManyToManyField(Agent, help_text='Ticket Assignee')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ticket-detail', args=[str(self.id)])
