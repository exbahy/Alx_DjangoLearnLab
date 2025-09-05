import os
import sys
import django

sys.path.append(os.path.abspath('.'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # --- إضافة بيانات تجريبية ---
    print(">>> Adding sample data...")
    author1, _ = Author.objects.get_or_create(name='Taha Hussein')
    book1, _ = Book.objects.get_or_create(title='Al-Ayyam', author=author1)
    book2, _ = Book.objects.get_or_create(title='The Future of Culture in Egypt', author=author1)
    
    library1, _ = Library.objects.get_or_create(name='Central Library')
    library1.books.add(book1, book2)
    
    librarian1, _ = Librarian.objects.get_or_create(name='Mohammed', library=library1)
    print(">>> Sample data added.\n")

    # --- تنفيذ الاستعلامات المطلوبة ---
    
    # الاستعلام الأول: هات كل كتب مؤلف معين
    print("--- Querying all books by a specific author (Taha Hussein) ---")
    author_name = 'Taha Hussein'
    author_books = Book.objects.filter(author__name=author_name)
    for book in author_books:
        print(f"- {book.title}")
    print("-" * 20)

    # الاستعلام الثاني: هات كل الكتب في مكتبة معينة (ده اللي صلحناه)
    print("\n--- Listing all books in a library (Central Library) ---")
    library_name = 'Central Library'
    library_to_check = Library.objects.get(name=library_name)
    for book in library_to_check.books.all():
        print(f"- {book.title}")
    print("-" * 20)  # <-- بص على المسافة هنا، رجعت لورا عشان تبقى مع الـ print والـ for

    # الاستعلام الثالث: هات أمين المكتبة بتاع مكتبة معينة
    print("\n--- Retrieving the librarian for a library (Central Library) ---")
    library_name_for_librarian = 'Central Library'
    librarian_found = Librarian.objects.get(library__name=library_name_for_librarian)
    print(f"The librarian is: {librarian_found.name}")
    print("-" * 20)

# السطر ده عشان لما نشغل الملف، ينفذ الفانكشن اللي فوق
if __name__ == '__main__':
    run_queries()