from django.db import reset_queries
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Contact

def register_customer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_customer')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register_customer')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password = password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register_customer')
    else:
        return render(request, 'accounts/register_customer.html')

def register_vendor(request):
    if request.method == 'POST':
        first_name = request.POST['shop_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        # shop_address = request.POST['shop_address'] // Need to save shop address
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_vendor')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email ID already exists')
                return redirect('register_vendor')
            else:
                user = User.objects.create_user(first_name=first_name, username=username, email=email, password = password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register_vendor')
    else:
        return render(request, 'accounts/register_vendor.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def profile(request):
    context = {'user': request.user}
    return render(request, 'accounts/profile.html', context)

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        messages = Contact.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
        messages.save()
        return render(request, 'contact_us.html')
    else:
        return render(request, 'contact_us.html')