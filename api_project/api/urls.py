from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router and register viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old endpoint for listing books
    path('books/', BookList.as_view(), name='book-list'),

    # CRUD endpoints via router
    path('', include(router.urls)),
]
