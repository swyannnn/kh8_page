from django.shortcuts import render
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    return render (request, 'blog/home.html')

def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})

def josephtan(request):
    context = {
        'posts': posts
    }
    return render (request, 'blog/josephtan.html', context, {'title': 'Joseph Tan'})

def mindyliew(request):
    return render (request, 'blog/mindyliew.html', {'title': 'Mindy Liew'})