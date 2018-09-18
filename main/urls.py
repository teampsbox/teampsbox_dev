from django.urls import path

# Function-Based Views
from . import views

from .views import HomePageView, AboutPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('<user.username>/', views.profile, name='profile'),
]
