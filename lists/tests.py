from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from . import views
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = views.home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        inputData = 'A new list item'
        request.method = 'POST'
        request.POST['item_text'] = inputData

        response = views.home_page(request)
        self.assertIn(inputData,response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':inputData}
        )
        self.assertEqual(response.content.decode(),expected_html)