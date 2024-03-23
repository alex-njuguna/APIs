from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):
    # run tests on the Post model

    @classmethod
    def setUpTestData(cls):
        # create a user
        test_user = User.objects.create(username='testuser', password='abc123')
        test_user.save()

        # create a blog
        test_post = Post.objects.create(author=test_user, title='Hello World', body='This is a test blog')
        test_post.save()

    def test_blog_content(self):
        # ascertain data is as intended
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Hello World')
        self.assertEqual(body, 'This is a test blog')
        