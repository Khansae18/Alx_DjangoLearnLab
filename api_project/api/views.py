from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()       
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]
    
    
class IsLibrarianOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        # Allow safe methods for everyone
        if request.method in SAFE_METHODS:
            return True
        # Write permissions only for staff (is_staff=True)
        return request.user and request.user.is_staff

