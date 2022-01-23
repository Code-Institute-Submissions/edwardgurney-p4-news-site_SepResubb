from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from news.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_news_one'] = Post.objects.all(
            ).order_by('-created_date')[0]
        context['home_news_two'] = Post.objects.all(
            ).order_by('-created_date')[1]
        context['home_news_three'] = Post.objects.all(
            ).order_by('-created_date')[2]
        context['top_five'] = Post.objects.annotate(
            upvotes_count=Count('upvotes')).order_by('-upvotes_count')[:5]
        return context


class ArticleDetailView(DetailView):
    model = Post
    form = CommentForm
    template_name = 'article_details.html'


@login_required
def submit_comment(request, slug):
    if request.method == "POST":
        user_comment = request.POST.get('body')
        comment_post = get_object_or_404(Post, slug=slug)
        user = request.user
        user_email = user.email
        user_username = user.username
        Comment.objects.create(
            post=comment_post,
            email=user_email,
            user_name=user_username,
            body=user_comment
            )
        return HttpResponseRedirect(
            reverse('article-detail', args=(comment_post.slug,)))


@login_required
def upvote(request, slug):
    comment_post = get_object_or_404(Post, slug=slug)
    comment_post.upvotes.add(request.user)
    return HttpResponseRedirect(
        reverse('article-detail', args=(comment_post.slug,)))


def search(request):
    search_word = request.GET.get('search_word')
    post_items = Post.objects.filter(title__icontains=search_word)
    return render(request, 'search_results.html', {'search_list': post_items})


@login_required
def downvote(request, slug):
    comment_post = get_object_or_404(Post, slug=slug)
    comment_post.downvotes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=(
        comment_post.slug,)))


@login_required
def inappropriate_comment(request, pk):
    flagged_comment = get_object_or_404(Comment, pk=pk)
    flagged_comment.inappropriate_post.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=(
        flagged_comment.post.slug,)))
