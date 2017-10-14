# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'base.html'
    paginate_by = 10
    context_object_name = 'articles'
