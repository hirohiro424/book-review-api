# books/serializers.py
from rest_framework import serializers
from .models import Book, Category
from authors.models import Author

class AuthorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSimpleSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True, allow_null=True
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'description', 'cover_image', 'publication_date',
            'author', 'author_id', 'category', 'category_id',
            'average_rating', 'review_count', 'created_at', 'updated_at'
        ]
