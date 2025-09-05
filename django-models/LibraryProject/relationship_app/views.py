from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
# هنحتاج الفورم بتاع إنشاء الحساب بس
from django.contrib.auth.forms import UserCreationForm

# --- VIEWS من التاسك اللي فات (متغيرتش) ---
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- فيو التسجيل فقط (ده اللي هو عايزه) ---
def register(request): # غيرنا اسمه لـ register بس عشان يطابق views.register
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # بعد التسجيل، يروح لصفحة الدخول
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})