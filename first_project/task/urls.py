from django.urls import  path
from . import  views
urlpatterns=[
    path("view",views.taskview,name="view"),
    path("newtask",views.addtask,name="add")
]