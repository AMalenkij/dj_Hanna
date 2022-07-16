from django.urls import path
from .views import *

urlpatterns = [
    path('news', NewsList.as_view(), name='news'),
    path('', HomeList.as_view(), name='home'),
    path('concerts/', ConcertsList.as_view(), name='concerts'),
    path('about/', AboutList.as_view(), name='about'),
    path('contacts/', index_3, name='contacts'),
    path('<slug:post_slug>/', show_post, name='post'),
]