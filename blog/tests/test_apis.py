from django.test import TestCase, Client
from blog.models import Post
import json
# Define a test case class for testing the Post API endpoints
class PostAPITestCase(TestCase):
    # Set up the test environment
    def setUp(self):
        self.client = Client()
        # Create a Post object for testing purposes
        self.post = Post.objects.create(title='Test Post', content='Test Content')
    # Test for retrieving a list of posts
    def test_get_posts(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains exactly one post (the one created in setUp)
        self.assertEqual(len(response.json()), 1)
    # Test for creating a new post
    def test_create_post(self):
        # Define data for creating a new post
        data = {'title': 'New Post', 'content': 'New Content'}
        # Send a POST request to the '/posts/' endpoint with the defined data
        response = self.client.post('/posts/', data=json.dumps(data), content_type='application/json')
        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)
        # Assert that there are now two posts in the database (the one created in setUp and the newly created one)
        self.assertEqual(Post.objects.count(), 2)