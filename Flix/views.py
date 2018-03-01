from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    test = 'Working'
    return render(request, 'index.html', {"test": test})
