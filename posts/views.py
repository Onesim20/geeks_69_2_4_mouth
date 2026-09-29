from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
# Create your views here.

def hello(r):
    return HttpResponse("<h1>Hello World!</h1>")

def name(r):
    name = "Onesim"
    return HttpResponse(f"<h1>Hello {name}!</h1>")

def time(r):
    dt = datetime.now()
    return HttpResponse(f"NOW:{dt.strftime('%Y-%m-%d %H:%M:%S')}")

def age(r):
    age = 16
    return HttpResponse(f"<h1>Onesim is {age} years old!</h1>")