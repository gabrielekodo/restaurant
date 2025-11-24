from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ReservationForm
from .models import MenuItems
# Create your views here.

def home(request):
    return render(request,'index.html')


def booking(request):
    form=ReservationForm()
    if request.method=='POST':
        form=ReservationForm(request.POST)

        if form.is_valid():
            print(form)
            form.save()


    return render(request,'booking.html',{'form':form})


def about(request):
    return render(request,'about.html')


def menu(request):
    menu_data=MenuItems.objects.all()
    print(menu_data)

    return render(request,'menu.html',{'menu':menu_data})

def display_menu_item(request,pk=None):
    if pk:
        menu_item=MenuItems.objects.get(pk=pk)

    else:
        menu_item=''

    return render(request,'menu_item.html',{'menu_item':menu_item})