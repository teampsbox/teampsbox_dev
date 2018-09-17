from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Class-based Views
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class PostListView(LoginRequiredMixin, ListView):
	model = Post	
	template_name = 'psblog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']	

class PostDetailView(DetailView):
	model = Post
	template_name = 'psblog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'psblog/post_new.html'
	fields = ['title', 'body']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'body']
	template_name = 'psblog/post_edit.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'psblog/post_delete.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class AboutPageView(TemplateView):
	template_name = 'psblog/about.html'


