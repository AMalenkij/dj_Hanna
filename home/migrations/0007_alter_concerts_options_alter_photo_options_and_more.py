# Generated by Django 4.0.4 on 2022-08-03 21:55

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_concerts_location_en_concerts_location_pl_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concerts',
            options={'ordering': ['-date'], 'verbose_name': 'Concert', 'verbose_name_plural': 'Concerts'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-date'], 'verbose_name_plural': 'foto'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_en',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_pl',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_uk',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]