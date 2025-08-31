# Delete Book Instance

```python  <-- أضف هذا السطر
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
print("Book deleted. Checking remaining books:")
remaining_books = Book.objects.all()
print(f"Total books remaining: {remaining_books.count()}")
```  <-- أضف هذا السطر

# Expected Output:
```   <-- أضف هذا السطر
(1, {'bookshelf.Book': 1})
Book deleted. Checking remaining books:
Total books remaining: 0
```   <-- أضف هذا السطر