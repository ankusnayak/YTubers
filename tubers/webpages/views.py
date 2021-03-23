from django.shortcuts import render
from .models import Slider,Team

# Create your views here.
#these are all method based views
def home(request):
    # get the data from database
    # consume all the slider objects present in the database 
    sliders = Slider.objects.all()
    teams=Team.objects.all()
    # now pass the array or list of object as a object form to the template 
    data = {
        'sliders': sliders,
        'teams':teams
    } 
    return render(request,'webpages/home.html',data)
def about(request):
    return render(request,'webpages/about.html')
def services(request):
    return render(request,'webpages/services.html')
def contact(request):
    return render(request,'webpages/contact.html')