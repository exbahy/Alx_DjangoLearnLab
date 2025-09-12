# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\relationship_app\query_samples.py

import os
import django
import sys
from pathlib import Path

# هذا المسار يشير إلى مجلد advanced_features_and_security/
sys.path.append(str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("--- Running Sample Queries ---")

    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    print("\nCreating Sample Data...")
    author_john = Author.objects.create(name="John Smith")
    author_jane = Author.objects.create(name="Jane Doe")

    book_python = Book.objects.create(title="Python Basics", author=author_john, publication_year=2020)
    book_django = Book.objects.create(title="Django Advanced", author=author_john, publication_year=2021)
    book_java = Book.objects.create(title="Java Fundamentals", author=author_jane, publication_year=2019)

    library_central = Library.objects.create(name="Central Library")
    library_central.books.add(book_python, book_django)

    library_community = Library.objects.create(name="Community Hub Library")
    library_community.books.add(book_java)

    librarian_alice = Librarian.objects.create(name="Alice Green", library=library_central)
    librarian_bob = Librarian.objects.create(name="Bob White", library=library_community)

    print("Sample data created successfully.")

    print("\n--- Query Results ---")

    print("\nTask: Query all books by a specific author.")
    specific_author_name = "John Smith"
    books_by_author = Book.objects.filter(author__name=specific_author_name)
    print(f"  Books by '{specific_author_name}':")
    for book in books_by_author:
        print(f"    - {book.title} (Author: {book.author.name})")

    print("\nTask: List all books in a library.")
    library_name = "Central Library"
    library_instance = Library.objects.get(name=library_name)
    books_in_library = library_instance.books.all()
    print(f"  Books in '{library_name}':")
    for book in books_in_library:
        print(f"    - {book.title}")

    print("\nTask: Retrieve the librarian for a library.")
    target_library_name = "Community Hub Library"
    target_library_instance = Library.objects.get(name=target_library_name)
    librarian_info = target_library_instance.librarian
    print(f"  Librarian for '{target_library_name}': {librarian_info.name}")

    print("\n--- Queries Completed ---")

if __name__ == '__main__':
    run_queries()