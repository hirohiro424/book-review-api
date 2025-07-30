from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    biography = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
