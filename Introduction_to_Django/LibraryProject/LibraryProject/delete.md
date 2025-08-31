# Delete Book Instance

```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
print("Book deleted. Checking remaining books:")
remaining_books = Book.objects.all()
print(f"Total books remaining: {remaining_books.count()}")