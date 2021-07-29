from rest_framework import serializers 
from .models import Article, Comment, Category
from users.models import User
from rest_framework import serializers
from users.serializers import UserDetailsSerializer
from rest_framework.serializers import SerializerMethodField



class CategorySerializer(serializers.ModelSerilaizer):
    user = serializers.ReadOnlyField(source = 'user.username')
    article = serializers.PrimaryKeyRelatedField(many = True, read_only = True)


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



class CategorySerializer(serializers.ModelSerilaizer):
    user = serializers.ReadOnlyField(source = 'user.username')
    article = serializers.PrimaryKeyRelatedField(many = True, read_only = True)


