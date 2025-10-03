from django.urls import path
from . import views

urlpatterns = [
    # Blog Post CRUD (new naming expected by checker)
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Authentication routes
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    # Comment routes (nested under post)
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('post/comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),
    path('post/comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
