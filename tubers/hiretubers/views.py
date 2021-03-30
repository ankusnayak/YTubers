from django.shortcuts import render
from .models import Hiretuber
# Create your views here.

def hiretuber(request):
    if request.method == "POST":
        first_name=requset.POST['first_name']
        last_name=requset.POST['last_name']
        email = requset.POST['email']
        
        
        tuber_id=requset.POST['tuber_id']
        tuber_name = requset.POST['tuber_name']
        
        city=requset.POST['city']
        state=requset.POST['state']
        phone = requset.POST['phone']
        
        message=requset.POST['message']
        user_id=requset.POST['user_id']



        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, tuber_id=tuber_id, tuber_name=tuber_name, city=city, state=state, phone=phone, message=message, user_id=user_id)
        
        hiretuber.save()

        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')