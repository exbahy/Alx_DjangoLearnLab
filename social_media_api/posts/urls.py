# posts/urls.py
from django.urls import path
from .views import (
    PostListCreateView, PostDetailView,
    LikePostView, UnlikePostView, FeedView
)

urlpatterns = [
    path('', PostListCreateView.as_view(), name='posts-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
    path('feed/', FeedView.as_view(), name='user-feed'),
]
