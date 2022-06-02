from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import News


def index(request):
    context = {
        'title': 'Home',
        'nav_footer': ['Home', 'News', 'About'],
    }
    return render(request, template_name='home/home.html', context=context)


class NewsList(ListView):
    paginate_by = 4
    model = News
    template_name = 'home/news.html'
    context_object_name = 'news'
    extra_context = {'title': 'News'}

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class HomeList(NewsList):
    paginate_by = 3
    template_name = 'home/home.html'
    extra_context = {'title': 'Home'}


def show_post(reqest, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'title': post.title,
        'content': post.content,
        'photo': post.photo,
        'created_at': post.created_at,
    }

    return render(reqest, template_name='home/detail.html', context=context)
