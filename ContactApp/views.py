from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm,UserLoginForm,UserContactForm,ContactUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Contact

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'index.html')

class RegisterView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,"register.html",{'form':form})
    
    def post(self,request):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            fname=form.cleaned_data.get('first_name')
            lname=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            uname=form.cleaned_data.get('username')
            psw=form.cleaned_data.get('password')            
            User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=psw)
            messages.success(request,'User Registered Succesfully')
            return redirect('home_view')
        else:
            messages.error(request,'Invalid Data')
            return redirect('reg_view')
        
class UserLoginView(View):
    def get(self,request):
        form=UserLoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request):
        uname=request.POST.get('username')
        psw=request.POST.get('password')
        User=authenticate(username=uname,password=psw)
        if User:
            login(request,User)
            messages.success(request,'WELCOME')
            return redirect('home_view')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('log_view')

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log_view')
    
class ContactCreateView(View):
    def get(self,request):
        form=UserContactForm()
        return render(request,'create.html',{'form':form})
    
    def post(self,request):
        if request.user.is_authenticated:
            form=UserContactForm(request.POST)
            if form.is_valid():
                user=request.user
                phone=form.cleaned_data.get('phone')
                address=form.cleaned_data.get('address')
                place=form.cleaned_data.get('place')
                Contact.objects.create(user=user,phone=phone,address=address,place=place)
                messages.success(request,'Added')
                return redirect('home_view')
            else:
                messages.error(request,'Invalid data')
                return redirect('create_view')
        else:
            messages.warning(request,'You must login first')
            return redirect('log_view')
        
class ContactListView(View):
    def get(self,request):
        user=request.user
        if user.is_authenticated:
            cont=Contact.objects.filter(user=request.user)
            return render(request,'list.html',{'cont':cont})
        else:
            messages.warning(request,'You must login first')
            return redirect('log_view')
class ContactDeleteView(View):
    def get(self,request,*args,**kwargs):
        cont=Contact.objects.get(user=request.user)
        cont.delete()
        return redirect('list_view')
class ContactUpdateView(View):
    def get(self,request,*args,**kwargs):
        cont=Contact.objects.get(user=request.user)
        form=ContactUpdateForm(instance=cont)
        return render(request,'update.html',{'form':form})
    def post(self,request,*args,**kwargs):
        cont=Contact.objects.get(user=request.user)
        form=ContactUpdateForm(request.POST,instance=cont)
        if form.is_valid():
            form.save()
            return redirect('list_view')

    





    

        
    


        




    
    
