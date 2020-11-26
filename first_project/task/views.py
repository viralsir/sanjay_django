from django.shortcuts import render,redirect
from  django import forms


# Create your views here.
tasklist=['check email','do homework','prepare notes','check balance']

class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",max_value=5,min_value=3)
    t_date=forms.DateField()



def taskview(request):
    return render(request,"task/view.html",{
        "tasks":tasklist
    })

def addtask(request):
    if request.method == 'POST' :
        form=NewTaskForm(request.POST)
        if form.is_valid():
            tasklist.append(form.cleaned_data["task"])
            return redirect('view')
        else :
            return render(request,"task/add.html",{
                "form":form
            })

    return render(request,"task/add.html",{
        "form": NewTaskForm()
    })