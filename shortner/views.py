from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Url
import uuid

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def Createurl(request):
    jsonData = JSONParser().parse(request)
    link = jsonData['link']
    print(jsonData)
    try:
        uid = Url.objects.get(url = link)
        return HttpResponse("already shortend : " + str(uid))
    except Url.DoesNotExist:
        uid = str(uuid.uuid4())[:5]
        url = Url()
        url.url = str(link)
        url.uuid = uid
        url.save() 
        return HttpResponse("url shortend " + str(uid))

def go(request, pk):
    try:
        obj = Url.objects.get(uuid = pk)
        return HttpResponse("long url is " + obj.url)
    except Url.DoesNotExist:
        return HttpResponse("No long url found!")
    
    


