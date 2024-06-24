# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello World! I'm Home")



def about(request):
    return render(request, 'about.html')
    #return HttpResponse("My about Page.")