from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from psblog.models import Post


class HomePageView(TemplateView):
    template_name = 'main/home.html'


class AboutPageView(TemplateView):
    template_name = 'main/about.html'


@login_required
def profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'main/profile.html', {'user_posts': user_posts, 'user': user})
