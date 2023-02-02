from django.db import models

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