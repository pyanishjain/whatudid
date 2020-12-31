from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['body']
        widgets = {'body': forms.Textarea(
            attrs={'class': 'form-control'})}
