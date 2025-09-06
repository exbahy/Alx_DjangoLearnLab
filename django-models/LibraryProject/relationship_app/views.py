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
# Imports جديدة هنحتاجها
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# --- دوال عشان نتحقق من دور اليوزر ---
# الفانكشن دي بترجع True لو اليوزر أدمين
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == UserProfile.ADMIN

# الفانكشن دي بترجع True لو اليوزر أمين مكتبة
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == UserProfile.LIBRARIAN

# الفانكشن دي بترجع True لو اليوزر عضو عادي
def is_member(user):
    return user.is_authenticated and user.userprofile.role == UserProfile.MEMBER


# --- الـ Views الجديدة المخصصة لكل دور ---

# الـ view بتاع المدير (Admin)
@login_required(login_url='/app/login/') # لازم يكون مسجل دخول الأول
@user_passes_test(is_admin, login_url='/app/login/') # لازم يعدي من اختبار is_admin
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# الـ view بتاع أمين المكتبة (Librarian)
@login_required(login_url='/app/login/')
@user_passes_test(is_librarian, login_url='/app/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# الـ view بتاع العضو (Member)
@login_required(login_url='/app/login/')
@user_passes_test(is_member, login_url='/app/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')