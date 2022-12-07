import imp
from django.urls import path
from . import views


urlpatterns = [
    path('',views.indexe,name='index'),
    path('cont',views.cont,name='cont'),
    path('abt',views.abt,name='abt'),
    path('destinations',views.destinations,name='destinations'),
    path('user_login1',views.user_login1,name='login1'),
    path('covid',views.covid,name='covid'),
    
    path('Login',views.user_login,name='Login'),
    path('register',views.register,name='register'),
    path('logout',views.user_logout,name='logout'),
]   