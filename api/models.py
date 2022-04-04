from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class Article(TimestampedModel):
    slug = models.CharField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles'
    )


    def __str__(self):
        return self.title
    

class Comment(TimestampedModel):
    body = models.TextField()
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )


class Tag(TimestampedModel):
    slug = models.SlugField(db_index=True, unique=True)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag