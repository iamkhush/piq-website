# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

from embed_video.fields import EmbedVideoField
from tinymce.models import HTMLField

from tags.models import Tag


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    image = models.ImageField(blank=True, upload_to='uploads/images')
    content = HTMLField(null=True, blank=True)
    url = EmbedVideoField(max_length=500, unique=False, blank=True, null=False)
    last_modified_on = models.DateTimeField(auto_now=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, unique=False)
    categories = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-last_modified_on',)
