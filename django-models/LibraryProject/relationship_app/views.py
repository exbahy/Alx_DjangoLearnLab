from django.shortcuts import render
from .models import Book
from .models import Library
# --- ده التعديل الوحيد والمطلوب ---
from django.views.generic.detail import DetailView # <--- المسار الطويل اللي هو عايزه
# -----------------------------------


# 1. الـ View الأول: من نوع Function-based
# وظيفته يعرض كل الكتب الموجودة في الداتا بيز
def all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# 2. الـ View التاني: من نوع Class-based
# وظيفته يعرض تفاصيل مكتبة واحدة معينة بالكتب اللي فيها
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'