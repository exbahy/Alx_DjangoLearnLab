# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\relationship_app\views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

def index(request):
    return HttpResponse("Welcome to Relationship App!")

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    return HttpResponse("You have permission to ADD a book!")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book_view(request, pk):
    return HttpResponse(f"You have permission to CHANGE book ID: {pk}!")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, pk):
    return HttpResponse(f"You have permission to DELETE book ID: {pk}!")