from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from dishly_app.models import Recipe

class ListDetailTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="lina", password="pw123456")
        self.recipe = Recipe.objects.create(
            name="Mansaf",
            description="Traditional Jordanian dish",
            user=self.user,
            category="AR",
        )

    def test_list_view_status(self):
        res = self.client.get(reverse("recipe-list"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Mansaf")

    def test_detail_view_status(self):
        res = self.client.get(reverse("recipe-detail", kwargs={"pk": self.recipe.pk}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Mansaf")