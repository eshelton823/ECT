from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'pcsite/index.html')


def about(request):
    return render(request, 'pcsite/about.html')

def signup(request):
    return render(request, 'pcsite/signup.html')

def login(request):
    return render(request, 'pcsite/login.html')

def contactus(request):
    return render(request, 'pcsite/contactus.html')

