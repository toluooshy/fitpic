import os
import platform
import getpass
import random
from django.core.management import call_command
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

if(platform.system() == 'Darwin'):
    dbpath = ('/Users/' + getpass.getuser() + '/Desktop/fitpic/data/')
elif(platform.system() == 'Windows'):
    dbpath = ('C:\\Users\\' + getpass.getuser() + '\\Desktop\\fitpic\\data\\')
else:
    dbpath = ('/home/' + getpass.getuser() + '/Desktop/fitpic/data/')
if not os.path.exists(dbpath):
    os.makedirs(dbpath)
if not os.path.isfile(os.path.join(dbpath, 'db.sqlite3')):
    open(os.path.join(dbpath, 'db.sqlite3'), 'w+')

# VIEWS:

def index(request):
    call_command('makemigrations')
    call_command('migrate')
    return render(request, 'outfits/index.html')

def outfit(request):
    call_command('makemigrations')
    call_command('migrate')
    if (len(Clothing.objects.all().filter(category='TOPS')) == 0):
        tops = '<try adding something here/>'
    else:
        tops = random.choice(Clothing.objects.all().filter(category='TOPS'))
    
    if (len(Clothing.objects.all().filter(category='BTTM')) == 0):
        bottoms = '<try adding something here/>'
    else:
        bottoms = random.choice(Clothing.objects.all().filter(category='BTTM'))

    if (len(Clothing.objects.all().filter(category='FTGR')) == 0):
        footgear = '<try adding something here/>'
    else:
        footgear = random.choice(Clothing.objects.all().filter(category='FTGR'))

    if (len(Clothing.objects.all().filter(category='HDGR')) == 0):
        headgear = '<try adding something here/>'
    else:
        headgear = random.choice(Clothing.objects.all().filter(category='HDGR'))

    if (len(Clothing.objects.all().filter(category='ACCS')) == 0):
        accessories = '<try adding something here/>'
    else:
        accessories = random.choice(Clothing.objects.all().filter(category='ACCS'))
    content = {
        'tops':tops,
        'bottoms':bottoms,
        'footgear':footgear,
        'headgear':headgear,
        'accessories':accessories
    }
    return render(request, 'outfits/outfit.html', content)

def inventory(request):
    call_command('makemigrations')
    call_command('migrate')
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
    call_command('makemigrations')
    call_command('migrate')
    return render(request, 'outfits/about.html')

def updateClothing(request, pk):
    call_command('makemigrations')
    call_command('migrate')
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
    call_command('makemigrations')
    call_command('migrate')
    item = Clothing.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/inventory')

    context = {'item':item}
    return render(request, 'outfits/deleteclothing.html', context)