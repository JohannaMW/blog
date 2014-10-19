from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase

# Create your tests here.
from blog.models import Tag


class ViewTestCase(TestCase):
    def add_user(self):


    @patch('cards.utils.requests')
    def test_home(self, mock_requests):
        mock_comic = {
            'num': 1433,
            'year': "2014",
            'safe_title': "Lightsaber",
            'alt': "A long time in the future, in a galaxy far, far, away.",
            'transcript': "An unusual gamma-ray burst originating from somewhere across the universe.",
            'img': "http://imgs.xkcd.com/comics/lightsaber.png",
            'title': "Lightsaber",
        }
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_comic
        mock_requests.get.return_value = mock_response
        response = self.client.get(reverse('home'))
        self.assertIn('<h3>{} - {}</h3>'.format(mock_comic['safe_title'], mock_comic['year']),
                      response.content)
        self.assertIn('<img alt="{}" src="{}">'.format(mock_comic['alt'], mock_comic['img']),
                      response.content)
        self.assertIn('<p>{}</p>'.format(mock_comic['transcript']), response.content)

    def test_add_tag(self):
        name = 'happy-test-tag'
        data = {
            'name': name,
            'post': post
        }
        response = self.client.post(reverse('add_tag'), data)

        # Check this tag was added in the database
        self.assertTrue(Tag.objects.filter(name=name).exists())

        # Check it redirects to the blog post page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endwith(reverse('home')))

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
        response = self.client.get(reverse('contact'), data)

        # Check to see if form exists
        self.assertIn(b'<input type="submit" value="Send contact request" />', response.content)

        # Check this message was added in the database
        self.assertTrue(Tag.objects.filter(name=name).exists())

        # Check it redirects to the blog post page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endwith(reverse('home')))