# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink
from django.utils.text import slugify
from django.contrib.auth.models import User

from tags.models import Tag


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(blank=True, upload_to='uploads/images')
    url = models.URLField(max_length=500, unique=False)
    last_modified_on = models.DateTimeField(auto_now=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, unique=False)
    categories = models.ManyToManyField(Tag)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)
