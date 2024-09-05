from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A Test Title",
            subtitle="A test subtitle",
            author="Testing Testerson",
            isbn="123456789",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A Test Title")
        self.assertEqual(self.book.subtitle, "A test subtitle")
        self.assertEqual(self.book.author, "Testing Testerson")
        self.assertEqual(self.book.isbn, "123456789")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A test subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
