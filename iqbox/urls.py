from django.urls import path

from .views import IqboxPageView

urlpatterns = [
	path('', IqboxPageView.as_view(), name='iqbox'),
]