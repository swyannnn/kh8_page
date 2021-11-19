from django.shortcuts import render
joseph_posts = [
    {
        'intro': 'Maths Personal Statement (Joseph Tan)',
        'description': 'Joseph Tan is not in a university yet. Please do note that he hates Python and somehow he is using django.',
        'content': ['My childhood is all about numbers and calculations. Born into a traditional Asian family, where our parents expect us to get straight A’s in all of our subjects. I usually spend all my time studying mathematics during the holidays. When I was 9, my mother gave me a book about Carl Friedrich Gauss and his formula to the sum of the natural numbers. Out of curiosity, I opened the book and had a peek. To my surprise, my holiday studies equipped me with the knowledge to understand how his formula works. I was stunned by how beautiful mathematics can be.',
        'In secondary school, I joined an olympiad team. At that time, I made a few friends who are also passionate about mathematics. We would often stay after school discussing olympiad questions or learning new concepts in mathematics. Subsequently, I got a high distinction in a local olympiad competition. I gained huge confidence from this achievement, for this reason, I am motivated to continue my studies and research in mathematics.']
    },

    {
        'intro': 'Maths Personal Statement (Mindy)',
        'description': 'Joseph Tan is not in a university yet. Please do note that he hates Python and somehow he is using django.',
        'content1': 'My childhood is all about numbers and calculations. Born into a traditional Asian family, where our parents expect us to get straight A’s in all of our subjects. I usually spend all my time studying mathematics during the holidays. When I was 9, my mother gave me a book about Carl Friedrich Gauss and his formula to the sum of the natural numbers. Out of curiosity, I opened the book and had a peek. To my surprise, my holiday studies equipped me with the knowledge to understand how his formula works. I was stunned by how beautiful mathematics can be.',
        'content2': 'In secondary school, I joined an olympiad team. At that time, I made a few friends who are also passionate about mathematics. We would often stay after school discussing olympiad questions or learning new concepts in mathematics. Subsequently, I got a high distinction in a local olympiad competition. I gained huge confidence from this achievement, for this reason, I am motivated to continue my studies and research in mathematics.'
    }
]
#this is a comment 
#this is another comment!
def home(request):
    return render (request, 'blog/home.html')

def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})

def josephtan(request):
    return render (request, 'blog/josephtan.html', {'title': 'Joseph Tan'})

def mindyliew(request):
    return render (request, 'blog/mindyliew.html', {'title': 'Mindy Liew'})

def test(request):
    context = {
        'posts': joseph_posts
    }
    return render (request, 'blog/test.html', context)  

