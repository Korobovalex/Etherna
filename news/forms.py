from django import forms
from .models import Post, Category


class NewsForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'type', 'category', 'tags', 'image', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 7}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

