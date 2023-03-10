from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PlayerCreationForm,PlayerLoginForm,bookingForm
from django.contrib.auth import authenticate,login,logout
from .models import player,Booking
from django.contrib import messages
from django.db.models import Count
import datetime
import matplotlib.pyplot as plt
from sklearn.cluster import Kmeans
# Create your views here.

# @csrf_exempt
def register(request):
    context={}
    if request.POST:
        form=PlayerCreationForm(request.POST)
        context['register_form']=form
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['reg_error']="INVALID REQUEST"
            return render(request,'my_app/register.html',context)
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
            context['login_form']=form
            context['log_error']="PROVIDE VALID LOGIN CREDENTIALS"
            return render(request,'my_app/login_us.html',context)
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

def about_us(request):
    return render(request,'my_app/about_us.html')

def profile(request):
    return render(request,'my_app/profile.html')

def booking(request):
    context={}
    if request.POST:
        time_r=request.POST.get('time-picker')
        date_r=request.POST.get('date')
        print(time_r,date_r)
        p_name_r=request.user.name
        form=bookingForm(p_name_r,date_r,time_r)
        if Booking.objects.filter(time=time_r,date=date_r):
            context['error']="<-- THE PROVIDED DATE/TIME IS ALREADY BOOKED -->"
            return render(request,'my_app/booking.html',context)
        if form is not None:
            Booking.objects.create(time=time_r, date=date_r,p_name=p_name_r)
            context['error']="<-- YOUR BOOKING IS SUCCESSFUL -->"
        context['booking_form']=form
        return render(request,'my_app/booking.html',context)
        
    else:
        context['day-chart']=d_chart()
        context['week-chart']=w_chart()
        context['count']=date_list()
        context['t_count']=time_list()
        form=bookingForm()
        context['booking_form']=form
        return render(request,'my_app/booking.html',context)

def d_chart():
    context={}


def booking_list(request):
    context={}
    context['books']=Booking.objects.all().filter(p_name=request.user.name)
    return render(request,'my_app/booking_list.html',context)

def date_list():
    c=[]
    for j in range(1,13):
        c1=[]
        for i in range(1,32):
            c1.insert(i, Booking.objects.filter(date__day=i, date__month=j).order_by('date').count())
        c.insert(j, c1)
    return c
    
def time_list():
    times=['09:00', '10:00', '11:00', '12:00', '1:00', '2:00', '3:00']
    c=[]
    for j in range(0,12):
        c1=[]
        for i in range(0,31):
            c2=[]
            for k in range(0,7):
                c1.insert(k, Booking.objects.filter(date__day=i, date__month=j,time=times[k]).order_by('date').count())
            c2.insert(i, c1)
        c.insert(j, c2)
    return c
    
