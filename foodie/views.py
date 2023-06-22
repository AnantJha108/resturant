from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')


def search_product(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            data = Foodie.objects.filter(name__contains=query_name)
            context = {'data' : data}
            return render(request, 'index.html',context)
    return render(request, 'index.html')
