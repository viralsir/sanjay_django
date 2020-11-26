from django.shortcuts import render
from .models import flight

# Create your views here.
def home(request):
    return render(request,"airline/home.html",{
        "flights":flight.objects.all()
    })

def flight_details(request,flight_id):
    flight_info=flight.objects.get(pk=flight_id)
    return render(request,"airline/flightdetail.html",{
        "flight":flight_info
    })