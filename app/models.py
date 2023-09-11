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



  


