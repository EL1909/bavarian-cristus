from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import ImagePost, Comment

class ImagePostForm(ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title', 'image', 'location', 'text',]

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if text and len(text) < 6:
            raise ValidationError("Comment must be at least 6 characters")
        return text

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if location and 'bayern' not in location.lower():
            raise ValidationError("Location must be within the state of Bavaria (Bayern).")
        return location


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
