from django.shortcuts import render,redirect
from django.http import *
from .models import Destination
# from django.contrib.auth import  login, logout
from django.contrib.auth.models import User,auth

# Create your views here.
def indexe(request):
    places = Destination.objects.all()
    return render(request,'index.html',{'places':places})

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username,email=email,password=password).save();
        #User.objects.create(username=username,email=email,password=password).save()
        return render(request,'index.html')
    return render(request,'index.html')

def user_login(request):
     if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)
            auth.login(request,user)
            #return HttpResponse('Logined Successfully  ' + request.POST['username'])
            return render(request,'index.html')
     return render(request, 'index.html')
 
 
def user_logout(request):
    auth.logout(request)
    return redirect('index')

def abt(request):
    return render(request,'abt.html')

def cont(request):
    return render(request,'cont.html')

# def user_login(request):
#     return render(request,'login.html')

def destinations(request):
    dests = Destination.objects.filter()
    return render(request,'famous.html',{'dests':dests})

def user_login1(request):
    return render(request,'login1.html')

def covid(request):
    return render(request,'covid.html')


