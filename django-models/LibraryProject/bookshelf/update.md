
markdown
python
from bookshelf.models import Book

book = Book.objects.get(author="George Orwell")
book.title = "Nineteen Eighty-Four"
book.save()
book  # <Book: Nineteen Eighty-Four by George Orwell (1949)>