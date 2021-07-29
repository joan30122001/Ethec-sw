from rest_framework import serializers 
from .models import Article, Comment
from users.models import User
from rest_framework import serializers
from users.serializers import UserDetailsSerializer
from rest_framework.serializers import SerializerMethodField


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'contain', 'created_at', 'update_at', 'user']



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    
    class Meta:
        model = Comment
        fields = ['id', 'contain', 'article', 'user', 'created_at']
