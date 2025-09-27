from django.contrib import admin
from django.urls import path, include
from api.views import AuthorListCreateView, AuthorDetailView, BookListCreateView, BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authors
    path('api/authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Books
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
