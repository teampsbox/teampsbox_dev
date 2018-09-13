from django.shortcuts import render

# Class-based Views
from django.views.generic import TemplateView


class HomePageView(TemplateView):	
	template_name = 'psblog/home.html'	


class AboutPageView(TemplateView):
	template_name = 'psblog/about.html'
