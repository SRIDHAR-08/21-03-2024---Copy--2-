from django.shortcuts import render,redirect
from .form import *

def home_page(request):
    return render(request,'index.html')

def form_page(request):
    if request.method == "POST":
        view_form = form_class(request.POST)
        view_form.save()
    context = {
        'view_context': form_class
    }
    return render(request,'form.html',context)

def view_page(request):
    context =  {
        'views_data': class_models.objects.all()
    }
    return render(request,"view.html",context)


def delete_student(request,id):
    select_id = class_models.objects.get(id=id)
    select_id.delete()
    return redirect('/view/')

def update_page(request,id):
    select_id = class_models.objects.get(id=id)
    view_form = form_class(request.POST,instance=select_id)
    if view_form.is_valid():
        view_form.save()
        return redirect('/view/')
    
    context = {
        "update_student" : form_class(instance=select_id)
    }
    return render(request,'form.html',context)

def update_page(request, id):
    instance = class_models.objects.get(id=id)  # Replace YourModel with your actual model class
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)  # Replace YourForm with your actual form class
        if form.is_valid():
            form.save()
            return redirect('/view/')  # Redirect to the appropriate URL after saving
    else:
        form = form_class(instance=instance)  # Replace YourForm with your actual form class

    context = {
        'form': form,
        'instance_id': id,
    }
    return render(request, 'form.html', context)