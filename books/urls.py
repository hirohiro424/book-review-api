# books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CategoryViewSet
from authors.views import AuthorViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)  # authors 앱에서 구현한 ViewSet 필요

urlpatterns = [
    path('', include(router.urls)),
]
