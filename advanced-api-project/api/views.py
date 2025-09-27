from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """List all books - accessible to anyone"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a book by ID - accessible to anyone"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookCreateView(generics.CreateAPIView):
    """Create a new book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """Update a book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer   # ✅ مصححة
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """Delete a book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer   # ✅ مصححة
    permission_classes = [IsAuthenticated]
