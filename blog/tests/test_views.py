from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.test import TestCase
from ..models import Author, BlogPost, Comment, Tag

def create_author():
    author = Author.objects.create(name='test_author')
    return author

class ViewTestCase(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertIn('Welcome', response.content)

    def test_authors_page(self):
        response = self.client.get(reverse('authors'))
        self.assertIn('Authors', response.content)

    def test_blogpost_page(self):
        response = self.client.get(reverse('blogposts'))
        self.assertIn('Posts', response.content)

    def test_comments_page(self):
        response = self.client.get(reverse('comments'))
        self.assertIn('Comments', response.content)

    def setUp(self):
        self.author = Author.objects.create(name='test_author')

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
        title = 'test_title'
        data = { 'title' : title,
                 'text' : 'test_text',
                 'author' : self.author }
        response = self.client.post(reverse('add_blogpost'), data)
        # Check if post was created
        self.assertTrue(BlogPost.objects.filter(title=title).exists())
        # check if there was a redirect
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('blogposts')))

    def test_add_comment(self):
        body = 'comment test body'
        data = { 'body' : body,
                 'author' : self.author }
        response = self.client.post(reverse('add_comment'), data)
        # Check if comment was created
        self.assertTrue(Comment.objects.filter(body=body).exists())
        # check if there was a redirect
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('comments')))

    def test_add_tag(self):
        name = 'happy-test-tag'
        post = 'happy-test-title'
        data = {
            'name': name,
            'post': post
        }
        response = self.client.post(reverse('add_tag'), data)

        # Check to see if form exists
        self.assertIn('Contact', response.content)

        # Check this tag was added in the database
        self.assertTrue(Tag.objects.filter(name=name).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('add_tag')))

    def test_contact(self):
        name = 'jane-test'
        email = 'jane-test@test.com'
        subject = 'testing contact form'
        message = 'if you can read this then the test was a success!'
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        response = self.client.post(reverse('contact'), data)

        # Check to see if form exists
        # self.assertIn(b'<input type="submit" value="Send contact request" />', response.content)

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('contact')))



