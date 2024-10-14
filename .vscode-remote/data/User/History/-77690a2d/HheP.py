from .models import ImagePost, Comment
from django import forms


class ImagePostForm(forms.ModelForm):
    class meta:
        model = ImagePost


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
