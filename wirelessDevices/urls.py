"""
URL configuration for wirelessDevices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('createAccount/',views.createAccount),
    path('login1/',views.login1),
    path('adminHome/',views.adminHome),
    path('home/',views.index),
    path('staffHome/',views.staffHome),
    path('sellerHome/',views.sellerHome),
    path('userHome/',views.userHome),

    path('addStaff/',views.addStaff),
    path('addStaffAccount/',views.addStaffAccount),

    path('addSeller/',views.addSeller),
    path('addSellerAccount/',views.addSellerAccount),

    path('addAccount/',views.addAccount),

    path('viewUser/',views.viewUser),
    path('updateStaff/',views.updateStaff),
    path('updateStaffAdd/<int:id>',views.updateStaffAdd),
    path('viewStaff/',views.viewStaff),
    path('deleteStaff/<int:id>',views.deleteStaff),
    path('viewSeller/',views.viewSeller),
    path('deleteSeller/<int:id>',views.deleteSeller),
    path('updateSeller/',views.updateSeller),
    path('updateSellerAdd/<int:id>',views.updateSellerAdd),
    path('login/',views.login),
    

    

]
