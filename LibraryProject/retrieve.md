# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949

---

### 💡 Explanation

| Line | Meaning |
|------|--------|
| `from bookshelf.models import Book` | Load the model into shell |
| `Book.objects.get(...)` | Retrieves the Book by title |
| `print(...)` | Displays the details of the book |
| `# Output:` | Shows what you saw in the shell |

---

### ✅ After This Step

You’ll have created:
- `create.md` ✅
- `retrieve.md` ✅

Your next step will be: **`update.md`** (updating the title of the book).

Would you like to move on to the `update.md` file now?

