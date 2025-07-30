from django.contrib import admin
from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Category는 이름만 보여주기

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publication_date', 'average_rating', 'review_count')
    list_filter = ('author', 'category', 'publication_date') 
    search_fields = ('title', 'description')  
