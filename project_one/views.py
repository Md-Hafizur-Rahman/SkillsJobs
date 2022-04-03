from django.http import HttpRequest
from django.shortcuts import render,  HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> hello django </h1>") 
def about(reqest):
    return HttpResponse('i am a developer')