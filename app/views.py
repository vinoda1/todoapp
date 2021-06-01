from django.shortcuts import render,redirect
from app.models import Task


from django.contrib import messages
# Create your views here.


def home(request):
        all_items=Task.objects.all()
        return render(request,"home.html",{"all_items":all_items})


def addTask(request):
    #returning task to the same page 
    t=Task(task=request.POST['task'])
    t.save()
    return redirect("/home")

    
def delete_data(request,id):
    one_task=Task.objects.get(id=id)
    one_task.delete()
    return redirect("/home")