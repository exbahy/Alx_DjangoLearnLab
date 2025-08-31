# Update Book Instance

```python
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984") # استخدم العنوان القديم للبحث
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(f"Updated book title: {book_to_update.title}")