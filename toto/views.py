from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import det,donor,receipent
from django.contrib.auth import authenticate,login as ln,logout
from django.http import HttpResponse
def index(request):
    return render(request, "toto/index.html")

def user_signin(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        gender=request.POST['gender']
        address=request.POST['address']
        bloodgroup=request.POST['bloodgroup']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print("Creating user:", username) 
         
        if not username.isalnum():
            messages.success(request,'username must be alphanumeric')
            return redirect('signin')
        if (password1 != password2):
            messages.success(request,'password doesnt match')
            return redirect('signin')
        
        myuser=User.objects.create_user(username=username, email=email, password=password1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        
        messages.success(request,'your account has been logged in')
        return redirect('main')
    else:
        return render(request, 'toto/signin.html')


def user_login(request):
    if request.method=='POST':
        loginusername=request.POST['lusername']
        loginpassword=request.POST['lpassword']
        user= authenticate(username=loginusername,password=loginpassword)
        
        if user is not None:
            ln(request,user)
            messages.success(request,"successfully logged in.")
            return redirect('main')
        else:
            messages.error(request,'invalid credentials.')
            return redirect('login')
    return render(request,'toto/login.html')


def donor_req(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        middlename = request.POST.get('middlename', '')
        lastname = request.POST.get('lastname', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        image = request.FILES.get('image')
        bloodgroup = request.POST.get('bloodgroup', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        new_donor = donor(
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            gender=gender,
            address=address,
            image=image,
            bloodgroup=bloodgroup,
            phone=phone,
            email=email,
            password=password
        )
        new_donor.save()

    return render(request, 'toto/register.html')




def receipent_req(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        middlename = request.POST.get('middlename', '')
        lastname = request.POST.get('lastname', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        image = request.FILES.get('image')
        bloodgroup = request.POST.get('bloodgroup', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        new_receipent = receipent(
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            gender=gender,
            address=address,
            image=image,
            bloodgroup=bloodgroup,
            phone=phone,
            email=email,

        )
        new_receipent.save()
    return render(request, 'toto/order.html') 
        # return render(request, 'toto/order.html')
   




def main(request):
    return render(request,'toto/main.html')

def service(request):
    return render(request, "toto/service.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        new_entry = det(name=name, email=email, message=message)
        new_entry.save()

        return render(request, 'toto/contact.html')  
    return render(request, 'toto/contact.html')

# def register(request):
#     return render(request, "toto/register.html")

def about(request):
    return render(request, "toto/about.html")

# def order(request):
#     return render(request, "toto/order.html")