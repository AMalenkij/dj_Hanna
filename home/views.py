from datetime import date

from decouple import config
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView

from .models import Concerts
from .models import Music
from .models import News
from .models import Photo


# Gallery in page about
class AboutList(ListView):
    paginate_by = 12
    model = Photo
    template_name = 'home/about.html'
    context_object_name = 'about'
    extra_context = {'title': 'about'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music'] = Music.objects.all()
        return context

    def get_queryset(self):
        return Photo.objects.filter(is_published=True)


# form contact send e-mail
def contact(request):
    context = {
        'title': 'Contact',
    }

    if request.method == "POST":
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_email,  # Subject
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
    # paginate_by = 10
    template_name = 'home/concerts.html'
    extra_context = {'title': 'Concerts'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['future'] = Concerts.objects.filter(date__gte=date.today())
        context['past'] = Concerts.objects.filter(date__lte=date.today())
        return context

    def get_queryset(self):
        return Concerts.objects.filter(is_published=True)


def show_post(reqest, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'title': post.title,
        'content': post.content,
        'photo': post.photo,
        'created_at': post.created_at,
    }

    return render(reqest, template_name='home/detail.html', context=context)
