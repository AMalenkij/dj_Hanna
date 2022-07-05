from modeltranslation.translator import register, TranslationOptions

from .models import Concerts
from .models import News
from .models import Photo


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'intro', 'intro', 'content',)


@register(Concerts)
class ConcertsTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'place',)


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)
