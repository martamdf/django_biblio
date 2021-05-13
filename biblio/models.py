from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField('Nombre Categoría', max_length=200)
    def __str__(self):
        return self.category_name
    def get_absolute_url(self):
        return reverse('home')

class Book(models.Model):
    title = models.CharField('Título', max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='uploads/')
    categoria = models.ManyToManyField(Category)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

