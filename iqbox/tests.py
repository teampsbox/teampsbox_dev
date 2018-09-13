import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Quote

class QuoteModelTest(TestCase):

	def setUp(self):
		Quote.objects.create(content='just a test')

	def test_content_content(self):
		quote = Quote.objects.get(id=1)
		expected_object_name = f'{quote.content}'
		self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):    

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')