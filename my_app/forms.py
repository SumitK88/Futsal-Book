from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from my_app.models import player,Booking

class PlayerCreationForm(UserCreationForm):
    class Meta:
        model=player
        fields=('email', 'name', 'phone', 'pimg', 'password1','password2')
        
class PlayerLoginForm(forms.ModelForm):
    password = forms.CharField(label="password",widget=forms.PasswordInput)
    
    class Meta:
        model=player
        fields=('email', 'password')
            
    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']
            
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("INVALID Email or Password")
            
class bookingForm(forms.ModelForm):
    time = forms.TimeField(label="time")
    date = forms.DateField(label="date")
    p_name = forms.CharField(max_length=100)
    class Meta:
        model=Booking
        fields=('p_name','date','time')