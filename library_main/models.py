from django.db import models
from django.urls import reverse
#from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    name = models.CharField(verbose_name='ФИО', max_length=50)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра', max_length=50)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('genre', args=[self.id])

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(verbose_name='Название книги', max_length=50)
    author = models.ForeignKey(Author, verbose_name='Автор книги', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name='Жанр книги', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(verbose_name='Обложка книги')
    linkLitress = models.TextField(verbose_name='Ссылка на покупку', null=True, blank=True)
    linkDowload = models.TextField(verbose_name='Ссылка на загрузку фрагмента', null=True, blank=True)
    linkOnline = models.TextField(verbose_name='Ссылка на онлайн фрагмент', null=True, blank=True)
    ageRestriction = models.IntegerField(verbose_name='Возрастное ограничение')
    date_of_writing = models.DateField(verbose_name='Дата написания')
    value = models.IntegerField(verbose_name='Количество страниц')
    isbn = models.CharField(verbose_name='Международный номер книги', max_length=200)

    def get_absolute_url(self):
        return reverse('single_book', args=[self.id])

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name

#class User(models.Model):
    #image = models.ImageField(verbose_name="Аватарка")
    #name = models.CharField(verbose_name='Имя', max_length=50)
    #date = models.DateField(verbose_name='Дата регистрации', auto_now_add=True)
    #date_of_birth = models.DateField(verbose_name='Дата рождения')

    #class Meta:
        #verbose_name = "Пользователь"
        #verbose_name_plural = "Пользователи"

    #def __str__(self):
        #return self.name

class News(models.Model):
    heading = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение',  null=True, blank=True)
    source = models.CharField(verbose_name='Источник Новости', max_length=100)
    pudlicachia_date = models.DateField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "новости"

    def __str__(self):
        return self.heading

class Quotes(models.Model):
    books = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.CASCADE)
    quotes = models.TextField(verbose_name='Цитата')

    class Meta:
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"

    def __str__(self):
        return self.books.name


class Contacts(models.Model):

    name = models.CharField(verbose_name='Имя', max_length=50)
    email = models.EmailField()
    namber = models.IntegerField(verbose_name='Номер телефона')
    adress = models.TextField(verbose_name='Адрес')

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name