from django.shortcuts import render

# Class-based Views
from django.views.generic import TemplateView, ListView
from .models import Quote

class HomePageView(ListView):
	model = Quote
	template_name = 'home.html'
	context_object_name = 'quotes'


class AboutPageView(TemplateView):
	template_name = 'about.html'
