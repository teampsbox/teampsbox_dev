from django.urls import path

from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	
)

urlpatterns = [
	path('posts/', PostListView.as_view(), name='post_all'),
	path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('new/', PostCreateView.as_view(), name='post_new'),
	path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
	path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
	

]