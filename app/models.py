from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=25)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=25)


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    mark_value = models.IntegerField(default=0)
