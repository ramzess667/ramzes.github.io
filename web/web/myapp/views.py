from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, 'home.html' , {'items': items})
   
def about(request):
    return render(request, 'about.html', {'title': 'О нас'})
 

# Create your views here.
