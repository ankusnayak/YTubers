from django.shortcuts import render
from .models import Youtuber
from django.shortcuts import get_object_or_404
# Create your views here.
def youtubers(request):
    #get all the tubers not featured_wise
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers':tubers,
    }
    return render(request,'youtubers/youtubers.html',data)
def youtubers_detail(request,id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber':tuber,
    }
    #it can response http response or render a template as response
    return render(request,'youtubers/youtubers_detail.html',data)
def search(request):
    #all data
    tubers = Youtuber.objects.order_by('-created_date')
    #all distinct city
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    #all distinct camera
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    #all distinct camera
    category_search=Youtuber.objects.values_list('category',flat=True).distinct()
    # this is key value pair type assume get request is a hash table and there is lots of key and value if this match with 'keyword' then take the value
    if 'keyword' in request.GET:
         keyword = request.GET['keyword']
         if keyword:
             tubers = tubers.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            #tuber object re assign here
            tubers=tubers.filter (city__iexact=city)     
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
            
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)
            

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search':category_search,
    }
    
    return render(request,'youtubers/search.html',data)