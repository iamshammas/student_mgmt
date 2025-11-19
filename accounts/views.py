from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'base.html')

def user_login(request):
    return render(request,'user_login.html')

def home(request):
    return HttpResponse('HELLO WORK')

def user_register(request):
    return HttpResponse('HELLO WORK')

def profile(request):
    return HttpResponse('HELLO WORK')

def logout(request):
    return HttpResponse('HELLO WORK')

def password_reset(request):
    return HttpResponse('HELLO WORK')