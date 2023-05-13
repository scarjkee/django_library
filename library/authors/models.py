from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Имя автора: {self.first_name}'

class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ManyToManyField(Author)


class Artical(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)




# Create your models here.
