from django.contrib import admin
from django.urls import path, include  # اتأكد إن include موجودة

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # السطر ده هو كل اللي المفروض يكون موجود هنا بخصوص الأبلكيشن بتاعنا
    path('app/', include('relationship_app.urls')), 
]