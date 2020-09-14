from django.shortcuts import render
from .models import Posts
# from django.http import HttpResponse


# function that handles the traffic to home page


def home(request):
    # add a context
    context = {
        'posts': Posts.objects.all()
    }
    # return HttpResponse('<doctype />...')
    return render(request, 'blog/home.html', context)

# function that handles the about page traffic


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
