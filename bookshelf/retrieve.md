# Retrieve Book Instance

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

Expected Output

('1984', 'George Orwell', 1949)