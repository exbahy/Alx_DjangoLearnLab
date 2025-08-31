# Retrieve Book Instance

```python
from bookshelf.models import Book
book_to_retrieve = Book.objects.get(title="1984")
print(f"Retrieved book: ID={book_to_retrieve.id}, Title={book_to_retrieve.title}, Author={book_to_retrieve.author}, Year={book_to_retrieve.publication_year}")