__author__ = 'johanna'
from django import forms
from blog.models import Author, BlogPost
from django.core.exceptions import ValidationError
import re

def no_swearwords_validator(value):
    if re.match("shit|fuck|bitch", value) is not None:
        raise ValidationError("You can not swear on this blog!")

class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    comment_body = forms.CharField(validators=[ no_swearwords_validator ])

class BlogPostForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    title = forms.CharField(max_length=120)
    text = forms.CharField()

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=120)

class TagForm(forms.Form):
    name = forms.CharField(max_length=120)
    post = forms.ModelChoiceField(queryset=BlogPost.objects.all())

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=400)