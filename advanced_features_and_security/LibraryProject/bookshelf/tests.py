from django.test import TestCase, Client
from django.urls import reverse

class SecurityTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_x_frame_options(self):
        resp = self.client.get(reverse("bookshelf:book_list"))
        self.assertEqual(resp.headers.get("X-Frame-Options"), "DENY")

    def test_nosniff(self):
        resp = self.client.get(reverse("bookshelf:book_list"))
        self.assertEqual(resp.headers.get("X-Content-Type-Options"), "nosniff")

    def test_csp_header_present(self):
        resp = self.client.get(reverse("bookshelf:book_list"))
        # basic presence check
        self.assertIn("Content-Security-Policy", resp.headers)

    def test_csrf_token_in_form(self):
        resp = self.client.get(reverse("bookshelf:create_book"))
        self.assertContains(resp, "csrfmiddlewaretoken")

