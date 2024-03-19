from django.test import TestCase, Client
from blog.models import Post
import json

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title='Test Post', content='Test Content')

    def test_get_posts(self):
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post('/posts', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.count(), 2)