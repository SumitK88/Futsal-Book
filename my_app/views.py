from django.shortcuts import render,redirect
from .forms import PlayerCreationForm,PlayerLoginForm
from django.contrib.auth import authenticate,login,logout
from .models import player
# Create your views here.

# @csrf_exempt
def register(request):
    context={}
    if request.POST:
        form=PlayerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context['register_form']=form
        
    else:
        form=PlayerCreationForm()
        context['register_form']=form
    return render(request,'my_app/register.html',context)
            
def login_us(request):
    context={}
    if request.POST:
        form=PlayerLoginForm(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            password=request.POST.get('password')
            player_r=authenticate(request,email=email,password=password)
            if player_r is not None:
                login(request,player_r)
                return redirect('home')
    else:
        form=PlayerLoginForm()
        context['login_form']=form
        return render(request,'my_app/login_us.html',context)

def logout_us(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request,'my_app/home.html')

def review(request):
    return render(request,'my_app/review.html')

def contact_us(request):
    return render(request,'my_app/contact_us.html')

def booking(request):
    return render(request,'my_app/booking.html')

def about_us(request):
    return render(request,'my_app/about_us.html')

def profile(request):
    return render(request,'my_app/profile.html')


