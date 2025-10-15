from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class SignupTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_page_loads(self):
        res = self.client.get(reverse("signup"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Sign")

    def test_user_signup_success(self):
        res = self.client.post(reverse("signup"), {
            "username": "newuser",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
        })
        self.assertIn(res.status_code, (302, 200))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_user_signup_password_mismatch(self):
        res = self.client.post(reverse("signup"), {
            "username": "baduser",
            "password1": "abc",
            "password2": "xyz",
        })
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Invalid sign up")