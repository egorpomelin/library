from django.db import models
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

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name

class User(models.Model):
    image = models.ImageField(verbose_name="Аватарка")
    name = models.CharField(verbose_name='Имя', max_length=50)
    date = models.DateField(verbose_name='Дата регистрации', auto_now_add=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name