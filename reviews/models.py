from django.db import models
from django.conf import settings
from books.models import Book
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg, Count

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user} on {self.book}'
    
@receiver(post_save, sender=Review)
@receiver(post_delete, sender=Review)
def update_book_rating(sender, instance, **kwargs):
    book = instance.book
    agg = book.reviews.aggregate(
        avg_rating=Avg('rating'),
        count=Count('id')
    )
    book.average_rating = agg['avg_rating'] or 0
    book.review_count = agg['count'] or 0
    book.save()
