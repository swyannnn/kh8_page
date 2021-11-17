from django.shortcuts import render

def home(request):
    return render (request, 'blog/home.html')


def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})

def josephtan(request):
    return render (request, 'blog/josephtan.html', {'title': 'Joseph Tan'})

def mindyliew(request):
    return render (request, 'blog/mindyliew.html', {'title': 'Mindy Liew'})