from django.test import TestCase
from django.urls import reverse, resolve


class URLTests(TestCase):
    def test_urls_resolve(self):
        names = [
            ("recipe-list", {}),
            ("recipe-detail", {"pk": 1}),
            ("recipe-create", {}),
            ("recipe-update", {"pk": 1}),
            ("recipe-delete", {"pk": 1}),
            ("myrecipe", {}),
            ("like-recipe", {"recipe_id": 1}),
        ]
        for name, kwargs in names:
            try:
                url = reverse(name, kwargs=kwargs or None)
                self.assertTrue(resolve(url))
            except Exception as e:
                self.fail(f"URL '{name}' failed to resolve: {e}")
