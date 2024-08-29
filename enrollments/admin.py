from django.contrib import admin
from .models import Ticket, Enrollment


admin.site.register(Enrollment)
admin.site.register(Ticket)
