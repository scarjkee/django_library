from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from authors.serializers import AuthorModelSerializer
from todo.models import Project, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    project_user = AuthorModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    create_user = AuthorModelSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
