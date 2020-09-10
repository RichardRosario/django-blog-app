from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Richard',
        "title": 'Blog Post #1',
        'content': 'first post contents',
        'date_posted': 'Sept 10, 2020'
    },
    {
        'author': 'Anna',
        "title": 'Blog Post #2',
        'content': 'Second post contents',
        'date_posted': 'Sept 8, 2020'
    },
    {
        'author': 'RichardR',
        "title": 'Blog Post #3',
        'content': 'third post contents',
        'date_posted': 'Sept 2, 2020'
    }
]

# function that handles the traffic to home page


def home(request):
    # add a context
    context = {
        'posts': posts
    }
    # return HttpResponse('<doctype />...')
    return render(request, 'blog/home.html', context)

# function that handles the about page traffic


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
