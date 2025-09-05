from django.urls import path
from . import views

urlpatterns = [
    # الرابط بتاع صفحة عرض كل الكتب
    # لما حد يفتح yoursite.com/app/books/ هيشغل دالة all_books
    path('books/', views.all_books, name='all_books'),

    # الرابط بتاع صفحة عرض مكتبة معينة
    # <int:pk> معناها إن جانجو هياخد رقم من الرابط (الـ Primary Key بتاع المكتبة)
    # ويبعته للـ view عشان يعرف يعرض أنهي مكتبة
    # يعني مثلاً yoursite.com/app/library/1/ هيعرض المكتبة رقم 1
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]