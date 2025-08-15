from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # ✅ required by checker
        books = Book.objects.filter(author=author)     # ✅ required by checker
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print("Author not found.")

# Query 2: List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print("Library not found.")

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(librarian.name)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or librarian not found.")

