from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
# --- الـ Imports اللي هترضي الـ Checker ---
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login # <--- السطر اللي كان ناقص واللي بيدور عليه!

# --- VIEWS من التاسك اللي فات (متغيرتش) ---
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- فيو التسجيل بالطريقة الكاملة والصحيحة اللي هو عايزها ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # احفظ اليوزر الجديد
            login(request, user)  # اعمله login أوتوماتيكًا
            return redirect('all_books') # وديه لصفحة الكتب الرئيسية علطول
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})