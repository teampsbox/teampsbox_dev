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


