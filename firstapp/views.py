from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.http import HttpResponse
from .forms import ReservationForm,LoginForm,RegistrationForm,AddMenuForm
from .models import MenuItems,CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate( password=password,email=email)
        print( {user})

        if user is not None:
            login(request, user)

            return redirect('home')  # Redirect to your home page name
        else:
            messages.info(request,'Invalid username or password.')
            return redirect('login')

    else:

        return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect(settings.LOGOUT_REDIRECT_URL)

def create_account(request):
    if request.user.is_authenticated:
        return redirect('home')


    if request.method=='POST':
        last_name=request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password= request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if CustomUser.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            else:
                user=CustomUser.objects.create_user(email=email,password=password,last_name=last_name,first_name=first_name)
                user.save()
                return redirect('login')



        else:
             messages.info(request,'Passwords are not matching')

             return redirect('register')

    return render(request,'registration.html')

def home(request):
    first_three_items = MenuItems.objects.all()[:3]

    return render(request,'home.html',{'menu':first_three_items})

@login_required()
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
    menu_data=MenuItems.objects.all().order_by('pk')


    return render(request,'menu.html',{'menu':menu_data})

@login_required()
def display_menu_item(request,pk=None):
    try:
        menu_item = MenuItems.objects.get(pk=pk)
        return render(request, 'menu_item.html', {'menu_item': menu_item})

    except MenuItems.DoesNotExist:
        menu_item = None
        return render(request, '404.html')



@login_required()
def add_recipe(request):
    items=MenuItems.objects.all().order_by('pk')
    form=AddMenuForm()
    if request.method=='POST':
        form=AddMenuForm(request.POST)
        print(form.data['name'])
        print(form.data['description'])
        print(form.data['image'])
        print(form.data['price'])
        if form.is_valid():
            form.save()
            messages.success(request,'successful!')
            return redirect('recipes')

        else:
            messages.info(request,'error in submitting your info')
    context={
        'items':items
    }

    return render(request,'recipes.html', context)

@login_required()
def view_recipe(request,id):
    try:
        menu_item = MenuItems.objects.get(pk=id)
        return render(request, 'menu_item.html', {'menu_item': menu_item})

    except MenuItems.DoesNotExist:
        menu_item = None
        return render(request, '404.html')




@login_required()
def delete_menu(request, id):
    item = get_object_or_404(MenuItems, id=id)

    if request.method == "GET":
        item.delete()
        return redirect("recipes")

    return render(request, "recipes.html", { "item": item })

@login_required()
def update_menu(request, id):
    item = get_object_or_404(MenuItems, pk=id)

    if request.method == "POST":
        item.name = request.POST.get("name")
        item.description = request.POST.get("description")
        item.image = request.POST.get("image")
        item.price = request.POST.get("price")
        item.save()
        return redirect('recipes')   # redirect to your table page

    return render(request, "viewrecipe.html", {"id": id})
