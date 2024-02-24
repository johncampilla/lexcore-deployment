from django.urls import path
from . import views

urlpatterns = [
    #path('', views.mylogin, name='my-login'),
    path('', views.userloginview, name='login'),
    path('otp', views.otp_view, name='otp'),
    path('userprofile/register', views.register, name='user-register'),
    path('userprofile/logout', views.logout, name='user-logout'),
    path('userprofile/createuser', views.newuser, name='new-user'),
    path('userprofile/userlist', views.userlist, name='list-user'),
    path("userprofile/removeuser/<int:pk>/'", views.removeuser, name='remove-user'),
    path("userprofile/userinfo/<int:pk>/'", views.userinfo, name='define-userinfo'),
         

]
    
