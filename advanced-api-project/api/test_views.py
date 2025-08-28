from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book
from django.contrib.auth.models import User
class BaseTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Authenticate the user
        self.client.login(username='testuser', password='testpass')
        
        # Example book data
        self.book_data = {
            "title": "Test Book",
            "author": "John Doe",
            "description": "A test description",
            "published_date": "2025-01-01"
        }
class BookAPITest(BaseTestCase):
    def test_create_book(self):
        url = reverse('book-list')  # make sure your view name is 'book-list'
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_get_book(self):
        book = Book.objects.create(**self.book_data)
        url = reverse('book-detail', kwargs={'pk': book.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        url = reverse('book-detail', kwargs={'pk': book.id})
        updated_data = {"title": "Updated Title", "author": "Jane Doe", "description": "Updated", "published_date": "2025-02-01"}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Updated Title")

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        url = reverse('book-detail', kwargs={'pk': book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_book(self):
        Book.objects.create(**self.book_data)
        url = reverse('book-list') + '?search=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_book(self):
        Book.objects.create(title="A Book", author="Author1")
        Book.objects.create(title="B Book", author="Author2")
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "A Book")

