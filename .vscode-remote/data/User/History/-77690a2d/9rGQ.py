from django.forms import ModelForm
from .models import ImagePost, Comment

class ImagePostForm(ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title', 'image', 'location', 'text', 'status']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
