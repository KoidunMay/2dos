from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request,'about.html')


def menu(request):
    rows = Menu.objects.all()
    context = {
        'rows': rows,
    }
    return render(request, 'menu.html',context)


def book(request):
    return render(request, 'book.html')