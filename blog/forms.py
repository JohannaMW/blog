from django.forms import ModelForm

__author__ = 'johanna'
from django import forms
from blog.models import Author, BlogPost
from django.core.exceptions import ValidationError
from models import Comment, Author, BlogPost, Tag
import re

def no_swearwords_validator(value):
    if re.match("shit|fuck|bitch", value) is not None:
        raise ValidationError("You can not swear on this blog!")

class CommentForm(ModelForm):
    class Meta:
        model = Comment

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost

class AuthorForm(ModelForm):
    class Meta:
        model = Author

class TagForm(ModelForm):
    class Meta:
        model = Tag

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=400)