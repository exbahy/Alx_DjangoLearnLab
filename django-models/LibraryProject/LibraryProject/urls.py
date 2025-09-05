"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# --- ده التعديل المهم ---
from .views import list_books, LibraryDetailView # <--- استدعينا كل واحد باسمه

urlpatterns = [
    # الرابط بتاع صفحة عرض كل الكتب
    # استخدمنا list_books مباشرة من غير views.
    path('books/', list_books, name='all_books'), # <--- غيرنا اسم الـ view هنا

    # الرابط بتاع صفحة عرض مكتبة معينة
    # استخدمنا LibraryDetailView مباشرة من غير views.
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]