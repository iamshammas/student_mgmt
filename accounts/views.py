from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Profile
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'base.html')

def admin_panel(request):
    return render(request,'admin_panel.html')
def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pswd = request.POST.get('password')
        userr = authenticate(request,username = uname,password =pswd)
        if userr is not None:
            login(request,userr)
            messages.success(request,'Logging Successfull')
            if userr.is_superuser:
                # return redirect('/admin/')
                return redirect('admin_panel')
            else:
                return redirect('home')
        else:
            messages.error(request,'Wrong Credentials')
            return redirect('user_login')
    return render(request,'user_login.html')

def home(request):
    return HttpResponse('HELLO WORK')

def user_register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        em = request.POST.get('email')
        pswd = request.POST.get('password1')
        roll_no = request.POST.get('roll_no')
        dept = request.POST.get('dept') 
        admission_year = request.POST.get('admission_year')
        user = User.objects.create_user(username=uname,email=em,password=pswd)
        Profile.objects.create(roll_no=roll_no,dept=dept,admission_year=admission_year,user=user)
        return redirect('home')
    return render(request,'user_register.html')

def profile(request):
    return HttpResponse('HELLO WORK')

def logout(request):
    return HttpResponse('HELLO WORK')

def password_reset(request):
    return HttpResponse('HELLO WORK')

def red(request):
    return redirect('user_login')