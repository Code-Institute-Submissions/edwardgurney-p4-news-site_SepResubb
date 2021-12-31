from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from news.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 6

class ArticleDetailView(DetailView):
    model = Post
    form = CommentForm
    template_name = 'article_details.html'

@login_required
def submit_comment(request, slug):
    if request.method == "POST":
        #form = CommentForm(request.POST)
        user_comment = request.POST.get('body')
        comment_post = get_object_or_404(Post, slug=slug)
        user =  request.user
        user_email = user.email
        user_username = user.username
        new_comment = Comment.objects.create(post =comment_post, email = user_email, user_name = user_username, body = user_comment)
        return HttpResponseRedirect(reverse('article-detail', args=(comment_post.slug,)))

@login_required
def upvote(request, slug):
    comment_post = get_object_or_404(Post, slug=slug)
    comment_post.upvotes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=(comment_post.slug,)))

def search(request):
    search_word = request.GET.get('search_word')
    post_items = Post.objects.filter(title__icontains=search_word)#| Post.objects.filter(sub_headline__icontains=search_word)
    return render(request, 'search_results.html', {'search_list':post_items})