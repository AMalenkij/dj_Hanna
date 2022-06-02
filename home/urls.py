from django.urls import path
from .views import *

urlpatterns = [
#    path('', index),
    path('news', NewsList.as_view(), name='news'),
    path('', HomeList.as_view(), name='home'),
    path('<slug:post_slug>/', show_post, name='post'),
]
