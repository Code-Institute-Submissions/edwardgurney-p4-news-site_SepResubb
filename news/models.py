from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="news_posts")
    updated_date = models.DateTimeField(auto_now=True)
    sub_headline = models.TextField()
    content = models.TextField(null=True)
    news_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvoted', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvoted',
                                       blank=True)

    # def __str__(self):
    #     return self.title + ' | ' + str(self.author)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    # def number_of_upvotes(self):
    #     return self.upvotes.count()

    # def number_of_downvotes(self):
    #     return self.downvotes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment_upvote = models.ManyToManyField(
        User, related_name='comment_upvoted', blank=True)
    comment_downvote = models.ManyToManyField(
        User, related_name='comment_downvoted', blank=True)
    inappropriate_post = models.ManyToManyField(
        User, related_name='inappropriate_posts', blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.user_name}"

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()

    def inappropriate_posts_count(self):
        return self.inappropriate_post.count()
