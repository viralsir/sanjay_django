from django.contrib import admin
from .models import *

class FlightAdmin(admin.ModelAdmin):
    list_display = ['source','destion','duration']

# Register your models here.
admin.site.register(airport)
admin.site.register(flight,FlightAdmin)
admin.site.register(passengers)