from django.test import TestCase

# Create your tests here.
class ViewTestCase(TestCase):
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

add_tag

    def test_contact(self):
            response = self.client.get(reverse('contact'))
            self.assertIn(b'<input type="submit" value="Send contact request" />', response.content)