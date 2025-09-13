# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\relationship_app\urls.py

from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:pk>/', views.change_book_view, name='change_book'),
    path('delete/<int:pk>/', views.delete_book_view, name='delete_book'),
]