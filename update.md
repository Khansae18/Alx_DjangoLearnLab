# Update Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four

---

### 💡 Explanation

| Line | Description |
|------|-------------|
| `Book.objects.get(title="1984")` | Fetches the book you created earlier |
| `book.title = "Nineteen Eighty-Four"` | Changes the title |
| `book.save()` | Saves the updated info to the database |
| `print(book.title)` | Confirms that the title was updated |
| `# Output:` | Shows expected shell output |

---

## ✅ Recap So Far

You should now have these three files completed:

| File         | Purpose                      |
|--------------|------------------------------|
| `create.md`  | Create a Book instance       |
| `retrieve.md`| Retrieve and display it      |
| `update.md`  | Update its title             |

---

Next: We'll do the **delete step** in `delete.md`.

Would you like to proceed to that now?

