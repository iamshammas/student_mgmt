from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'base.html')

def user_login(request):
    return render(request,'user_login.html')