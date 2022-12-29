from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def translation(request):
    return HttpResponse("Hello, I am WORKING!")
