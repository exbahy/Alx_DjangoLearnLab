from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """List all books - accessible to anyone"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ أي حد يقرأ، التعديل يتطلب تسجيل دخول


class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a book by ID - accessible to anyone"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # ✅ نفس الفكرة


class BookCreateView(generics.CreateAPIView):
    """Create a new book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ لازم يكون مسجّل دخول


class BookUpdateView(generics.UpdateAPIView):
    """Update a book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ لازم يكون مسجّل دخول


class BookDeleteView(generics.DestroyAPIView):
    """Delete a book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ لازم يكون مسجّل دخول
