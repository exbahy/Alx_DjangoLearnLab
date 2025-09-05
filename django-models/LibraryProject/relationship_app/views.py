from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# 1. الـ View الأول: من نوع Function-based
# وظيفته يعرض كل الكتب الموجودة في الداتا بيز
def all_books(request):
    # هنجيب كل أوبجكتات الكتب
    books = Book.objects.all()
    # هنحضر الـ context اللي هنبعته للـ template
    # المفتاح 'books' هو اللي بنستخدمه جوه الـ template في الـ for loop
    context = {'books': books}
    # هنرجع الـ template بعد ما ندمجه بالـ context
    return render(request, 'relationship_app/list_books.html', context)


# 2. الـ View التاني: من نوع Class-based
# وظيفته يعرض تفاصيل مكتبة واحدة معينة بالكتب اللي فيها
class LibraryDetailView(DetailView):
    # بنحدد الموديل اللي الـ view ده هيتعامل معاه
    model = Library
    # بنحدد اسم الـ template اللي هيتعرض فيه تفاصيل المكتبة
    template_name = 'relationship_app/library_detail.html'
    # بنغير اسم المتغير الافتراضي 'object' لاسم أوضح هو 'library'
    # عشان نقدر نستخدمه في الـ template كده: {{ library.name }}
    context_object_name = 'library'