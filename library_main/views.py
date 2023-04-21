from django.shortcuts import render
from library_main.models import Author, Category, Genre, Book, News, Quotes

def index(request):
    sale = Author.objects.all()

    context = {'promotion' : sale}
    return render(request, 'index.html', context=context)
