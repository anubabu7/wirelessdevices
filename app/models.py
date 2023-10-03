from django.db import models

#Create your models here.
class tbl_userAccount(models.Model):
      username=models.CharField(max_length=30)
      firstname=models.CharField(max_length=30)
      email=models.CharField(max_length=30)
      phone=models.IntegerField()
      accountType=models.CharField(max_length=30)
      class Meta:
        db_table="tbl_userAccount"
class tbl_userDetails(models.Model):
      username=models.CharField(max_length=30)
      firstname=models.CharField(max_length=30)
      lastname=models.CharField(max_length=30)
      gender=models.CharField(max_length=30)
      email=models.CharField(max_length=30)
      phone=models.IntegerField()
      address=models.CharField(max_length=50)
      district=models.CharField(max_length=30)
      photo=models.CharField(max_length=50)
     
      class Meta:
        db_table="tbl_userDetails"

class tbl_sellerDetails(models.Model):
      username=models.CharField(max_length=30)
      firstname=models.CharField(max_length=30)
      lastname=models.CharField(max_length=30)
      gender=models.CharField(max_length=30)
      email=models.CharField(max_length=30)
      phone=models.IntegerField()
      address=models.CharField(max_length=50)
      district=models.CharField(max_length=30)
      photo=models.CharField(max_length=50)
     
      class Meta:
        db_table="tbl_sellerDetails"


class tbl_staffDetails(models.Model):
      username=models.CharField(max_length=30)
      firstname=models.CharField(max_length=30)
      lastname=models.CharField(max_length=30)
      staffid=models.IntegerField()
      designation=models.CharField(max_length=30)
      age=models.IntegerField()
      gender=models.CharField(max_length=30)
      email=models.CharField(max_length=30)
      phone=models.IntegerField()
      address=models.CharField(max_length=50)
      district=models.CharField(max_length=30)
      photo=models.CharField(max_length=50)
      
      class Meta:
        db_table="tbl_staffDetails"

class tbl_productDetails(models.Model):
      sellername=models.CharField(max_length=30)
      brandname=models.CharField(max_length=30)
      modelname=models.CharField(max_length=30)
      color=models.CharField(max_length=30)
      price=models.IntegerField()
      offer=models.CharField(max_length=50)
      battery=models.CharField(max_length=30)
      playback=models.CharField(max_length=30)
      status=models.CharField(max_length=30)
      photo=models.CharField(max_length=50)
      class Meta:
          db_table="tbl_productDetails"

class tbl_feedback(models.Model):
      username=models.CharField(max_length=30)
      brandname=models.CharField(max_length=30)
      feedback=models.CharField(max_length=200)
      status=models.CharField(max_length=30)
      class Meta:
          db_table="tbl_feedback"

class tbl_offer(models.Model):
      sellername=models.CharField(max_length=30)
      brandname=models.CharField(max_length=30)
      modelname=models.CharField(max_length=30)
      offer=models.CharField(max_length=50)
      start_date=models.DateField()
      end_date=models.DateField()
      class Meta:
          db_table="tbl_offer"
class tbl_cart(models.Model):
    username=models.CharField(max_length=30)
    modelname=models.CharField(max_length=30)
    brandname=models.CharField(max_length=30)
    sellername=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.IntegerField()
    
    total_amount=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    photo=models.CharField(max_length=50)
    class Meta:
        db_table="tbl_cart"
class tbl_order(models.Model):
    username=models.CharField(max_length=30)
    modelname=models.CharField(max_length=30)
    brandname=models.CharField(max_length=30)
    sellername=models.CharField(max_length=30)
    order_date=models.DateField()
    status=models.CharField(max_length=30)
    payment=models.CharField(max_length=30)
    total_amount=models.CharField(max_length=30)
    photo=models.CharField(max_length=50)
    class Meta:
        db_table="tbl_order"





  


