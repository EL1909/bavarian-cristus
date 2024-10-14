from django.contrib import admin
from .models import ImagePost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ImagePost)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'user')
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'text', 'image_post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
