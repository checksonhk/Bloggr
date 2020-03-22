from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

'''
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(default='default-post.jpg', upload_to='post_pics')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





