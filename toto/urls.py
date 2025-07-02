from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('', views.index, name='index'),
    path('signin.html', views.user_signin,name='signin'),
    path('main.html', views.main,name='main'),
    path('service.html', views.service, name='service'),
    path('register.html', views.donor_req, name='register'),
    path('contact.html', views.contact, name='contact'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('order.html', views.receipent_req, name='order'),
    path('login.html', views.user_login, name='login'),
 
]
