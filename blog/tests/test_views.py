from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase

# Create your tests here.
from blog.models import Tag, User


class ViewTestCase(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        # Check to see if form exists
        self.assertIn(b'<h1>Welcome to my Blog!</h1>', response.content)


    def test_add_tag(self):
        name = 'happy-test-tag'
        post = 'happy-test-title'
        data = {
            'name': name,
            'post': post
        }
        response = self.client.post(reverse('add_tag'), data)

        # Check to see if form exists
        self.assertIn(b'<input type="submit" value="Send contact request" />', response.content)

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

        # Check this message was added in the database ???
        # self.assertTrue(User.objects.filter(name=name).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('contact')))
