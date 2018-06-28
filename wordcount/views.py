from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def portfolio(request):
    return render(request, 'portfolio.html')
