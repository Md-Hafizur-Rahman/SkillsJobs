from django.shortcuts import render,HttpResponse
from .models import Category,Product

# Create your views here.
def category(req):
    cat=Category.objects.all()
    return HttpResponse(cat)

def product(req):
    pdc=Product.objects.all()
    return HttpResponse(pdc)