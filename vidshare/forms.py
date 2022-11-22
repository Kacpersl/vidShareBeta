from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea
from .models import Comment, Video

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'text']
        labels = {
            "username": "Your Name",
            "text": "",
        }
        widgets = {
            'text': Textarea(attrs={'placeholder': 'Enter Your Comment'}),
        }

