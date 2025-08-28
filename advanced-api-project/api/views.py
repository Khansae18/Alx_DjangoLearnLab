from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view
     filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']

# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users
    def perform_create(self, serializer):
        """
        Customize saving behavior.
        For example, automatically associate the logged-in user as the creator.
        """
        serializer.save(created_by=self.request.user)  

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_update(self, serializer):
        """
        Customize update behavior.
        Example: log the user who updated the book.
        """
        serializer.save(updated_by=self.request.user)  

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
