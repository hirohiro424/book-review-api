from rest_framework import serializers
from .models import Review
from books.models import Book

class ReviewSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book',
        write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)  # 유저 정보 출력용

    class Meta:
        model = Review
        fields = ['id', 'book', 'book_id', 'user', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['book', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
