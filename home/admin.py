from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Concerts
from .models import News
from .models import Photo


class NewsAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'created_at', "updated_at", 'is_published')
    list_display_links = ("id", 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


class ConcertsAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'location', 'place', 'is_published')


class PhotoAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'is_published')


admin.site.register(News, NewsAdmin)
admin.site.register(Concerts, ConcertsAdmin)
admin.site.register(Photo, PhotoAdmin)
