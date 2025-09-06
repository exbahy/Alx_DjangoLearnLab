# في ملف relationship_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required # مهم لاستيراد هذا الـ decorator

# دالة بسيطة لصفحة الترحيب الرئيسية للتطبيق
def index(request):
    return HttpResponse("Welcome to Relationship App!")

# View لإضافة كتاب (تتطلب صلاحية can_add_book)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    # في مشروع حقيقي، هنا سيكون لديك فورم لإضافة الكتاب ومعالجة البيانات
    return HttpResponse("You have permission to ADD a book!")

# View لتعديل كتاب (تتطلب صلاحية can_change_book)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book_view(request, pk): # pk هو Primary Key للكتاب المراد تعديله
    # في مشروع حقيقي، هنا سيكون لديك فورم لتعديل الكتاب ومعالجة البيانات
    return HttpResponse(f"You have permission to CHANGE book ID: {pk}!")

# View لحذف كتاب (تتطلب صلاحية can_delete_book)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, pk): # pk هو Primary Key للكتاب المراد حذفه
    # في مشروع حقيقي، هنا سيكون لديك منطق لحذف الكتاب بعد تأكيد
    return HttpResponse(f"You have permission to DELETE book ID: {pk}!")