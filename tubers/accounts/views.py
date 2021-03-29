from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.

#base_url/accounts/login
def login(request):
    return render(request, 'accounts/login.html')

# base_base_url/accounts/logout    
def logout_user(request):
    logout(request)
    return redirect('home')

#base_url/accounts/register    
def register(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password = request.POST['confirm_password']
        

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()

                messages.success(request, 'Account created successfully')
                return redirect('login')
            
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')

    return render(request, 'accounts/register.html')
    
#base_url/accounts/dashboard    
def dashboard(request):
    return render(request,'accounts/dashbaord.html')