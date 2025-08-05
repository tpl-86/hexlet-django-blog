from django.db import models

# Create your models here.
class ArticleComment(models.Model):
    content = models.CharField("content", max_length=100)
    
class Article(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    