from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    Includes validation for publication_year to ensure it's not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    Includes nested representation of related books using BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)  # ✅ nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
