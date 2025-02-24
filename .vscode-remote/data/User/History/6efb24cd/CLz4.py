from django.contrib import admin
from .models import ImagePost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ImagePost)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title,')}
    summernote_fields = ('content')
