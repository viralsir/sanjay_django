from django.shortcuts import render
from datetime import  datetime

# Create your views here.
def index(request):
    date=datetime.now()
    return render(request,"newyear/home.html",{
        "newyear": date.day==1 and date.month==1
    })