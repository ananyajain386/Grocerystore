from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class sections(models.Model):
   SectionName = models.CharField(max_length=30, blank=False,default="",unique=True)
   Img = models.ImageField(upload_to='Pictures/',blank=True, null=True) 
   removed=models.BooleanField(default=False) 
   class Meta:
      #  abstract = True
       db_table = "music_album"
class products(models.Model):
   section=models.ForeignKey(sections,on_delete=models.CASCADE,null=True)
   ProductName = models.CharField(max_length=30, blank=False,default="")
   qt = models.IntegerField(blank=True,default=1)
   Mf_Date = models.DateField(null=True)
   Ep_Date = models.DateField(null=True)
   Priceperun = models.IntegerField(blank=False, default=0)
   Img = models.ImageField(upload_to='Pictures1/',blank=True, null=True)
   removed=models.BooleanField(default=False)
class cart(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    Quantity = models.IntegerField(blank=False,default=1)
    removed=models.BooleanField(default=False)
    Priceperun = models.IntegerField(blank=False, default=0)
    Netprice= models.IntegerField(blank=False, default=0)
    ordered=models.BooleanField(default=False)

# class buy(models.Model):
    #   product=models.ForeignKey(products,on_delete=models.CASCADE)
    #   customer=models.ForeignKey(User,on_delete=models.CASCADE)
    #   Quantity = models.IntegerField(blank=False, default=0)



# class register(models.Model):
#   User = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#   Userame = models.CharField(max_length=30, blank=False,default="")
#   Firstname = models.CharField(max_length=30, blank=False,default="")
#   Lastname = models.CharField(max_length=30, blank=False,default="")
#   Email = models.EmailField(max_length=50, blank= False, unique=True,default="",error_messages={'unique':("A user with that email already exists.")})
#   Password = models.CharField(max_length=100, blank=False, default="")
#   Login = models.IntegerField(blank=False, default=0)