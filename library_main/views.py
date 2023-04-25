from random import randint
from django.shortcuts import render
from library_main.models import Author, Category, Genre, Book, News, Quotes

def index(request):
    max_id = Book.objects.all().count()
    
    rand = randint(1, max_id)
    if rand - 3 > 0:
        rand -=3
    else:
        rand = 1
    book = Book.objects.filter(id = rand) | Book.objects.filter(id = rand+1) | Book.objects.filter(id = rand+2)[:3]
   
    now = Book.objects.all().order_by('-date_of_writing')[:3]
    print(book, now)
    context = {'now' : now, 'book' : book,}
    return render(request, 'index.html', context=context)
