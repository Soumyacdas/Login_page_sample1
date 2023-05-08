from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import destination

# Create your views here.
@never_cache
def Homepage(request):
    if request.user.is_authenticated:
        dests=destination.objects.all()
        return render(request,'home.html',{'dests':dests})
    else:
        return redirect('log_in')
@never_cache
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 != password2:
            messages.info(request,'Incorrect Credentials')
        else:
            my_user=User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect('log_in')
        
    return render(request,'signup.html')
@never_cache
def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Incorrect Credentials')
    return render(request,'login.html')
def Logoutpage(request):
    logout(request)
    return redirect('log_in')
