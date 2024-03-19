from django.test import TestCase, Client

class IntegrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_integration(self):
        # Test API integration by making requests and verifying responses
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)