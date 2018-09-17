from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from .models import Post

class HomePageViewTest(TestCase):	
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200) 

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'psblog/home.html')
    

class AboutPageViewTest(TestCase):
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
		self.assertTemplateUsed(response, 'psblog/about.html')

""" For PSBLOG Tests """
class BlogTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='testuser',
			email='test@email.com',
			password='secret'
		)

		self.post = Post.objects.create(
			title='A good title',
			body='Nice body content',
			author=self.user,
		)

	def test_string_representation(self):
		post = Post(title='A sample title')
		self.assertEqual(str(post), post.title)

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'A good title')
		self.assertEqual(f'{self.post.body}', 'Nice body content')
		self.assertEqual(f'{self.post.author}', 'testuser')

	def test_post_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Nice body content')
		# self.assertTemplateUsed(response, 'home.html')
	
	def test_post_detail_view(self):
		response = self.client.get('/post/1/')
		no_response = self.client.get('/post/100000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'A good title')
		self.assertTemplateUsed(response, 'psblog/post_detail.html')
