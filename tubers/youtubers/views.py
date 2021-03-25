from django.shortcuts import render
from .models import Youtuber
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
    return render(request,'youtubers/youtubers_detail.html',data)
def search(request):
    pass