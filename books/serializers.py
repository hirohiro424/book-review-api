from rest_framework import serializers
from .models import Book, Review, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']

class BookSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'created_at', 'avg_rating', 'review_count']

    def get_avg_rating(self, obj):
        reviews = obj.reviews.all()
        return round(sum(r.rating for r in reviews) / len(reviews), 1) if reviews else 0

    def get_review_count(self, obj):
        return obj.reviews.count()