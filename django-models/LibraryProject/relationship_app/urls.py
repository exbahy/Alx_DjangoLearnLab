# في ملف relationship_app/urls.py

from django.urls import path
from . import views # استيراد views من نفس المجلد

app_name = 'relationship_app' # مهم لتحديد اسم التطبيق في الـ URLs

urlpatterns = [
    path('', views.index, name='index'), # صفحة رئيسية بسيطة للتطبيق
    path('add/', views.add_book_view, name='add_book'),
    path('change/<int:pk>/', views.change_book_view, name='change_book'), # <int:pk> لالتقاط رقم الكتاب
    path('delete/<int:pk>/', views.delete_book_view, name='delete_book'), # <int:pk> لالتقاط رقم الكتاب
]