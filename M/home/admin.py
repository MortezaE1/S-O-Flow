from django.contrib import admin
from .models import Post, Comment, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated')
    search_fields = ('slug', 'body')
    ordering = ('-updated',)
    list_filter = ('updated', 'user')
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created', 'is_reply')
    ordering = ('-created',)
    raw_id_fields = ('user', 'post', 'reply')
    search_fields = ('body',)
    list_filter = ('user', 'created', 'is_reply')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created')
    ordering = ('created',)
    raw_id_fields = ('user', 'post')
    list_filter = ('user', 'created')
