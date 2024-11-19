from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=10,null=True,blank=True)
    pfimg = models.ImageField(upload_to='Profiles/',default='pfle.png')
    cash = models.IntegerField(default=0)

class Coupon(models.Model):
    pfchs = [('None','Select'), ('Phonepe','Phonepe'), ('Google Pay','Google Pay'), ('Amazon','Amazon'), ('Paytm','Paytm'), ('Flipkart','Flipkart'), ('Myntra','Myntra'), ('Others','Others')]
    sts = [('Uploaded','Uploaded'), ('Requested','Requested'), ('Used','Used'), ('Expired','Expired')]
    PfName = models.CharField("Platform Name",choices=pfchs,default='None',max_length=15)
    Title = models.CharField("Title",max_length=100)
    Company = models.CharField("Company",max_length=100)
    ExpDate = models.DateField("Expiry Date")
    Code = models.CharField("Coupon Code", max_length=15)
    Description = models.FileField(upload_to='CouponDetails/')
    Status = models.CharField("Status",choices=sts,default='Uploaded',max_length=20)
    st = models.ForeignKey(User,on_delete=models.CASCADE)
    demandedamount = models.IntegerField("Demanded Amount",default=0)
    requestedby = models.IntegerField(null=True)
    usedby = models.IntegerField(null=True)

class Transaction(models.Model):
    tp = [("Deposit","Deposit"), ("Coupon Used","Coupon Used")]
    TranDate = models.DateField("Transaction Date",default=date.today())
    debitfrom = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Debit")
    creditto = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Credit")
    coupondet = models.OneToOneField(Coupon,on_delete=models.CASCADE,null=True)
    amount = models.IntegerField()
    type = models.CharField("Type of transaction",choices=tp,default="Deposit",max_length=15)


