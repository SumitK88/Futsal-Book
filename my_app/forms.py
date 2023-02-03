from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from my_app.models import player

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