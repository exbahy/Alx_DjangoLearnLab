# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\relationship_app\models.py

from django.db import models
from django.contrib.auth import get_user_model # الأفضل استخدامها للوصول لموديل المستخدم

# User = get_user_model() # لا نحتاجها هنا لأن لا يوجد ربط مباشر بموديل المستخدم في هذا التطبيق

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model): # هذا هو موديل الكتاب الخاص بـ relationship_app (مختلف عن bookshelf.Book)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Librarian of {self.library.name})"