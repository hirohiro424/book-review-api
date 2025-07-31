
from django.urls import path
from .views_template import (
    BookTemplateListView, BookTemplateCreateView,
    BookTemplateUpdateView, BookTemplateDetailView,
    ReviewTemplateListView, ReviewTemplateCreateView,
    ReviewTemplateUpdateView, ReviewTemplateDetailView,
    AuthorTemplateListView, AuthorTemplateCreateView,  
    AuthorTemplateUpdateView
)

urlpatterns = [
    # Book templates
    path('books/', BookTemplateListView.as_view(), name='book_list'),
    path('books/create/', BookTemplateCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookTemplateUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/', BookTemplateDetailView.as_view(), name='book_detail'),

    # Review templates
    path('reviews/', ReviewTemplateListView.as_view(), name='review_list'),
    path('reviews/create/', ReviewTemplateCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/update/', ReviewTemplateUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/', ReviewTemplateDetailView.as_view(), name='review_detail'),

     # Author templates ✅ 추가
    path('authors/', AuthorTemplateListView.as_view(), name='author_list'),
    path('authors/create/', AuthorTemplateCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorTemplateUpdateView.as_view(), name='author_update'),
]