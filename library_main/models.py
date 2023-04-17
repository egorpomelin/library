from django.db import models

class Author(models.Model):
    image = models.ImageField(verbose_name='�����������')
    name = models.CharField(verbose_name='���', max_length=50)

    class Meta:
        verbose_name = "�����"
        verbose_name_plural = "������"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name='���������')

    class Meta:
        verbose_name = "���������"
        verbose_name_plural = "���������"

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(verbose_name='�������� �����')
    category = models.ForeignKey(Category, verbose_name='��������� �����', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "����"
        verbose_name_plural = "�����"

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(verbose_name='�������� �����', max_length=50)
    author = models.ForeignKey(Author, verbose_name='����� �����', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name='���� �����', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='�������� �����')
    image = models.ImageField(verbose_name='������� �����')

    class Meta:
        verbose_name = "�����"
        verbose_name_plural = "�����"

    def __str__(self):
        return self.name