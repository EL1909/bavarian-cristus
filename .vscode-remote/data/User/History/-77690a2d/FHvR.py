from .models import ImagePost, Comment
from django import forms


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ('image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
