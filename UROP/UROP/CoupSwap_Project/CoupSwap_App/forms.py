from django import forms
from .models import User,Coupon
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from datetime import date

class UserForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Re-Enter Password"}))
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"email":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Email",
			}),
		}
                
class UpdatePf(forms.ModelForm):
    class Meta:
        model=User
        fields = ["username","first_name","last_name","email","mobile","pfimg"]
        widgets ={
            "username":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Username",}),
            "first_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"First Name",}),
            "last_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Last Name",}),
            "mobile":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Mobile",}),
			"email":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Email",}),
		}

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ["PfName","Title","Company","ExpDate","Code","demandedamount","Description"]
        widgets ={
            "PfName":forms.Select(attrs={"class":"form-control my-2"}),
            "Title":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Title"}),
            "Company":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Company"}),
            "ExpDate":forms.DateInput(attrs={"type":"date","class":"form-control my-2","placeholder":"Expiry Date","min":date.today()}),
            "Code":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Coupon Code"}),
            "demandedamount":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Demanded Amount"}),
        }

class ChgPwdForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Old Password"}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"New Password"}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = "__all__"