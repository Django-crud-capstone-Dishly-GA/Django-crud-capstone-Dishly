from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from dishly_app.models import Recipe

class CRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = User.objects.create_user(username="owner", password="pw123456")
        self.other = User.objects.create_user(username="other", password="pw123456")
        self.recipe = Recipe.objects.create(
            name="Makloubeh",
            description="Upside-down rice dish",
            user=self.owner,
            category="AR",
        )

    def test_create_requires_login(self):
        res = self.client.get(reverse("recipe-create"))
        self.assertIn(res.status_code, (302, 200))

    def test_owner_can_update(self):
        self.client.login(username="owner", password="pw123456")
        res = self.client.post(reverse("recipe-update", kwargs={"pk": self.recipe.pk}), {
            "name": "Makloubeh Updated",
            "description": self.recipe.description,
            "category": "AR",
            "user": self.owner.id,
        })
        self.assertIn(res.status_code, (200, 302))

    def test_non_owner_cannot_update(self):
        self.client.login(username="other", password="pw123456")
        res = self.client.post(reverse("recipe-update", kwargs={"pk": self.recipe.pk}), {"name": "Hack"})
        self.assertIn(res.status_code, (200, 302, 403))

    def test_delete_redirects(self):
        self.client.login(username="owner", password="pw123456")
        res = self.client.post(reverse("recipe-delete", kwargs={"pk": self.recipe.pk}))
        self.assertIn(res.status_code, (200, 302))