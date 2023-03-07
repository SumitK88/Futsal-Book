"""Footbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import register,login_us,logout_us,home,contact_us,review,booking,about_us,profile,booking_list

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name="register"),
    path('login/',login_us,name="login"),
    path('logout/',logout_us,name="logout"),
    path('home/',home,name="home"),
    path('profile/',profile,name="profile"),
    path('review/',review,name="review"),
    path('booking/',booking,name="booking"),
    path('booking_list/',booking_list,name="booking_list"),
    path('about_us/',about_us,name="about_us"),
    path('contact_us/',contact_us,name="contact_us"),
]
