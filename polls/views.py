from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("<h2>Hello dear Hurmat</h1>")

def blog(request):
    return HttpResponse("<h3>Welcome to the blog page</h3>")