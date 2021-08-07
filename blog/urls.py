from django.urls import path
from blog import views
from .views import ArticleViewSet, CommentViewSet, CategoryViewSet, LikeListCreate, TagViewSet

urlpatterns = [
   path("article" , ArticleViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('article/<str:pk>', ArticleViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("comment" , CommentViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('comment/<str:pk>', CommentViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("category" , CategoryViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('category/<str:pk>', CategoryViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path('article/<int:id>/like/', LikeListCreate.as_view(), name = 'article_like'),
    path("tag" , TagViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('tag/<str:pk>', TagViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]