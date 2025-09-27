from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """List all books with filtering, searching, and ordering"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ إضافة Filtering, Searching, Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # 🟢 1. Filtering: السماح بتصفية الكتب
    filterset_fields = ['title', 'author', 'publication_year']

    # 🟢 2. Searching: البحث في العنوان و المؤلف
    search_fields = ['title', 'author']

    # 🟢 3. Ordering: ترتيب النتائج
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering by title


class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a book by ID - accessible to anyone"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """Create a new book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """Update a book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """Delete a book - only for authenticated users"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
