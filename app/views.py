from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from app.models import tbl_userAccount,tbl_userDetails,tbl_sellerDetails,tbl_staffDetails

# Create your views here.
def index(request):
    return render(request,"index.html")
    # return render(request,"adminHome.html")
    #return render(request,"staffHome.html")
    return render(request,"sellerHome.html")
    #return render(request,"userHome.html")
    

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

#-----create account for user
def createAccount(request):
    return render(request,"createaccount.html")
def addAccount(request):
    a=User()
    b=tbl_userAccount()
    c=tbl_userDetails()
  
    a.username=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    a.set_password(pwd)
    a.first_name=request.POST.get('fname')
    a.email=request.POST.get('email')
    b.username=request.POST.get('uname')
    b.firstname=request.POST.get('fname')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phn')
    b.accountType="User"

    c.username=request.POST.get('uname')
    c.firstname=request.POST.get('fname')
    c.lastname=request.POST.get('lname')
    c.gender=request.POST.get('gender')
    c.email=request.POST.get('email')
    c.phone=request.POST.get('phn')
    c.accountType="user"
    c.address=request.POST.get('address')
    c.district=request.POST.get('district')
    img=request.FILES['img']
    fs=FileSystemStorage()
    filename=fs.save(img.name,img)
    fileurl=fs.url(filename)
    c.photo=fileurl
    
    a.save()
    b.save()
    c.save()
  
    return redirect('/')
#-------------end user accound creation ----------------
#-------------seller account creation-----------------
def addSeller(request):
    return render(request,"addSeller.html")
def addSellerAccount(request):
    a=User()
    b=tbl_userAccount()
    d=tbl_sellerDetails()
    
    a.username=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    a.set_password(pwd)
    a.first_name=request.POST.get('fname')
    a.email=request.POST.get('email')
    b.username=request.POST.get('uname')
    b.firstname=request.POST.get('fname')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phn')
    b.accountType="seller"
  
    d.username=request.POST.get('uname')
    d.firstname=request.POST.get('fname')
    d.lastname=request.POST.get('lname')
    d.gender=request.POST.get('gender')
    d.email=request.POST.get('email')
    d.phone=request.POST.get('phn')
    d.address=request.POST.get('address')
    d.district=request.POST.get('district')
    img=request.FILES['img']
    fs=FileSystemStorage()
    filename=fs.save(img.name,img)
    fileurl=fs.url(filename)
    d.photo=fileurl
 
   
    a.save()
    b.save()
    d.save()
 
    return redirect('/')
# -------------------end seller account creation------------
# ------------  staff account creation -------------------
def addStaff(request):
    return render(request,"addStaff.html")
def addStaffAccount(request):
    a=User()
    b=tbl_userAccount()
    e=tbl_staffDetails()
    a.username=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    a.set_password(pwd)
    a.first_name=request.POST.get('fname')
    a.email=request.POST.get('email')
    b.username=request.POST.get('uname')
    b.firstname=request.POST.get('fname')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phn')
    b.accountType="staff"
    
    e.username=request.POST.get('uname')
    e.firstname=request.POST.get('fname')
    e.lastname=request.POST.get('lname')
    e.staffid=request.POST.get('staffid')
    e.designation=request.POST.get('desg')
    e.age=request.POST.get('age')
    e.gender=request.POST.get('gender')
    e.email=request.POST.get('email')
    e.phone=request.POST.get('phn')
    e.address=request.POST.get('address')
    e.district=request.POST.get('district')
    img=request.FILES['img']
    fs=FileSystemStorage()
    filename=fs.save(img.name,img)
    fileurl=fs.url(filename)
    e.photo=fileurl
   
    a.save()
    b.save()
    e.save()
    return redirect('/') 

#------staff account creation-------------------

