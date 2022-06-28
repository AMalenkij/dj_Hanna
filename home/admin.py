from django.contrib import admin
from .models import News
from .models import Concerts


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', "updated_at", 'is_published')
    list_display_links = ("id", 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Concerts)
