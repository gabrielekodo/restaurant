from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .forms import ReservationForm,LoginForm,RegistrationForm
from .models import MenuItems
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    print(request.method)
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        print(f"{form.data['email']}\n{form.data['password']}")
        user = authenticate(request, email=form.data['email'], password=form.data['password'],username='admin',role='admin')
        print( {user})
        print(form.is_valid())
        if user is not None:
            login(request, user)

            return redirect('home')  # Redirect to your home page name
        else:
            form.add_error(None, "Invalid username or password.")




    else:
            form = AuthenticationForm()

    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

def create_account(request):
    form=RegistrationForm()

    if request.method=='POST':
        form=RegistrationForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('login')

    return render(request,'registration.html',{'form':form})

def home(request):
    first_three_items = MenuItems.objects.all()[:3]

    return render(request,'home.html',{'menu':first_three_items})


def booking(request):
    form=ReservationForm()
    if request.method=='POST':
        form=ReservationForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('home')

    return render(request,'booking.html',{'form':form})


def about(request):
    return render(request,'about.html')

@login_required()
def menu(request):
    menu_data=MenuItems.objects.all()


    return render(request,'menu.html',{'menu':menu_data})

def display_menu_item(request,pk=None):
    try:
        menu_item = MenuItems.objects.get(pk=pk)
        return render(request, 'menu_item.html', {'menu_item': menu_item})

    except MenuItems.DoesNotExist:
        menu_item = None
        return render(request, '404.html')

    # if pk:
    #     menu_item=MenuItems.objects.get(pk=pk)
    #     print(menu_item.pk)
    #
    # else:
    #     menu_item=''
    #     return render(request,'index.html')
    #
    # return render(request,'menu_item.html',{'menu_item':menu_item})


