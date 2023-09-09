from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return render(request,"index.html")
    #return render(request,"adminHome.html")
    # return render(request,"staffHome.html")
    # return render(request,"sellerHome.html")
    return render(request,"userHome.html")
def createAccount(request):
    return render(request,"createAccount.html")
def login1(request):
     return render(request,"login1.html")
def userHome(request):
    return render(request,"userHome.html")
def adminHome(request):
    return render(request,"adminHome.html")
def staffHome(request):
    return render(request,"staffHome.html")
def sellerHome(request):
    return render(request,"sellerHome.html")

