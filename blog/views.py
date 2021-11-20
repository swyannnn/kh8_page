from django.shortcuts import render
joseph_posts = [
    {
        'intro': 'Maths Personal Statement (Joseph Tan)',
        'description': 'Joseph Tan is not in a university yet. Please do note that he hates Python and somehow he is using django.',
        'content': ['My childhood is all about numbers and calculations. Born into a traditional Asian family, where our parents expect us to get straight A’s in all of our subjects. I usually spend all my time studying mathematics during the holidays. When I was 9, my mother gave me a book about Carl Friedrich Gauss and his formula to the sum of the natural numbers. Out of curiosity, I opened the book and had a peek. To my surprise, my holiday studies equipped me with the knowledge to understand how his formula works. I was stunned by how beautiful mathematics can be.',
        'In secondary school, I joined an olympiad team. At that time, I made a few friends who are also passionate about mathematics. We would often stay after school discussing olympiad questions or learning new concepts in mathematics. Subsequently, I got a high distinction in a local olympiad competition. I gained huge confidence from this achievement, for this reason, I am motivated to continue my studies and research in mathematics.',
        '“Fermat’s Enigma” by Simon Singh explains the history of mathematics through the topic of Fermat’s Last Theorem, a conjecture stating that xn+yn=zn do not exist for n greater or equal to 3. This book solidified my understanding in mathematics as it explains how different areas of mathematics are discovered and created. I was also shocked when I read about how Pythagoras threw his disciple into the water because he introduced the existence of irrational numbers, which Pythagoras did not wish to believe existed.',
        'I love joining mathematics competitions, as it stimulates my brain into thinking of different methods to solve a question. I have received a Gold Award in the UKMT Competition, whilst ranking the first amongst my year. I also won a bronze medal in the IMO selection test in Malaysia. The preparation for these competitions is hard to plan, as the questions vary from algebraic expressions to using different methods of proof to show that a given statement is true. My strategy is to research different areas in mathematics to further deepen my understanding for each of the topics.',
        'As a senior in school, I utilize the knowledge I’ve gained from joining olympiad competitions to prepare my juniors for different competitions. To this end, I create targeted puzzles for them to solve. I developed my abilities to communicate and to present as I teach the juniors and discover the best ways to explain difficult concepts. I am passionate about developing games in my free time, applying mathematics that I learn in school to help develop them, or finding different mathematical equations that can be used to achieve different effects. For example, adding a vibrating path to a travelling particle uses different math equations - programming a sine wave in terms of time, scaling the vibration with the magnitude of the speed, and also calculating the velocity.',
        'I am really interested, and motivated to study mathematics in the most prestigious universities in the UK as an undergraduate and to achieve a Doctoral degree. I aspire to become a university professor educating mathematics content, and help those students that are interested in mathematics.']
    
    }
]

mindy_posts = [
    {
        'intro': 'Maths Personal Statement (Mindy)',
        'description': 'Joseph Tan is not in a university yet. Please do note that he hates Python and somehow he is using django.',
        'content1': 'My childhood is all about numbers and calculations. Born into a traditional Asian family, where our parents expect us to get straight A’s in all of our subjects. I usually spend all my time studying mathematics during the holidays. When I was 9, my mother gave me a book about Carl Friedrich Gauss and his formula to the sum of the natural numbers. Out of curiosity, I opened the book and had a peek. To my surprise, my holiday studies equipped me with the knowledge to understand how his formula works. I was stunned by how beautiful mathematics can be.',
        'content2': 'In secondary school, I joined an olympiad team. At that time, I made a few friends who are also passionate about mathematics. We would often stay after school discussing olympiad questions or learning new concepts in mathematics. Subsequently, I got a high distinction in a local olympiad competition. I gained huge confidence from this achievement, for this reason, I am motivated to continue my studies and research in mathematics.'
    }
]
def home(request):
    return render (request, 'blog/home.html')

def about(request):
    return render (request, 'blog/about.html', {'title': 'About'})

def josephtan(request):
    context = {
        'posts': joseph_posts
    }
    return render (request, 'blog/josephtan.html', context)

def mindyliew(request):
    return render (request, 'blog/mindyliew.html', {'title': 'Mindy Liew'})

def test(request):
    context = {
        'posts': joseph_posts
    }
    return render (request, 'blog/test.html', context)  

