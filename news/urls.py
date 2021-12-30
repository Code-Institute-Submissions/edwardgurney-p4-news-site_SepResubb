from django.urls import path
from .views import HomeView, ArticleDetailView, submit_comment


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<slug>', ArticleDetailView.as_view(), name='article-detail'),
    path('comment/<slug>', submit_comment, name='submit-comment'),
]
