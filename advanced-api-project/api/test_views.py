from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Book, Author

User = get_user_model()

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_create_book(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-list')
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_book(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-detail', args=[self.book.id])
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        url = reverse('book-list') + f'?title={self.book.title}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_search_books(self):
        url = reverse('book-list') + f'?search={self.book.title}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_order_books(self):
        Book.objects.create(title="A Book", publication_year=2019, author=self.author)
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_permission_required_for_update(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {"title": "No Auth Update", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permission_required_for_delete(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
