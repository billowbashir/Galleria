from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('welcome to my gallery app')
