from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'outfits/index.html')

def outfit(request):
    return render(request, 'outfits/outfit.html')

def inventory(request):
    clothes = Clothing.objects.all()

    form = ClothingForm()

    if request.method == 'POST':
        form = ClothingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/inventory')

    context = {'clothes':clothes, 'form':form}
    return render(request, 'outfits/inventory.html', context)

def about(request):
    return render(request, 'outfits/about.html')

def updateClothing(request, pk):
    clothes = Clothing.objects.get(id=pk)

    form = ClothingForm(instance=clothes)

    if request.method == 'POST':
        form = ClothingForm(request.POST, instance=clothes)
        if form.is_valid():
            form.save()
            return redirect('/inventory')

    context = {'form':form}

    return render(request, 'outfits/updateclothing.html', context)

def deleteClothing(request, pk):
    item = Clothing.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/inventory')

    context = {'item':item}
    return render(request, 'outfits/deleteclothing.html', context)