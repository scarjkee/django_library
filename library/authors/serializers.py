from django.db import models
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Author, Artical, Biography, Book
from rest_framework import serializers


class AuthorModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BiographyModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Biography
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class ArticalModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Artical
        fields = '__all__'

# class Autor:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
# class AutorSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     year = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Autor(**validated_data)
#
#     def validate_year(self, year):
#         if year < 0:
#             raise serializers.ValidationError('birthday no 0')
#         return year
#
#     def validate(self, attrs):
#         if attrs['name'] == 'Aydar' and attrs['year'] != 1987:
#             raise serializers.DjangoValidationError('ERROR 404')
#         return attrs
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.year = validated_data.get('year', instance.year)
#         return instance
#
#
# data ={'name': 'Aydar', 'year': 1987}
# serializer = AutorSerializer(data=data)
# serializer.is_valid()
# autor = serializer.save()
# print(autor .__dict__)
# print(autor.name, autor.year)
#
# new = {'name': 'babayka'}
# serializer = AutorSerializer(autor, data=new, partial=True)
# serializer.is_valid()
# autor = serializer.save()
# print(autor.__dict__)
