from django.db import models
from users.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 255)
    contain = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    update_at = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']



class Comment(models.Model):
    contain = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['created_at']



class Category(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()