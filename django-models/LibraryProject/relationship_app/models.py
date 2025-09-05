# في ملف relationship_app/models.py

from django.db import models

# 1. Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey to Author (Many-to-One: A book has one author, an author can have many books)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(default=2000) # إضافة حقل publication_year من المهمة السابقة

    def __str__(self):
        return f"{self.title} by {self.author.name}"

# 3. Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    # ManyToManyField to Book (Many-to-Many: A library can have many books, a book can be in many libraries)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# 4. Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField to Library (One-to-One: A librarian manages one library, a library has one librarian)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Librarian of {self.library.name})"