# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: 1984

---

## 📖 Explanation of Each Line

| Line | Explanation |
|------|-------------|
| `# Create Operation` | This is a **Markdown heading** (for readability). |
| ```python | This starts a **code block** in Python format. |
| `from bookshelf.models import Book` | You import the `Book` model inside the Django shell. |
| `book = Book.objects.create(...)` | You create a new `Book` instance. |
| `print(book)` | You print it to confirm it's created. |
| `# Output: 1984` | You document the output (what you saw in the shell). |
| ``` | This ends the code block. |

---

## 🔁 Summary

You are typing the **commands you used** in Django shell to:
- **Create** a book
- And what the result/output was

This shows that your code works and helps the reviewer check it quickly.

---

Do you want me to give you the content for the other 3 files too (`retrieve.md`, `update.md`, and `delete.md`)?
