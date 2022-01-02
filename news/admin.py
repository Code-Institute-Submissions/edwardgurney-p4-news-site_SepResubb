from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug' : ('title',)}
    list_filter = ('created_date', 'upvotes', 'downvotes', 'author', 'updated_date')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'author', 'created_date', 'updated_date')
    search_fields = ('title', 'content', 'author', 'created_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('comment_upvote', 'comment_downvote', 'created_on')
    list_display = ('user_name', 'body', 'created_on', 'inappropriate_posts')
    search_fields = ('user_name', 'created_on', 'email')


# Register your models here.
