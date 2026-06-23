from django.shortcuts import render
from django.http import HttpResponse

def home(requests):
    return HttpResponse("Hello Django")

def example(requests):
    return HttpResponse("Hii I Am Venkat")

# Create your views here.
