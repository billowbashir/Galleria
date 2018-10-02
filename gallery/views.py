from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

def welcome(request):
    images=Image.objects.all()
    print (images)
    return render(request,'welcome.html',{"images":images,})
