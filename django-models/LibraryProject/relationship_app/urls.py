from django.urls import path
# هنستدعي الـ views الجاهزة من جانجو
from django.contrib.auth import views as auth_views
# هنستدعي الـ views بتاعتنا (عشان نجيب منها register بس)
from . import views

urlpatterns = [
    # --- روابط التاسك اللي فات ---
    path('books/', views.list_books, name='all_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # --- روابط التاسك الجديد بالطريقة اللي بترضيه ---
    path('register/', views.register, name='register'), # <-- بيستخدم الفانكشن بتاعتنا
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'), # <-- بيستخدم الجاهز
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), # <-- بيستخدم الجاهز
]