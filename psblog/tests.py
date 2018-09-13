from django.test import SimpleTestCase
from django.urls import reverse

class HomePageViewTest(SimpleTestCase):	
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200) 

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '<h1>Homepage</h1>')
		self.assertTemplateUsed(response, 'home.html')
    

class AboutPageViewTest(SimpleTestCase):
	def test_about_page_status_code(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('about'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '<h1> About Page </h1>')
		self.assertTemplateUsed(response, 'about.html')