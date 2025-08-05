from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show in list
    list_filter = ('publication_year',)  # Add filter by year
    search_fields = ('title', 'author')  # Add search by title/author
