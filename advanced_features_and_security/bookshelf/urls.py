# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\bookshelf\urls.py

from django.urls import path
from django.http import HttpResponse

app_name = 'bookshelf'

def index(request):
    return HttpResponse("Welcome to Bookshelf App!")

urlpatterns = [
    path('', index, name='index'),
]