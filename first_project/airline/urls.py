from django.urls import path
from . import views
urlpatterns =[

    path("home",views.home,name="airline-home"),
    path("flights/<int:flight_id>",views.flight_details,name="flightdetails")
]