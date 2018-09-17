from django.shortcuts import render

# Class-based Views
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


class HomePageView(ListView):
	model = Post	
	template_name = 'psblog/home.html'	

class BlogDetailView(DetailView):
	model = Post
	template_name = 'psblog/post_detail.html'


class AboutPageView(TemplateView):
	template_name = 'psblog/about.html'


