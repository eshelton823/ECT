from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Here's the homepage!")

def about(request):
    return HttpResponse("Here's the about page!")

def signup(request):
    return HttpResponse("Here's the signup page!")

def login(request):
    return HttpResponse("Here's the login page!")

def contactus(request):
    return HttpResponse("Here's the contact us page!")

