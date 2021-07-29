from django.urls import path
from blog import views
from .views import ArticleList,  ArticleDetail

urlpatterns = [
    path('article/', views.ArticleList.as_view()),
    path('article/<int:pk>/', views.ArticleDetail.as_view()),
]