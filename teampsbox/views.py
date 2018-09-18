from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from .models import Profile
from psblog.models import Post


class HomePageView(TemplateView):
    template_name = 'teampsbox/home.html'


class AboutPageView(TemplateView):
    template_name = 'teampsbox/about.html'


@login_required
def profile(request, username):
    user_posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'teampsbox/profile.html', {'user_posts': user_posts})
