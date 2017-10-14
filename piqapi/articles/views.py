# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 1
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'base.html'
    context_object_name = 'article'
