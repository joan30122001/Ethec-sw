from django.shortcuts import render
from rest_framework import serializers, generics, permissions, viewsets, status
from blog.permissions import IsUserOrReadOnly
from .serializers import ArticleSerializer, CommentSerializer, CategorySerializer, LikeSerializer, TagSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import Article, Comment, Category, Tag, Like
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





class CommentViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = CommentSerializer(Comment.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





class CategoryViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        category = Category.objects.get(id=pk)
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class LikeListCreate(APIView):
    def get(self, request, id):
        post = Article.objects.filter(id = id)
        like_count = post.article.count()
        serializer = LikeSerializer(like_count, many = True)
        return Response(serializer.data)


    def post(self, request, id):
        user = request.user
        article = Article.filter(id = id)
        serializer = LikeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user, article)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)




class TagViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = TagSerializer(Tag.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        tag = Tag.objects.get(id=pk)
        serializer = TagSerializer(tag)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        tag = Tag.objects.get(id=pk)
        serializer = TagSerializer(instance=tag, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        tag = Tag.objects.get(id=pk)
        tag.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)