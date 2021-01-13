from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['body']
        widgets = {'body': forms.Textarea(
            attrs={'class': 'form-control'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['reply']
        widgets = {'reply': forms.Textarea(attrs={'class': 'form-control'})}
