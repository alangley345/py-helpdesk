from django.contrib import admin
from .models import Category,Agent,TicketInstance

#customizing administration site itself
admin.site.site_header = "Py-Helpdesk"
admin.site.site_title  = "Py-Helpdesk"
admin.site.index_title = "Welcome to my helpdesk app!"

admin.site.register(Category)
admin.site.register(Agent)
admin.site.register(TicketInstance)
