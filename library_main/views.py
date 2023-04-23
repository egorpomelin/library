from django.shortcuts import render
from library_main.models import Author, Category, Genre, Book, News, Quotes

def index(request):
    now = Book.objects.all().order_by('-date_of_writing')[:3]
    context = {'now' : now,}
    return render(request, 'index.html', context=context)
