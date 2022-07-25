from django.urls import path
from .views import *

urlpatterns = [
    path('news', NewsList.as_view(), name='news'),
    path('', HomeList.as_view(), name='home'),
    path('concerts/', ConcertsList.as_view(), name='concerts'),
    path('about/', AboutList.as_view(), name='about'),
    path('contact/', contact, name='contact'),
    path('<slug:post_slug>/', show_post, name='post'),
]