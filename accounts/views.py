from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def index(request):
    return render(request,'base.html')

def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pswd = request.POST.get('password')
        userr = authenticate(request,username = uname,password =pswd)
        login(request,userr)
        return redirect('home')
    return render(request,'user_login.html')

def home(request):
    return HttpResponse('HELLO WORK')

def user_register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        em = request.POST.get('email')
        pswd = request.POST.get('password1')
        User.objects.create_user(username=uname,email=em,password=pswd)
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