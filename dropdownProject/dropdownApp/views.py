from django.shortcuts import render
from .models import Country,City
import json
from django.http import JsonResponse
# Create your views here.


def index(request):
    countries = Country.objects.all()
    context = {
        'countries' : countries,
    }
    return render(request,'index.html',context=context)



def ajax_handler(request,id):
    cities = City.objects.filter(country__id=id).values_list('id','name')
    print(cities)
    cities = dict(cities)
    return JsonResponse({
        'cities' : cities,
    })



