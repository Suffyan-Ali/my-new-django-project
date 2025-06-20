from django.test import TestCase, Client

class HelloViewTest(TestCase):
    def test_hello_view_returns_correct_message(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, Jenkins CI/CD with Django!")

