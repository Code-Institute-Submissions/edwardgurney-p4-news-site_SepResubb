from django.urls import path
from .views import HomeView, ArticleDetailView


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<slug>', ArticleDetailView.as_view(), name='article-detail'),
]
