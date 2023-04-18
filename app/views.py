from django.shortcuts import render

from rest_framework import generics
from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer


class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
