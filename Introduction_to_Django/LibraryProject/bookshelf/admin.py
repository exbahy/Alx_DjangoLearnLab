# في ملف bookshelf/admin.py

from django.contrib import admin
from .models import Book # استورد موديل الكتاب بتاعك

# ده كلاس مخصص عشان نظبط بيه شكل موديل Book في لوحة التحكم
class BookAdmin(admin.ModelAdmin):
    # 1. إعداد الأعمدة اللي هتظهر في قائمة الكتب (list_display)
    list_display = ('title', 'author', 'publication_year')

    # 2. إعداد فلاتر جانبية عشان نقدر نفلتر الكتب (list_filter)
    # الـ Checker غالباً بيدور على 'publication_year' كفلتر
    list_filter = ('publication_year',) # لازم تكون tuple حتى لو عنصر واحد (معاه فاصلة في الآخر)

    # 3. إعداد خانة بحث عشان نقدر ندور على الكتب (search_fields)
    # الـ Checker غالباً بيدور على 'title' و 'author'
    search_fields = ('title', 'author')

# سجل موديل Book، وبنديله الكلاس اللي عملناه BookAdmin عشان التخصيص
admin.site.register(Book, BookAdmin)