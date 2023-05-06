from random import randint
from django.shortcuts import render, get_object_or_404
from library_main.models import Author, Category, Genre, Book, News, Quotes, Contacts

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

def Genre_views(request, id):
    genre = get_object_or_404(Genre, pk=id)
    book = Book.objects.filter(genre__exact=genre).order_by('-date_of_writing')
    context = {'genre1' : genre, 'book' : book}
    return render(request, 'genre_book.html', context=context)

def Single_book_views(request, id):
    book = get_object_or_404(Book, pk=id)
    quotes = Quotes.objects.filter(books__exact=book)
    context = {'book' : book, 'quotes' : quotes}
    return render(request, 'single_book.html', context=context)

def Contact(request):
    contact = get_object_or_404(Contacts, pk=1)
    context = {'contact' : contact}
    return render(request, 'contacts.html', context=context)