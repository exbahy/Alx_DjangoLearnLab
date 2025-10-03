from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Blog Post CRUD
    path('posts/', views.PostListView.as_view(), name='list'),
    path('posts/new/', views.PostCreateView.as_view(), name='create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
