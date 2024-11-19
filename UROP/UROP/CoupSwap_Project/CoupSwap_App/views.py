from django.shortcuts import render,redirect
from .forms import UserForm,CouponForm,UpdatePf,ChgPwdForm
from static.images.companies.imagefind import downloadimg
from .models import Coupon,User,Transaction
from django.contrib import messages
from datetime import date
from django.core.mail import send_mail
from CoupSwap_Project import settings
import razorpay

# Create your views here.
def home(request):
    cp = Coupon.objects.all()
    for i in cp:
        if i.ExpDate < date.today() and i.Status!="Used":
            i.Status="Expired"
            i.usedby=None
            i.save()
    cp = Coupon.objects.filter(Status="Uploaded")
    if request.method == "POST":
        if request.POST['Company'] != "":
            lst=[]
            for i in cp:
                if request.POST['Company'].lower() in i.Company:
                    lst.append(i)
            cp=lst
    return render(request,'html/home.html',{'ccf':cp})

def Register(request):
    if request.method == 'POST':
        uf=UserForm(data=request.POST)
        if uf.is_valid():
            uf.save()
        messages.success(request,"Registeration Sucessfull!")
        send_mail("Welcome to Coup Swap!","Registration Successfull you can now Login to your account to access coupons and claim rewards",settings.EMAIL_HOST_USER,[request.user.email])
        return redirect('/login/')
    uf = UserForm()
    return render(request,'html/Register.html',{'Userf':uf})

def Coupons(request):
    cp = Coupon.objects.filter(st_id=request.user.id)
    return render(request,'html/Coupons.html',{'yrcpn':cp})

def AddCoupon(request):
    if request.method == "POST":
        cf = CouponForm(request.POST,request.FILES)
        if cf.is_valid():
            d = cf.save(commit=False)
            print(d.Description)
            d.Company = d.Company.lower()
            d.st_id = request.user.id
            d.save()
            downloadimg(d.Company)
            messages.success(request,"Coupon Added!")
            return redirect('/AddCoupon')
    else:
        cf = CouponForm()
    return render(request,'html/AddCoupon.html',{'ccf':cf})

def UpdateCoupon(request,i):
    k = Coupon.objects.get(id=i)
    upcpnform = CouponForm(instance=k)
    if request.method == "POST":
        upcpnform = CouponForm(request.POST,request.FILES,instance=k)
        if upcpnform.is_valid:
            de = upcpnform.save(commit=False)
            de.Company = de.Company.lower()
            de.save()
            messages.success(request,"Coupon Updated!")
            downloadimg(de.Company)
            return redirect('/AddCoupon')
    return render(request,'html/UpdateCoupon.html',{'ucform':upcpnform,'coupid':i,'coupdesc':'images/'+str(k.Description)})

def CouponDetails(request,i):
    details = Coupon.objects.get(id=i)
    if request.method == "POST":
        details.Status = "Requested"
        details.requestedby = request.user.id
        details.usedby = None
        details.save()
        send_mail("Coupon Requested SuccessFully!","Company: "+details.Company+"\nTitle: "+details.Title+"\nExpiry Date: "+str(details.ExpDate),settings.EMAIL_HOST_USER,[request.user.email])
        send_mail(request.user.username+" has Requested for your Coupon","Coupon details: Company: "+details.Company+"\nTitle: "+details.Title+"\nExpiry Date: "+str(details.ExpDate)+"\n\nRequested By:\nUsername: "+request.user.username+"\nMail: "+request.user.email,settings.EMAIL_HOST_USER,[User.objects.get(id=details.st_id).email])
        messages.success(request,"Coupon Requested!")
        return redirect('/')
    imgpt = "images/companies/"+details.Company+".png"
    return render(request,'html/CouponDetails.html',{'det':details,'imgpth':imgpt,'owner':User.objects.get(id=details.st_id),'coupdesc':'images/'+str(details.Description)})

