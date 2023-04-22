from django.shortcuts import render
from library_main.models import Author, Category, Genre, Book, News, Quotes

def index(request):

    #context = {'news' : news}
    return render(request, 'index.html',) #context=context
