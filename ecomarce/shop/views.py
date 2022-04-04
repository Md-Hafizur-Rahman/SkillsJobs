from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.style import context
from .models import Category,Product

# Create your views here.
def categories(request):
    p = Category.objects.all()

    context = {
         'categories': p,   # 'function':variable
     }
    return render(request, 'index.html', context)

def select_category(request):
    category = Category.objects.filter(cat_name__startswith = "women")
    print(category)
    print(category.query)


    return render(request, 'index.html', {'category': category})

def product(req):
    product = Product.objects.filter(product_name__startswith="pant") | Product.objects.filter(slug__startswith='shirt')
    print(product.query)
    return render(req, 'index.html', {'products': product})


def product_union_with_category(request):
    product = Product.objects.all().values_list("product_name").union(Category.objects.all().values_list("cat_name"))
    print(product)
    print(product.query)
    return render(request, 'index.html', {'products': product})


def not_product(request):
    p = Product.objects.exclude(price__gt = 120.00)
    print(p)
    print(p.query)
    return render(request, 'index.html', {'p': p})