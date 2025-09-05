# في ملف relationship_app/query_samples.py

import sys
from pathlib import Path

# سطرين جداد: بنضيف مجلد المشروع الرئيسي لمسارات بايثون
# Path(__file__).resolve().parent.parent بيوصل للمجلد اللي فيه manage.py (اللي هو LibraryProject)
sys.path.append(str(Path(__file__).resolve().parent.parent))
import os
import django

# ضبط إعدادات Django عشان السكريبت ده يقدر يوصل للموديلز
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("--- Running Sample Queries ---")

    # 1. Create Sample Data (هذه الخطوة ضرورية لتجربة الاستعلامات)
    print("\nCreating Sample Data...")
    author1 = Author.objects.create(name="Jane Doe")
    author2 = Author.objects.create(name="John Smith")
    print(f"Authors created: {author1.name}, {author2.name}")

    book1 = Book.objects.create(title="The First Book", author=author1, publication_year=2020)
    book2 = Book.objects.create(title="Another Great Story", author=author1, publication_year=2021)
    book3 = Book.objects.create(title="A New Adventure", author=author2, publication_year=2022)
    print(f"Books created: {book1.title}, {book2.title}, {book3.title}")

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2) # إضافة الكتب للمكتبة (ManyToMany)
    library2 = Library.objects.create(name="Community Reading Hub")
    library2.books.add(book3)
    print(f"Libraries created: {library1.name}, {library2.name}")

    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    print(f"Librarian created: {librarian1.name} for {librarian1.library.name}")
    librarian2 = Librarian.objects.create(name="Bob Williams", library=library2)
    print(f"Librarian created: {librarian2.name} for {librarian2.library.name}")

    print("\n--- Query Results ---")

    # Query 1: Query all books by a specific author (ForeignKey)
    print("\nQuery 1: Books by Jane Doe")
    jane_books = Book.objects.filter(author__name="Jane Doe") # استخدام __name للوصول لاسم المؤلف
    for book in jane_books:
        print(f"- {book.title} (Published: {book.publication_year})")

    # Query 2: List all books in a library (ManyToManyField)
    print("\nQuery 2: Books in Central Library")
    central_library = Library.objects.get(name="Central Library")
    books_in_central = central_library.books.all()
    for book in books_in_central:
        print(f"- {book.title} by {book.author.name}")

    # Query 3: Retrieve the librarian for a library (OneToOneField)
    print("\nQuery 3: Librarian for Community Reading Hub")
    community_library = Library.objects.get(name="Community Reading Hub")
    community_librarian = community_library.librarian # الوصول لمدير المكتبة مباشرة
    print(f"- Librarian Name: {community_librarian.name}")

    print("\n--- Queries Completed ---")

if __name__ == '__main__':
    run_queries()
    