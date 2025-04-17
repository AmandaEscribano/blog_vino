from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog

class BlogModelTest(TestCase):
    def test_str_returns_title(self):
        user = User.objects.create_user(username='testuser', password='12345')
        blog = Blog.objects.create(title='Mi primer post', body='Texto', author=user)
        self.assertEqual(str(blog), 'Mi primer post')
