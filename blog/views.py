from django.shortcuts import render

def home(request):
    return render (request, 'blog/home.html')


def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})

def major(request):
    return render (request, 'blog/major.html', {'title': 'Major'})