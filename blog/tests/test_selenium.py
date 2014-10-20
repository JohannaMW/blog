from time import sleep
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from blog.models import Author, Comment, BlogPost


def create_author():
        author = Author.objects.create(name='test')
        return author

def create_post():
        author = Author.objects.create(name='test')
        post = BlogPost.objects.create(title='testtitle', text = 'testtext', author=author)
        return post


class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_add_author(self):
        self.selenium.get("{}{}".format(self.live_server_url, reverse('home')))
        sleep(.5)
        self.selenium.find_elements_by_link_text("Add an Author")[0].click()
        sleep(.5)
        self.selenium.find_element_by_name('name').send_keys('test')
        sleep(.5)
        self.selenium.find_element_by_css_selector("input[value='Submit author']").click()
        sleep(.5)

    def test_add_blogpost(self):
        author = create_author()
        self.selenium.get("{}{}".format(self.live_server_url, reverse('home')))
        sleep(.5)
        self.selenium.find_elements_by_link_text("Add a Blogpost")[0].click()
        sleep(.5)
        author_dropdown = self.selenium.find_element_by_name('author')
        for option in author_dropdown.find_elements_by_tag_name('option'):
            if option.text == author.name:
                option.click()

        self.selenium.find_element_by_name('title').send_keys('testtitle')
        sleep(.5)
        self.selenium.find_element_by_name('text').send_keys('testtext')
        self.selenium.find_element_by_css_selector("input[value='Submit blog post']").click()
        sleep(.5)

    def test_add_comment(self):
        author = create_author()
        self.selenium.get("{}{}".format(self.live_server_url, reverse('home')))
        sleep(.5)
        self.selenium.find_elements_by_link_text("Add a comment")[0].click()
        sleep(.5)
        author_dropdown = self.selenium.find_element_by_name('author')
        for option in author_dropdown.find_elements_by_tag_name('option'):
            if option.text == author.name:
                option.click()

        self.selenium.find_element_by_name('comment_body').send_keys('testcomment')
        sleep(.5)

        self.selenium.find_element_by_css_selector("input[value='Submit comment']").click()
        sleep(.5)

    def test_add_tag(self):
        post = create_post()
        self.selenium.get("{}{}".format(self.live_server_url, reverse('home')))
        sleep(.5)
        self.selenium.find_elements_by_link_text("Add a Tag")[0].click()
        sleep(.5)
        self.selenium.find_element_by_name('name').send_keys('testtag')
        post_dropdown = self.selenium.find_element_by_name('post')
        for option in post_dropdown.find_elements_by_tag_name('option'):
            if option.text == post.title:
                option.click()

        sleep(.5)
        self.selenium.find_element_by_css_selector("input[value='Submit tag']").click()
        sleep(.5)

    # def test_admin_login(self):
    #     # Create a superuser
    #     User.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
    #     self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
    #     self.selenium.find_element_by_name('username').send_keys('superuser')
    #     password_input = self.selenium.find_element_by_name('password')
    #     password_input.send_keys('mypassword')
    #     password_input.send_keys(Keys.RETURN)
    #     sleep(.5)
    #
    # def admin_login(self):
    #     # Create a superuser
    #     User.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
    #     self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
    #     self.selenium.find_element_by_name('username').send_keys('superuser')
    #     password_input = self.selenium.find_element_by_name('password')
    #     password_input.send_keys('mypassword')
    #     password_input.send_keys(Keys.RETURN)
    #     sleep(.5)


    # def test_admin_create_blog_post(self):
    #     author = create_author()
    #     self.admin_login()
    #     sleep(.5)
    #     self.selenium.find_elements_by_link_text('Blog posts')[0].click()
    #     sleep(.5)
    #     self.selenium.find_element_by_link_text('Add blog post').click()
    #     self.selenium.find_element_by_name('title').send_keys('title_test')
    #     self.selenium.find_element_by_name('text').send_keys('test_text')
    #     sleep(.5)
    #     author_dropdown = self.selenium.find_element_by_name('author')
    #     for option in author_dropdown.find_elements_by_tag_name('option'):
    #         if option.text == author.name:
    #             option.click()
    #     self.selenium.find_element_by_css_selector("input[value='Save']").click()
    #     sleep(.5)









