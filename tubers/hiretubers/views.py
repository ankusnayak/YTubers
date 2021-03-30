from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages
# Create your views here.

def hiretuber(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email = request.POST['email']
        
        
        tuber_id=request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        
        city=request.POST['city']
        state=request.POST['state']
        phone = request.POST['phone']
        
        message=request.POST['message']
        user_id=request.POST['user_id']



        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, tuber_id=tuber_id, tuber_name=tuber_name, city=city, state=state, phone=phone, message=message, user_id=user_id)
        
        hiretuber.save()

        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')
        #after sucessfully submision this page redirect to youtubers page and we need to generate a success message  like line 28