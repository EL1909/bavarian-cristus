from django.contrib import admin
from .models import ImagePost, Comment, Payment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Payment)


@admin.register(ImagePost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'user', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content', 'user']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'user')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'text', 'image_post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
