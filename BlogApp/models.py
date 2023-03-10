from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    short_info = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('only_post', args=[str(self.pk)])

    