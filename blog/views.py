from django.shortcuts import render, redirect, render_to_response
from django.core.mail import send_mail
# Create your views here.
from blog.forms import CommentForm, BlogPostForm, AuthorForm, TagForm, ContactForm
from models import Comment, BlogPost, Author, Tag,  Reader

def home(request):
    return render_to_response("home.html")

def comments(request):
    return render_to_response("comments.html")

def blogposts(request):
    return render_to_response("blogposts.html")

def authors(request):
    return render_to_response("authors.html")

def add_comment(request):
    data = { "comment_form": CommentForm() }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
           # Comment.objects.create(author=form.cleaned_data['author'], body = form.cleaned_data['comment_body'])
            return redirect("comments")

        else:
            data = { "comment_form": CommentForm(request.POST) }
            return render(request, "add_comment.html", data)

    else:
        return render(request, "add_comment.html", data)

def add_blogpost(request):
    data = { "blogpost_form": BlogPostForm() }
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogposts")

    else:
        data = { "blogpost_form": BlogPostForm() }
    return render(request, "add_blogpost.html", data)

def add_author(request):
    data = { "author_form": AuthorForm() }
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("authors")

    else:
        data = { "author_form": AuthorForm() }
    return render(request, "add_author.html", data)

def add_tag(request):
    data = { "tag_form": TagForm() }
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = Tag.objects.create(name=form.cleaned_data['name'])
            form.cleaned_data['post'].tag.add(tag)
            form.cleaned_data['post'].save()

            return redirect("/tag/new/")

    else:
        data = { "tag_form": TagForm() }
    return render(request, "add_tag.html", data)

def contact(request):
    data = { "contact_form": ContactForm() }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user = Reader.objects.create(name=form.cleaned_data['name'], email = form.cleaned_data['email'])
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'jweinsziehr@gmx.de', [user.email] )
            return redirect("/contact/")

        else:
            data = { "comment_form": ContactForm(request.POST) }
            return render(request, "contact.html", data)

    else:
        return render(request, "contact.html", data)
