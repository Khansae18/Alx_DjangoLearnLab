# CRUD Operations for Book Model

---

## 🔹 Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: 1984
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())
# Output: <QuerySet []>

---

## ✅ Summary

Now your `CRUD_operations.md` includes:
- ✅ All four operations
- ✅ Python commands used
- ✅ Output comments showing success

This file proves you understand how to interact with Django models using the shell.

---

Would you like help committing and pushing this to your GitHub repo next?