#  --------authentication--------------
def login(request):
    uname=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    print(uname,pwd,"test2")
    p=authenticate(username=uname,password=pwd)
    print(p,"test1")
    request.session['username']=uname
    if p is not None and p.is_superuser==1:
       
        return redirect('/adminHome/')
    elif p is not None and p.is_superuser==0:
        x=tbl_userAccount.objects.get(username=p)
        if x.accountType=="User":
            return redirect('/userHome/')
        elif x.accountType=="staff":
            return redirect('/staffHome/')
        elif x.accountType=="seller":
            return redirect('/sellerHome/')
        else:
            pass
    else:
        return HttpResponse('Invalid Response')


# ---------viewuser------------

def viewUser(request):
    p=tbl_userDetails.objects.all()
    return render(request,"viewUser.html",{'data':p})
#--------updatestaff--------
def updateStaff(request):
    a=request.session['username']
    p=tbl_staffDetails.objects.get(username=a)
    
    return render(request,"updateStaff.html",{ 'data':p})
def updateStaffAdd(request,id):
    a=request.session['username']
    e=tbl_staffDetails.objects.get(username=a)
    
    try:
        e.username=request.POST.get('uname')
        e.firstname=request.POST.get('fname')
        e.lastname=request.POST.get('lname')
        e.staffid=request.POST.get('staffid')
        e.designation=request.POST.get('desg')
        e.age=request.POST.get('age')
        e.gender=request.POST.get('gender')
        e.email=request.POST.get('email')
        e.phone=request.POST.get('phn')
        e.address=request.POST.get('address')
        e.district=request.POST.get('district')
        img=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        fileurl=fs.url(filename)
        e.photo=fileurl
        e.save()
    except:
        e.username=request.POST.get('uname')
        e.firstname=request.POST.get('fname')
        e.lastname=request.POST.get('lname')
        e.staffid=request.POST.get('staffid')
        e.designation=request.POST.get('desg')
        e.age=request.POST.get('age')
        e.gender=request.POST.get('gender')
        e.email=request.POST.get('email')
        e.phone=request.POST.get('phn')
        e.address=request.POST.get('address')
        e.district=request.POST.get('district')
        e.save()
        return redirect('/ViewStaff/')


def updateSeller(request):
    a=request.session['username']
    p=tbl_sellerDetails.objects.get(username=a)
    
    return render(request,"updateSeller.html",{ 'data':p})
def updateSellerAdd(request,id):
    a=request.session['username']
    e=tbl_sellerDetails.objects.get(username=a)
    
    try:
        e.username=request.POST.get('uname')
        e.firstname=request.POST.get('fname')
        e.lastname=request.POST.get('lname')
        
        e.gender=request.POST.get('gender')
        e.email=request.POST.get('email')
        e.phone=request.POST.get('phn')
        e.address=request.POST.get('address')
        e.district=request.POST.get('district')
        img=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        fileurl=fs.url(filename)
        e.photo=fileurl
        e.save()
    except:
        e.username=request.POST.get('uname')
        e.firstname=request.POST.get('fname')
        e.lastname=request.POST.get('lname')
        
        e.gender=request.POST.get('gender')
        e.email=request.POST.get('email')
        e.phone=request.POST.get('phn')
        e.address=request.POST.get('address')
        e.district=request.POST.get('district')
        e.save()
        return redirect('/ViewSeller/')
    
def viewStaff(request):
    p=tbl_staffDetails.objects.all()
    return render(request,"viewStaff.html",{'data':p})
def deleteStaff(request,id):
    p=tbl_staffDetails.objects.get(id=id)
    a=User.objects.get(username=p.username)
    p.delete()
    a.delete()
    return redirect('/viewStaff/')
def viewSeller(request):
    p=tbl_sellerDetails.objects.all()
    return render(request,"viewSeller.html",{'data':p})
def deleteSeller(request,id):
    p=tbl_sellerDetails.objects.get(id=id)
    a=User.objects.get(username=p.username)
    p.delete()
    a.delete()
    return redirect('/viewSeller/')

