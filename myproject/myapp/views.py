from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
    'name': 'Saifur Rahman Udoy',
    'age': 18,
    'nationality': 'Bangladesh'
    }
    return render(request, 'index.html', context)


def counter(request):
    # text = request.GET['text']
    text = request.POST['text']
    amouts_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amouts_of_words})