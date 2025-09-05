from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
# --- Imports جديدة بالطريقة اللي هو عايزها ---
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# --- VIEWS من التاسك اللي فات (متغيرتش) ---
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- VIEWS جديدة للتاسك الحالي بالطريقة المطلوبة ---

# 1. فيو لإنشاء الحساب (شبه اللي فات بس أبسط)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # بنعمل login لليوزر الجديد علطول
            return redirect('all_books') # بنوديه لصفحة الكتب
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# 2. فيو لتسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('all_books') # بنوديه لصفحة الكتب
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# 3. فيو لتسجيل الخروج
def logout_view(request):
    if request.method == 'POST': # مهم نخليه POST عشان الأمان
        logout(request)
        return redirect('login') # بنوديه لصفحة الدخول تاني
    # لو حد حاول يفتح الرابط بـ GET, رجعه للصفحة الرئيسية أو صفحة الدخول
    return redirect('login') 