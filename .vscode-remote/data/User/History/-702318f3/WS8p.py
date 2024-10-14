from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import ImagePost, Comment


class ImagePostForm(ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title', 'image', 'location', 'text', 'status']

    def validText(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        if text and len(text) < 6:
            raise ValidationError("Comment must be at least 6 characters")


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
