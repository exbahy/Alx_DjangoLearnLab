# Create Book Instance

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created book: {book.title} by {book.author} (ID: {book.id})")