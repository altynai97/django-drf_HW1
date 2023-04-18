from rest_framework import serializers
from .models import Tweet
from .models import Comment


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'title', 'body', 'created_at', 'author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'date', 'tweet', 'mark_value']