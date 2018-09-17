from django.shortcuts import render

# Class-based Views
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class HomePageView(ListView):
	model = Post	
	template_name = 'psblog/home.html'	

class BlogDetailView(DetailView):
	model = Post
	template_name = 'psblog/post_detail.html'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'psblog/post_new.html'
	fields = '__all__'

class BlogUpdateView(UpdateView):
	model = Post
	fields = ['title', 'body']
	template_name = 'psblog/post_edit.html'

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'psblog/post_delete.html'
	success_url = reverse_lazy('home')

class AboutPageView(TemplateView):
	template_name = 'psblog/about.html'


