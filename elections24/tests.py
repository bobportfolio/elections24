from django.test import TestCase


class TestIndex(TestCase):
    def test_hello_world(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'elections24/index.html')
        self.assertContains(response, "elections 24")
