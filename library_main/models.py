from django.db import models

class Author(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    name = models.CharField(verbose_name='ФИО', max_length=50)

class Category(models.Model):
    name = models.CharField(verbose_name='Категория')

class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра')
    category = models.ForeignKey(Category, verbose_name='Категория жанра', on_delete=models.CASCADE)

class Book(models.Model):

    name = models.CharField(verbose_name='Название книги', max_length=50)
    author = models.ForeignKey(Author, verbose_name='Автор книги', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name='Жанр книги', on_delete=models.CASCADE)