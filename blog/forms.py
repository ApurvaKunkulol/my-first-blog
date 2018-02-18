from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    Description: A form class for the Post model. It will create and save any changes to individual posts.
    """
    class Meta:
        model = Post
        fields = ('title', 'text')