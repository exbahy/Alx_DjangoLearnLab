
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
	books = Book.objects.all()
	return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_detail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'bookshelf/book_detail.html', {'book': book})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
	return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return render(request, 'bookshelf/book_form.html', {'book': book})
