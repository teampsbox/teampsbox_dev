from django.shortcuts import render

# Class-based Views
from django.views.generic import TemplateView, ListView
from .models import Quote

class IqboxPageView(ListView):
	model = Quote
	template_name = 'iqbox/iqbox.html'
	context_object_name = 'quotes'

