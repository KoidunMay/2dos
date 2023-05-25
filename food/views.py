from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    menus = Menu.objects.all()
    products = Product.objects.all()
    sale = Discount.objects.all()

    context = {
        'menus': menus,
        'products': products,
        'sales': sale
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request,'about.html')


def menu(request):
    rows = Menu.objects.all()
    products = Product.objects.all()
    context = {
        'menus': rows,
        'products': products,

    }
    return render(request, 'menu.html',context)


def book(request):
    return render(request, 'book.html')