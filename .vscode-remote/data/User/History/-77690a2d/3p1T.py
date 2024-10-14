from django.forms import ModelForm
from .models import ImagePost, Comment

class ImagePostForm(ModelForm):
    class Meta:
        model = ImagePost
        fields = ('image',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
