from django.urls import path
# هنستدعي الـ views الجديدة بتاعتنا
from .views import (
    list_books, 
    LibraryDetailView, 
    register_view, 
    login_view, 
    logout_view
)

urlpatterns = [
    # --- روابط التاسك اللي فات ---
    path('books/', list_books, name='all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # --- روابط التاسك الجديد (بسيطة ومباشرة) ---
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]