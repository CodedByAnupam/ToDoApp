from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully added to the list.'))
            return redirect("home")
    else:
        items = List.objects.all()
        context = {"items":items}
        return render(request, "todo_list/home.html",context)

def delete(request, id):
    item = List.objects.get(pk=id)
    item.delete()
    messages.success(request, ('Item has been deleted.'))
    return redirect('home')

def cross_off(request, id):
    item = List.objects.get(pk=id)
    item.completed = True
    item.save()
    messages.success(request, ('Item has been marked as completed.'))
    return redirect('home')

def uncross(request, id):
    item = List.objects.get(pk=id)
    item.completed = False
    item.save()
    messages.success(request, ('Item has been marked as not completed.'))
    return redirect('home')

def edit(request, id):
    if request.method == 'POST':
        item = List.objects.get(pk=id)
        form = ListForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been successfully edited.'))
            return redirect('home')
    else: 
        item = List.objects.get(pk=id)
        return render(request, 'todo_list/edit.html', {'item': item})
