"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors import views
from authors.views import ArticalModelViewSet, BiographyModelViewSet, BookModelViewSet, AuthorModelViewSet
from todo.views import TodoModelViewSet, ProjectModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('Articale', ArticalModelViewSet)
router.register('Biography', BiographyModelViewSet)
router.register('Book', BookModelViewSet)
router.register('Todo', TodoModelViewSet)
router.register('Project', ProjectModelViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('todo/', include(router.urls)),
    # path('api/author/<int:pk>/', views.AuthorRetrieveAPIView.as_view()),
    # path('api/author/', views.AuthorCreateAPIView.as_view()),
]
