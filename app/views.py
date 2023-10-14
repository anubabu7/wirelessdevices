from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from app.models import tbl_userAccount,tbl_userDetails,tbl_sellerDetails,tbl_staffDetails,tbl_productDetails,tbl_feedback,tbl_offer,tbl_cart,tbl_order,tbl_staffDuties
import datetime
from django.core.paginator import Paginator
from django.db import connection
#  from django.core.paginator import Paginator
# Create your views here.
def index(request):
   return render(request,"index.html")
   
    

def login1(request):
     return render(request,"login1.html")
def userHome(request):
    p=request.session['username']
    b=tbl_userDetails.objects.get(username=p)
    
    return render(request,"userHome.html",{'x':b})
def adminHome(request):
    return render(request,"adminHome.html")
def staffHome(request):
    p=request.session['username']
    b=tbl_staffDetails.objects.get(username=p)
    return render(request,"StaffHome.html",{'x':b})
    
def sellerHome(request):
    p=request.session['username']
    b=tbl_sellerDetails.objects.get(username=p)
    return render(request,"SellerHome.html",{'x':b})
    
def viewProfileUser(request):
    p=request.session['username']
    b=tbl_userDetails.objects.get(username=p)
    return render(request,"viewProfileUser.html",{'x':b} )
def viewProfileStaff(request):
    p=request.session['username']
    b=tbl_staffDetails.objects.get(username=p)
    return render(request,"viewProfileStaff.html",{'x':b} )
def viewProfileSeller(request):
    p=request.session['username']
    b=tbl_sellerDetails.objects.get(username=p)
    return render(request,"viewProfileSeller.html",{'x':b} )

#-----create account for user
def createAccount(request):
    return render(request,"createAccount.html")
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
 
    return redirect('/adminHome/')
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
    return redirect('/adminHome/') 

#------staff account creation-------------------

#  --------authentication--------------
def login(request):
    uname=request.POST.get('uname')
    pwd=request.POST.get('pwd')
    p=authenticate(username=uname,password=pwd)
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


#--------updatestaff--------
def updateStaff(request,username):
    #a=request.session['username']
    p=tbl_staffDetails.objects.get(username=username)
    
    return render(request,"updateStaff.html",{ 'data':p})
def updateStaffAdd(request,username):
    #a=request.session['username']
    e=tbl_staffDetails.objects.get(username=username)
    b=tbl_userAccount.objects.get(username=username)

    
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
        b.username=request.POST.get('uname')
        b.firstname=request.POST.get('fname')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phn')
        b.accountType="staff"
        e.save()
        b.save()
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
        b.username=request.POST.get('uname')
        b.firstname=request.POST.get('fname')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phn')
        b.accountType="staff"
        e.save()
        b.save()
        return redirect('/viewStaff/')


def updateSeller(request,username):
    p=tbl_sellerDetails.objects.get(username=username)
    # a=request.session['username']
    return render(request,"updateSeller.html",{'data':p})
def updateSellerAdd(request,username):
    e=tbl_sellerDetails.objects.get(username=username)
    b=tbl_userAccount.objects.get(username=username)
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
        b.username=request.POST.get('uname')
        b.firstname=request.POST.get('fname')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phn')
        b.accountType="seller"
        e.save()
        b.save()
    except:
        e.username=request.POST.get('uname')
        e.firstname=request.POST.get('fname')
        e.lastname=request.POST.get('lname')
        
        e.gender=request.POST.get('gender')
        e.email=request.POST.get('email')
        e.phone=request.POST.get('phn')
        e.address=request.POST.get('address')
        e.district=request.POST.get('district')
        b.username=request.POST.get('uname')
        b.firstname=request.POST.get('fname')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phn')
        b.accountType="seller"
        e.save()
        b.save()
        return redirect('/viewSeller/')
    
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
def viewSellerUser(request):
    p=tbl_sellerDetails.objects.all()
    return render(request,"viewSellerUser.html",{'data':p})
