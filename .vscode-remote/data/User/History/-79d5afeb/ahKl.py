from .models import Comment
from django import forms


class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
