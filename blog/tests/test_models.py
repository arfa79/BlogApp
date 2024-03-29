from django.test import TestCase
from blog.models import Post, Comment  # Import the Post and Comment models from the blog app

# Define a test case class for testing the Post model
class PostModelTestCase(TestCase):

    def setUp(self):
        # Create a Post object for testing purposes
        self.post = Post.objects.create(title='Test Post', content='Test Content')

    # Test for Post creation
    def test_post_creation(self):
        # Assert that the created post has the correct title and content
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'Test Content')

# Define a test case class for testing the Comment model
class CommentModelTestCase(TestCase):
    def setUp(self):
        # Create a Post object for testing purposes
        self.post = Post.objects.create(title='Test Post', content='Test Content')
        # Create a Comment object associated with the created Post
        self.comment = Comment.objects.create(post=self.post, text='Test Comment', email='test@example.com')

    # Test for Comment creation
    def test_comment_creation(self):
        # Assert that the created comment has the correct text and email
        self.assertEqual(self.comment.text, 'Test Comment')
        self.assertEqual(self.comment.email, 'test@example.com')
