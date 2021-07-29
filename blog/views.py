from django.shortcuts import render
from rest_framework import serializers, generics, permissions, viewsets, status
from blog.permissions import IsUserOrReadOnly
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import Article, Comment
from rest_framework.response import Response

# Create your views here.


class ArticleViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = ArticleSerializer(Article.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        article = Article.objects.get(id=pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)