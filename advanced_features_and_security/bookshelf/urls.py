# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\bookshelf\urls.py

from django.urls import path
from django.http import HttpResponse # استيراد HttpResponse
# from . import views # لا نحتاجها هنا إذا كانت View مباشرة في urls.py

app_name = 'bookshelf'

# دالة index هنا يمكن أن تكون View بسيطة
def index(request):
    return HttpResponse("Welcome to Bookshelf App!")

urlpatterns = [
    path('', index, name='index'),
]