def viewSellerStaff(request):
    p=tbl_sellerDetails.objects.all()
    return render(request,"viewSellerStaff.html",{'data':p})
def viewProductStaff1(request):
    p=tbl_productDetails.objects.all()
    return render(request,"viewProductStaff1.html",{'data':p})
def viewProductStaff(request,username):
    p=request.session['username']
    p1=tbl_productDetails.objects.filter(sellername=username)
    return render(request,"viewProductStaff.html",{'data':p1,'x':p})


def deleteSeller(request,id):
    p=tbl_sellerDetails.objects.get(id=id)
    a=User.objects.get(username=p.username)
    p.delete()
    a.delete()
    return redirect('/viewSeller/')


#-----------------updateuser----------------
def updateUser(request,username):
    #a=request.session['username']
    p=tbl_userDetails.objects.get(username=username)
    
    return render(request,"updateUser.html",{'data':p})
def updateUserAdd(request,username):
    #a=request.session['username']
    e=tbl_userDetails.objects.get(username=username)
    b=tbl_userAccount.objects.get(username=username)
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
        b.username=request.POST.get('uname')
        b.firstname=request.POST.get('fname')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phn')
        b.accountType="User"
        e.save()
        b.save()
    except:
        e.username=request.POST.get('uname')
        e.firstname=request.POST.get('fname')
        e.lastname=request.POST.get('lname')
        e.gender=request.POST.get('gender')
        e.email=request.POST.get('email')
        e.phone=request.POST.get('phn')
        e.address=request.POST.get('address')
        e.district=request.POST.get('district')
        b.username=request.POST.get('uname')
        b.firstname=request.POST.get('fname')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phn')
        b.accountType="User"
        e.save()
        b.save()
        return redirect('/userHome/')
    

def deleteUser(request,id):
    p=tbl_userDetails.objects.get(id=id)
    a=User.objects.get(username=p.username)
    p.delete()
    a.delete()
    return redirect('/viewUser/')

    #-----------PRODUCT DETAILS-----------
def product(request):
    p=request.session['username']
    return render(request,"product.html",{'x':p})
def addProduct(request):
    a=tbl_productDetails()
    a.sellername=request.POST.get('sellername')
    a.brandname=request.POST.get('brandname')
    a.modelname=request.POST.get('modelname')
    a.color=request.POST.get('color')
    a.price=request.POST.get('price')
    a.offer=request.POST.get('offer')
    a.battery=request.POST.get('battery')
    a.playback=request.POST.get('playback')
    a.status=request.POST.get('status')
    img=request.FILES['img']
    fs=FileSystemStorage()
    filename=fs.save(img.name,img)
    fileurl=fs.url(filename)
    a.photo=fileurl
    a.save()
    return redirect('/sellerHome/')

def viewProduct(request):
    p=tbl_productDetails.objects.all()
    return render(request,"viewProduct.html",{'data':p})
def viewProductSeller(request):
    a=request.session['username']
    p=tbl_productDetails.objects.filter(sellername=a)
    return render(request,"viewProduct.html",{'data':p})

def viewProductUser(request):
    p=tbl_productDetails.objects.all()
    return render(request,"viewProductUser.html",{'data':p})
def updateProduct(request,id):
    p=tbl_productDetails.objects.get(id=id)
    return render(request,"updateProduct.html",{'data':p})
def updateProductAdd(request,id):
        a=tbl_productDetails.objects.get(id=id)
        try:
            a.sellername=request.POST.get('sellername')
            a.brandname=request.POST.get('brandname')
            a.modelname=request.POST.get('modelname')
            a.color=request.POST.get('color')
            a.price=request.POST.get('price')
            a.offer=request.POST.get('offer')
            a.battery=request.POST.get('battery')
            a.playback=request.POST.get('playback')
            a.status=request.POST.get('status')
            img=request.FILES['img']
            fs=FileSystemStorage()
            filename=fs.save(img.name,img)
            fileurl=fs.url(filename)
            a.photo=fileurl
            a.save()
        except:
            a.sellername=request.POST.get('sellername')
            a.brandname=request.POST.get('brandname')
            a.modelname=request.POST.get('modelname')
            a.color=request.POST.get('color')
            a.price=request.POST.get('price')
            a.offer=request.POST.get('offer')
            a.battery=request.POST.get('battery')
            a.playback=request.POST.get('playback')
            a.status=request.POST.get('status')
            a.save()
        return redirect('/sellerHome/')
