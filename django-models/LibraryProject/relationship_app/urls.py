# في ملف relationship_app/urls.py

from django.urls import path
from . import views # استيراد views من نفس المجلد

app_name = 'relationship_app' # مهم لتحديد اسم التطبيق في الـ URLs


urlpatterns = [
    path('', views.index, name='index'),
    # <<<<<<<<<<<<<<<<< التعديل هنا لـ 'add_book/' <<<<<<<<<<<<<<<<<
    path('add_book/', views.add_book_view, name='add_book'),
    # <<<<<<<<<<<<<<<<< التعديل هنا لـ 'edit_book/<int:pk>/' <<<<<<<<<<<<<<<<<
    path('edit_book/<int:pk>/', views.change_book_view, name='change_book'),
    path('delete/<int:pk>/', views.delete_book_view, name='delete_book'),
]