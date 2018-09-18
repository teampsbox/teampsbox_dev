from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

from .models import Profile
from psblog.models import Post
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'teampsbox/home.html'


class AboutPageView(TemplateView):
    template_name = 'teampsbox/about.html'


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)    
    user_posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'teampsbox/profile.html', {'user_posts': user_posts, 'user': user})
