from django.urls import path
from .views import TweetList, CommentList


urlpatterns = [
    path('tweets/', TweetList.as_view(), name='tweet_list'),
    path('comments/', CommentList.as_view(), name='comment_list'),
]