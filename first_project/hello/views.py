from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"first.html")

def hivimal(request):
    return render(request,"vimal.html")

def hivishal(request):
    return render(request,"vishal.html")

def greetings(request,name):

    return render(request,"greetings.html",{"username":name})