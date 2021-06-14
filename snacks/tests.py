from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestingPages(TestCase):
    
    def test_home_response_status_ok(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)