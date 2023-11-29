from django import forms
from django.forms import Textarea, TextInput
from discussify.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "title", "content",)
        widgets = {
            'author': TextInput(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {"author", "comment",}
        widgets = {
            'author': TextInput(attrs={'class': 'form-control'}),
            'comment': TextInput(attrs={'class': 'form-control'})
        }