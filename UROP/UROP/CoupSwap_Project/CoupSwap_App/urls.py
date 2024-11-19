from django.urls import path
from CoupSwap_App import views
from django.contrib.auth import views as ad


urlpatterns = [
    path('',views.home,name="hm"),
    path('register/',views.Register,name='rg'),
    path('login/',ad.LoginView.as_view(template_name="html/login.html"),name='ln'),
    path('logout/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lo"),
    path('Coupons/',views.Coupons,name='co'),
    path('AddCoupon/',views.AddCoupon,name='ac'),
    path('Profile/',views.Profile,name='pf'),
    path('UpdateCoupon/<int:i>',views.UpdateCoupon,name='uc'),
    path('DeleteCoupon/<int:i>',views.DeleteCoupon,name='dc'),
    path('CouponDetails/<int:i>',views.CouponDetails,name='cd'),
    path('ViewRequest/<int:i>',views.ViewRequest,name='vr'),
    path('Payment',views.Payment,name='pa'),
    path('success',views.Success,name='su'),
    path('History/<int:i>',views.History,name='hi'),
    path('Change Password/',views.chgepwd,name='cp'),
    path('Update Profile/',views.UpPfl,name='up'),
]