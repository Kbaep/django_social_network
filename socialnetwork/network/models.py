from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    post_like = models.SmallIntegerField(default=0)
    post_dislike = models.SmallIntegerField(default=0)
    user = models.ForeignKey(User, verbose_name='Profile',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
