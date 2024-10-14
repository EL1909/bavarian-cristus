from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ImagePost)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
