from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView
from decouple import config

from .models import Concerts
from .models import News
from .models import Photo


class AboutList(ListView):
    paginate_by = 12
    model = Photo
    template_name = 'home/about.html'
    context_object_name = 'about'
    extra_context = {'title': 'about'}

    def get_queryset(self):
        return Photo.objects.filter(is_published=True)


def contact(request):
    context = {
        'title': 'Contact',
    }

    if request.method == "POST":
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'web-hanna' + message_email,  # Subject
            message,  # message
            message_email,  # from email
            [config('EMAIL')],  # to email
            fail_silently=False,
        )
        return render(request, 'home/contact.html', {'message_email': message_email})
    else:
        return render(request, 'home/contact.html', context)


class NewsList(ListView):
    paginate_by = 5
    model = News
    template_name = 'home/news.html'
    context_object_name = 'news'
    extra_context = {'title': 'News'}

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class HomeList(NewsList):
    paginate_by = 4
    template_name = 'home/home.html'
    extra_context = {'title': 'Home'}


class ConcertsList(ListView):
    context_object_name = 'concerts'
    model = Concerts
    paginate_by = 10
    template_name = 'home/concerts.html'
    extra_context = {'title': 'Concerts'}


def show_post(reqest, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'title': post.title,
        'content': post.content,
        'photo': post.photo,
        'created_at': post.created_at,
    }

    return render(reqest, template_name='home/detail.html', context=context)
