from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """docstring for ."""
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # on_delete means if a user has been removerd, all the articles created by him
    # will be deleted too

    def __str__(self):
        return self.title