def deleteProduct(request,id):
    p=tbl_productDetails.objects.get(id=id)
    p.delete()
    return redirect('/viewProduct/')


#------------OFFER--------------

def offer(request):
    p=request.session['username']
    tb=tbl_productDetails.objects.filter(sellername=p)
    return render(request,"offer.html",{'x':p,'data':tb})
def addOffer(request):
    a=tbl_offer()
    a.sellername=request.POST.get('sellername')
    a.brandname=request.POST.get('brandname')
    a.modelname=request.POST.get('modelname')
    a.offer=request.POST.get('offer')
    a.start_date=request.POST.get('startdate')
    a.end_date=request.POST.get('enddate')
    
    a.save()
    return redirect('/sellerHome/')

def viewOffer(request):
    p=tbl_offer.objects.all()
    return render(request,"viewOffer.html",{'data':p})
def viewOfferUser(request):
    p=tbl_offer.objects.all()
    return render(request,"viewOfferUser.html",{'data':p})
def updateOffer(request,id):
    p=tbl_offer.objects.get(id=id)
    return render(request,"updateOffer.html",{'data':p})
def updateOfferAdd(request,id):
        a=tbl_offer.objects.get(id=id)
        a.sellername=request.POST.get('sellername')
        a.brandname=request.POST.get('brandname')
        a.modelname=request.POST.get('modelname')
        a.offer=request.POST.get('offer')
        a.start_date=request.POST.get('startdate')
        a.end_date=request.POST.get('enddate')
        
        a.save()
        return redirect('/sellerHome/')
def deleteOffer(request,id):
    p=tbl_offer.objects.get(id=id)
    p.delete()
    return redirect('/viewOffer/')


#----------------FEEDBACKS-------------


def feedback(request):
    return render(request,"feedback.html")
def addFeedback(request):
    a=tbl_feedback()
    a.username=request.POST.get('uname')
    a.brandname=request.POST.get('brandname')
    a.feedback=request.POST.get('feedback')
    a.status=request.POST.get('status')
    a.save()
    return redirect('/userHome/')

def viewFeedback(request):
    p=tbl_feedback.objects.all()
    return render(request,"viewFeedback.html",{'data':p})

def deleteFeedback(request,id):
    p=tbl_feedback.objects.get(id=id)
    p.delete()
    return redirect('/viewFeedback/')
def addToCart(request,id):
    p=request.session['username']
    
    b=tbl_productDetails.objects.get(id=id)
    return render (request,"addToCart.html",{'x':p,'data':b})
def addToCart1(request):
        id=request.POST.get('id')
        b=tbl_productDetails.objects.get(id=id)
        a=tbl_cart()
        a.username=request.POST.get('uname')
        a.sellername=b.sellername
        a.modelname=b.modelname
        a.brandname=b.brandname
        a.quantity=request.POST.get('quantity')
        a.price=b.price
        a.photo=b.photo
        a.total_amount= int(a.price)*int(a.quantity)
        a.status="In-Cart"
        a.save()
        return redirect('/userHome/')

        
def viewCart(request):
    a=request.session['username']
    p=tbl_cart.objects.filter(username=a,status="In-Cart")
   
    sum =0
    qty=0
    for x in p:
        sum=sum + int(x.total_amount)
        qty= qty + int(x.quantity)
    paginator = Paginator(p, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)   
    print(page_obj,"test2") 
    return render(request,"viewCart.html",{'data':p,'y':a,'m':sum ,'q':qty,"page_obj": page_obj})
