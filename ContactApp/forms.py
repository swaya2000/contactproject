from django import forms
from django.contrib.auth.models import User
from .models import Contact

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets={
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),
        'email':forms.EmailInput(attrs={"class":'form-control','placeholder':'Email'}),
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
        'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),    
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }

class UserContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['phone','address','place']
        widgets={
            'phone':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Phone number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'place':forms.TextInput(attrs={'class':'form-control','placeholder':'place'}),
        }
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['phone','address','place']
        widgets={
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'place':forms.TextInput(attrs={'class':'form-control','placeholder':'place'}),
        }
        
        

        
        