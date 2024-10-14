from .models import ImagePost, Comment
from django.forms import ModelForm


class ImagePostForm(ModelForm):
    class Meta:
        model = ImagePost
        fields = ('image',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