def DeleteCoupon(request,i):
    d = Coupon.objects.get(id=i)
    if request.method == "POST":
        d.delete()
        messages.warning(request,"Coupon Deleted!")
        return redirect('/AddCoupon')
    return render(request,'html/DeleteCoupon.html',{'det':d,'coupdesc':'images/'+str(d.Description),'compimg':'images/companies/'+str(d.Company)+'.png'})

def ViewRequest(request,i):
    coupdet = Coupon.objects.get(id=i)
    reuserdet = User.objects.get(id=coupdet.requestedby)
    if request.method == "POST":
        if 'Decline' in request.POST:
            coupdet.Status = "Uploaded"
            coupdet.requestedby = coupdet.usedby = None
            messages.warning(request,"Request Declined!")
            coupdet.save()
            send_mail("Coupon Request Declined!","You Request for this coupon is declined\nCompany: "+coupdet.Company+"\nTitle: "+coupdet.Title+"\nExpiry Date: "+str(coupdet.ExpDate),settings.EMAIL_HOST_USER,[reuserdet.email])
        elif 'Accept' in request.POST:
            request.user.cash+=coupdet.demandedamount
            request.user.save()
            reuserdet.cash-=coupdet.demandedamount
            reuserdet.save()
            coupdet.Status = "Used"
            coupdet.usedby = coupdet.requestedby
            coupdet.requestedby = None
            coupdet.save()
            newtr = Transaction.objects.create(TranDate=date.today(),debitfrom_id=reuserdet.id,creditto_id=request.user.id,coupondet_id=i,amount=coupdet.demandedamount,type="Coupon Used")
            newtr.save()
            send_mail("Coupon Request Accepted!","You Request for this coupon is Accepted!\nCompany: "+coupdet.Company+"\nTitle: "+coupdet.Title+"\nExpiry Date: "+str(coupdet.ExpDate)+"\nCode: "+coupdet.Code,settings.EMAIL_HOST_USER,[reuserdet.email])
            messages.success(request,"Request Accepted!")
        return redirect('/AddCoupon')
    imgpt = "images/companies/"+coupdet.Company+".png"
    return render(request,'html/ViewRequest.html',{'det':coupdet,'rd':reuserdet,'imgpth':imgpt})

def Profile(request):
    return render(request,'html/Profile.html')


def UpPfl(request):
    k = User.objects.get(id=request.user.id)
    upform = UpdatePf(instance=k)
    if request.method == "POST":
        upform = UpdatePf(request.POST,request.FILES,instance=k)
        if upform.is_valid():
            upform.save()
            messages.success(request,"Profile Updated")
            return redirect('/Profile/')
    return render(request,'html/UpdateProfile.html',{'upf':upform})

def chgepwd(request):
	if request.method == "POST":
		n = ChgPwdForm(user=request.user,data=request.POST)
		if n.is_valid():
			n.save()
			return redirect('/lgn')
	n = ChgPwdForm(user=request)
	return render(request,'html/ChangePassword.html',{'h':n})

def Payment(request):
    amt,n = 50000,0
    if request.method == "POST":
        if 'amount' in request.POST:
            amt,n = request.POST['amount']+"00",1
        client = razorpay.Client(auth=("rzp_test_nODbGBtvMlQEzs", "kktaQSIZJTzIyJriETB8BjvN"))
        payment = client.order.create({'amount': amt, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
        request.user.cash+=int(amt[:-2])
        request.user.save()
        newtr = Transaction.objects.create(TranDate=date.today(),debitfrom_id=request.user.id,creditto_id=1,coupondet_id=None,amount=amt[:-2],type="Deposit")
        newtr.save()
    return render(request,'html/Payment.html',{'amt':amt,'n':n})

def Success(request):
    return render(request,'html/success.html')

def History(request,i):
    trans=Transaction.objects.all()
    reqcp = Coupon.objects.filter(requestedby=request.user.id)
    usecp = Coupon.objects.filter(usedby=request.user.id)
    return render(request,'html/History.html',{'transactions':trans,'reqcpn':reqcp,'usecpn':usecp,'i':i})
