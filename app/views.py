from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rejection(request):
    return HttpResponse('<h1>hii guys</h1>')
def hello(request):
    return HttpResponse('<marquee>hello avinash</marquee>')
    