from django.urls import path
from blog import views
from .views import ArticleViewSet

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
]