from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.test import TestCase
from ..models import Author, BlogPost, Comment

def create_author():
    author = Author.objects.create(name='test_author')
    return author

class ViewTestCase(TestCase):

    def test_add_author(self):
        name = 'test_author'
        data = { 'name' : name }
        response = self.client.post(reverse('add_author'), data)
        # Check if author was successfully created in the database
        author = Author.objects.filter(name=name)
        self.assertTrue(Author.objects.filter(name=name).exists())
        # Check if it's a redirect
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('authors')))
        return author

    def test_add_blogpost(self):
        author = create_author()
        title = 'test_title'
        data = { 'title' : title,
                 'text' : 'test_text',
                 'author' : author }
        response = self.client.post(reverse('add_blogpost'), data)
        # Check if post was created
        self.assertTrue(BlogPost.objects.filter(title=title).exists())
        # check if there was a redirect
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('blogposts')))

    def test_add_comment(self):
        author = create_author()
        body = 'comment test body'
        data = { 'body' : body,
                 'author' : author }
        response = self.client.post(reverse('add_comment'), data)
        # Check if comment was created
        self.assertTrue(Comment.objects.filter(body=body).exists())
        # check if there was a redirect
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('comments')))


