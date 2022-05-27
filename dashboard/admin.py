from django.contrib import admin
from .models import Category, Agent, Ticket

#customizing administration site itself
admin.site.site_header = "Py-Helpdesk"
admin.site.site_title  = "Py-Helpdesk"
admin.site.index_title = "Welcome to my helpdesk app!"

class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'summary', 'display_status', 'display_category'
    )

admin.site.register(Category)
admin.site.register(Agent)
admin.site.register(Ticket, TicketAdmin)



