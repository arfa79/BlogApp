from django.test import TestCase
from models import Post, Comment

class PostModelTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='Test Content')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'Test Content')

class CommentModelTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='Test Content')
        self.comment = Comment.objects.create(post=self.post, text='Test Comment', email='test@example.com')

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, 'Test Comment')
        self.assertEqual(self.comment.email, 'test@example.com')