def delCartItem(request,id):
    p=tbl_cart.objects.get(id=id)
    p.delete()
    return redirect('/viewCart/')
def order(request,id):
    a=request.session['username']
    p=tbl_cart.objects.get(id=id)
    return render(request,"order.html",{'data':p,'x':a})
    
def addOrder(request):
    id=request.POST.get('id')
    p=tbl_cart.objects.get(id=id)
    a=tbl_order()
   
    a.username=request.POST.get('uname')
    a.brandname=request.POST.get('brandname')
    a.sellername=p.sellername
    a.modelname=p.modelname
    a.order_date=datetime.datetime.now() 
    a.status="In-Order"
    a.payment=request.POST.get('payment')
    a.total_amount=request.POST.get('total')
    a.photo=p.photo
    p.status="In-order"
    p.save()
    a.save()
   
    return redirect('/userHome/')
def viewOrder(request):
    a=request.session['username']
    p=tbl_order.objects.filter(username=a)
    sum =0
    for x in p:
        sum=sum + int(x.total_amount)
    paginator = Paginator(p, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)   
    print(page_obj,"test2") 
    return render(request,"viewOrder.html",{'data':p,'y':a,'m':sum, "page_obj": page_obj })
def viewUser(request):
    p=tbl_userDetails.objects.all()
    paginator = Paginator(p, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)   
    print(page_obj,"test2") 
    return render(request,"viewUser.html",{'data':p, "page_obj": page_obj })
def viewProductImg(request,id):
    b=tbl_productDetails.objects.get(id=id)
    return render(request,"viewProductImg.html",{'x':b})
def viewOrderStaff(request):
    a=request.session['username']
    p=tbl_order.objects.filter(sellername=a,status="In-order")
    return render(request,"viewOrderStaff.html",{'data':p,'y':a})
def viewOrderStaffAssign(request):
    a=request.session['username']
    p=tbl_order.objects.filter(sellername=a,status="Order Approved")
    return render(request,"viewOrderStaffAssign.html",{'data':p,'y':a})
def assignStaffForm(request,id):
    p=request.session['username']
    tb=tbl_staffDetails.objects.all()
    a=tbl_order.objects.get(id=id)
    
    return render(request,"assignStaffForm.html",{'x':p,'data':tb,'y':a})
    
def assignStaff(request):
    b=tbl_staffDuties()
    b.sellername=request.POST.get('sellername')
    b.staffname=request.POST.get('uname')
    b.assigned_date=datetime.datetime.now() 
    b.status="Pending"
    b.instructions=request.POST.get('instructions')
    b.order_id=request.POST.get('orderid')
    b.save()
    return redirect('/viewOrderStaffAssign/')
def approveOrder(request,id):
    p=tbl_order.objects.get(id=id)
    p.status="Order Approved"
    p.save()
    return redirect('/viewOrderStaffAssign/')
def deleteOrder(request,id):
    p=tbl_order.objects.get(id=id)
    p.delete()
    return redirect('/viewOrderStaffAssign/')
def orderCancel(request,id):
    p=tbl_order.objects.get(id=id)
    p.status="Order Cancelled"
    p.save()
    return redirect('/viewOrderStaffAssign/')
def readyDispatch(request,id):
    p=tbl_order.objects.get(id=id)
    p.status="Ready To Dispatch"
    p.save()
    return redirect('/viewOrderStaffHome/')
def viewDuty(request):
    a=request.session['username']
    p=tbl_staffDuties.objects.filter(staffname=a)
    return render(request,"viewDuty.html",{'data':p})
def viewOrderStaffHome(request):
    
    p=tbl_order.objects.all()
    return render(request,"viewOrderStaffHome.html",{'data':p})
def viewStatus(request):
    a=request.session['username']
    p=tbl_order.objects.filter(username=a)
    return render(request,"viewStatus.html",{'data':p})



def demo(request):
    p=tbl_productDetails.objects.all()
    return render(request,"demo.html",{'data':p})

   




    

    






























