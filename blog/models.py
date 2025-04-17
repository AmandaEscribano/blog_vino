from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
