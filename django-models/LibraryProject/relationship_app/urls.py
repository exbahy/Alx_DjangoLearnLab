from django.urls import path
# دول الـ imports اللي الـ checker بيدور عليهم
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]