from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    settings = Setting.objects.latest('id')
    menus = Menu.objects.all()
    products = Product.objects.all()
    sale = Discount.objects.all()
    recall = Coment.objects.all()

    context = {
        'settings': settings,
        'menus': menus,
        'products': products,
        'sales': sale,
        'recalls': recall,
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



def users(request):
   return render(request, 'register.html')