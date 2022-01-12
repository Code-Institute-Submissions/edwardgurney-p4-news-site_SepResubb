from django.urls import path
from .views import HomeView, ArticleDetailView, submit_comment, upvote, search, downvote, inappropriate_comment


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<slug>', ArticleDetailView.as_view(), name='article-detail'),
    path('comment/<slug>', submit_comment, name='submit-comment'),
    path('upvote/<slug>', upvote, name='upvote'),
    path('search', search, name='search_posts'),
    path('downvote/<slug>', downvote, name='downvote'),
    path('inappropriate/<pk>', inappropriate_comment,
         name='inappropriate_comment'),
    ]
