from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

def welcome(request):
    images=Image.objects.all()
    modals=Image.objects.order_by('id').all()
    return render(request,'welcome.html',{"images":images,"modals":modals,})
