from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says hey there partner. Wanna go to the about page?'
                        +' <a href="/rango/about/">click here</a>')

def about(request):
    return HttpResponse("Rango says here is the about page.")