from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

def welcome(request):
    images=Image.objects.all()
    
    return render(request,'welcome.html',{"images":images,})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get('category')
        searched_images=Image.search_by_category(search_term)
        message=f'{search_term}'

        return render(request,'search.html',{"message":message,"images":searched_images,})

    else:
        message='You Havent searched for any category'

        return render(request, 'search.html',{"message":message},)
