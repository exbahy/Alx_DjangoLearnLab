git mv Introduction_to_Django/LibraryProject .
git commit -m "refactor: Move LibraryProject to root for checker compliance"
git pushfrom django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
