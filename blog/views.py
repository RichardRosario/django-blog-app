from django.shortcuts import render
from django.http import HttpResponse

# function that handles the traffic to home page


def home(request):
    return HttpResponse('<h1>You are in the Blog Homepage</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
