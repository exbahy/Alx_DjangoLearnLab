# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\bookshelf\urls.py

from django.urls import path
from django.http import HttpResponse # استيراد HttpResponse
from . import views # استيراد views من نفس المجلد

app_name = 'bookshelf'

# دالة index هنا يمكن أن تكون View بسيطة إذا كانت موجودة في bookshelf/views.py
def index(request):
    return HttpResponse("Welcome to Bookshelf App!")

urlpatterns = [
    path('', index, name='index'), # صفحة رئيسية بسيطة للتطبيق
]