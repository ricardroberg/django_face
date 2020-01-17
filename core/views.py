from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1>Home Page</h1>')


def login(request):
    return HttpResponse('<h1>Log In</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')
