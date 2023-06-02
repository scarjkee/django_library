from django.db import models
from uuid import uuid4

from authors.models import Author


class Project(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    project_name = models.CharField(max_length=256)
    link = models.TextField()
    project_user = models.OneToOneField(Author, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Имя Проекта: {self.project_name}'


class Todo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    project_name_todo = models.CharField(max_length=256)
    notes = models.CharField(max_length=1026)
    create_user = models.OneToOneField(Author, on_delete=models.CASCADE)
    text_notes = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status_notes = models.BooleanField()

    # def __str__(self):
    #     id = models.UUIDField(default=uuid4, primary_key=True)
    #     project_name_todo = models.CharField(max_length=256)
    #     notes = models.CharField(max_length=1026)
    #     create_user = models.OneToOneField(Author, on_delete=models.CASCADE)
    #     text_notes = models.TextField()
    #     time_create = models.DateTimeField(auto_now_add=True)
    #     time_update = models.DateTimeField(auto_now=True)
    #     status_notes = models.BooleanField()

    def __str__(self):
        return f'Имя Проекта Todo: {self.project_name_todo}'


