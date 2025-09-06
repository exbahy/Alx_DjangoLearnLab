# في ملف LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include # تأكد من وجود 'include' هنا

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('books/', include('bookshelf.urls')), # هذا السطر قد يكون موجوداً إذا كنت قد أنجزت المهمة 1
    # <<<<<<<<<<<<<<<<< هذا هو السطر الذي يربط مسارات العلاقة الجديدة <<<<<<<<<<<<<<<<<
    path('relationships/', include('relationship_app.urls')),
]