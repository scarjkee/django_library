from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import Author, Biography, Book, Artical
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographyModelSerializer, ArticalModelSerializer


class AuthorModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class AuthorRetrieveAPIView(RetrieveAPIView):
    # renderer_classes = [JSONRenderer]
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
