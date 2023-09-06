from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
    # return render(request,"admin1.html")
    # return render(request,"user1.html")

def createaccount(request):
    return render(request,"createaccount.html")
def user1(request):
    return render(request,"user1.html")
def admin1(request):
    return render(request,"admin1.html")
