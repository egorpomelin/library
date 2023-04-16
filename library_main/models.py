from django.db import models

class Author(models.Model):
    image = models.ImageField(verbose_name='�����������')
    name = models.CharField(verbose_name='���', max_length=50)

class Category(models.Model):
    name = models.CharField(verbose_name='���������')

class Genre(models.Model):
    name = models.CharField(verbose_name='�������� �����')
    category = models.ForeignKey(Category, verbose_name='��������� �����', on_delete=models.CASCADE)

class Book(models.Model):

    name = models.CharField(verbose_name='�������� �����', max_length=50)
    author = models.ForeignKey(Author, verbose_name='����� �����', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name='���� �����', on_delete=models.CASCADE)