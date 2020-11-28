from django.core.urlresolvers import resolve
from django.test import TestCase
from coookit.views import home
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        self.assertIn(b'<h1>Contact Form</h1>', response.content)


class ArticlesTestCase(TestCase):
    pass