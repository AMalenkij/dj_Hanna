from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    intro = models.TextField(blank=True)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Concerts(models.Model):
    title = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    place = models.CharField(max_length=500)
    link = models.URLField(max_length=200)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Concert'
        verbose_name_plural = 'Concerts'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Photo(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'foto'
        ordering = ['id']

    def __str__(self):
        return self.title


class Music(models.Model):
    band_name = models.CharField(max_length=50)
    song_name = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to='music/audio/')
    song_img = models.ImageField(upload_to='music/photo/', blank=True)

    class Meta:
        verbose_name_plural = 'Music'

    def __str__(self):
        return self.band_name
