from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import News
from .models import Concerts



def index(request):
    context = {
        'title': 'About',
    }
    return render(request, 'home/about.html', context)


def index_3(request):
    context = {
        'title': 'Cotacts',
    }
    return render(request, 'home/contacts.html', context)


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

class ConcertsList(ListView):
    context_object_name = 'concerts'
    model = Concerts
    paginate_by = 10
    template_name = 'home/concerts.html'
    extra_context = {'title': 'Concerts'}

    # def index_2(request):
    #    context = {
    #        'title': 'Concerts',
    #    }
    #    return render(request, 'home/concerts.html', context)


def show_post(reqest, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'title': post.title,
        'content': post.content,
        'photo': post.photo,
        'created_at': post.created_at,
    }

    return render(reqest, template_name='home/detail.html', context=context)
