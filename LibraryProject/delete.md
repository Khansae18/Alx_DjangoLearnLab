# Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())
# Output: <QuerySet []>

---

### 💡 Explanation

| Line | Description |
|------|-------------|
| `Book.objects.get(...)` | Fetch the updated book instance |
| `book.delete()` | Deletes it from the database |
| `Book.objects.all()` | Verifies it was deleted (should return an empty QuerySet) |
| `# Output:` | Shows result confirming deletion |

---

## ✅ Final Step: Combine All into `CRUD_operations.md` (Optional Summary File)

Now you can create one last file (if your task asks for it) called `CRUD_operations.md` and copy the contents of:

- `create.md`
- `retrieve.md`
- `update.md`
- `delete.md`

into one file.

This file summarizes the entire CRUD flow.

---

## 🎉 You Did It!

✅ You created all 4 Markdown documentation files  
✅ Each file includes Django shell commands + expected output  
✅ You followed all ALX submission instructions

If you'd like, I can generate the full content of `CRUD_operations.md` for you — just say the word!

