from django.urls import path
from .views import *

urlpatterns = [
    path('news', NewsList.as_view(), name='news'),
    path('', HomeList.as_view(), name='home'),
    path('about/', index, name='about'),
    path('<slug:post_slug>/', show_post, name='post'),
]
