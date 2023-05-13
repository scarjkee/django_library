from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author, Biography, Book, Artical
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticalModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticalModelViewSet(ModelViewSet):
    queryset = Artical.objects.all()
    serializer_class = ArticalModelSerializer


# def index(request):
#     return render(request, '../frontend/index.html')
# # Create your views here.
