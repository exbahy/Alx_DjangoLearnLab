

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

# Create your views here.

def home(request):
	return HttpResponse("<h1>Welcome to the Library Project</h1><p>Go to <a href='/books/'>/books/</a> to see the books.</p>")

# This view is protected by the 'can_view_book' permission
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
	books = Book.objects.all()
	# In a real app, you would render a template here
	return HttpResponse("You have permission to view the list of books.")

# This view is protected by the 'can_create_book' permission
@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
	# In a real app, you would have form logic here
	return HttpResponse("You have permission to create a new book.")

# This view is protected by the 'can_edit_book' permission
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
	# In a real app, you would have form logic here for a specific book
	return HttpResponse(f"You have permission to edit book with id {pk}.")
