from django.shortcuts import render
from .models import *
from random import *
# Create your views here.

def index(request):
    settings = Setting.objects.latest('id')
    menus = Menu.objects.all()
    products = Product.objects.all()
    sale = Discount.objects.all()
    recall = Coment.objects.all()
    
    sliders = Product.objects.filter(menuObject=choice(menus)).order_by('?')
    context = {
        'settings': settings,
        'menus': menus,
        'products': products,
        'sales': sale,
        'sliders': sliders,
        'recalls': recall,
        'numbers': range(1,len(sliders)),
    }
    return render(request, 'index.html', context)

def about(request):
    settings = Setting.objects.latest('id')
    aboutfoot = Aboutfoot.objects.all()
    context = {
        'about':aboutfoot,
        'settings': settings,
    }
    return render(request,'about.html',context)


def menu(request):
    rows = Menu.objects.all()
    settings = Setting.objects.latest('id')
    products = Product.objects.all()
    context = {
        'menus': rows,
        'products': products,
        'settings': settings,

    }
    return render(request, 'menu.html',context)


def book(request):
    settings = Setting.objects.latest('id')
    context = {
        'settings': settings,

    }
    return render(request, 'book.html',context)



def users(request):
   return render(request, 'register.html')



def major(request):
   return render(request, 'major.html')