from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PlayerCreationForm,PlayerLoginForm,bookingForm,PlayerChangeForm
from django.contrib.auth import authenticate,login,logout
from .models import player,Booking
from datetime import datetime
import plotly.express as px
import pandas as pd
# Create your views here.
from django.contrib.auth.forms import UserChangeForm

# @csrf_exempt
def register(request):
    context={}
    if request.POST:
        form=PlayerCreationForm(request.POST,request.FILES)
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
    if request.POST:
        revi=request.POST.get('revi')
        return render(request,'my_app/review.html')
    else:    
        return render(request,'my_app/review.html')

def contact_us(request):
    return render(request,'my_app/contact_us.html')

def about_us(request):
    return render(request,'my_app/about_us.html')

def profile(request):
    context={}
    context['book_cnt']=Booking.objects.all().filter(p_name=request.user.name).count()
    return render(request,'my_app/profile.html',context)

def booking(request):
    context={}
    if request.POST:
        d_chart()
        w_chart()
        date_string=request.POST.get('date')
        time_string=request.POST.get('time')
        date_r=datetime.strptime(date_string, '%d/%m/%Y').date()
        time_r=datetime.strptime(time_string, '%H:%M:%S').time()
        p_name_r=request.user.name
        form=bookingForm(p_name_r,date_r,time_r)
        if Booking.objects.filter(time=time_r,date=date_r):
            context['error']="ALREADY BOOKED"
            return render(request,'my_app/booking.html',context)
        if form is not None:
            Booking.objects.create(time=time_r, date=date_r,p_name=p_name_r)
            context['error']="<-- YOUR BOOKING IS SUCCESSFUL -->"
        context['booking_form']=form
        return render(request,'my_app/booking.html',context)
        
    else:  
        d_chart()
        w_chart()
        context['count']=date_list()
        context['t_count']=time_list()
        form=bookingForm()
        context['booking_form']=form
        return render(request,'my_app/booking.html',context)

def d_chart():
    times=['09:00:00', '10:00:00', '11:00:00', '12:00:00', '1:00:00', '2:00:00', '3:00:00']
    time_s=['09:00', '10:00', '11:00', '12:00', '1:00', '2:00', '3:00']
    # df=Booking.objects.values_list('time',c)
    c=[]
    for i in range(0,7):
            c.insert(i, Booking.objects.filter(time=times[i]).order_by('time').count())
    
    d = {'TIME(HH:MM)': time_s, 'FREQUENCY': c}
    df = pd.DataFrame(data=d)
    fig=px.line(df,x='TIME(HH:MM)',y='FREQUENCY',title="DAILY CHARTS")
    fig.write_html("my_app/static/my_app/day.html")

def w_chart():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    c=[]
    for i in range(0,7):
            c.insert(i, Booking.objects.filter(date__week_day=i+1).order_by('date__week_day').count())
    d={'DAYS':days,'FREQUENCY': c}
    df=pd.DataFrame(data=d)
    fig=px.line(df,x='DAYS',y='FREQUENCY',title="WEEKLY CHARTS")
    fig.write_html("my_app/static/my_app/week.html")

def booking_list(request):
    context={}
    context['books']=Booking.objects.all().filter(p_name=request.user.name).order_by('-date')
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
    times=['09:00:00', '10:00:00', '11:00:00', '12:00:00', '1:00:00', '2:00:00', '3:00:00']
    c=[]
    for j in range(1,13):
        c1=[]
        for i in range(1,32):
            c2=[]
            for k in range(1,8):
                c1.insert(k, Booking.objects.filter(date__day=i, date__month=j,time=times[k-1]).order_by('date').count())
            c2.insert(i, c1)
        c.insert(j, c2)
    print(c)
    return c

def edit_profile(request):
    if request.POST:
        form=PlayerChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=PlayerChangeForm(instance=request.user)
    return render(request,'my_app/edit_profile.html',{'al':form})
    
